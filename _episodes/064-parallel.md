---
title: "What is Parallel Computing"
teaching: 15
exercises: 5
questions:
- "How do we execute a task in parallel?"
- "What benefits arise from parallel execution?"
- "What are the limits of gains from execution in parallel?"
- "What is the difference between inplicit and explict parallelisation."
objectives:
- "Prepare a job submission script for the parallel executable."
keypoints:
- "Parallel programming allows applications to take advantage of
  parallel hardware; serial code will not 'just work.'"
- "There are multiple ways you can run "
---

You are most likely using an hpc because you need your work to run faster. This performance improvement is provided by increasing the number of CPUs.


## Methods of Parallel Computing

Three main types are shared memory, distributed and data level parallism. These methods are not exclusive, a job taking advantage of both SMP and MPI is said to be "Hybrid". Also mentioned is using a "job array", which isn't technically parallel computing, but serves a similar function.

Which methods are available to you is _largely dependent on the software being used_, 

### Shared-Memory (SMP)

Shared-memory multiproccessing divides work among _CPUs_ ( threads or cores ), all of these threads require access to the same memory. This means that all CPUs must be on the same node, most Mahuika nodes have 72 CPUs.

Number of CPUs to use is specified by the Slurm option `--cpus-per-task`.

### Distributed-Memory (MPI)

Message Passing Interface (MPI) is a communication standard for distributed-memory multiproccessing.
Distributed-memory multiproccessing divides work among _tasks_, a task may contain multiple CPUs (provided they all share memory, as discussed previously). 

Each task has it's own exclusive memory, tasks can be spread across multiple nodes, communicating via and _interconnect_. This allows MPI jobs to be much larger than shared memory jobs. It also means that memory requirements are more likely to increase proportionally with CPUs.

The NeSI platforms have _Hyperthreading_ enabled (not worth getting into). This means there are two _logical cpus_ per physical core. Every task— and therefore every job must have an even number of CPUs.

Distributed-Memory multiproccessing predates shared-memory multiproccessing, and is more common with classical high performance applications.

Number of tasks to use is specified by the Slurm option `--ntasks`, because tasks do not share memory you will also likely want to specify memory using `--mem-per-cpu` rather than `--mem`. Unless otherwise specified, each task will have `--cpus-per-task=2` (the minimum amount).

### Job Array

Job arrays are not "multiproccessing" in the same way as the previous two methods.
Ideal for _embarrassingly parallel_ problems, where there are little to no dependencies between the different jobs.

Can be thought of less as running a single job in parallel and more about running multiple serial-jobs simultaneously.
Often this is a type of _Data level parallelism_ where the same process is run on multiple inputs.

Embarrassingly parallel jobs should be able scale without any loss of efficiency. If this type of parallelisation is an option, it will almost certainly be the best choice.

A job array can be specified using `--array`

If you are writing your own code, then this is something you will probably have to specify yourself.

## How to Utilise Multiple CPUs

Requesting extra resources through Slurm only means that more resources will be available, it does not guarantee your program will be able to make use of them. 

Generally speaking, Parallelism is either _implicit_ where the software figures out everything behind the scenes, or _explicit_ where the software requires extra direction from the user.

### Scientific Software

The first step when looking to run particular software should always be to read the (f*) documentation. 
On one end of the scale, some software may claim to make use of multiple cores implicitly, but this should be verified as the methods used to determine available resources are not gauranteed to work.

Some software will require you to specify number of cores (e.g. `-n 8` or `-np 16`), or even type of paralellisation (e.g. `-dis` or `-mpi=intelmpi`).

Occasionally your input files may require rewriting/regenerating for every new CPU combintation (e.g. domain based parallelism without automatic partitioning). 


### Writing Code

Occasionally requesting more CPUs in your Slurm job is all that is required and whatever program you are running will automagically take advantage of the additional resources.
However, it's more likely to require some amount of effort on your behalf (or will oper )

Elaborate on 

It is important to determine this before you start requesting more resources through Slurm  

If you are writing your own code, some programming languages will have functions that can make use of multiple CPUs without requiring you to changes your code. 
However, unless that function is where the majority of time is spent, this is unlikely to give you the performance you are looking for.

{%- comment -%} (matlab, numpy?) {%- endcomment -%}

{%- comment -%} 
Python [Multiproccessing](https://docs.python.org/3/library/multiprocessing.html)
MATLAB [Parpool](https://au.mathworks.com/help/parallel-computing/parpool.html) {%- endcomment -%}

Shared memory parallelism is what is used in our example script `array_sum.r`.


## Scaling Test

Last time we submitted a job, we did not specify a number of CPUs, and therefore got the default of `2` (1 'core').

As a reminder, our slurm script `example-job.sl` should currently look like this.

```
{% include example_scripts/example-job.sl.1 %}
```
{: .language-bash}


Using the information we collected from the previous job (`nn_seff <job-id>`), we will submit the same job again with more CPUs and our best estimates of required resources.
We ask for more CPUs using by adding `#SBATCH --cpus-per-task 4` to our script.

Your script should now look like this:

```
{% include example_scripts/example-job.sl.2 %}
```
{: .language-bash} 

And then submit using `sbatch` as we did before.

> ## acctg-freq
>
> We will also add the argument `--acctg-freq 1`.
> By default SLURM records job data every 30 seconds. This means any job running for less than 30 
> seconds will not have it's memory use recorded.
> This is the same as specifying `#SBATCH --acctg-freq 1` inside the script.
{: .callout}

```
{{ site.remote.prompt }} sbatch --acctg-freq 1 example-job.sl
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/basic-job-script.snip %}

> ## Watch
>
> We can prepend any command with `watch` in order to periodically (default 2 seconds) run a command. e.g. `watch 
> squeue --me` will give us up to date information on our running jobs. 
> Care should be used when using `watch` as repeatedly running a command can have adverse effects.  
{: .callout}

Checking on our job with `sacct`.
Oh no! 
{% include {{ site.snippets }}/scaling/OOM.snip %}

{: .language-bash}

{% include links.md %}