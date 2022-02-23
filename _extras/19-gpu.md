---
title: "Running a parallel job on the GPU"
teaching: 30
exercises: 30
questions:
- "How do we execute a task in parallel on a GPU?"
objectives:
- "Understand what a GPU is."
- "See how to run a parallel job on a GPU."
- "Learn how thread configuration affect GPU performance."
keypoints:
- "GPUs are becoming more commonplace in clusters and can provide higher performance than CPUs for certain applications."
- "There are a number of frameworks targeting GPUs, PyCUDA is one of the more accessible ones for beginners."
- "To get good performance on GPUs the thread configuration must be considered."
---

We now turn our attention to running a job using a GPU. This is another
important aspect of HPC systems, as GPU parallelism can bring added performance
benefits for many applications.
The example in this section reimplements the estimation of Pi example as introduced for MPI in
the [Running a Parallel Job]({{ page.root }}/16-parallel/#a-serial-solution-to-the-problem) lesson.   
  
  

## What is a GPU?

While most CPUs now have several processor cores inside, GPUs instead have several thousand
lightweight cores which can provide high performance when given the same instructions.
Below a simplified view of the inside of a CPU are compared to the inside of a GPU.   
{% include figure.html url="" caption="" max-width="60%"
   file="/fig/gpu-vs-cpu.png"
   alt="Simplified View of a CPU and GPU" %}

Originally, Graphics Processing Units were designed to accelerate graphics calculations, 
but increasingly they have been targeted by other types of codes (this is known as GPGPU - or 
"General Purpose GPU" - Programming). They provide a natural fit for parallel codes as they 
were designed specifically for this purpose. 

However, there is an additional complexity for programming GPUs as there must be separate 
instructions for what runs on the GPU on and what runs on the host (usually CPU) side. As well 
as this, getting good performance on  GPUs often requires tuning the threads targeting the GPU, 
thus requiring another level of expertise.


## Example GPU Code 

As an example, we will reimplement the stochastic algorithm for estimating the value of
&#960;, the ratio of the circumference to the diameter of a circle on the GPU. 
To recap, the program generates a large number of random points on a 1&times;1 square
centered on (&frac12;,&frac12;), and checks how many of these points fall
inside the unit circle.
On average, &#960;/4 of the randomly-selected points should fall in the
circle, so &#960; can be estimated from 4*f*, where *f* is the observed
fraction of points that fall in the circle.
Each sample is independent, making this algorithm easily implementable in parallel. 
For more details about the algorithm, see the 
[Running a Parallel Job]({{ page.root }}/16-parallel/#a-serial-solution-to-the-problem) 
lesson.

{% include figure.html url="" caption="" max-width="40%"
   file="/fig/pi.png"
   alt="Algorithm for computing pi through random sampling" %}

## Running the Example Code on the GPU

In this example we will use PyCUDA for parallelism. PyCUDA employs the CUDA parallel API 
within the python framework. CUDA is a very popular framework for GPUs on HPC systems, 
however it is limited to only NVIDIA GPUs.

> ## What is CUDA?
> CUDA (Compute Unified Device Architecture) is a GPU programming interface developed by
> NVIDIA. In the CUDA API, data must be wrapped in special buffers and explicitly transferred 
> to the device (GPU). In addition, the threads which perform the work on the GPU must also be explicitly set, 
> which unfortunately is not an exact science. 
> In addition, kernels must be written to perform computations on the GPU. 
> Kernels are a type of function containing select keywords that indicate a code will be run on the GPU.
{: .callout}

> ## What is PyCuda?
> PyCUDA provides a relatively simple python syntax for using CUDA, which can be difficult to learn for HPC beginners. 
> While PyCUDA itself provides a syntax for
> copying data to/from the GPU and running a kernel, complicated kernels must still be written in a C-like 
> syntax and included as a header file or wrapped in a string.  
>
> Note that there are several ways of running PyCUDA ranging from managing all CUDA calls to 
> having minimal control.
> This tutorial aims to provide an example which lies somewhere in the middle. More detailed information and examples can be
> found in the [PyCUDA documentation tutorial](https://documen.tician.de/pycuda/tutorial.html).
{: .callout}


> ## What Changes Are Needed for a CUDA Version of the &#960; Calculator?
>
> Several modules must be imported to use pycuda. The `pycuda.driver` module must first be imported 
> (which in this example we rename to `cuda` for convenience). 
> `SourceModule` from the `pycuda.compiler` module must also be imported, which will 
> read in the GPU kernel. 
> Finally, the `pycuda.autoinit` module must be imported, which automatically initialises and cleans
> up CUDA calls. 
>
> Additional modifications to the serial script demonstrate three important concepts:
>
> * Defining the estimation kernel on the GPU 
> * Transferring data to the GPU 
> * Defining the thread configuration for running the estimation kernel
>
> The kernel is where all the calculations will be performed for estimating pi. In this example,
> the number of samples corresponds to the number of threads launched and each thread performs a single
> check for a given sample number. If a sample is inside the circle, it puts in a count of 1 
> and if it is outside of the circle the count is zero.  
> After the kernel has run, the number of values inside the circle is counted up on 
> the host (CPU) side.
>
> The kernel is called from the host side, so data that is used inside the kernel may need to be defined 
> on the host side. In this example, the x and y values and an array for keeping track of the number of
> points inside and outside the circle are defined on the host side and then passed to the kernel.
> Special instructions are given to the data buffers to define whether they are read-only, write-only or
> both readable and writeable.
>
> In addition to passing these three array inputs, the thread setup must also be passed into the kernel.
> This is done with two additional parameters: 
> * Number of thread blocks in a grid (can be 1D)
> * Number of threads in a block (can be 1D, but both parameters must be the same dimension)
>
> Below shows a 2D example of how threads combine to form a block and threadblocks combine form a grid.
> More information about threads on the GPU can be found in [Selecting a CUDA Thread Configuration]({{ page.root }}/19-gpu/#selecting-a-cuda-thread-configuration). 
{: .discussion}
{% include figure.html url="" caption="" max-width="60%"
   file="/fig/cudathreadblock.png"
   alt="Simplified View of Threads and Thread Blocks" %}

We will now step through these changes to the code in more detail.\
  \
First, instead of allocating the x and y value arrays in the estimation function, this is now done first on the host side:
```
x_values = np.random.uniform(size=SZ)
x_values = x_values.astype(np.float32)
y_values = np.random.uniform(size=SZ)
y_values = y_values.astype(np.float32)
total_count = np.zeros((SZ,), dtype='int32')
```
{: .language-python}
As previously, `np` comes from `import numpy as np`.

Then the GPU kernel (`calculatePi`) is read in as a `SourceModule` object 
in the variable `mod`. 

```
mod = SourceModule("""
    __global__ void calculatePi(float *x_values, float *y_values, int *total_count) {
            int tid = threadIdx.x + blockIdx.x * blockDim.x;
                if ((x_values[tid] * x_values[tid]) + (y_values[tid] * y_values[tid]) < 1.0f) {
                    total_count[tid] = 1;
                }
                else{
                    total_count[tid] = 0;
                }    
    }
        """)

```
{: .language-python}
The syntax of this function is C-like, although it also contains the keyword `__global__`, indicating
that it is a function which is called from the host to be run on the GPU. 
  \
However, the `SourceModule` actually compiles this into CUDA code, so we still need one extra step to 
call this kernel from PyCUDA:  
```
func = mod.get_function("calculatePi")
```
{: .language-python}

`func` can now be called from the host, passing in three inputs to the GPU kernel `calculatePi`.
The first two of these are `x_values` and `y_values`, which are used in the calculation and are read-only. 
Thus, when they are passed in with `func,` they are wrapped in a `cuda.In` call which means they
are only read in as input on the GPU. The array `count` however is wrapped in a `cuda.InOut` call indicating 
that this array is readable and writeable. 
```
func(cuda.In(x_values),cuda.In(y_values), cuda.InOut(total_count), grid=(NUM_BLOCK,1,1),block=(NUM_THREAD,1, 1))
```
{: .language-python}

Two additional parameters are passed into `func`:
```
grid = (NUM_BLOCK,1,1)
block = (NUM_THREAD,1,1)
```
{: .language-python}

These parameters correspond to the number of parallel threads which are designated for the GPU (behind the scenes
in the hardware, it is slightly more complicated than this, but this is a good approximation from the programmer's
perspective). In our simple example, 
`NUM_BLOCK` and `NUM_THREAD` are both the same value which is defined by the input parameter to the program 
(this value is squared to determine the number of samples).
The grid that is passed in to the GPU kernel indicates the number of threadblocks to use.  
Each block then contains a number of threads. In our example only the first dimension is used, but up to 
three dimensions can be used for each. 

After the kernel has run, the number of values inside the circle is counted up into `count` back on the host side. 
```
count = sum(total_count)
```
{: .language-python}

Then the value of pie can be calculated as previously.


A fully commented version of the final GPU parallel python code is available
[here](/files/pi-pycuda.py).

> ## Selecting a CUDA Thread Configuration
>
> In this simple example, only the number of samples (ie. `NUM_BLOCK`\*`NUM_THREAD`) to calculate pi are performed 
> by the GPU. However, there is a limit to how many threads can run on the GPU and datasets are often much larger than this. 
> As such, these large datasets will not be able to simply divide up the number of points by the number of threads. 
> Instead, threads will need to handle more work and achieving good performance in this manner may require tuning 
> the number of thread blocks as well as the number of threads per block. 
> Unfortunately there is not an exact science for this and certain thread group configurations provide better 
> performance than others (powers of two, as one example) for different applications.
> In particular, those where consecutive threads access memory from the same region (or are "coalesced") tend to
> perform well. There are some heuristics available; however, optimal performance often requires
> manual experimentation. Alternatively, a variety of tuning frameworks are available to perform
> this automatically or tools like [NVIDIA NSight](https://docs.nvidia.com/nsight-compute/NsightCompute/index.html#occupancy-calculator), 
> which can help determine optimal occupancy (or how well utilised the GPU is).
{: .callout}
  \
  \
Now we will create a submission file to run our code on a single GPU on a compute node:

```
{{ site.remote.prompt }} nano gpu-pi.sh
{{ site.remote.prompt }} cat gpu-pi.sh
```
{: .language-bash}

```
#!/usr/bin/env bash
#SBATCH -J gpu-pi
#SBATCH --partition=gpu
#SBATCH --qos=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --exclusive

# Load the computing environment we need
module use /lustre/sw/modulefiles.miniconda3
module load pytorch/1.10.1-gpu

# Execute the task
python gpu-pi.py 128 
```
{: .language-bash}

Then submit your job. We will use the batch file to set the options,
rather than the command line.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} gpu-pi.sh
```
{: .language-bash}

As before, use the status commands to check when your job runs.
Use `ls` to locate the output file, and examine it.
Is it what you expected?

* How good is the value for &#960;?
* How much faster was this run than the serial run with 16384 points?

Modify the job script to increase the number of samples to 256, 512 and 1024. 
and resubmit the job each time.

* How good is the value for &#960;?
* How long did the job take to run?



In an HPC environment, we try to reduce the execution time for all types of
jobs, and CUDA is another popular method for using GPUs to target an application.
To learn about parallelization more generally, see the 
[parallel novice lesson](http://www.hpc-carpentry.org/hpc-parallel-novice/)

{% include links.md %}
