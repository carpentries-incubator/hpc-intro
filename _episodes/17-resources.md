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
- "Understand problems and limitations involved in using multiple CPUs."
keypoints:
- As your task gets larger, so does the potential for inefficiencies.
- "The smaller your job (time, CPUs, memory, etc), the faster it will schedule."
- scaling testing involves running jobs with increasing resources and measuring the efficiency in order to establish a pattern informed descisions about future job submissions.
---
In previous episodes we covered *how* to request resources, but what you may not know is *what* resources you need to request. The solution to this problem is testing!
Understanding the resources you have available and how to use them most efficiently is a vital skill in high performance computing.

<table>
**Resource**	Asking for too much	Not asking for enough
Number of CPUs The job may wait in the queue for longer. Your fair share score will fall rapidly (your project will be charged for CPU cores that it reserved but didn't use)
The job will run more slowly than expected, and so may run out of time and get killed for exceeding its time limit.
**Memory**	
The job may wait in the queue for longer.
Your fair share score will fall more than necessary. (see here and here for information about how memory use is charged to projects)
Your job will fail, probably with an 'OUT OF MEMORY' error, segmentation fault or bus error. This may not happen immediately.
**Wall time**
The job may wait in the queue for longer than necessary
The job will run out of time and get killed. 
</table>

## Estimating Required Resources

How do we know what resources to ask for in our scripts? In general, unless the software
documentation or user testimonials provide some idea, we won't know how much
memory or compute time a program will need.

> ## Read the Documentation
>
> Most HPC facilities maintain documentation as a wiki, a website, or a
> document sent along when you register for an account. Take a look at these
> resources, and search for the software you plan to use: somebody might have
> written up guidance for getting the most out of it.
{: .callout}

The best way to determine the resources required for a job to run is to submit a test job,
and then ask the scheduler about its
impact using `{{ site.sched.hist }}`.

## Test Job

As you may have to run this a few times you want to spend as little time waiting as possible.
A test job should not run for more than 15mins. This could involve using a smaller input, coarser parameters or using a subset of the calculations.
As well as being quick to run, you want your test job to be quick to start (e.g. get through queue quickly), the best way to ensure this is keep the resources requested (memory, CPUs, time) small.
Similar as possible to actual jobs e.g. same functions etc.
Use same workflow. (most issues are caused by small issues, typos, missing files etc, your test job is a jood chance to sort out these issues.).
Make sure outputs are going somewhere you can see them.
> ## Serial Test
>
> Often a good first test to run, is to execute your job *serially* e.g. using only 1 CPU.
> This not only saves you time by being fast to start, but serial jobs can often be easier to debug.
> If you confirm your job works in its most simple state you can identify problems caused by
> paralellistaion much more easily.
{: .callout}

You generally should ask for 20% to 30% more time and memory than you think the job will use.
Testing allows you to become more more precise with your resource requests.


## Measuring Resource Usage of a Finished Job

<!-- New example maybe? -->
After the completion of our test job we will use the `{{ site.sched.hist }}` command.

```
{{ site.remote.prompt }} {{ site.sched.hist }}
```
{: .language-bash}

{% include {{ site.snippets }}/resources/account-history.snip %}

This shows all the jobs we ran recently (note that there are multiple entries
per job). To get info about a specific job, we change command slightly.

```
{{ site.remote.prompt }} {{ site.sched.hist }} {{ site.sched.flag.histdetail }} 1965
```
{: .language-bash}

It will show a lot of info, in fact, every single piece of info collected on
your job by the scheduler. It may be useful to redirect this information to
`less` to make it easier to view (use the left and right arrow keys to scroll
through fields).

```
{{ site.remote.prompt }} {{ site.sched.hist }} {{ site.sched.flag.histdetail }} 1965 | less
```
{: .language-bash}

Some interesting fields include the following:

* **Hostname**: Where did your job run?
* **MaxRSS**: What was the maximum amount of memory used?
* **Elapsed**: How long did the job take?
* **State**: What is the job currently doing/what happened to it?
* **MaxDiskRead**: Amount of data read from disk.
* **MaxDiskWrite**: Amount of data written to disk.

> ## `nn_seff`
>
> For convenince, we have provided the command `nn_seff <jobid>` to calculate **S**lurm **Eff**iciency (all NeSI commands start with `nn_`, for **N**eSI **N**IWA). 
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} nn_seff <jobid>
> > ```
> > {: .language-bash}
> > ```
> > Job ID: 22278992
> > Cluster: mahuika
> > User/Group: username/username
> > State: TIMEOUT (exit code 0)
> > Cores: 1
> > Tasks: 1
> > Nodes: 1
> > Job Wall-time:  100.33%  00:15:03 of 00:15:00 time limit
> > CPU Efficiency: 0.55%  00:00:05 of 00:15:03 core-walltime
> > Mem Efficiency: 0.20%  2.09 MB of 1.00 GB
> > ```
> > {: .output}
> >
> > If you were to submit this same job again what resources would you request?
> {: .solution}
{: .challenge}

## Measuring the System Load From Currently Running Tasks

Typically, clusters allow users to connect directly to compute nodes from the
head node. This is useful to check on a running job and see how it's doing, but
is not a recommended practice in general, because it bypasses the resource
manager. To reduce the risk of interfering with other users, some clusters will
only allow you to connect to nodes on which you have running jobs. Let's
practice by taking a look at what's running on the login node right now.

### Monitor System Processes With `htop`

The most reliable way to check current system stats is with `htop`. Some sample
output might look like the following (type `q` to exit `htop`):

```
{{ site.remote.prompt }} htop
```
{: .language-bash}

{% include {{ site.snippets }}/resources/monitor-processes-top.snip %}

Overview of the most important fields:

* `PID`: What is the numerical id of each process?
* `USER`: Who started the process?
* `RES`: What is the amount of memory currently being used by a process (in
  bytes)?
* `%CPU`: How much of a CPU is each process using? Values higher than 100
  percent indicate that a process is running in parallel.
* `%MEM`: What percent of system memory is a process using?
* `TIME+`: How much CPU time has a process used so far? Processes using 2 CPUs
  accumulate time at twice the normal rate.
* `COMMAND`: What command was used to launch a process?

If `htop` isn't available on your system `top` provides a similar (but less pretty) function.

```
{{ site.remote.prompt }} htop
```
{: .language-bash}

<!-- Now that you know the efficiency of your small test job what next? Throw 100 more CPUs at the problem for 100x speedup?

You can use this knowledge to set up the
next job with a closer estimate of its load on the system. A good general rule
is to ask the scheduler for 20% to 30% more time and memory than you expect the
job to need. This ensures that minor fluctuations in run time or memory use
will not result in your job being cancelled by the scheduler. Keep in mind that
if you ask for too much, your job may not run even though enough resources are
available, because the scheduler will be waiting for other people's jobs to
finish and free up the resources needed to match what you asked for. -->
## Scaling behaviour

Unfortunately we cannot assume speedup will be linear (e.g. double CPUs won't usually half runtime, double data won't necessarily double runtime) therefore more testing is required. This is called *scaling testing*.

The aim of these tests will be to establish how a jobs requirements change with size (CPUs, inputs) and ultemately figure out the best way to run your jobs.

Using the information we collected from the previous job, we will submit a larger version with our best estimates of requred resources.

Example here

Examine outputs

Repeat this processes several times until a pattern has been established.

Submit more, maybe a few at once.

Most jobs will look something like this

Under ideal scaling speedup increases 1:1 with number of CPUs. Embarrasingly paralell work will have ideal scaling.

Depending on the fraction of your code that is paralell, th

- start small.
- record everything.


<!-- ### `ps`

To show all processes from your current session, type `ps`.

```
{{ site.remote.prompt }} ps
```
{: .language-bash}

```
  PID TTY          TIME CMD
15113 pts/5    00:00:00 bash
15218 pts/5    00:00:00 ps
```
{: .output}

Note that this will only show processes from our current session. To show all
processes you own (regardless of whether they are part of your current session
or not), you can use `ps ux`.

```
{{ site.remote.prompt }} ps ux
```
{: .language-bash}

```
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
{{ site.remote.user }}  67780  0.0  0.0 149140  1724 pts/81   R+   13:51   0:00 ps ux
{{ site.remote.user }}  73083  0.0  0.0 142392  2136 ?        S    12:50   0:00 sshd: {{ site.remote.user }}@pts/81
{{ site.remote.user }}  73087  0.0  0.0 114636  3312 pts/81   Ss   12:50   0:00 -bash
```
{: .output}

This is useful for identifying which processes are doing what. -->

{% include links.md %}
