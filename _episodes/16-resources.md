---
title: "Using resources effectively"
teaching: 15
exercises: 10
questions:
- "How do we monitor our jobs?"
- "How can I get my jobs scheduled more easily?" 
objectives:
- "Understand how to look up job statistics and profile code."
- "Understand job size implications."
keypoints:
- "The smaller your job, the faster it will schedule."
---

We now know virtually everything we need to know about getting stuff on a cluster. We can log on,
submit different types of jobs, use preinstalled software, and install and use software of our own.
What we need to do now is use the systems effectively.

## Estimating required resources using the scheduler

Although we covered requesting resources from the scheduler earlier, how do we know how much and
what type of resources we will need in the first place?

Answer: we don't. Not until we've tried it ourselves at least once. We'll need to benchmark our job
and experiment with it before we know how much it needs in the way of resources.

The most effective way of figuring out how much resources a job needs is to submit a test job, and
then ask the scheduler how many resources it used.

A good rule of thumb is to ask the scheduler for more time and memory than you expect your job to
need. This ensures that minor fluctuations in run time or memory use will not result in your job
being canceled by the scheduler. Recommendations for how much extra to ask for vary but 10% is 
probably the minimum, with 20-30% being more typical. Keep in mind that if you ask for too much,
your job may not run even though enough resources are available, because the scheduler will be
waiting to match what you asked for.

> ## Benchmarking `fastqc`
>
> Create a job that runs the following command in the same directory as the `.fastq` files
> 
> ```
> {{site.remote.prompt }} fastqc name_of_fastq_file
> ```
> {: .bash}
> 
> The `fastqc` command is provided by the `fastqc` module. You'll need to figure out a good amount
> of resources to allocate for this first "test run". You might also want to have the scheduler 
> email you to tell you when the job is done.
>
> *Hint:* The job only needs 1 CPU and not too much memory or time. The trick is figuring out just 
> how much you'll need!
>
> > ## Solution
> >
> > First, write the {{ site.sched.name }} script to run `fastqc` on the
> > file supplied at the command-line.
> >
> > ```
> > {{ site.remote.prompt }} cat fastqc-job.sh
> > ```
> > {: .bash}
> >
> > ```
> > #!/bin/bash
> > {{ site.sched.comment }} {{ site.sched.flag.time }} 00:10:00
> >
> > fastqc $1
> > ```
> >
> > Now, create and run a script to launch a job for each `.fastq` file.
> >
> > ```
> > {{ site.remote.prompt }} cat fastqc-launcher.sh
> > ```
> > {: .bash}
> >
> > ```
> > for f in *.fastq
> > do
> >     {{ site.sched.submit.name }} {{ site.sched.submit.options }} fastqc-job.sh $f
> > done 
> > ```
> > {: .output}
> >
> > ```
> > {{ site.remote.prompt }} chmod +x fastqc-launcher.sh
> > {{ site.remote.prompt }} ./fastqc-launcher.sh
> > ```
> > {: .bash}
> {: .solution}
{: .challenge}

Once the job completes (note that it takes much less time than expected), we can query the scheduler
to see how long our job took and what resources were used. We will use `{{ site.sched.hist }}` to
get statistics about our job.

```
{{ site.remote.prompt }} {{ site.sched.hist }}
```
{: .bash}

{% include {{ site.snippets }}/16/stat_output.snip %}

This shows all the jobs we ran recently (note that there are multiple entries per job). To get
detailed info about a job, we change command slightly.

```
{{ site.remote.prompt }} {{ site.sched.hist }} {{ site.sched.flag.histdetail }} 1965
```
{: .bash}

It will show a lot of info, in fact, every single piece of info collected on your job by the
scheduler. It may be useful to redirect this information to `less` to make it easier to view (use
the left and right arrow keys to scroll through fields).

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
> Typically, clusters allow users to connect directly to compute nodes from the head 
> node. This is useful to check on a running job and see how it's doing, but is not
> a recommended practice in general, because it bypasses the resource manager.
>
> If you need to do this, check where a job is running with `{{ site.sched.status }}`, then
> run `ssh nodename`.
>
> Give it a try!
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} ssh {{ site.remote.node }}
> > ```
> > {: .bash}
> {: .solution}
{: .challenge}

We can also check on stuff running on the login node right now the same way (so it's 
not necessary to `ssh` to a node for this example).

### Monitor system processes with `top`

The most reliable way to check current system stats is with `top`. Some sample output might look
like the following (`Ctrl + c` to exit):

```
{{ site.remote.prompt }} top
```
{: .bash}

{% include {{ site.snippets }}/16/top_output.snip %}

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

`htop` provides a [curses]()-based overlay for `top`, producing a better-organized and "prettier"
dashboard in your terminal. Unfortunately, it is not always available. If this is the case,
*politely* ask your system administrators to install it for you.

### Check memory load with `free`

Another useful tool is the `free -h` command. This will show the currently used/free amount of
memory.

```
{{ site.remote.prompt }} free -h
```
{: .bash}

{% include {{ site.snippets }}/16/free_output.snip %}

The key fields here are total, used, and available - which represent the amount of memory that the
machine has in total, how much is currently being used, and how much is still available. When a
computer runs out of memory it will attempt to use "swap" space on your hard drive instead. Swap
space is very slow to access - a computer may appear to "freeze" if it runs out of memory and 
begins using swap. However, compute nodes on HPC systems usually have swap space disabled so when
they run out of memory you usually get an "Out Of Memory (OOM)" error instead.

### `ps `

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

Note that this will only show processes from our current session. To show all processes you own
(regardless of whether they are part of your current session or not), you can use `ps ux`.

```
{{ site.remote.prompt }} ps ux
```
{: .bash}

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
auser  67780  0.0  0.0 149140  1724 pts/81   R+   13:51   0:00 ps ux
auser  73083  0.0  0.0 142392  2136 ?        S    12:50   0:00 sshd: auser@pts/81
auser  73087  0.0  0.0 114636  3312 pts/81   Ss   12:50   0:00 -bash
```
{: .output}

This is useful for identifying which processes are doing what.

## Killing processes

To kill all of a certain type of process, you can run `killall commandName`. For example,

```
{{ site.remote.prompt }} killall rsession
```
{: .bash}

would kill all `rsession` processes created by RStudio. Note that you can only kill
your own processes.

You can also kill processes by their PIDs. For example, your `ssh` connection to the server is
listed above with PID 73083. If you wish to close that connection forcibly, you could `kill 73083`.

Sometimes, killing a process does not work instantly. To kill the process in the most aggressive
manner possible, use the `-9` flag, i.e., `kill -9 73083`. It's recommended to kill using without
`-9` first: this sends the process a "terminate" signal (`SIGTERM`), giving it the chance to clean
up child processes and exit cleanly. However, if a process just isn't responding, use `-9` to
terminate it instantly (`SIGKILL`).

{% include links.md %}
