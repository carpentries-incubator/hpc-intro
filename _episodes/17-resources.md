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
learn about estimating resource usage and why it might matter.

## Estimating required resources using the scheduler

Although we covered requesting resources from the scheduler earlier with the &#960; code,
how do we know what type of resources the software will need in the first place, and its
demand for each? In general, unless the software documentation or user testimonials
provide some idea, we won't know how much memory or compute time a program will need.

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

## Stats

Since we already submitted `pi.py` to run on the cluster, we can query the scheduler to
see how long our job took and what resources were used. We will use `{{ site.sched.hist
}}` to get statistics about `parallel-pi.sh`.

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

## Measuring the system load from currently running tasks

Typically, clusters allow users to connect directly to compute nodes from the head node.
This is useful to check on a running job and see how it's doing, but is not a
recommended practice in general, because it bypasses the resource manager.
To reduce the risk of interfering with other users, some clusters will only allow you to connect to nodes on which you have running jobs.
Let's practice by taking a look at what's running on the login node right now.

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
* `%CPU`: How much of a CPU is each process using? Values higher than 100 percent indicate
  that a process is running in parallel.
* `%MEM`: What percent of system memory is a process using?
* `TIME+`: How much CPU time has a process used so far? Processes using 2 CPUs accumulate
  time at twice the normal rate.
* `COMMAND`: What command was used to launch a process?

`htop` provides an overlay for `top` using [curses](
https://en.wikipedia.org/wiki/Curses_(programming_library)), producing a better-organized
and "prettier" dashboard in your terminal. Unfortunately, it is not always available. If
this is the case, ask your system administrators to install it for you. Don't be shy,
they're here to help!

```
{{ site.remote.prompt }} htop
```
{: .bash}


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
