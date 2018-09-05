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
then ask the scheduler how many resources it used. A good rule of thumb is to ask the scheduler for
more time and memory than your job can use. This value is typically two to three times what you
think your job will need.

> ## Benchmarking `fastqc`
>
> Create a job that runs the following command in the same directory as `.fastq` files
> 
> ```
> fastqc name_of_fastq_file
> ```
> {: .bash}
> 
> The `fastqc` command is provided by the `fastqc` module. You'll need to figure out a good amount
> of resources to ask for for this first "test run". You might also want to have the scheduler email
> you to tell you when the job is done.
>
> Hint: the job only needs 1 CPU and not too much memory or time. The trick is figuring out just how
>  much you'll need!
{: .challenge}

Once the job completes (note that it takes much less time than expected), we can query the scheduler
to see how long our job took and what resources were used. We will use `sacct` to get statistics
about our job.

By itself, `sacct -u yourUsername` shows all commands that we ran since midnight on the previous day
(we can change this behaviour with the `--start-time` option).

```
[remote]$ sacct -u yourUsername
```
{: .bash}
```
      JobID    JobName  Partition    Account  AllocCPUS      State ExitCode 
------------ ---------- ---------- ---------- ---------- ---------- --------
1964               bash   standard    default          1  COMPLETED      0:0
1964.extern      extern               default          1  COMPLETED      0:0
1964.0             bash               default          1  COMPLETED      0:0
1965         build-ind+ summer-sc+    default          1  COMPLETED      0:0
1965.batch        batch               default          1  COMPLETED      0:0
1965.extern      extern               default          1  COMPLETED      0:0
```
{: .output}

This shows all the jobs we ran recently (note that there are multiple entries per job). To get
detailed info about a job, we change our `sacct` command slightly (`-j` corresponds to job id).

```
[remote]$ sacct -j 1965 -l
```
{: .bash}

It will show a ton of info, in fact, every single piece of info collected on your job by the
scheduler. It may be useful to redirect this information to `less` to make it easier to view (use
the left and right arrow keys to scroll through fields).

```
[remote]$ sacct -j 1965 -l | less
```
{: .bash}

Some interesting fields include the following:

* **Hostname** - Where did your job run?
* **MaxRSS** - What was the maximum amount of memory used?
* **Elapsed** - How long did the job take?
* **State** - What is the job currently doing/what happened to it?
* **MaxDiskRead** - Amount of data read from disk.
* **MaxDiskWrite** - Amount of data written to disk.

## Measuring the statistics of currently running tasks

One very useful feature of SLURM is the ability to SSH to a node where a job is running and check
how it's doing. To do this, check where a job is running with `squeue`, then run `ssh nodename`.

However, we can also check on stuff running on the login node right now the same way (so it's not
necessary to `ssh` to a node for this example).

### top

The best way to check current system stats is with `top` (`htop` is a prettier version of `top` but
may not be available on your system).

Some sample output from my laptop might look like the following (`Ctrl + c` to exit):

```
top
```
{: .bash}
```
top - 21:00:19 up  3:07,  1 user,  load average: 1.06, 1.05, 0.96
Tasks: 311 total,   1 running, 222 sleeping,   0 stopped,   0 zombie
%Cpu(s):  7.2 us,  3.2 sy,  0.0 ni, 89.0 id,  0.0 wa,  0.2 hi,  0.2 si,  0.0 st
KiB Mem : 16303428 total,  8454704 free,  3194668 used,  4654056 buff/cache
KiB Swap:  8220668 total,  8220668 free,        0 used. 11628168 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 1693 jeff      20   0 4270580 346944 171372 S  29.8  2.1   9:31.89 gnome-shell
 3140 jeff      20   0 3142044 928972 389716 S  27.5  5.7  13:30.29 Web Content
 3057 jeff      20   0 3115900 521368 231288 S  18.9  3.2  10:27.71 firefox
 6007 jeff      20   0  813992 112336  75592 S   4.3  0.7   0:28.25 tilix
 1742 jeff      20   0  975080 164508 130624 S   2.0  1.0   3:29.83 Xwayland
    1 root      20   0  230484  11924   7544 S   0.3  0.1   0:06.08 systemd
   68 root      20   0       0      0      0 I   0.3  0.0   0:01.25 kworker/4:1
 2913 jeff      20   0  965620  47892  37432 S   0.3  0.3   0:11.76 code
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.02 kthreadd
```
{: .output}

Overview of the most important fields:

* `PID` - What is the numerical id of each process?
* `USER` - Who started the process?
* `RES` - What is the amount of memory currently being used by a process (in bytes)?
* `%CPU` - How much of a CPU is each process using? Values higher than 100 percent indicate that a
  process is running in parallel.
* `%MEM` - What percent of system memory is a process using?
* `TIME+` - How much CPU time has a process used so far? Processes using 2 CPUs accumulate time at
  twice the normal rate.
* `COMMAND` - What command was used to launch a process?

### free

Another useful tool is the `free -h` command. This will show the currently used/free amount of
memory.

```
$ free -h
```
{: .bash}
```
              total        used        free      shared  buff/cache   available
Mem:           3.8G        1.5G        678M        327M        1.6G        1.6G
Swap:          3.9G        170M        3.7G
```
{: .output}

The key fields here are total, used, and available - which represent the amount of memory that the
machine has in total, how much is currently being used, and how much is still available. When a
computer runs out of memory it will attempt to use "swap" space on your hard drive instead. Swap
space is very slow to access - a computer may appear to "freeze" if it runs out of memory and begins
using swap.

### ps 

To show all processes from your current session, type `ps`.

```
$ ps
```
{: .bash}
```
  PID TTY          TIME CMD
15113 pts/5    00:00:00 bash
15218 pts/5    00:00:00 ps
```
{: .output}

Note that this will only show processes from our current session. To show all processes you own
(regardless of whether they are part of your current session or not), you can use `ps -ef` and
`grep` for your username.

```
$ ps -ef | grep yourUsername
```
{: .bash}
```
jeff      1594     1  0 14:23 ?        00:00:00 /usr/lib/systemd/systemd --user
jeff      1599  1594  0 14:23 ?        00:00:00 (sd-pam)
jeff      1610     1  0 14:23 ?        00:00:01 /usr/bin/gnome-keyring-daemon --daemonize --login
jeff      1627  1586  0 14:23 tty2     00:00:00 /usr/libexec/gdm-wayland-session gnome-session
jeff      1629  1594  0 14:23 ?        00:00:01 /usr/bin/dbus-daemon --session --address=systemd:...
jeff      1632  1627  0 14:23 tty2     00:00:00 /usr/libexec/gnome-session-binary
jeff      1692  1594  0 14:23 ?        00:00:00 /usr/libexec/gvfsd
```
{: .output}

This is useful for identifying which processes are doing what.

## Killing processes

To kill all of a certain type of process, you can run `killall commandName`. `killall rsession`
would kill all `rsession` processes created by RStudio, for instance. Note that you can only kill
your own processes.

You can also kill processes by their PIDs using `kill 1234` where `1234` is a `PID`. Sometimes
however, killing a process does not work instantly. To kill the process in the most hardcore manner
possible, use the `-9` flag. It's recommended to kill using without `-9` first. This gives a process
the chance to clean up child processes, and exit cleanly. However, if a process just isn't
responding, use `-9` to kill it instantly.

{% include links.md %}
