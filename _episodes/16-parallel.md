---
title: "Running a parallel job"
teaching: 30
exercises: 60
questions:
- "How do we execute a task in parallel?"
- "What benefits arise from parallel execution?"
- "What are the limits of gains from execution in parallel?"
objectives:
- "Prepare a job submission script for the parallel executable."
- "Launch jobs with parallel execution."
- "Record and summarize the timing and accuracy of jobs."
- "Describe the relationship between job parallelism and performance."
keypoints:
- "Parallel programming allows applications to take advantage of
  parallel hardware."
- "The queuing system facilitates executing parallel tasks."
- "Performance improvements from parallel execution do not scale linearly."
---

We now have the tools we need to run a multi-processor job. This is a very
important aspect of HPC systems, as parallelism is one of the primary tools
we have to improve the performance of computational tasks.

## Help!

Many command-line programs include a "help" message. Navigate to the directory
of the decompressed files, then print the `amdahl` program's help message:

```
{{ site.remote.prompt }} cd hpc-intro-code
{{ site.remote.prompt }} ./amdahl --help
```
{: .language-bash}

```
usage: amdahl [-h] [-p [PARALLEL_PROPORTION]] [-w [WORK_SECONDS]]

optional arguments:
  -h, --help            show this help message and exit
  -p [PARALLEL_PROPORTION], --parallel-proportion [PARALLEL_PROPORTION]
                        Parallel proportion should be a float between 0 and 1
  -w [WORK_SECONDS], --work-seconds [WORK_SECONDS]
                        Total seconds of workload, should be an integer greater than 0
```
{: .output}

This message doesn't tell us much about what the program _does_, but it does
tell us the important flags we might want to use when launching it.

## Running the Job on a Compute Node

Create a submission file, requesting one task on a single node, then launch it.

```
{{ site.remote.prompt }} nano serial-job.sh
{{ site.remote.prompt }} cat serial-job.sh
```
{: .language-bash}

{% include {{ site.snippets }}/parallel/one-task-jobscript.snip %}

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} serial-job.sh
```
{: .language-bash}

As before, use the {{ site.sched.name }} status commands to check whether your job
is running and when it ends:

```
{{ site.remote.prompt }} {{ site.sched.status }}{{ site.sched.flag.user }}
```
{: .language-bash}

Use `ls` to locate the output file. The `-t` flag sorts in
reverse-chronological order: newest first. What was the output?

> ## Read the Job Output
>
> The cluster output should be written to a file in the folder you launched the
> job from.
>
> ```
> {{ site.remote.prompt }} ls -t
> ```
> {: .language-bash}
> ```
> slurm-347087.out  serial-job.sh  amdahl  README.md  LICENSE.txt
> ```
> {: .output}
> ```
> {{ site.remote.prompt }} cat slurm-347087.out
> ```
> {: .language-bash}
> ```
> Doing 30.000000 seconds of 'work' on 1 processor,
> which should take 30.000000 seconds with 0.850000 parallel proportion of the workload.
>
>   Hello, World! I am process 0 of 1 on {{ site.remote.node }}. I will do all the serial 'work' for 4.500000 seconds.
>   Hello, World! I am process 0 of 1 on {{ site.remote.node }}. I will do parallel 'work' for 25.500000 seconds.
>
> Total execution time (according to rank 0): 30.033140 seconds
> ```
> {: .output}
{: .solution}

`amdahl` takes two optional parameters as input: the amount of work and the
proportion of that work that is parallel in nature. Based on the output, we can
see that the code uses a default of 30 seconds of work that is 85%
parallel. The program ran for just over 30 seconds in total, and if we run the
numbers, it is true that 15% of it was marked 'serial' and 85% was 'parallel'.

Since we only gave the job one CPU, this job wasn't really parallel at
all.

## Running the Parallel Job

The `amdahl` program uses the Message Passing Interface (MPI) for parallelism
-- this is a common tool on HPC systems.

> ## What is MPI?
>
> The Message Passing Interface is a set of tools which allow multiple tasks
> running simultaneously to communicate with each other.
> Typically, a single executable is run multiple times, possibly on different
> machines, and the MPI tools are used to inform each instance of the
> executable about its sibling processes, and which instance it is.
> MPI also provides tools to allow communication between instances to
> coordinate work, exchange information about elements of the task, or to
> transfer data.
> An MPI instance typically has its own copy of all the local variables.
{: .callout}

While MPI-aware executables can generally be run as stand-alone programs, in
order for them to run in parallel they must use an MPI _run-time environment_,
which is a specific implementation of the MPI _standard_.
To activate the MPI environment, the program should be started via a command
such as `mpiexec` (or `mpirun`, or `srun`, etc. depending on the MPI run-time
you need to use), which will ensure that the appropriate run-time support for
parallelism is included.

> ## MPI Runtime Arguments
>
> On their own, commands such as `mpiexec` can take many arguments specifying
> how many machines will participate in the execution,
> and you might need these if you would like to run an MPI program on your
> own (for example, on your laptop).
> In the context of a queuing system, however, it is frequently the case that
> MPI run-time will obtain the necessary parameters from the queuing system,
> by examining the environment variables set when the job is launched.
{: .callout}

Let's modify the job script to request more cores and use the MPI run-time.

```bash
{{ site.remote.prompt }} cp serial-job.sh parallel-job.sh
{{ site.remote.prompt }} nano parallel-job.sh
{{ site.remote.prompt }} cat parallel-job.sh
```

{% include {{ site.snippets }}/parallel/four-tasks-jobscript.snip %}

Then submit your job. Note that the submission command has not really changed
from how we submitted the serial job: all the parallel settings are in the
batch file rather than the command line.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} parallel-job.sh
```
{: .language-bash}

As before, use the status commands to check when your job runs.
Use `ls` to locate the output file, and examine it.

> ## Is it 4× faster?
>
> The parallel job received 4× more processors as the serial job.
> Does that mean that the job completed in ¼ the time?
>
> > ## Check the Result
> >
> > ```
> > {{ site.remote.prompt }} ls -t
> > ```
> > {: .language-bash}
> > ```
> > slurm-347178.out  parallel-job.sh  slurm-347087.out  serial-job.sh  amdahl  README.md  LICENSE.txt
> > ```
> > {: .output}
> > ```
> > {{ site.remote.prompt }} cat slurm-347178.out
> > ```
> > {: .language-bash}
> > ```
> > Doing 30.000000 seconds of 'work' on 4 processors,
> > which should take 10.875000 seconds with 0.850000 parallel proportion of the workload.
> >
> >   Hello, World! I am process 0 of 4 on {{ site.remote.node }}. I will do all the serial 'work' for 4.500000 seconds.
> >   Hello, World! I am process 2 of 4 on {{ site.remote.node }}. I will do parallel 'work' for 6.375000 seconds.
> >   Hello, World! I am process 1 of 4 on {{ site.remote.node }}. I will do parallel 'work' for 6.375000 seconds.
> >   Hello, World! I am process 3 of 4 on {{ site.remote.node }}. I will do parallel 'work' for 6.375000 seconds.
> >   Hello, World! I am process 0 of 4 on {{ site.remote.node }}. I will do parallel 'work' for 6.375000 seconds.
> >
> > Total execution time (according to rank 0): 10.887713 seconds
> > ```
> > {: .output}
> >
> > The parallel job did take _less_ time: 11 seconds is better than 30!
> > But it is only a 2.7× improvement, not 4×.
> {: .solution}
{: .challenge}

## How Much Does MPI Improve Performance?

In theory, by dividing up the calculations among _n_ MPI processes,
we should see run times reduce by a factor of _n_.
In practice, some time is required to start the additional MPI processes,
for the MPI processes to communicate and coordinate, and some types of
calculations may only be able to run effectively on a single CPU.

Additionally, if the MPI processes operate on different physical CPUs
in the computer, or across multiple compute nodes, additional time is
required for communication compared to all processes operating on a
single CPU.

[Amdahl's Law][amdahl] is one way of predicting improvements in execution time
for a __fixed__ parallel workload.  If a workload needs 20 hours to complete on
a single core, and one hour of that time is spent on tasks that cannot be
parallelized, only the remaining 19 hours could be parallelized.  Even if an
infinite number of cores were used for the parallel parts of the workload, the
total run time cannot be less than one hour.

In practice, it's common to evaluate the parallelism of an MPI program by

* running the program across a range of CPU counts,
* recording the execution time on each run,
* comparing each execution time to the time when using a single CPU.

The speedup factor _S_ is calculated as the single-CPU execution time divided
by the multi-CPU execution time.
For a laptop with 8 cores, the graph of speedup factor versus number of cores
used shows relatively consistent improvement when using 2, 4, or 8 cores, but
using additional cores shows a diminishing return.

{% include figure.html url="" caption="" max-width="50%"
   file="/fig/laptop-mpi_Speedup_factor.png"
   alt="MPI speedup factors on an 8-core laptop" %}

For a set of HPC nodes containing 28 cores each, the graph of speedup factor
versus number of cores shows consistent improvements up through three nodes
and 84 cores, but __worse__ performance when adding a fourth node with an
additional 28 cores.
This is due to the amount of communication and coordination required among
the MPI processes requiring more time than is gained by reducing the amount
of work each MPI process has to complete. This communication overhead is not
included in Amdahl's Law.

{% include figure.html url="" caption="" max-width="50%"
   file="/fig/hpc-mpi_Speedup_factor.png"
   alt="MPI speedup factors on an 8-core laptop" %}

In practice, MPI speedup factors are influenced by:

* CPU design,
* the communication network between compute nodes,
* the MPI library implementations, and
* the details of the MPI program itself.

In an HPC environment, we try to reduce the execution time for all types of
jobs, and MPI is an extremely common way to combine dozens, hundreds, or
thousands of CPUs into solving a single problem. To learn more about
parallelization, see the [parallel novice lesson][parallel-novice] lesson.

{% include links.md %}

[amdahl]: https://en.wikipedia.org/wiki/Amdahl's_law
[cmd-line]: https://swcarpentry.github.io/python-novice-inflammation/12-cmdline/index.html
[inflammation]: https://swcarpentry.github.io/python-novice-inflammation/
[np-dtype]: https://numpy.org/doc/stable/reference/generated/numpy.dtype.html
[parallel-novice]: http://www.hpc-carpentry.org/hpc-parallel-novice/
[python-func]: https://swcarpentry.github.io/python-novice-inflammation/08-func/index.html
[units]: https://en.wikipedia.org/wiki/Byte#Multiple-byte_units
