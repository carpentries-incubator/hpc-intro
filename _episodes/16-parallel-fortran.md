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

We now have the tools we need to run a multi-processor job. This is a very
important aspect of HPC systems, as parallelism is one of the primary tools we
have to improve the performance of computational tasks.

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

{% include figure.html url="" caption="" max-width="40%"
   file="/fig/pi.png"
   alt="Algorithm for computing pi through random sampling" %}

## A Serial Solution to the Problem

We start from a Fortran program.
We want to allow the user to specify how many random points should be used
to calculate &#960; through a command-line parameter.
This program will only use a single CPU for its entire run, so it's classified
as a serial process.

Let's write a Fortran program, `pi.f90`, to estimate &#960; for us.

```
PROGRAM pi
        IMPLICIT NONE
        
        INTEGER(kind=8), PARAMETER :: n_samples = 100

END PROGRAM
```
{: .language-fortran}

We define a function `inside_circle` that accepts a single parameter
for the number of random points used to calculate &#960;.
It randomly samples points with both *x* and *y* on the half-open interval
[0, 1).
It then computes their distances from the origin (i.e., radii), and returns
how many of those distances were less than or equal to 1.0.
All of this is done using double-precision (64-bit)
floating-point values.

```
SUBROUTINE inside_circle(total_count,counter)
  IMPLICIT NONE
  INTEGER(kind=8) :: i
  REAL(kind=8) :: x
  REAL(kind=8) :: y
  INTEGER(kind=8), INTENT(OUT) :: counter
  INTEGER(kind=8), INTENT(IN)  :: total_count
  counter=0
  DO i = 1,total_count
    CALL random_number(x)
    CALL random_number(y)
    IF ((x**2 + y**2) .le. 1.0 ) THEN
      counter = counter +1
    END IF
  END DO

END SUBROUTINE
```
{: .language-fortran}

Next, we call the `inside_circle`  function from the main program and
calculate &#960; from its returned result.

```
PROGRAM pi
        IMPLICIT NONE

        INTEGER(kind=8), PARAMETER :: n_samples = 100
        INTEGER(kind=8) :: counter
        REAL(kind=8) :: pi_estimate

        CALL inside_circle(n_samples,counter)
        pi_estimate = 4.0*REAL( counter, kind(8))/REAL(n_samples,kind(8))
        PRINT *,'Estimate of pi is ',pi_estimate

END PROGRAM
```
{: .language-fortran}

If we compile and run the Fortran program, we should see the script print its estimate of
&#960;:

```
{{ site.local.prompt }} gfortran -o pi pi.f90
{{ site.local.prompt }} ./pi
3.10546875
```
{: .language-bash}

## Measuring Performance of the Serial Solution

The stochastic method used to estimate &#960; should converge on the true
value as the number of random points increases.
But as the number of points increases, the program requires more time.
Eventually, the time required may be too long to meet a deadline.
So we'd like to take some measurements of how much time the script
requires, and later take the same measurements after creating a parallel
version of the script to see the benefits of parallelizing the calculations
required.

### Estimating Calculation Time

Most of the calculations required to estimate &#960; are in the
`inside_circle` function:

1. Generating `n_samples` random values for `x` and `y`.
1. Calculating `n_samples` values of `radii` from `x` and `y`.
1. Counting how many values in `radii` are under 1.0.

There's also one multiplication operation and one division operation required
to convert the `counts` value to the final estimate of &#960; in the main
function.

A simple way to measure the calculation time is to use Fortran's `system_clock`
function to store the computer's current date and time before and after the
calculations, and calculate the difference between those times.

To add the time measurement to the script, modify the main program as follows, 
below the line `REAL(kind=8) :: pi_estimate` add

```
        REAL(kind=8) :: execution_time
        INTEGER(kind=4) :: start
        INTEGER(kind=4) :: finish
        INTEGER(kind=4) :: count_rate

        CALL system_clock(start,count_rate)
```
{: .language-fortran}

Then, add the following line immediately below the line calculating 
`pi_estimate = 4.0*REAL( counter, kind(8))/REAL(n_samples,kind(8))`:

```        
        CALL system_clock(finish,count_rate)
        execution_time = REAL(finish-start,kind(0d0))/REAL(count_rate,kind(0d0))
```
{: .language-fortran}


And finally, modify the `print` statement with the following:

```
PRINT *,'Estimate of pi is ',pi_estimate,' elapsed time ',execution_time,' s.'
```
{: .language-fortran}

The final Fortran program for the serial solution is:

```
SUBROUTINE inside_circle(total_count,counter)
  IMPLICIT NONE
  INTEGER(kind=8) :: i
  REAL(kind=8) :: x
  REAL(kind=8) :: y
  INTEGER(kind=8), INTENT(OUT) :: counter
  INTEGER(kind=8), INTENT(IN)  :: total_count
  counter=0
  DO i = 1,total_count
    CALL random_number(x)
    CALL random_number(y)
    IF ((x**2 + y**2) .le. 1.0 ) THEN
      counter = counter +1
    END IF
  END DO

END SUBROUTINE

PROGRAM pi
        IMPLICIT NONE

        INTEGER(kind=8), PARAMETER :: n_samples = 1000
        INTEGER(kind=8) :: counter
        REAL(kind=8) :: pi_estimate
        REAL(kind=8) :: execution_time
        INTEGER(kind=4) :: start
        INTEGER(kind=4) :: finish
        INTEGER(kind=4) :: count_rate

        CALL system_clock(start,count_rate)
        CALL inside_circle(n_samples,counter)
        pi_estimate = 4.0*REAL( counter, kind(8))/REAL(n_samples,kind(8))
        CALL system_clock(finish,count_rate)
        execution_time = REAL(finish-start,kind(0d0))/REAL(count_rate,kind(0d0))
        PRINT *,'Estimate of pi is ',pi_estimate,' elapsed time ',execution_time,' s.'

END PROGRAM
```
{: .language-fortran}

Run the script again with a few different values for the number of samples,
and see how the solution time changes:

```
{{ site.local.prompt }} gfortran -o pi pi.f90
{{ site.local.prompt }} ./pi 
```
{: .bash }


On a particular computer, one gets the following

| Number of points | Estimate of &#960; | Time for computation (s) |
| --               |  --                | --                       |
| 1000             | 3.1879999637603760 | 0.0000000000000000       |       
| 10000            | 3.1203999519348145 | 1.0000000000000000E-003  |
| 100000           | 3.1357200145721436 | 8.9999999999999993E-003  |
| 1000000          | 3.1394519805908203 | 0.10700000000000000      |
| 10000000         | 3.1417131423950195 | 0.70099999999999996      |
| 100000000        | 3.1415488719940186 | 6.5899999999999999       |   

Here we can see that the amount of time required scales approximately linearly
with the number of samples used.
There could be some variation in additional runs of the script with the same
number of samples, since the elapsed time is affected by other programs
running on the computer at the same time.
But if the script is the most computationally-intensive process running at the
time, its calculations are the largest influence on the elapsed time.

Now that we've developed our initial script to estimate &#960;, we can see
that as we increase the number of samples:

1. The estimate of &#960; tends to become more accurate.
1. The amount of time to calculate scales approximately linearly.

In general, achieving a better estimate of &#960; requires a greater number of
points.
Take a closer look at `inside_circle`: should we expect to get high accuracy
quickly on a single machine?

Probably not.

## Running the Serial Job on a Compute Node

Create a submission file, requesting one task on a single node and enough
memory to prevent the job from running out of memory:

```
{{ site.remote.prompt }} nano serial-pi.sh
{{ site.remote.prompt }} cat serial-pi.sh
```
{: .language-bash}

{% include {{ site.snippets }}/parallel/one-task-with-memory-jobscript.snip %}

Then submit your job. We will use the batch file to set the options,
rather than the command line.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} serial-pi.sh
```
{: .language-bash}

As before, use the status commands to check when your job runs.
Use `ls` to locate the output file, and examine it. Is it what you expected?

* How good is the value for &#960;?
* How long did the job take to run?

Modify the job script to increase both the number of samples requested 
(perhaps by a factor of 2, then by a factor of 10),
and resubmit the job each time.

* How good is the value for &#960;?
* How long did the job take to run?

A script could require enormous amounts of time to calculate on a single CPU.
To reduce the amount of time required,
we need to modify the script to use multiple CPUs for the calculations.
In the largest problem scales,
we could use multiple CPUs in multiple compute nodes,
distributing the memory requirements across all the nodes used to
calculate the solution.

## Running the Parallel Job

We will run an example that uses the Message Passing Interface (MPI) for
parallelism &mdash; this is a common tool on HPC systems.

> ## What is MPI?
>
> The Message Passing Interface is a set of tools which allow multiple parallel
> jobs to communicate with each other.
> Typically, a single executable is run multiple times, possibly on different
> machines, and the MPI tools are used to inform each instance of the
> executable about how many instances there are, which instance it is.
> MPI also provides tools to allow communication and coordination between
> instances.
> An MPI instance typically has its own copy of all the local variables.
{: .callout}

While MPI jobs can generally be run as stand-alone executables, in order for
them to run in parallel they must use an MPI *run-time system*, which is a
specific implementation of the MPI *standard*.
To do this, they should be started via a command such as `mpiexec` (or
`mpirun`, or `srun`, etc. depending on the MPI run-time you need to use),
which will ensure that the appropriate run-time support for parallelism is
included.

> ## MPI run-time arguments
>
> On their own, commands such as `mpiexec` can take many arguments specifying
> how many machines will participate in the execution,
> and you might need these if you would like to run an MPI program on your
> laptop (for example).
> In the context of a queuing system, however, it is frequently the case that
> we do not need to specify this information as the MPI run-time will have been
> configured to obtain it from the queuing system,
> by examining the environment variables set when the job is launched.
{: .callout}

> ## What changes are needed for an MPI version of the &#960; calculator?
>
> First, we need to import use the `MPI` module by
> adding an `USE MPI` line immediately below the `PROGRAM
> pi` line.
>
> Second, we need to modify the program to perform the overhead and
> accounting work required to:
>
> * subdivide the total number of points to be sampled,
> * *partition* the total workload among the various parallel processors
>   available,
> * have each parallel process report the results of its workload back
>   to the "rank 0" process,
>   which does the final calculations and prints out the result.
>
> The modifications to the serial script demonstrate four important concepts:
>
> * MPI_COMM_WORLD: the default MPI Communicator, providing a channel for all the
>   processes involved in this `mpiexec` to exchange information with one
>   another.
> * MPI_REDUCE: One rank collects all the results
> * Conditional Output: since every rank is running the *same code*, the
>   partitioning, the final calculations, and the `print` statement are
>   wrapped in a conditional so that only one rank performs these operations.
{: .discussion}


We modify the variable declaration lines to become
```
INTEGER(kind=8), PARAMETER :: n_samples = 100000000
INTEGER(kind=8) :: counter, my_counter, my_n_samples
REAL(kind=8) :: pi_estimate
REAL(kind=8) :: execution_time, start, finish
INTEGER(kind=4) :: ierr, myid, nprocs
```
{: .language-fortran}

Below the line `INTEGER(kind=4) :: ierr, myid, nprocs`,we add the lines:

```
! Initialize MPI
CALL MPI_INIT(ierr)
CALL MPI_COMM_RANK(MPI_COMM_WORLD, myid, ierr)
CALL MPI_COMM_SIZE(MPI_COMM_WORLD, nprocs, ierr)
```
{: .language-fortran}

immediately before the `n_samples` line to set up the MPI environment for
each process.

We replace the `start_time` and `counts` lines with the lines:

```
  IF ( myid .ne. 0 ) THEN
    my_n_samples = n_samples/nprocs
  ELSE
    start = MPI_WTIME()
    my_n_samples = n_samples - ( (nprocs-1)*(n_samples/nprocs) )
  ENDIF
```
{: .language-fortran}

This ensures that the rank 0 process measures times and does the
the residual work that has been left after distribution to all the ranks.



Illustrations of these steps are shown below.

---

Setup the MPI environment and initialize local variables &mdash; including the
vector containing the number of points to generate on each parallel processor:

{% include figure.html url="" caption="" max-width="50%"
   file="/fig/initialize.png"
   alt="MPI initialize" %}

Distribute the number of points from the originating vector to all the parallel
processors:

{% include figure.html url="" caption="" max-width="50%"
   file="/fig/scatter.png"
   alt="MPI scatter" %}

Perform the computation in parallel:

{% include figure.html url="" caption="" max-width="50%"
   file="/fig/compute.png"
   alt="MPI compute" %}

Retrieve counts from all the parallel processes:

{% include figure.html url="" caption="" max-width="50%"
   file="/fig/gather.png"
   alt="MPI gather" %}

Print out the report:

{% include figure.html url="" caption="" max-width="50%"
   file="/fig/finalize.png"
   alt="MPI finalize" %}

---

Finally, we'll ensure the `Print` line only runs on rank 0.
Otherwise, every parallel processor will print its local value,
and the report will become hopelessly garbled:

```
  IF(myid .eq. 0) THEN
    pi_estimate = 4.0*REAL( counter, kind(8))/REAL(n_samples,kind(8))
    finish = MPI_WTIME()
    execution_time = finish-start
    PRINT *,'Estimate of pi is ',pi_estimate,' elapsed time ',execution_time,' s.'
  ENDIF
  CALL MPI_FINALIZE(ierr)
```
{: .language-fortran}

A final commented version of MPI parallel Fortran code is available
[here](/files/pi-mpi.f90).

Our purpose here is to exercise the parallel workflow of the cluster.
Rather than push our local machines to the breaking point (or, worse, the login
node), let's give it to a cluster node with more resources.

Create a submission file, requesting more than one task on a single node:

```
{{ site.remote.prompt }} nano parallel-pi.sh
{{ site.remote.prompt }} cat parallel-pi.sh
```
{: .language-bash}

{% include {{ site.snippets }}/parallel/four-tasks-jobscript.snip %}

Then submit your job. We will use the batch file to set the options,
rather than the command line.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} parallel-pi.sh
```
{: .language-bash}

As before, use the status commands to check when your job runs.
Use `ls` to locate the output file, and examine it.
Is it what you expected?

* How good is the value for &#960;?
* How much faster was this run than the serial run with 100000000 points?

Modify the job script to increase both the number of samples requested 
(perhaps by a factor of 2, then by a factor of 10),
and resubmit the job each time.
You can also increase the number of CPUs.

* How good is the value for &#960;?
* How long did the job take to run?

## How Much Does MPI Improve Performance?

In theory, by dividing up the &#960; calculations among *n* MPI processes,
we should see run times reduce by a factor of *n*.
In practice, some time is required to start the additional MPI processes,
for the MPI processes to communicate and coordinate, and some types of
calculations may only be able to run effectively on a single CPU.

Additionally, if the MPI processes operate on different physical CPUs
in the computer, or across multiple compute nodes, additional time is
required for communication compared to all processes operating on a
single CPU.

[Amdahl's Law](https://en.wikipedia.org/wiki/Amdahl's_law) is one way of
predicting improvements in execution time for a **fixed** parallel workload.
If a workload needs 20 hours to complete on a single core,
and one hour of that time is spent on tasks that cannot be parallelized,
only the remaining 19 hours could be parallelized.
Even if an infinite number of cores were used for the parallel parts of
the workload, the total run time cannot be less than one hour.

In practice, it's common to evaluate the parallelism of an MPI program by

* running the program across a range of CPU counts,
* recording the execution time on each run,
* comparing each execution time to the time when using a single CPU.

The speedup factor *S* is calculated as the single-CPU execution time divided
by the multi-CPU execution time.
For a laptop with 8 cores, the graph of speedup factor versus number of cores
used shows relatively consistent improvement when using 2, 4, or 8 cores, but
using additional cores shows a diminishing return.

{% include figure.html url="" caption="" max-width="50%"
   file="/fig/laptop-mpi_Speedup_factor.png"
   alt="MPI speedup factors on an 8-core laptop" %}

For a set of HPC nodes containing 28 cores each, the graph of speedup factor
versus number of cores shows consistent improvements up through three nodes
and 84 cores, but **worse** performance when adding a fourth node with an
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
thousands of CPUs into solving a single problem.

{% include links.md %}
