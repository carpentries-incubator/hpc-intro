---
title: "What is Parallel Computing"
teaching: 15
exercises: 5
questions:
- "How do we execute a task in parallel?"
- "What benefits arise from parallel execution?"
- "What are the limits of gains from execution in parallel?"
- "What is the difference between implicit and explicit parallelisation."
objectives:
- "Prepare a job submission script for the parallel executable."
keypoints:
- "Parallel programming allows applications to take advantage of
  parallel hardware; serial code will not 'just work.'"
- "There are multiple ways you can run "
---

## Methods of Parallel Computing

The two main types of parallel computing we will discuss are _shared memory_ and _distributed memory_.

To understand the difference we first need to clarify some terms.

{% include figure.html url="" max-width="40%"
   file="/fig/clusterDiagram.png"
   alt="Node anatomy" caption="" %}

CPU: Unit that does the computations.
Task: One or more CPUs that share memory.
Node: The physical hardware. The upper limit on how many CPUs can be in a task.

Shared Memory Parallelism is when multiple CPUs are used within a single task.
Distributed Memory Parallelism is when multiple tasks are used.

Which methods are available to you is largely dependent on the nature of the problem and software being used.

Exercises in this episode will require a copy of the `whothis.sh` file from the workshop directory.

```
{{ site.remote.prompt }}  cp ../whothis.sh .
```
{: .language-bash}

### Shared-Memory (SMP)

Shared-memory multiproccessing divides work among _CPUs_ or _threads_, all of these threads require access to the same memory.

Often called `Multithreading`.

This means that all CPUs must be on the same node, most Mahuika nodes have 72 CPUs.

Shared memory parallelism is what is used in our example script `array_sum.r`.

Number of threads to use is specified by the Slurm option `--cpus-per-task`.

{% include {{ site.snippets }}/parallel/smp-example.snip %}

### Distributed-Memory (MPI)

Distributed-memory multiproccessing divides work among _tasks_, a task may contain multiple CPUs (provided they all share memory, as discussed previously).

Message Passing Interface (MPI) is a communication standard for distributed-memory multiproccessing. While there are other standards, often 'MPI' is used synonymously with Distributed parallelism.  

Each task has it's own exclusive memory, tasks can be spread across multiple nodes, communicating via and _interconnect_. This allows MPI jobs to be much larger than shared memory jobs. It also means that memory requirements are more likely to increase proportionally with CPUs.

Distributed-Memory multiproccessing predates shared-memory multiproccessing, and is more common with classical high performance applications (older computers had one CPU per node).

Number of tasks to use is specified by the Slurm option `--ntasks`, because the number of tasks ending up on one node is variable you should use `--mem-per-cpu` rather than `--mem` to ensure each task has enough.

Tasks cannot share cores, this means in most circumstances leaving `--cpus-per-task` unspecified will get you `2`.

{% include {{ site.snippets }}/parallel/mpi-example.snip %}

Using a combination of Shared and Distributed memory is called _Hybrid Parallel_.

{% include {{ site.snippets }}/parallel/hyb-example.snip %}

### Job Array

Job arrays are not "multiproccessing" in the same way as the previous two methods.
Ideal for _embarrassingly parallel_ problems, where there are little to no dependencies between the different jobs.

Can be thought of less as running a single job in parallel and more about running multiple serial-jobs simultaneously.
Often this will involve running the same process is run on multiple inputs.

Embarrassingly parallel jobs should be able scale without any loss of efficiency. If this type of parallelisation is an option, it will almost certainly be the best choice.

A job array can be specified using `--array`

If you are writing your own code, then this is something you will probably have to specify yourself.

{% include {{ site.snippets }}/parallel/array-example.snip %}

## How to Utilise Multiple CPUs

Requesting extra resources through Slurm only means that more resources will be available, it does not guarantee your program will be able to make use of them.

Generally speaking, Parallelism is either _implicit_ where the software figures out everything behind the scenes, or _explicit_ where the software requires extra direction from the user.

### Scientific Software

The first step when looking to run particular software should always be to read the ███████ documentation.
On one end of the scale, some software may claim to make use of multiple cores implicitly, but this should be verified as the methods used to determine available resources are not guaranteed to work.

Some software will require you to specify number of cores (e.g. `-n 8` or `-np 16`), or even type of paralellisation (e.g. `-dis` or `-mpi=intelmpi`).

Occasionally your input files may require rewriting/regenerating for every new CPU combintation (e.g. domain based parallelism without automatic partitioning).

### Writing Code

Occasionally requesting more CPUs in your Slurm job is all that is required and whatever program you are running will automagically take advantage of the additional resources.
However, it's more likely to require some amount of effort on your behalf.

It is important to determine this before you start requesting more resources through Slurm  

If you are writing your own code, some programming languages will have functions that can make use of multiple CPUs without requiring you to changes your code.
However, unless that function is where the majority of time is spent, this is unlikely to give you the performance you are looking for.

{%- comment -%} (matlab, numpy?) {%- endcomment -%}

Python [Multiproccessing](https://docs.python.org/3/library/multiprocessing.html)
MATLAB [Parpool](https://au.mathworks.com/help/parallel-computing/parpool.html)

{% include links.md %}
