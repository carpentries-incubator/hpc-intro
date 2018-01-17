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
- "Be a good person and be nice to other users."
keypoints:
- "The smaller your job, the faster it will schedule."
- "Don't run stuff on the login node."
- "Again, don't run stuff on the login node."
- "Don't be a bad person and run stuff on the login node."
---

We now know virtually everything we need to know about getting stuff on a cluster.
We can log on, submit different types of jobs, use preinstalled software, 
and install and use software of our own.
What we need to do now is use the systems effectively.

## Estimating required resources using the scheduler

Although we covered requesting resources from the scheduler earlier,
how do we know how much and what type of resources we will need in the first place?

Answer: we don't. 
Not until we've tried it ourselves at least once.
We'll need to benchmark our job and experiment with it before
we know how much it needs in the way of resources.

The most effective way of figuring out how much resources a job needs is to submit a test job,
and then ask the scheduler how many resources it used.
A good rule of thumb is to ask the scheduler for more time and memory than your job can use.
This value is typically two to three times what you think your job will need.

> ## Benchmarking `fastqc`
> Create a job that runs the following command 
> in the same directory as `.fastq` files
> 
> ```
> fastqc name_of_fastq_file
> ```
> {: .bash}
> 
> The `fastqc` command is provided by the `fastqc` module.
> You'll need to figure out a good amount of resources to ask for for this first "test run".
> You might also want to have the scheduler email you to tell you when the job is done.
>
> Hint: the job only needs 1 cpu and not too much memory or time.
>  The trick is figuring out just how much you'll need!
{: .challenge}

Once the job completes (note that it takes much less time than expected),
we can query the scheduler to see how long our job took and what resources were used.
We will use `sacct` to get statistics about our job.

By itself, `sacct -u yourUsername` shows all commands that we ran 
since midnight on the previous day 
(we can change this behavior with the `--start-time` option).

```
sacct -u yourUsername
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

This shows all the jobs we ran recently 
(note that there are multiple entries per job).
To get detailed info about a job, 
we change our `sacct` command slightly
(`-j` corresponds to job id).

```
sacct -j 1965 -l
```
{: .bash}

It will show a ton of info, in fact, every single piece of info
collected on your job by the scheduler.
It may be useful to redirect this information to `less` to make it easier to view (use the left and right arrow keys to scroll through fields).

```
sacct -j 1965 -l | less
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

One very useful feature of SLURM is the ability to SSH 
to a node where a job is running and check how it's doing.
To do this, check where a job is running with `squeue`,
then run `ssh nodename`.

However, we can also check on stuff running on the login node right now the same way
(so it's not necessary to `ssh` to a node for this example).

### top

The best way to check current system stats is with `top`
(`htop` is a prettier version of `top` but may not be available on your system).

Some sample output from my laptop might look like the following:

```
Tasks: 296 total,   1 running, 295 sleeping,   0 stopped,   0 zombie
%Cpu(s):  4.3 us,  0.8 sy,  0.0 ni, 93.5 id,  0.8 wa,  0.4 hi,  0.3 si,  0.0 st
KiB Mem :  3948524 total,   119504 free,  1882172 used,  1946848 buff/cache
KiB Swap:  4083708 total,  3909192 free,   174516 used.  1084104 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                   
 1712 jeff      20   0 3189124 247912  87788 S  13.2  6.3   7:52.10 gnome-shell                                           
12958 jeff      20   0 1109104 141568  54128 S   5.0  3.6   2:15.18 tilix                                             
 2381 jeff      20   0 4209548 178632  29960 S   1.3  4.5   1:29.64 geary                                            
15150 jeff      20   0  153904   4216   3468 R   0.7  0.1   0:00.03 top                                               
   37 root      20   0       0      0      0 S   0.3  0.0   0:01.08 rcuos/3                                              
  612 root     -51   0       0      0      0 S   0.3  0.0   0:07.06 irq/28-INT55D5:                                        
 1326 root      20   0  448704   4928   2424 S   0.3  0.1   0:11.77 docker-containe                                        
13947 jeff      20   0  310624  18368  11556 S   0.3  0.5   0:01.11 hugo                                                      
14288 jeff      20   0  620256 105408  81212 S   0.3  2.7   0:02.33 vivaldi-bin                                             
    1 root      20   0  224048   7868   5452 S   0.0  0.2   0:01.99 systemd                                                   
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.01 kthreadd                                                
    4 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0:0H                                              
    6 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 mm_percpu_wq                                                   
    7 root      20   0       0      0      0 S   0.0  0.0   0:00.03 ksoftirqd/0         
```
{: .output}

Overview of the main fields:

* `PID` - What is the numerical id of each process?
* `USER` - Who started the process?
* `RES` - What is the amount of memory currently being used by a process?
* `%CPU` - How much of a CPU is each process using? Values higher than 100 percent indicate that a process is running in parallel.
* `%MEM` - What percent of system memory is a process using?
* `TIME+` - How much CPU time has a process used so far? Processes using 2 CPUs accumulate time at twice the normal rate.
* `COMMAND` - What command was used to launch a process?

### free

Another useful tool is the `free -h` command. 
This will show the currently used/free amount of memory.

```
free -h
```
{: .bash}
```
              total        used        free      shared  buff/cache   available
Mem:           3.8G        1.5G        678M        327M        1.6G        1.6G
Swap:          3.9G        170M        3.7G
```
{: .output}

This one is fairly easy to interpret, though keep in mind that `buff/cache` counts as free memory.

### ps 

To show all processes from your current session, type `ps`.

```
ps
```
{: .bash}
```
  PID TTY          TIME CMD
15113 pts/5    00:00:00 bash
15218 pts/5    00:00:00 ps
```
{: .output}

Note that this will only show processes from our current session. 
To show all processes of a user, regardless of a session, you can use `ps -ef` and grep for your username.

```
ps -ef | grep yourUsername
```
{: .bash}
```
jeff      1594     1  0 14:23 ?        00:00:00 /usr/lib/systemd/systemd --user
jeff      1599  1594  0 14:23 ?        00:00:00 (sd-pam)
jeff      1610     1  0 14:23 ?        00:00:01 /usr/bin/gnome-keyring-daemon --daemonize --login
jeff      1627  1586  0 14:23 tty2     00:00:00 /usr/libexec/gdm-wayland-session gnome-session
jeff      1629  1594  0 14:23 ?        00:00:01 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
jeff      1632  1627  0 14:23 tty2     00:00:00 /usr/libexec/gnome-session-binary
jeff      1692  1594  0 14:23 ?        00:00:00 /usr/libexec/gvfsd
```
{: .output}

This is useful for identifying which processes are doing what.

## Killing processes

To kill all of a certain type of process, you can run `killall commandName`.
`killall rsession` would kill all `rsession` processes created by RStudio,
for instance.
Note that you can only kill your own processes.

You can also kill processes by their PIDs using `kill 1234` where `1234` is a `PID`.
Sometimes however, killing a process does not work instantly.
To kill the process in the most hardcore manner possible, use the `-9` flag.
It's recommended to kill using without `-9` first.
This gives a process the chance to clean up child processes, and exit cleanly.
However, if a process just isn't responding, use `-9` to kill it instantly.

## Playing nice in the sandbox

You now have everything you need to run jobs, transfer files, use/install software,
and monitor how many resources your jobs are using.

So here are a couple final words to live by:

* Don't run jobs on the login node, though quick tests are generally fine. 
  A "quick test" is generally anything that uses less than 10GB of memory, 4 CPUs, and 15 minutes of time.
  Remember, the login node is to be shared with other users.

* If someone is being inappropriate and using the login node to run all of their stuff, 
  message an administrator to take a look at things and deal with them.

* Compress files before transferring to save file transfer times with large datasets.

* Use a VCS system like git to keep track of your code. Though most systems have some form
  of backup/archival system, you shouldn't rely on it for something as key as your research code.
  The best backup system is one you manage yourself.

* Before submitting a large run of jobs, submit one as a test first to make sure everything works.

* The less resources you ask for, the faster your jobs will find a slot in which to run.
  Lots of small jobs generally beat a couple big jobs.

* You can generally install software yourself, but if you want a shared installation of some kind,
  it might be a good idea to message an administrator.

* Always use the default compilers if possible. Newer compilers are great, but older stuff generally
  has less compatibility issues.
