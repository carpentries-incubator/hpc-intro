---
title: Running a parallel job
teaching: 30
exercises: 60
---

::::::::::::::::::::::::::::::::::::::: objectives

- Prepare a job submission script for the parallel executable.
- Launch jobs with parallel execution.
- Record and summarize the timing and accuracy of jobs.
- Describe the relationship between job parallelism and performance.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do we execute a task in parallel?
- What benefits arise from parallel execution?
- What are the limits of gains from execution in parallel?

::::::::::::::::::::::::::::::::::::::::::::::::::


## Running the Job on a Compute Node

At this point, we have installed the `amdahl` executable on the
system, and can now run it on the cluster.

Create a submission file, requesting one task on a single node, then launch it.


```bash
[yourUsername@login1 ~]$ nano serial-job.sh
[yourUsername@login1 ~]$ cat serial-job.sh
```

```bash
#!/bin/bash
#SBATCH --job-name solo-job
#SBATCH --partition cpubase_bycore_b1
#SBATCH -N 1
#SBATCH -n 1

# Load the computing environment we need
module load Python

# Execute the task
amdahl
```

```bash
[yourUsername@login1 ~]$ sbatch serial-job.sh
```

As before, use the Slurm status commands to check whether your job
is running and when it ends:

```bash
[yourUsername@login1 ~]$ squeue -u yourUsername
```

Use `ls` to locate the output file. The `-t` flag sorts in
reverse-chronological order: newest first. What was the output?

:::::::::::::::  spoiler

## Read the Job Output

The cluster output should be written to a file in the folder you launched the
job from. For example,

```bash
[yourUsername@login1 ~]$ ls -t
```

```output
slurm-347087.out  serial-job.sh  amdahl  LICENSE  pyproject.toml  README.md
```

```bash
[yourUsername@login1 ~]$ cat slurm-347087.out
```

```output
Doing 30.000000 seconds of 'work' on 1 processor,
which should take 30.000000 seconds with 0.800000 parallel proportion of the workload.

  Hello, World! I am process 0 of 1 on smnode1. I will do all the serial 'work' for 7.021608 seconds.
  Hello, World! I am process 0 of 1 on smnode1. I will do parallel 'work' for 26.302983 seconds.

Total execution time (according to rank 0): 33.326056 seconds
```

:::::::::::::::::::::::::

As we saw before, two of the `amdahl` program flags set the amount of work and
the proportion of that work that is parallel in nature. Based on the output, we
can see that the code uses a default of 30 seconds of work that is 80%
parallel. The program ran for just over 30 seconds in total, and if we run the
numbers, it is true that 20% of it was marked 'serial' and 80% was 'parallel'.

Since we only gave the job one CPU, this job wasn't really parallel: the same
processor performed the 'serial' work for 7.02 seconds, then the 'parallel' part
for 26.30 seconds, and no time was saved. The cluster can do better, if we ask.

## Running the Parallel Job

The `amdahl` program uses the Message Passing Interface (MPI) for parallelism
-- this is a common tool on HPC systems.

:::::::::::::::::::::::::::::::::::::::::  callout

## What is MPI?

The Message Passing Interface is a set of tools which allow multiple tasks
running simultaneously to communicate with each other.
Typically, a single executable is run multiple times, possibly on different
machines, and the MPI tools are used to inform each instance of the
executable about its sibling processes, and which instance it is.
MPI also provides tools to allow communication between instances to
coordinate work, exchange information about elements of the task, or to
transfer data.
An MPI instance typically has its own copy of all the local variables.


::::::::::::::::::::::::::::::::::::::::::::::::::

While MPI-aware executables can generally be run as stand-alone programs, in
order for them to run in parallel they must use an MPI *run-time environment*,
which is a specific implementation of the MPI *standard*.
To activate the MPI environment, the program should be started via a command
such as `mpiexec` (or `mpirun`, or `srun`, etc. depending on the MPI run-time
you need to use), which will ensure that the appropriate run-time support for
parallelism is included.

:::::::::::::::::::::::::::::::::::::::::  callout

## MPI Runtime Arguments

On their own, commands such as `mpiexec` can take many arguments specifying
how many machines will participate in the execution,
and you might need these if you would like to run an MPI program on your
own (for example, on your laptop).
In the context of a queuing system, however, it is frequently the case that
MPI run-time will obtain the necessary parameters from the queuing system,
by examining the environment variables set when the job is launched.

::::::::::::::::::::::::::::::::::::::::::::::::::

Let's modify the job script to request more cores and use the MPI run-time.


```bash
[yourUsername@login1 ~]$ cp serial-job.sh parallel-job.sh
[yourUsername@login1 ~]$ nano parallel-job.sh
[yourUsername@login1 ~]$ cat parallel-job.sh
```

```bash
#!/bin/bash
#SBATCH --job-name parallel-job
#SBATCH --partition cpubase_bycore_b1
#SBATCH -N 1
#SBATCH -n 4

# Load the computing environment we need
# (mpi4py and numpy are in SciPy-bundle)
module load Python
module load SciPy-bundle

# Execute the task
mpiexec amdahl
```

Then submit your job. Note that the submission command has not really changed
from how we submitted the serial job: all the parallel settings are in the
batch file rather than the command line.

```bash
[yourUsername@login1 ~]$ sbatch parallel-job.sh
```

As before, use the status commands to check when your job runs.

```bash
[yourUsername@login1 ~]$ ls -t
```

```output
slurm-347178.out  parallel-job.sh  amdahl   pyproject.toml
slurm-347087.out  serial-job.sh    LICENSE  README.md
```

```bash
[yourUsername@login1 ~]$ cat slurm-347178.out
```

```output
Doing 30.000000 seconds of 'work' on 4 processors,
 which should take 12.000000 seconds with 0.800000 parallel proportion of the workload.

  Hello, World! I am process 0 of 4 on smnode1. I will do all the serial 'work' for 6.851971 seconds.
  Hello, World! I am process 2 of 4 on smnode1. I will do parallel 'work' for 6.726753 seconds.
  Hello, World! I am process 1 of 4 on smnode1. I will do parallel 'work' for 6.742398 seconds.
  Hello, World! I am process 3 of 4 on smnode1. I will do parallel 'work' for 6.782674 seconds.
  Hello, World! I am process 0 of 4 on smnode1. I will do parallel 'work' for 6.468167 seconds.

Total execution time (according to rank 0): 13.579746 seconds
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Is it 4× faster?

The parallel job received 4× more processors than the serial job:
does that mean it finished in ¼ the time?

:::::::::::::::  solution

## Solution

The parallel job did take *less* time: 11 seconds is better than 30!
But it is only a 2.7× improvement, not 4×.

Look at the job output:

- While "process 0" did serial work, processes 1 through 3 did their
  parallel work.
- While process 0 caught up on its parallel work,
  the rest did nothing at all.

Process 0 always has to finish its serial task before it can start on the
parallel work. This sets a lower limit on the amount of time this job will
take, no matter how many cores you throw at it.

This is the basic principle behind [Amdahl's Law][amdahl], which is one way
of predicting improvements in execution time for a **fixed** workload that
can be subdivided and run in parallel to some extent.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## How Much Does Parallel Execution Improve Performance?

In theory, dividing up a perfectly parallel calculation among *n* MPI processes
should produce a decrease in total run time by a factor of *n*.
As we have just seen, real programs need some time for the MPI processes to
communicate and coordinate, and some types of calculations can't be subdivided:
they only run effectively on a single CPU.

Additionally, if the MPI processes operate on different physical CPUs in the
computer, or across multiple compute nodes, even more time is required for
communication than it takes when all processes operate on a single CPU.

In practice, it's common to evaluate the parallelism of an MPI program by

- running the program across a range of CPU counts,
- recording the execution time on each run,
- comparing each execution time to the time when using a single CPU.

Since "more is better" -- improvement is easier to interpret from increases in
some quantity than decreases -- comparisons are made using the speedup factor
*S*, which is calculated as the single-CPU execution time divided by the multi-CPU
execution time. For a perfectly parallel program, a plot of the speedup *S*
versus the number of CPUs *n* would give a straight line, *S* = *n*.

Let's run one more job, so we can see how close to a straight line our `amdahl`
code gets.


```bash
[yourUsername@login1 ~]$ nano parallel-job.sh
[yourUsername@login1 ~]$ cat parallel-job.sh
```

```bash
#!/bin/bash
#SBATCH --job-name parallel-job
#SBATCH --partition cpubase_bycore_b1
#SBATCH -N 1
#SBATCH -n 8

# Load the computing environment we need
# (mpi4py and numpy are in SciPy-bundle)
module load Python
module load SciPy-bundle

# Execute the task
mpiexec amdahl
```

Then submit your job. Note that the submission command has not really changed
from how we submitted the serial job: all the parallel settings are in the
batch file rather than the command line.

```bash
[yourUsername@login1 ~]$ sbatch parallel-job.sh
```

As before, use the status commands to check when your job runs.

```bash
[yourUsername@login1 ~]$ ls -t
```

```output
slurm-347271.out     slurm-347178.out  serial-job.sh  LICENSE         README.md
parallel-job.sh      slurm-347087.out  amdahl         pyproject.toml
```

```bash
[yourUsername@login1 ~]$ cat slurm-347178.out
```

```output
Doing 30.000000 seconds of 'work' on 8 processors,
 which should take 9.000000 seconds with 0.800000 parallel proportion of the workload.

  Hello, World! I am process 4 of 8 on smnode1. I will do parallel 'work' for 3.157831 seconds.
  Hello, World! I am process 0 of 8 on smnode1. I will do all the serial 'work' for 6.031285 seconds.
  Hello, World! I am process 2 of 8 on smnode1. I will do parallel 'work' for 3.215214 seconds.
  Hello, World! I am process 1 of 8 on smnode1. I will do parallel 'work' for 3.524280 seconds.
  Hello, World! I am process 3 of 8 on smnode1. I will do parallel 'work' for 3.589039 seconds.
  Hello, World! I am process 5 of 8 on smnode1. I will do parallel 'work' for 3.501589 seconds.
  Hello, World! I am process 6 of 8 on smnode1. I will do parallel 'work' for 3.207707 seconds.
  Hello, World! I am process 7 of 8 on smnode1. I will do parallel 'work' for 3.071680 seconds.
  Hello, World! I am process 0 of 8 on smnode1. I will do parallel 'work' for 3.482018 seconds.

Total execution time (according to rank 0): 9.514393 seconds
```

::::::::::::::::::::::::::::::::::::::  discussion

## Non-Linear Output

When we ran the job with 4 parallel workers, the serial job wrote its output
first, then the parallel processes wrote their output, with process 0 coming
in first and last.

With 8 workers, this is not the case: since the parallel workers take less
time than the serial work, it is hard to say which process will write its
output first, except that it will *not* be process 0!

::::::::::::::::::::::::::::::::::::::::::::::::::

Now, let's summarize the amount of time it took each job to run:

| Number of CPUs | Runtime (sec) |
| -------------- | ------------- |
| 1              | 33\.326056    |
| 4              | 13\.579746    |
| 8              | 9\.514393     |

Then, use the first row to compute speedups $S$, using Python as a command-line
calculator and the formula

$$
S(t_{n}) = \frac{t_{1}}{t_{n}}
$$

```bash
[yourUsername@login1 ~]$ for n in 33.326056 13.579746 9.514393; do python3 -c "print(33.326056 / $n)"; done
```

| Number of CPUs | Speedup        | Ideal |
| -------------- | -------------- | ----- |
| 1              | 1\.0           | 1     |
| 4              | 2\.45          | 4     |
| 8              | 3\.50          | 8     |

The job output files have been telling us that this program is performing 80%
of its work in parallel, leaving 20% to run in serial. This seems reasonably
high, but our quick study of speedup shows that in order to get a 4× speedup,
we have to use 8 or 9 processors in parallel. In real programs, the speedup
factor is influenced by

- CPU design
- communication network between compute nodes
- MPI library implementations
- details of the MPI program itself

Using Amdahl's Law, you can prove that with this program, it is *impossible*
to reach 8× speedup, no matter how many processors you have on hand. Details of
that analysis, with results to back it up, are left for the next class in the
HPC Carpentry workshop, *HPC Workflows*.

In an HPC environment, we try to reduce the execution time for all types of
jobs, and MPI is an extremely common way to combine dozens, hundreds, or
thousands of CPUs into solving a single problem. To learn more about
parallelization, see the [parallel novice lesson][parallel-novice] lesson.


[amdahl]: https://en.wikipedia.org/wiki/Amdahl\'s_law
[parallel-novice]: https://www.hpc-carpentry.org/hpc-parallel-novice/


:::::::::::::::::::::::::::::::::::::::: keypoints

- Parallel programming allows applications to take advantage of parallel hardware.
- The queuing system facilitates executing parallel tasks.
- Performance improvements from parallel execution do not scale linearly.

::::::::::::::::::::::::::::::::::::::::::::::::::
