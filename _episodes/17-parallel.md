---
title: "Running a parallel job"
teaching: 30
exercises: 60
questions:
- "How do we execute a task in parallel?"
- "What benefits arise from parallel execution?"
- "What are the limits of gains from execution in parallel?"
objectives:
- "Install a Python package using `pip`"
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

If you disconnected, log back in to the cluster.

```
{{ site.local.prompt }} ssh {{ site.remote.user }}@{{ site.remote.login }}
```
{: .language-bash}

## Install the Amdahl Program

With the Amdahl source code on the cluster, we can install it, which will
provide access to the `amdahl` executable.
Move into the extracted directory, then use the Package Installer for Python,
or `pip`, to install it in your ("user") home directory:

```
{{ site.remote.prompt }} cd amdahl
{{ site.remote.prompt }} python3 -m pip install --user .
```
{: .language-bash}

> ## Amdahl is Python Code
>
> The Amdahl program is written in Python, and installing or using it requires
> locating the `python3` executable on the login node.
> If it can't be found, try listing available modules using `module avail`,
> load the appropriate one, and try the command again.
{: .callout}

### MPI for Python

The Amdahl code has one dependency: __mpi4py__.
If it hasn't already been installed on the cluster, `pip` will attempt to
collect mpi4py from the Internet and install it for you.
If this fails due to a one-way firewall, you must retrieve mpi4py on your
local machine and upload it, just as we did for Amdahl.

> ## Retrieve and Upload `mpi4py`
>
> If installing Amdahl failed because mpi4py could not be installed,
> retrieve the tarball from <https://github.com/mpi4py/mpi4py/tarball/master>
> then `rsync` it to the cluster, extract, and install:
>
> ```
> {{ site.local.prompt }} wget -O mpi4py.tar.gz https://github.com/mpi4py/mpi4py/releases/download/3.1.4/mpi4py-3.1.4.tar.gz
> {{ site.local.prompt }} scp mpi4py.tar.gz {{ site.remote.user }}@{{ site.remote.login }}:
> # or
> {{ site.local.prompt }} rsync -avP mpi4py.tar.gz {{ site.remote.user }}@{{ site.remote.login }}:
> ```
> {: .language-bash}
>
> ```
> {{ site.local.prompt }} ssh {{ site.remote.user }}@{{ site.remote.login }}
> {{ site.remote.prompt }} tar -xvzf mpi4py.tar.gz  # extract the archive
> {{ site.remote.prompt }} mv mpi4py* mpi4py        # rename the directory
> {{ site.remote.prompt }} cd mpi4py
> {{ site.remote.prompt }} python3 -m pip install --user .
> {{ site.remote.prompt }} cd ../amdahl
> {{ site.remote.prompt }} python3 -m pip install --user .
> ```
> {: .language-bash}
{: .discussion}

> ## If `pip` Raises a Warning...
>
> `pip` may warn that your user package binaries are not in your PATH.
>
> ```
> WARNING: The script amdahl is installed in "${HOME}/.local/bin" which is
> not on PATH. Consider adding this directory to PATH or, if you prefer to
> suppress this warning, use --no-warn-script-location.
> ```
> {: .warning}
>
> To check whether this warning is a problem, use `which` to search for the
> `amdahl` program:
>
> ```
> {{ site.remote.prompt }} which amdahl
> ```
> {: .language-bash}
>
> If the command returns no output, displaying a new prompt, it means the file
> `amdahl` has not been found. You must update the environment variable named
> `PATH` to include the missing folder.
> Edit your shell configuration file as follows, then log off the cluster and
> back on again so it takes effect.
>
> ```
> {{ site.remote.prompt }} nano ~/.bashrc
> {{ site.remote.prompt }} tail ~/.bashrc
> ```
> {: .language-bash}
> ```
> export PATH=${PATH}:${HOME}/.local/bin
> ```
> {: .output}
>
> After logging back in to {{ site.remote.login }}, `which` should be able to
> find `amdahl` without difficulties.
> If you had to load a Python module, load it again.
{: .discussion}

## Help!

Many command-line programs include a "help" message. Try it with `amdahl`:

```
{{ site.remote.prompt }} amdahl --help
```
{: .language-bash}

```
usage: amdahl [-h] [-p [PARALLEL_PROPORTION]] [-w [WORK_SECONDS]] [-t] [-e] [-j [JITTER_PROPORTION]]

optional arguments:
  -h, --help            show this help message and exit
  -p [PARALLEL_PROPORTION], --parallel-proportion [PARALLEL_PROPORTION]
                        Parallel proportion: a float between 0 and 1
  -w [WORK_SECONDS], --work-seconds [WORK_SECONDS]
                        Total seconds of workload: an integer greater than 0
  -t, --terse           Format output as a machine-readable object for easier analysis
  -e, --exact           Exactly match requested timing by disabling random jitter
  -j [JITTER_PROPORTION], --jitter-proportion [JITTER_PROPORTION]
                        Random jitter: a float between -1 and +1
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
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .language-bash}

Use `ls` to locate the output file. The `-t` flag sorts in
reverse-chronological order: newest first. What was the output?

> ## Read the Job Output
>
> The cluster output should be written to a file in the folder you launched the
> job from. For example,
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
> Doing 30.000 seconds of 'work' on 1 processor,
> which should take 30.000 seconds with 0.850 parallel proportion of the workload.
>
>   Hello, World! I am process 0 of 1 on {{ site.remote.node }}. I will do all the serial 'work' for 4.500 seconds.
>   Hello, World! I am process 0 of 1 on {{ site.remote.node }}. I will do parallel 'work' for 25.500 seconds.
>
> Total execution time (according to rank 0): 30.033 seconds
> ```
> {: .output}
{: .solution}

As we saw before, two of the `amdahl` program flags set the amount of work and
the proportion of that work that is parallel in nature. Based on the output, we
can see that the code uses a default of 30 seconds of work that is 85%
parallel. The program ran for just over 30 seconds in total, and if we run the
numbers, it is true that 15% of it was marked 'serial' and 85% was 'parallel'.

Since we only gave the job one CPU, this job wasn't really parallel: the same
processor performed the 'serial' work for 4.5 seconds, then the 'parallel' part
for 25.5 seconds, and no time was saved. The cluster can do better, if we ask.

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
{: .language-bash}

{% include {{ site.snippets }}/parallel/four-tasks-jobscript.snip %}

Then submit your job. Note that the submission command has not really changed
from how we submitted the serial job: all the parallel settings are in the
batch file rather than the command line.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} parallel-job.sh
```
{: .language-bash}

As before, use the status commands to check when your job runs.

```
{{ site.remote.prompt }} ls -t
```
{: .language-bash}
```
slurm-347178.out  parallel-job.sh  slurm-347087.out  serial-job.sh  amdahl  README.md  LICENSE.txt
```
{: .output}
```
{{ site.remote.prompt }} cat slurm-347178.out
```
{: .language-bash}
```
Doing 30.000 seconds of 'work' on 4 processors,
which should take 10.875 seconds with 0.850 parallel proportion of the workload.

  Hello, World! I am process 0 of 4 on {{ site.remote.node }}. I will do all the serial 'work' for 4.500 seconds.
  Hello, World! I am process 2 of 4 on {{ site.remote.node }}. I will do parallel 'work' for 6.375 seconds.
  Hello, World! I am process 1 of 4 on {{ site.remote.node }}. I will do parallel 'work' for 6.375 seconds.
  Hello, World! I am process 3 of 4 on {{ site.remote.node }}. I will do parallel 'work' for 6.375 seconds.
  Hello, World! I am process 0 of 4 on {{ site.remote.node }}. I will do parallel 'work' for 6.375 seconds.

Total execution time (according to rank 0): 10.888 seconds
```
{: .output}

> ## Is it 4× faster?
>
> The parallel job received 4× more processors than the serial job:
> does that mean it finished in ¼ the time?
>
> > ## Solution
> >
> > The parallel job did take _less_ time: 11 seconds is better than 30!
> > But it is only a 2.7× improvement, not 4×.
> >
> > Look at the job output:
> >
> > * While "process 0" did serial work, processes 1 through 3 did their
> >   parallel work.
> > * While process 0 caught up on its parallel work,
> >   the rest did nothing at all.
> >
> > Process 0 always has to finish its serial task before it can start on the
> > parallel work. This sets a lower limit on the amount of time this job will
> > take, no matter how many cores you throw at it.
> >
> > This is the basic principle behind [Amdahl's Law][amdahl], which is one way
> > of predicting improvements in execution time for a __fixed__ workload that
> > can be subdivided and run in parallel to some extent.
> {: .solution}
{: .challenge}

## How Much Does Parallel Execution Improve Performance?

In theory, dividing up a perfectly parallel calculation among _n_ MPI processes
should produce a decrease in total run time by a factor of _n_.
As we have just seen, real programs need some time for the MPI processes to
communicate and coordinate, and some types of calculations can't be subdivided:
they only run effectively on a single CPU.

Additionally, if the MPI processes operate on different physical CPUs in the
computer, or across multiple compute nodes, even more time is required for
communication than it takes when all processes operate on a single CPU.

In practice, it's common to evaluate the parallelism of an MPI program by

* running the program across a range of CPU counts,
* recording the execution time on each run,
* comparing each execution time to the time when using a single CPU.

Since "more is better" -- improvement is easier to interpret from increases in
some quantity than decreases -- comparisons are made using the speedup factor
_S_, which is calculated as the single-CPU execution time divided by the multi-CPU
execution time. For a perfectly parallel program, a plot of the speedup _S_
versus the number of CPUs _n_ would give a straight line, _S_ = _n_.

Let's run one more job, so we can see how close to a straight line our `amdahl`
code gets.

```bash
{{ site.remote.prompt }} nano parallel-job.sh
{{ site.remote.prompt }} cat parallel-job.sh
```

{% include {{ site.snippets }}/parallel/eight-tasks-jobscript.snip %}

Then submit your job. Note that the submission command has not really changed
from how we submitted the serial job: all the parallel settings are in the
batch file rather than the command line.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} parallel-job.sh
```
{: .language-bash}

As before, use the status commands to check when your job runs.

```
{{ site.remote.prompt }} ls -t
```
{: .language-bash}
```
slurm-347271.out  parallel-job.sh  slurm-347178.out  slurm-347087.out  serial-job.sh  amdahl  README.md  LICENSE.txt
```
{: .output}
```
{{ site.remote.prompt }} cat slurm-347178.out
```
{: .language-bash}
```
which should take 7.688 seconds with 0.850 parallel proportion of the workload.

  Hello, World! I am process 4 of 8 on {{ site.remote.node }}. I will do parallel 'work' for 3.188 seconds.
  Hello, World! I am process 0 of 8 on {{ site.remote.node }}. I will do all the serial 'work' for 4.500 seconds.
  Hello, World! I am process 2 of 8 on {{ site.remote.node }}. I will do parallel 'work' for 3.188 seconds.
  Hello, World! I am process 1 of 8 on {{ site.remote.node }}. I will do parallel 'work' for 3.188 seconds.
  Hello, World! I am process 3 of 8 on {{ site.remote.node }}. I will do parallel 'work' for 3.188 seconds.
  Hello, World! I am process 5 of 8 on {{ site.remote.node }}. I will do parallel 'work' for 3.188 seconds.
  Hello, World! I am process 6 of 8 on {{ site.remote.node }}. I will do parallel 'work' for 3.188 seconds.
  Hello, World! I am process 7 of 8 on {{ site.remote.node }}. I will do parallel 'work' for 3.188 seconds.
  Hello, World! I am process 0 of 8 on {{ site.remote.node }}. I will do parallel 'work' for 3.188 seconds.

Total execution time (according to rank 0): 7.697 seconds
```
{: .output}

> ## Non-Linear Output
>
> When we ran the job with 4 parallel workers, the serial job wrote its output
> first, then the parallel processes wrote their output, with process 0 coming
> in first and last.
>
> With 8 workers, this is not the case: since the parallel workers take less
> time than the serial work, it is hard to say which process will write its
> output first, except that it will _not_ be process 0!
{: .discussion}

Now, let's summarize the amount of time it took each job to run:

| Number of CPUs | Runtime (sec) |
| ---            | ---           |
| 1              | 30.033        |
| 4              | 10.888        |
| 8              |  7.697        |

Then, use the first row to compute speedups _S_, using Python as a command-line calculator:

```
{{ site.remote.prompt }} for n in 30.033 10.888 7.697; do python3 -c "print(30.033 / $n)"; done
```
{: .language-bash}

| Number of CPUs | Speedup | Ideal |
| ---            | ---     | ---   |
| 1              | 1.0     | 1     |
| 4              | 2.75    | 4     |
| 8              | 3.90    | 8     |

The job output files have been telling us that this program is performing 85%
of its work in parallel, leaving 15% to run in serial. This seems reasonably
high, but our quick study of speedup shows that in order to get a 4× speedup,
we have to use 8 or 9 processors in parallel. In real programs, the speedup
factor is influenced by

* CPU design
* communication network between compute nodes
* MPI library implementations
* details of the MPI program itself

Using Amdahl's Law, you can prove that with this program, it is _impossible_
to reach 8× speedup, no matter how many processors you have on hand. Details of
that analysis, with results to back it up, are left for the next class in the
HPC Carpentry workshop, _HPC Workflows_.

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
