---
title: "Using a cluster: Scheduling jobs"
teaching: 0
exercises: 0
questions:
- "What is a scheduler?"
- "Why do we use a scheduler?"
- "How do we submit a job?"
objectives:
- "Submit a job and have it complete successfully."
- "Submit an interactive job."
keypoints:
- "The scheduler handles how compute resources are shared between users."
- "Everything you do should be run through the scheduler."
- "A job is just a shell script."
---

An HPC system might have thousands of nodes and thousands of users.
How do we decide who gets what and when?
How do we ensure that a task is run with the resources it needs?
This job is handled by a special piece of software called the scheduler.
On an HPC system, the scheduler manages which jobs run where and when.

The scheduler used in this lesson is SLURM.
Although SLURM is not used everywhere, 
running jobs is quite similar regardless of what software is being used.
The exact syntax might change, but the concepts remain the same.

## Running a batch job

The most basic use of the scheduler is to run a command non-interactively.
This is also referred to as batch job submission.
In this case, a job is just a shell script.
Let's create a demo shell script to run as a test.

> ## Creating our test job
> 
> Using your favorite text editor, create the following script and run it.
> Does it run on the cluster or just our login node?
>
>```
>#!/bin/bash
>
> echo 'This script is running on:'
> hostname
> sleep 120
>```
{: .challenge}

If you completed the previous challenge successfully, 
you probably realize that there is a distinction between 
running the job through the scheduler and just "running it".

To submit this job to the scheduler, we use the `sbatch` command.

```
sbatch example-job.sh
```
{: .bash}
```
Submitted batch job 36855
```
{: .output}

And that's all we need to do to submit a job. 
To check on our job's status, we use the command `squeue`.

```
squeue -u yourUsername
```
{: .bash}
```
   JOBID     USER ACCOUNT           NAME  ST REASON    START_TIME                TIME  TIME_LEFT NODES CPU
S
   36856 yourUsername yourAccount example-job.sh   R None      2017-07-01T16:47:02       0:11      59:49     1
1
```
{: .output}

We can see all the details of our job, most importantly that it is in the "R" or "RUNNING" state.
Sometimes our jobs might need to wait in a queue ("PENDING") or have an error.
The best way to check our job's status is with `squeue`.
Of course, running `squeue` repeatedly to check on things can be a little tiresome.
To see a real-time view of our jobs, we can use the `watch` command.
`watch` reruns a given command at 2-second intervals. 
Let's try using it to monitor another job.

```
sbatch example-job.sh
watch squeue -u yourUsername
```
{: .bash}

You should see an auto-updating display of your job's status.
When it finishes, it will disappear from the queue.
Press `Ctrl-C` when you want to stop the `watch` command.

## Customizing a job

The job we just ran used all of the schedulers default options.
In a real-world scenario, that's probably not what we want.
The default options represent a reasonable minimum.
Chances are, we will need more cores, more memory, more time, 
among other special considerations.
To get access to these resources we must customize our job script.

Comments in UNIX (denoted by `#`) are typically ignored.
But there are exceptions.
For instance the special `#!` comment at the beginning of scripts
specifies what program should be used to run it (typically `/bin/bash`).
Schedulers like SLURM also have a special comment used to denote special 
scheduler-specific options.
Though these comments differ from scheduler to scheduler, 
SLURM's special comment is `#SBATCH`.
Anything following the `#SBATCH` comment is interpreted as an instruction to the scheduler.

Let's illustrate this by example. 
By default, a job's name is the name of the script,
but the `-J` option can be used to change the name of a job.

Submit the following job (`sbatch example-job.sh`):

```
#!/bin/bash
#SBATCH -J new_name

echo 'This script is running on:'
hostname
sleep 120
```

```
squeue -u yourUsername
```
{: .bash}
```
   JOBID     USER ACCOUNT           NAME  ST REASON    START_TIME                TIME  TIME_LEFT NODES CPUS
   38191 yourUsername yourAccount       new_name  PD Priority  N/A                       0:00    1:00:00     1  1
```
{: .output}

Fantastic, we've successfully changed the name of our job!

> ## Setting up email notifications
> 
> Jobs on an HPC system might run for days or even weeks.
> We probably have better things to do than constantly check on the status of our job
> with `squeue`.
> Looking at the [online documentation for `sbatch`](https://slurm.schedmd.com/sbatch.html)
> (you can also google "sbatch slurm"),
> can you set up our test job to send you an email when it finishes?
> 
> Hint: you will need to use the `--mail-user` and `--mail-type` options.
{: .challenge}

### Resource requests

But what about more important changes, such as the number of CPUs and memory for our jobs?
One thing that is absolutely critical when working on an HPC system is specifying the 
resources required to run a job.
This allows the scheduler to find the right time and place to schedule our job.
If you do not specify requirements (such as the amount of time you need), 
you will likely be stuck with your site's default allocation,
which is not what we want.

The following are several key resource requests:

* **-c <ncpus>** - How many CPUs does your job need?

* **--mem <megabytes>** - How much memory on a node does your job need in megabytes? You can also specify gigabytes using by adding a little "g" afterwards (example: `--mem 5g`)

* **--time <days-hours:minutes:seconds>** - How much real-world time (walltime) will your job take to run? The `<days>` part can be omitted.

> ## Submitting resource requests
>
> Submit a job that will use 2 cpus, 4 gigabytes of memory, and 5 minutes of walltime.

Resource requests are typically binding.
If you exceed them, your job will be killed.
Let's use walltime as an example.
We will request 30 seconds of walltime, 
and attempt to run a job for two minutes.

```
#!/bin/bash
#SBATCH -t 0:0:30

echo 'This script is running on:'
hostname
sleep 120
```
