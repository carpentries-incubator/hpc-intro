---
title: "Running a parallel job"
teaching: 30
exercises: 30
questions:
- "How do we execute a task in parallel?"
objectives:
- "Understand how to run a parallel job on a cluster."
keypoints:
- "Parallelism is an important feature of HPC clusters."
- "MPI parallelism is a common case."
- "The queuing system facilitates executing parallel tasks."
---

We now have the tools we need to run a multi-processor job. This is a very important
aspect of HPC systems, as parallelism is one of the primary tools we have to improve the
performance of computational tasks.

Our example implements a stochastic algorithm for estimating the value of
&#960;, the ratio of the circumference to the diameter of a circle.
The program generates a large number of random points on a 1&times;1 square
centered on (&frac12;,&frac12;), and checks how many of these points fall
inside the unit circle.
On average, &#960;/4 of the randomly-selected points should fall in the
circle, so &#960; can be estimated from 4*f*, where *f* is the observed
fraction of points that fall in the circle.
Because each sample is independent, this algorithm is easily implemented
in parallel.

## A Serial Solution to the Problem

We start from a Python script using concepts taught in Software Carpentry's
[Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/)
workshops.
We want to allow the user to specify how many random points should be used
to calculate &#960; through a command-line parameter.
This script will only use a single CPU for its entire run, so it's classified
as a serial process.

In the Python script, we start by importing the `numpy` module for calculating
the results, and the `sys` module to process command-line parameters:

```
#!/usr/bin/env python3
import numpy as np
import sys
```

We define a Python function `inside_circle` that accepts a single parameter
for the number of random points used to calculate &#960;.
It creates `x` and `y` arrays of random values on the interval [0,1), then
counts how many of those (x,y) coordinates are within a distance 1.0 from
the origin:

```
def inside_circle(total_count):
    x = np.random.uniform(size=total_count)
    y = np.random.uniform(size=total_count)
    radii = np.sqrt(x*x + y*y)
    count = len(radii[np.where(radii<=1.0)])
    return count
```

Next, we create a main function to call the `inside_circle` function and
calculate &#960; from its returned result:

```
if __name__ == '__main__':
    n_samples = int(sys.argv[1])
    counts = inside_circle(n_samples)
    my_pi = 4.0 * counts / n_samples
    print(my_pi)
```

The entire Python script is:

```
#!/usr/bin/env python3
import numpy as np
import sys

def inside_circle(total_count):
    x = np.random.uniform(size=total_count)
    y = np.random.uniform(size=total_count)
    radii = np.sqrt(x*x + y*y)
    count = len(radii[np.where(radii<=1.0)])
    return count

if __name__ == '__main__':
    n_samples = int(sys.argv[1])
    counts = inside_circle(n_samples)
    my_pi = 4.0 * counts / n_samples
    print(my_pi)
```

If we run the Python script with a command-line parameter, as in
`python pi-serial.py 1024`, we should see the script print its estimate of
&#960;:

```
$ python pi-serial.py 1024
3.10546875
```

## Measuring Performance of the Serial Solution

The stochastic method used to estimate &#960; should converge on the true
value as the number of random points increases.
But as the number of points increases, creating the variables `x`, `y`, and
`radii` requires more time and more memory.
Eventuially, the memory required may exceed what's available on our local
laptop or desktop, or the time required may be too long to meet a deadline.
So we'd like to take some measurements of how much memory and time the script
requires, and later take the same measurements after creating a parallel
version of the script to see the benefits of parallelizing the calculations
required.

### Estimating Memory Requirements

Since the largest variables in the script are `x`, `y`, and `radii`, each
containing `n_samples` points, we'll modify the script to calculate their
total memory required.
Each point in `x`, `y`, or `radii` is stored as a NumPy `float64`, we can
use the NumPy's [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html)
function to calculate the size of a `float64`.

Replace the `print(my_pi)` line with the following:

```
size_of_float = np.dtype(np.float64).itemsize
memory_required = 3 * n_samples * size_of_float / (1024**2)
print("Pi: {}, memory: {} MiB".format(my_pi, memory_required))
```

The first line calculates the bytes of memory required for a single `float64`
value using the `dtype`function.
The second line estimates the total amount of memory required to store three
variables containing `n_samples` `float64` values, converting the value into
units of [mebibytes](https://en.wikipedia.org/wiki/Byte#Multiple-byte_units).
The third line prints both the estimate of &#960; and the estimated amount of
memory used by the script.

Run the script again with a few different values for the number of samples, and
see how the memory required changes:

```
$ python pi-serial-minimized.py 1000
Pi: 3.144, memory: 0.02288818359375 MiB
$ python pi-serial-minimized.py 2000
Pi: 3.18, memory: 0.0457763671875 MiB
$ python pi-serial-minimized.py 1000000
Pi: 3.140944, memory: 22.88818359375 MiB
$ python pi-serial-minimized.py 100000000
Pi: 3.14182724, memory: 2288.818359375 MiB
```

Here we can see that the estimated amount of memory required scales linearly
with the number of samples used.
In practice, there is some memory required for other parts of the script,
but the `x`, `y`, and `radii` variables are by far the largest influence
on the memory required.

### Estimating Calculation Time

Most of the calculations required to estimate &#960; are in the
`inside_circle` function:

1. Generating `n_samples` random values for `x` and `y`.
2. Calculating `n_samples` values of `radii` from `x` and `y`.
3. Counting how many values in `radii` are under 1.0.

There's also one multiplication operation and one division operation required
to convert the `counts` value to the final estimate of &#960; in the main
function.

A simple way to measure the calculation time is to use Python's `datetime`
module to store the computer's current date and time before and after the
calculations, and calculate the difference between those times.

To add the time measurement to the script, add the following line below the
`import sys` line:

```
import datetime
```

Then, add the following line immediately above the line calculating `counts`:

```
start_time = datetime.datetime.now()
```

Add the following two lines immediately below the line calculating `counts`:

```
end_time = datetime.datetime.now()
elapsed_time = (end_time - start_time).total_seconds()
```

And finally, modify the `print` statement with the following:

```
print("Pi: {}, memory: {} MiB, time: {} s".format(my_pi, memory_required, elapsed_time))
```

Run the script again with a few different values for the number of samples, and
see how the solution time changes:

```
$ python pi-serial-minimized.py 1000000
Pi: 3.141108, memory: 22.88818359375 MiB, time: 0.037298 s
python pi-serial-minimized.py 10000000
Pi: 3.141774, memory: 228.8818359375 MiB, time: 0.346355 s
python pi-serial-minimized.py 100000000
Pi: 3.1413742, memory: 2288.818359375 MiB, time: 4.030354 s
```

Here we can see that the amount of time required scales approximately linearly
with the number of samples used.
There could be some variation in additional runs of the script with the same
number of samples, since the elapsed time is affected by other programs
running on the computer at the same time.
But if the script is the most computationally-intensive process running at the
time, its calculations are the largest influence on the elapsed time.

## Running the Parallel Job

We will run an example that uses the Message Passing Interface (MPI) for parallelism &mdash;
this is a common tool on HPC systems.

> ## What is MPI?
> 
> The Message Passing Interface is a set of tools which allow multiple parallel jobs to
> communicate with each other. Typically, a single executable is run multiple times,
> possibly on different machines, and the MPI tools are used to inform each instance of
> the executable about how many instances there are, which instance it is. MPI also
> provides tools to allow communication and coordination between instances.
> An MPI instance typically has its own copy of all the local variables.
{: .callout}

MPI jobs cannot generally be run as stand-alone executables. Instead, they should be
started with the `mpirun` command, which ensures that the appropriate run-time support for
parallelism is included.

On its own, `mpirun` can take many arguments specifying how many machines will participate
in the process. In the context of our queuing system, however, we do not need to specify
this information, the `mpirun` command will obtain it from the queuing system, by
examining the environment variables set when the job is launched.

We have provided a Python implementation, which uses MPI and NumPy, a popular library for
efficient numerical operations.

Download the Python executable using the following command:

```
{{ site.remote.prompt }} wget {{ site.url }}{{ site.baseurl }}/files/pi.py
```
{: .bash}

Let's take a quick look inside the file. It is richly commented, and should explain itself
clearly. Press "q" to exit the pager program (`less`).

```
{{ site.remote.prompt }} less pi.py
```
{: .bash}

> ## What's `pi.py` doing?
>
> One subroutine, `inside_circle`, does all the work. It randomly samples points with both
> *x* and *y* on the half-open interval [0, 1). It then computes their distances from the
> origin (i.e., radii), and returns those values. All of this is done using *vectors* of
> single-precision (32-bit) floating-point values.
>
> The implicitly defined "main" function performs the overhead and accounting work
> required to subdivide the total number of points to be sampled and *partitioning* the
> total workload among the various parallel processors available. At the end, all the
> workers report back to a "rank 0," which prints out the result.
>
> This relatively simple program exercises four important concepts:
>
> * COMM_WORLD: the default MPI Communicator, providing a channel for all the
>   processes involved in this `mpirun` to exchange information with one
>   another.
> * Scatter: A collective operation in which an array of data on one MPI rank
>   is divided up, with separate portions being sent out to the partner ranks.
>   Each partner rank receives data from the matching index of the host array.
> * Gather: The inverse of scatter. One rank populates a local array, with the
>   array element at each index assigned the value provided by the
>   corresponding partner rank &mdash; including the host's own value.
> * Conditional Output: since every rank is running the *same code*, the
>   general `print` statements are wrapped in a conditional so that only one
>   rank does it.
>
{: .discussion}

In general, achieving a better estimate of π requires a greater number of points. Take a
closer look at `inside_circle`: should we expect to get high accuracy on a single
machine?

Probably not. The function allocates two arrays of size *N* equal to the number of points
belonging to this process. Using 32-bit floating point numbers, the memory footprint of
these arrays can get quite large. The default total number &mdash; 8,738,128 &mdash; was
selected to achieve a 100 MB memory footprint. Pushing this number to a billion yields a
memory footprint of 11.2 GB: if your machine has less RAM than that, it will grind
to a halt. If you have 16 GB installed, you won't quite make it to 1&frac12; billion points.

Our purpose here is to exercise the parallel workflow of the cluster, not to optimize the
program to minimize its memory footprint. Rather than push our local machines to the
breaking point (or, worse, the login node), let's give it to a cluster node with more
resources. 

Create a submission file, requesting more than one task on a single node:

```
{{ site.remote.prompt }} nano parallel-pi.sh
{{ site.remote.prompt }} cat parallel-pi.sh
```
{: .bash}

```
#!/bin/bash
{{ site.sched.comment }} {{ site.sched.flag.name }} parallel-pi
{{ site.sched.comment }} {{ site.sched.flag.queue }} {{ site.sched.queue.testing }}
{% include {{ site.snippets }}/parallel/four-tasks.snip %}
module load python3
mpirun ./pi.py 1431652028
```
{: .output}

Then submit your job. We will use the batch file to set the options,
rather than the command line.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} parallel-pi.sh
```
{: .bash}

As before, use the status commands to check when your job runs. Use `ls` to locate the
output file, and examine it. Is it what you expected?

* How good is the value for &#960;?
* How much memory did it need?
* How much of that memory was used on each node?
