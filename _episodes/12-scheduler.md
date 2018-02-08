---
title: "Scheduling jobs"
teaching: 45
exercises: 30
questions:
- "What is a scheduler and why are they used?"
- "How do we submit a job?"
objectives:
- "Submit a job and have it complete successfully."
- "Understand how to make resource requests."
- "Submit an interactive job."
keypoints:
- "The scheduler handles how compute resources are shared between users."
- "Everything you do should be run through the scheduler."
- "A job is just a shell script."
- "If in doubt, request more resources than you will need."
---

An HPC system might have thousands of nodes and thousands of users.
How do we decide who gets what and when?
How do we ensure that a task is run with the resources it needs?
This job is handled by a special piece of software called the scheduler.
On an HPC system, the scheduler manages which jobs run where and when.

> ## Job scheduling roleplay (optional)
> 
> Your instructor will divide you into groups taking on 
> different roles in the cluster (users, compute nodes 
> and the scheduler).  Follow their instructions as they 
> lead you through this exercise.  You will be emulating 
> how a job scheduling system works on the cluster.  
> 
> [Notes for the instructor here](../guide)
{: .challenge}

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
[remote]$ sbatch example-job.sh
```
{: .bash}
```
Submitted batch job 36855
```
{: .output}

And that's all we need to do to submit a job. 
To check on our job's status, we use the command `squeue`.

```
[remote]$ squeue -u yourUsername
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
[remote]$ sbatch example-job.sh
[remote]$ watch squeue -u yourUsername
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
[remote]$ squeue -u yourUsername
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
you will likely be stuck with your site's default resources,
which is probably not what we want.

The following are several key resource requests:

* `-c <ncpus>` - How many CPUs does your job need?

* `--mem=<megabytes>` - How much memory on a node does your job need in megabytes? You can also specify gigabytes using by adding a little "g" afterwards (example: `--mem=5g`)

* `--time <days-hours:minutes:seconds>` - How much real-world time (walltime) will your job take to run? The `<days>` part can be omitted.

> ## Submitting resource requests
>
> Submit a job that will use 2 cpus, 4 gigabytes of memory, and 5 minutes of walltime.
{: .challenge}

> ## Job environment variables
>
> When SLURM runs a job, it sets a number of environment variables for the job.
> One of these will let us check our work from the last problem.
> The `SLURM_CPUS_PER_TASK` variable is set to the number of CPUs we requested with `-c`.
> Using the `SLURM_CPUS_PER_TASK` variable, 
> modify your job so that it prints how many CPUs have been allocated.
{: .challenge}

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

Submit the job and wait for it to finish. 
Once it is has finished, check the log file.
```
[remote]$ sbatch example-job.sh
[remote]$ watch squeue -u yourUsername
[remote]$ cat slurm-38193.out
```
{: .bash}
```
This job is running on:
gra533
slurmstepd: error: *** JOB 38193 ON gra533 CANCELLED AT 2017-07-02T16:35:48 DUE TO TIME LIMIT ***
```
{: .output}

Our job was killed for exceeding the amount of resources it requested.
Although this appears harsh, this is actually a feature.
Strict adherence to resource requests allows the scheduler to find the best possible place
for your jobs.
Even more importantly, 
it ensures that another user cannot use more resources than they've been given.
If another user messes up and accidentally attempts to use all of the CPUs or memory on a node, 
SLURM will either restrain their job to the requested resources or kill the job outright.
Other jobs on the node will be unaffected.
This means that one user cannot mess up the experience of others,
the only jobs affected by a mistake in scheduling will be their own.

## Canceling a job

Sometimes we'll make a mistake and need to cancel a job.
This can be done with the `scancel` command.
Let's submit a job and then cancel it using its job number.

```
[remote]$ sbatch example-job.sh
[remote]$ squeue -u yourUsername
```
{: .bash}
```
Submitted batch job 38759

   JOBID     USER ACCOUNT           NAME  ST REASON    START_TIME                TIME  TIME_LEFT NODES CPUS
   38759 yourUsername yourAccount example-job.sh  PD Priority  N/A                       0:00       1:00     1    1
```
{: .output}

Now cancel the job with it's job number. 
Absence of any job info indicates that the job has been successfully canceled.

```
[remote]$ scancel 38759
[remote]$ squeue -u yourUsername
```
{: .bash}
```
   JOBID     USER ACCOUNT           NAME  ST REASON    START_TIME                TIME  TIME_LEFT NODES CPUS
```
{: .output}

> ## Cancelling multiple jobs
>
> We can also all of our jobs at once using the `-u` option. 
> This will delete all jobs for a specific user (in this case us).
> Note that you can only delete your own jobs.
>
> Try submitting multiple jobs and then cancelling them all with 
> `scancel -u yourUsername`.
{: .challenge}

## Other types of jobs

Up to this point, we've focused on running jobs in batch mode.
SLURM also provides the ability to run tasks as a one-off or start an interactive session.

There are very frequently tasks that need to be done semi-interactively.
Creating an entire job script might be overkill, 
but the amount of resources required is too much for a login node to handle.
A good example of this might be building a genome index for alignment with a tool like [HISAT2](https://ccb.jhu.edu/software/hisat2/index.shtml).
Fortunately, we can run these types of tasks as a one-off with `srun`.

`srun` runs a single command on the cluster and then exits.
Let's demonstrate this by running the `hostname` command with `srun`.
(We can cancel an `srun` job with `Ctrl-c`.)

```
[remote]$ srun hostname
```
{: .bash}
```
gra752
```
{: .output}

`srun` accepts all of the same options as `sbatch`.
However, instead of specifying these in a script, 
these options are specified on the command-line when starting a job.
To submit a job that uses 2 cpus for instance, 
we could use the following command
(note that SLURM's environment variables like `SLURM_CPUS_PER_TASK` are only available to batch jobs run with `sbatch`):

```
[remote]$ srun -c 2 echo "This job will use 2 cpus."
```
{: .bash}
```
This job will use 2 cpus.
```
{: .output}

### Interactive jobs

Sometimes, you will need a lot of resource for interactive use.
Perhaps it's our first time running an analysis 
or we are attempting to debug something that went wrong with a previous job.
Fortunately, SLURM makes it easy to start an interactive job with `srun`:

```
[remote]$ srun --x11 --pty bash
```
{: .bash}

> ## Note for administrators
> 
> The `--x11` option will not work unless the [slurm-spank-x11](https://github.com/hautreux/slurm-spank-x11) plugin is installed.
> You should also make sure `xeyes` is installed as an example X11 app 
> (`xorg-x11-apps` package on CentOS).
> If you do not have these installed, just have students use `srun --pty bash` instead.
{: .callout}

You should be presented with a bash prompt.
Note that the prompt will likely change to reflect your new location, 
in this case the worker node we are logged on.
You can also verify this with `hostname`.

> ## Creating remote graphics
> 
> To demonstrate what happens when you create a graphics window on the remote node, 
> use the `xeyes` command. 
> A relatively adorable pair of eyes should pop up (press `Ctrl-c` to stop).
>
> Note that this command requires you to have connected with X-forwarding enabled
> (`ssh -X username@host.address.ca`). If you are using a Mac, you must have installed
> XQuartz (and restarted your computer) for this to work.
{: .challenge}

When you are done with the interactive job, type `exit` to quit your session.

