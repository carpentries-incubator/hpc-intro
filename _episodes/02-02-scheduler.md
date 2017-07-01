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

> # Creating our test job
> 
> Using your favorite text editor, create the following script and run it.
>```
>#!/bin/bash
>
> echo 'This script is running on:'
> hostname
> sleep 120
>```
>
> Did it run on the cluster or just the login node?
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
   36856 <username> <account name> example-job.sh   R None      2017-07-01T16:47:02       0:11      59:49     1
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


