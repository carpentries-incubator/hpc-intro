---
title: "Running a parallel job"
teaching: 10
exercises: 5
questions:
- "How do we execute a task in parallel?"
objectives:
- "Understand how to run a parallel job on a cluster."
keypoints:
- "Parallelism is an important feature of HPC clusters."
- "MPI parallelism is a common case."
- "The queuing system facilitates executing parallel tasks."
---

We now have the tools we need to run a multi-processor job. This
is a very important aspect of HPC systems, as parallelism is 
one of the primary tools we have to improve the performance of
computationnal tasks.

## Running the Parallel Job

We will run an example that uses the Message Passing Interface (MPI)
for parallelism -- this is a common tool on HPC systems.

> ## What is MPI?
> 
> The Message Passing Interface is a set of tools which allow
> multiple parallel jobs to communicate with each other. Typically,
> a single executable is run multiple times, possibly on different
> machines, and the MPI tools are used to inform each instance 
> of the executable about how many instances there are, which 
> instance it is. MPI also provides communication tools to allow
> communication and coordination between instances. An MPI instance
> typically has its own copy of all the local variables.
{: .callout}

MPI jobs cannot generally be run as stand-alone executables.
Instead, they should be started with the `mpirun` command, which
ensures that the appropriate run-time support for parallelism
is included. 

On its own, `mpirun` can take many arguments 
specifying how many machines will partcipate in the process. 
In the context of our queuing system, however, we do not need
to specify this information, the `mpirun` command will obtain
it from the queuing system, by examining the environment
variables set when the job is launched.

Our example implements a stochastic algorithm for estimating
the value of pi, the ratio of the circumference to the diameter
of a circle. The program generates a large number of random points
on a 2x2 square centered on the origin, and checks how many of
these points fall inside the unit circle. On average, pi/4 of the
randomly-selected points should fall in the circle, so pi can
be estimated from 4*f, where f is the observed fraction of points
that fall in the circle. Because each sample is independent, this
algorithm is easily implemented in parallel.

We have provided a Python implementation, which uses MPI and Numpy.

Download the Python executable using the following command:

```
{{ site.remote.prompt }} wget {{ site.url }}{{ site.baseurl }}/files/pi.py
```
{: .bash}

Feel free to examine the code in an editor -- it is richly commented,
and should provide some educational value.

Our purpose here is to exercise the parallel workflow of the 
cluster.

Create a submission file, requesting more than one task on a single node:
```
{{ site.remote.prompt }} nano parallel-example.sh
{{ site.remote.prompt }} cat parallel-example.sh
```
{: .bash}
```
#!/bin/bash
{{ site.sched.comment }} {{ site.sched.flag.name }} parallel-example
{{ site.sched.comment }} {{ site.sched.flag.queue }} {{ site.sched.queue.testing }}
{% include {{ site.snippets }}/parallel/four-tasks.snip %}
module load python3
mpirun ./pi.py
```
{: .output}

Then submit your job. We will use the batch file to set the options,
rather than the command line.
```
{{ site.remote.prompt }} {{ site.sched.submit.name }} parallel-example.sh
```
{: .bash}

As before, use the status commands to check when your job runs, 
and use `ls` to locate the output file, and examine it.

Is it what you expected? How good is the value for pi?
