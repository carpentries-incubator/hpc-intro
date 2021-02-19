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

Our example implements a stochastic algorithm for estimating the value of &#960;, the
ratio of the circumference to the diameter of a circle. The program generates a large
number of random points on a 1&times;1 square centered on (&frac12;,&frac12;), and checks
how many of these points fall inside the unit circle. On average, &#960;/4 of the
randomly-selected points should fall in the circle, so &#960; can be estimated from 4*f*,
where *f* is the observed fraction of points that fall in the circle. Because each sample
is independent, this algorithm is easily implemented in parallel.

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
module load {{ site.remote.module_python3 }}
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
