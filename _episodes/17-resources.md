---
title: "Using resources effectively"
teaching: 10
exercises: 30
questions:
- "How do we monitor our jobs?"
- "How can I get my jobs scheduled more easily?" 
objectives:
- "Understand how to look up job statistics and profile code."
- "Understand job size implications."
keypoints:
- "The smaller your job, the faster it will schedule."
---

We've touched on all the skills you need to interact with an HPC cluster: logging in over
SSH, loading software modules, submitting parallel jobs, and finding the output. Let's
exercise the latter steps, and learn about estimating resource usage and why it might
matter.

## Back to the Data

Nelle Nemo is a biologist studying gelatinous marine life in the region of the [North
Pacific Gyre]( https://en.wikipedia.org/wiki/North_Pacific_Gyre). She has sampled 1,520
creatures, and has run them through assay machines to determine the levels of 300
important proteins in each specimen. The machines generated a report for each assay with
300 rows that correspond to the measured concentration of each protein.

Nelle wants to gather a basic understanding of the protein concentrations by computing the
means and ranges for each, across the entire dataset. From the summary of [collective MPI
functions](https://mpi4py.readthedocs.io/en/stable/overview.html#collective-communications)
where she previously learned about Scatter and Gather, Nelle notices this line:

> * Global reduction operations such as sum, maximum, minimum, etc.
{: .quotation}

Intrigued, Nelle reads the documentation (and checks out some tutorials), finally coming
up with a parallel Python program to crunch the numbers. You can get it here: 
<{{ site.url }}{{ site.baseurl }}/files/goostats.py>

> ## Get `goostats.py`
>
> Please download `goostats.py` and transfer it to {{ site.remote.name }}.
>
> > ## Commands
> > 
> > 1. Download directly on {{ site.remote.name }}:
> >    ```
> >    {{ site.remote.prompt }} wget {{ site.url }}{{ site.baseurl }}/files/goostats.py
> >    ```
> >    {: .bash}
> > 2. Download locally, then upload through the firewall:
> >    ```
> >    {{ site.local.prompt }} wget {{ site.url }}{{ site.baseurl }}/files/goostats.py
> >    {{ site.local.prompt }} scp goostats.py {{ site.remote.user }}@{{ site.remote.login }}:~/
> >    ```
> >    {: .bash}
> {: .solution}
{: .challenge}

Nelle's program takes a folder path as input. It finds all the valid files in that folder,
distributing roughly equal numbers of files to all the parallel processes. All at once,
the processes load their assigned files into NumPy arrays, then compute the protein
statistics for the datasets known locally. Finally, a trio of MPI Reduce operations
computes the stats for all 300 proteins across all datasets, using the local stats
reported by each MPI process.

> ## How's it work?
>
> Take a look inside `goostats.py`. Can you identify the subroutine that performs each of
> these tasks? How does the program guard against invalid assay files?
>
> *Hint:* Start from the "main" function, defined toward the end of the file.
>
> > ## Solution
> >
> > The subroutines are defined roughly in order, with some small extra helpers.
> > 
> > 1. The program gets the path to scan by reading the first command line argument,
> >    provided by the system as the second item in the `argv` list, or `argv[1]`.
> > 2. The `get_local_file_names` function has rank 0 scan through the directory and
> >    build a list of files matching Nelle's naming scheme. Files ending with "Z" are
> >    excluded. It then uses NumPy to divide that list into a number of roughly-equal
> >    pieces, one for each rank. All processes then participate in a call to the MPI
> >    Scatter function, which simultaneously sends each rank its own private list of
> >    files. Rank 0 even sends one to itself.
> > 3. Each rank calls `get_assay_results` to read the contents of each file into a NumPy
> >    array. If the array contains 300 numbers, it gets saved in the list of results.
> > 4. Each rank then calls one of three NumPy functions on the list of returned results.
> >    These functions apply the specified operation to the rows, i.e. files, to report
> >    300-element NumPy arrays of computed values.
> > 5. Since MPI Reduce has no option to compute an average, the sum is used instead,
> >    followed by division by the total number of values.
> > 6. After the Reduce operations complete, the root process (rank 0) holds the average,
> >    minimum, and maximum concentrations of the 300 proteins from all the valid reports
> >    in the specified folder. It stores these in a comma-separated value file,
> >    which is given the folder name with a "csv" extension.
> {: .solution}
{: .discussion}

After running `goostats.py`, Nelle will have a single CSV file summarizing the entire
dataset. She has some ideas to expand the analysis, perhaps computing the standard
deviation as well.

Nelle is concerned about the resource requirements of the program. While it processes the
test folder in less than a second, processing all 1,520 files, and doing more work for
each one as she has planned, could be disastrous for her laptop. We can estimate the
memory footprint, since the number of values is known ahead of time. Assuming
double-precision numbers, the entire dataset by itself has a memory footprint of (1520
files &times; 300 numbers per file &times; 64 bits per number) &#247; (8 bits per
byte &times; 1024&sup2; bytes per MB) = 3.5 MB. Even if Python keeps dozens of copies
in memory at once, memory won't be a problem. The runtime, on the other hand, can be
extremely difficult to estimate, especially as Nelle adds features. Perhaps of greater
concern is the fact that the program opens thousands of files, almost all at once. Even
with a local solid-state hard drive, reading data will probably take longer than crunching
the numbers. On a networked filesystem, this could create a real problem.

## Estimating required resources using the scheduler

Although we covered requesting resources from the scheduler earlier with the π code, how
do we know what type of resources the software will need in the first place, and its
demand for each? In general, unless the software documentation or user testimonials
provide some idea, we don't up front how much memory or compute time a program will need.

> ## Read the Documentation
>
> Most HPC facilities maintain documentation as a wiki, a website, or a document sent along
> when you register for an account. Take a look at these resources, and search for the
> software you plan to use: somebody might have written up guidance for getting the most
> out of it.
{: .callout}

A convenient way of figuring out the resources required for a job to run successfully is
to submit a test job, and then ask the scheduler about its impact using `{{
site.sched.hist }}`. You can use this knowledge to set up the next job with a closer
estimate of its load on the system. A good general rule is to ask the scheduler for 20% to
30% more time and memory than you expect the job to need. This ensures that minor
fluctuations in run time or memory use will not result in your job being cancelled by the
scheduler. Keep in mind that if you ask for too much, your job may not run even though
enough resources are available, because the scheduler will be waiting for other people's
jobs to finish and free up the resources needed to match what you asked for.


```
{{ site.remote.prompt }} nano parallel-goostats.sh
{{ site.remote.prompt }} cat parallel-goostats.sh
```
{: .bash}

```
#!/bin/bash
{{ site.sched.comment }} {{ site.sched.flag.name }} parallel-goostats
{{ site.sched.comment }} {{ site.sched.flag.queue }} {{ site.sched.queue.testing }}
{% include {{ site.snippets }}/parallel/four-tasks.snip %}
module load python3
mpirun ./goostats.py hpc-intro-data/north-pacific-gyre
```
{: .output}

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} parallel-goostats.sh
```
{: .bash}


## Stats

Once the job completes (note that it takes much less time than expected), we can query the
scheduler to see how long our job took and what resources were used. We will use `{{
site.sched.hist }}` to get statistics about our job.

```
{{ site.remote.prompt }} {{ site.sched.hist }}
```
{: .bash}

{% include {{ site.snippets }}/resources/account-history.snip %}

This shows all the jobs we ran recently (note that there are multiple entries per job). To
get info about a specific job, we change command slightly.

```
{{ site.remote.prompt }} {{ site.sched.hist }} {{ site.sched.flag.histdetail }} 1965
```
{: .bash}

It will show a lot of info, in fact, every single piece of info collected on your job by
the scheduler. It may be useful to redirect this information to `less` to make it easier
to view (use the left and right arrow keys to scroll through fields).

```
{{ site.remote.prompt }} {{ site.sched.hist }} {{ site.sched.flag.histdetail }} 1965 | less
```
{: .bash}

Some interesting fields include the following:

* **Hostname**: Where did your job run?
* **MaxRSS**: What was the maximum amount of memory used?
* **Elapsed**: How long did the job take?
* **State**: What is the job currently doing/what happened to it?
* **MaxDiskRead**: Amount of data read from disk.
* **MaxDiskWrite**: Amount of data written to disk.

## Measuring the statistics of currently running tasks

> ## Connecting to Nodes
>
> Typically, clusters allow users to connect directly to compute nodes from the head node.
> This is useful to check on a running job and see how it's doing, but is not a
> recommended practice in general, because it bypasses the resource manager.
>
> If you need to do this, check where a job is running with `{{ site.sched.status }}`, then
> run `ssh nodename`.
>
> Give it a try!
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} ssh {{ site.sched.node }}
> > ```
> > {: .bash}
> {: .solution}
{: .challenge}

We can also check on stuff running on the login node right now the same way (so it's not
necessary to `ssh` to a node for this example).

### Monitor system processes with `top`

The most reliable way to check current system stats is with `top`. Some sample output
might look like the following (type `q` to exit `top`):

```
{{ site.remote.prompt }} top
```
{: .bash}

{% include {{ site.snippets }}/resources/monitor-processes-top.snip %}

Overview of the most important fields:

* `PID`: What is the numerical id of each process?
* `USER`: Who started the process?
* `RES`: What is the amount of memory currently being used by a process (in bytes)?
* `%CPU`: How much of a CPU is each process using? Values higher than 100 percent indicate that a
  process is running in parallel.
* `%MEM`: What percent of system memory is a process using?
* `TIME+`: How much CPU time has a process used so far? Processes using 2 CPUs accumulate time at
  twice the normal rate.
* `COMMAND`: What command was used to launch a process?

`htop` provides an overlay for `top` using [curses](
https://en.wikipedia.org/wiki/Curses_(programming_library)), producing a better-organized
and "prettier" dashboard in your terminal. Unfortunately, it is not always available. If
this is the case, ask your system administrators to install it for you. Don't be shy,
they're here to help!

### `ps`

To show all processes from your current session, type `ps`.

```
{{ site.remote.prompt }} ps
```
{: .bash}

```
  PID TTY          TIME CMD
15113 pts/5    00:00:00 bash
15218 pts/5    00:00:00 ps
```
{: .output}

Note that this will only show processes from our current session. To show all processes
you own (regardless of whether they are part of your current session or not), you can use
`ps ux`.

```
{{ site.remote.prompt }} ps ux
```
{: .bash}

```
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
{{ site.remote.user }}  67780  0.0  0.0 149140  1724 pts/81   R+   13:51   0:00 ps ux
{{ site.remote.user }}  73083  0.0  0.0 142392  2136 ?        S    12:50   0:00 sshd: {{ site.remote.user }}@pts/81
{{ site.remote.user }}  73087  0.0  0.0 114636  3312 pts/81   Ss   12:50   0:00 -bash
```
{: .output}

This is useful for identifying which processes are doing what.
