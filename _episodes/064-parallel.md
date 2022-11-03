---
title: "What is parallel"
teaching: 30
exercises: 60
questions:
- "How do we execute a task in parallel?"
- "What benefits arise from parallel execution?"
- "What are the limits of gains from execution in parallel?"
objectives:
- "Prepare a job submission script for the parallel executable."
keypoints:
- "Parallel programming allows applications to take advantage of
  parallel hardware; serial code will not 'just work.'"
- "There are multiple ways you can run "
---

You are most likely using an hpc because you need your work to run faster. This performance improvment is provided by increasing the number of CPUs.


If you are writing your own code, then this is something you will probably have to specify yourself.

## How to utilise Parallel Computing

### Scientific Software 
Many scientific software applications are written to take advantage of multiple CPUs in some way. Often this must be specifically requested by the user at the time they run the program, rather than happening automatically.
RTFM.

Will usually involve providing extra flags on stratup `-n 8` or whatever.

### Implicit Parallelism
Some programming langauges will have functions that can make use of multiple CPUs without requiring you to changes your code. However, unless that function is where the majority of time is spent, this is unlikely to give you the performance you are looking for.

(matlab, numpy?)

### Explicit Parallelism

Python [Multiproccessing](https://docs.python.org/3/library/multiprocessing.html)
MATLAB [Parpool](https://au.mathworks.com/help/parallel-computing/parpool.html)


### Array Programming
Vectorisation magic
Not relevent maybe?



## Methods of Parallel Computing

Three main types are shared memory, distributed and data level parallism. These methods are not exclusive, a job taking advantage of both SMP and MPI is said to be "Hybrid". Also mentioned is using a "job array", which isn't technically parallel computing, but serves a similar funtion.

Which methods are available to you is _largely dependent on the software being used_, 
### Shared-Memory (SMP)

Shared-memory multiproccessing divides work among _CPUs_ ( threads or cores ), all of these threads require access to the same memory. This means that all CPUs must be on the same node, most Mahuika nodes have 72 CPUs.

Number of CPUs to use is specified by the Slurm option `--cpus-per-task`.


```
{% include {{ site.snippets }}/scaling/shared-mem-example.snip %}
```
{: .language-bash}


### Distributed-Memory (MPI)

Message Passing Interface (MPI) is a communication standard for distributed-memory multiproccessing.
Distributed-memory multiproccessing divides work among _tasks_, a task may contain multiple CPUs (provided they all share memory, as discussed previously). 

Each task has it's own exclusive memory, tasks can be spread across multiple nodes, communicating via and _interconnect_. This allows MPI jobs to be much larger than shared memory jobs. It also means that memory requirements are more likely to increase proportionally with CPUs.

The NeSI platforms have _Hyperthreading_ enabled (not worth getting into). This means there are two _logical cpus_ per physical core. Every task— and therefore every job must have an even number of CPUs.

Distributed-Memory multiproccessing predates shared-memory multiproccessing, and is more common with classical high performance applications.

Number of tasks to use is specified by the Slurm option `--ntasks`, because tasks do not share memory you will also likely want to specify memory using `--mem-per-cpu` rather than `--mem`. Unless otherwise specified, each task will have `--cpus-per-task=2` (the minimum amount).


```
{% include {{ site.snippets }}/scaling/distibuted-mem-example.snip %}
```
{: .language-bash}

### Job Array

Job arrays are not "multiproccessing" in the same way as the previous two methods.
Ideal for _embarrassingly parallel_ problems, where there are little to no dependencies between the different jobs.

Can be thought of less as running a single job in parallel and more about running multiple serial-jobs simultaneously.
Often this is a type of _Data level parallelism_ where the same process is run on multiple inputs.

Embarrassingly parallel jobs should be able scale without any loss of efficiency. If this type of parallelisation is an option, it will almost certainly be the best choice.

A job array can be specified using `--array`

```
{% include {{ site.snippets }}/scaling/array-example.snip %}
```
{: .language-bash}

{% include links.md %}