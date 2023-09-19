---
title: "Using resources effectively"
teaching: 20
exercises: 15
questions:
- "How can I review past jobs?"
- "How can I use this knowledge to create a more accurate submission script?"
objectives:
- "Understand how to look up job statistics and profile code."
- "Understand job size implications."
- "Understand problems and limitations involved in using multiple CPUs."
keypoints:
- "As your task gets larger, so does the potential for inefficiencies."
- "The smaller your job (time, CPUs, memory, etc), the faster it will schedule."
---
<!--
- scaling testing involves running jobs with increasing resources and measuring the efficiency in order to establish a pattern informed decisions about future job submissions.-->

## What Resources?

Last time we submitted a job, we did not specify a number of CPUs, and therefore
we were provided the default of `2` (1 _core_).

As a reminder, our slurm script `example-job.sl` currently looks like this.

```
{% include example_scripts/example-job.sl.1 %}
```
{: .language-bash}

We will now submit the same job again with more CPUs.
We ask for more CPUs using by adding `#SBATCH --cpus-per-task 4` to our script.
Your script should now look like this:

```
{% include example_scripts/example-job.sl.2 %}
```
{: .language-bash}

And then submit using `sbatch` as we did before.

```
{{ site.remote.prompt }} sbatch example-job.sl
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/basic-job-script.snip %}

> ## Watch
>
> We can prepend any command with `watch` in order to periodically (default 2 seconds) run a command. e.g. `watch
> squeue --me` will give us up to date information on our running jobs.
> Care should be used when using `watch` as repeatedly running a command can have adverse effects.
> Exit `watch` with <kbd>ctrl</kbd> + <kbd>c</kbd>.
{: .callout}

Note in squeue, the number under cpus, should be '4'.

Checking on our job with `sacct`.
Oh no!

{% include {{ site.snippets }}/scaling/OOM.snip %}
{: .language-bash}

To understand why our job failed, we need to talk about the resources involved.

Understanding the resources you have available and how to use them most efficiently is a vital skill in high performance computing.

Below is a table of common resources and issues you may face if you do not request the correct amount.

<table>
    <thead>
        <tr>
            <th>  </th>
            <th>Not enough</th>
            <th>Too Much</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>   CPU   </b></td>
            <td>The job will run more slowly than expected, and so may run out of time and get killed for exceeding its time limit.</td>
            <td>The job will wait in the queue for longer. <br>
             You will be charged for CPUs regardless of whether they are used or not.<br>
            Your fair share score will fall more.
           </td>
        </tr>
        <tr>
            <td><b>   Memory   </b></td>
            <td>Your job will fail, probably with an 'OUT OF MEMORY' error, segmentation fault or bus error (may not happen immediately).</td>
            <td>The job will wait in the queue for longer.<br>
             You will be charged for memory regardless of whether it is used or not.<br>
             Your fair share score will fall more.</td>
        </tr>
        <tr>
            <td><b>   Walltime   </b></td>
            <td>The job will run out of time and be terminated by the scheduler.</td>
            <td>The job will wait in the queue for longer.</td>
        </tr>
    </tbody>
</table>

## Measuring Resource Usage of a Finished Job

Since we have already run a job (succesful or otherwise), this is the best source of info we currently have.
If we check the status of our finished job using the `sacct` command we learned earlier.

```
{{ site.remote.prompt }} sacct
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/basic-job-status-sacct.snip %}

With this information, we may determine a couple of things.

Memory efficiency can be determined by comparing <strong style="color:#66cdaa">ReqMem</strong> (requested memory) with <strong style="color:#00e400">MaxRSS</strong> (maximum used memory), MaxRSS is  given in KB, so a unit conversion is usually required.

{% include figure.html url="" max-width="75%" caption=""
   file="/fig/mem_eff.svg"
   alt="Memory Efficiency Formula" %}

So for the above example we see that <strong style="color:#00e400">0.1GB</strong> (102048K) of our requested <strong style="color:#66cdaa">1GB</strong> meaning the memory efficincy was about <strong>10%</strong>.

CPU efficiency can be determined by comparing <strong style="color:#ff8c00">TotalCPU</strong>(CPU time), with the maximum possible CPU time. The maximum possible CPU time equal to <strong style="color:#ff1493">Alloc</strong> (number of allocated CPUs) multiplied by <strong style="color:#0000ff">Elapsed</strong> (Walltime, actual time passed).

{% include figure.html url="" max-width="75%" caption=""
   file="/fig/cpu_eff.svg"
   alt="CPU Efficiency Formula" %}

For the above example <strong style="color:#ff8c00">33 seconds</strong> of computation was done,

where the maximum possible computation time was **96 seconds** (<strong style="color:#ff1493">2 CPUs</strong> multiplied by <strong style="color:#0000ff">48 seconds</strong>), meaning the CPU efficiency was about <strong>35%</strong>.

Time Efficiency is simply the <strong style="color:#0000ff">Elapsed Time</strong> divided by <strong style="color:#1ebfff">Time Requested</strong>.

{% include figure.html url="" max-width="75%" caption=""
   file="/fig/time_eff.svg"
   alt="Time Efficiency Formula" %}

<strong style="color:#0000ff">48 seconcds</strong> out of <strong style="color:#1ebfff">15 minutes</strong> requested give a time efficiency of about <strong>5%</strong>

> ## Efficiency Exercise
>
> Calculate for the job shown below,
>
> ```
> JobID           JobName          Alloc     Elapsed     TotalCPU  ReqMem   MaxRSS State
> --------------- ---------------- ----- ----------- ------------ ------- -------- ----------
> 37171050        Example-job          8    00:06:03     00:23:04     32G           FAILED
> 37171050.batch  batch                8    00:06:03    23:03.999         14082672k FAILED
> 37171050.extern extern               8    00:06:03    00:00.001                0  COMPLETED
> ```
>
> a. CPU efficiency.
>
> b. Memory efficiency.
>
> > ## Solution
> >
> > a. CPU efficiency is `( 23 / ( 8 * 6 ) ) x 100` or around **48%**.
> >
> > b. Memory efficiency is `( 14 / 32 ) x 100` or around **43%**.
> {: .solution}
{: .challenge}

For convenience, NeSI has provided the command `nn_seff <jobid>` to calculate **S**lurm **Eff**iciency (all NeSI commands start with `nn_`, for **N**eSI **N**IWA).
```
{{ site.remote.prompt }} nn_seff <jobid>
```
{: .language-bash}

{% include {{ site.snippets }}/resources/seff.snip %}

Knowing what we do now about job efficiency, lets submit the previous job again but with more appropriate resources.

{% include example_scripts/example-job.sl.2 %}

```
{{ site.remote.prompt }} sbatch example-job.sl
```
{: .language-bash}

Hopefully we will have better luck with this one!

## Measuring the System Load From Currently Running Tasks

On Mahuika, we allow users to connect directly to compute nodes from the
login node. This is useful to check on a running job and see how it's doing, however, we
only allow you to connect to nodes on which you have running jobs.

The most reliable way to check current system stats is with `htop`.
`htop` is an interactive process viewer that can be launched from command line.

### Finding job node

Before we can check on our job, we need to find out where it is running.
We can do this with the command `squeue --me`, and looking under the 'NODELIST' column.

```
{{ site.remote.prompt }} squeue --me
```
{: .language-bash}

{% include  {{ site.snippets }}/resources/get-job-node.snip %}

Now that we know the location of the job (wbn189) we can use `ssh` to run `htop` _on that node_.

```
{{ site.remote.prompt }} ssh wbn189 -t htop -u $USER
```
{: .language-bash}

You may get a message:

```
ECDSA key fingerprint is SHA256:############################################
ECDSA key fingerprint is MD5:9d:############################################
Are you sure you want to continue connecting (yes/no)?
```
{: .language-bash}

If so, type `yes` and <kbd>Enter</kbd>

You may also need to enter your cluster password.

If you cannot connect, it may be that the job has finished and you have lost permission to `ssh` to that node.

### Reading Htop

You may see something like this,

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

To exit press <kbd>q</kbd>.

Running this command as is will show us information on tasks running on the login node (where we should not be running resource intensive jobs anyway).

## Running Test Jobs

As you may have to run several iterations before you get it right, you should choose your test job carefully.
A test job should not run for more than 15 mins. This could involve using a smaller input, coarser parameters or using a subset of the calculations.
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
Testing allows you to become more more precise with your resource requests. We will cover a bit more on running tests in the last lesson.

> ## Efficient way to run tests jobs using debug QOS (Quality of Service)
>
> Before submitting a large job, first submit one as a test to make
> sure everything works as expected. Often, users discover typos in their submit
> scripts, incorrect module names or possibly an incorrect pathname after their job
> has queued for many hours. Be aware that your job is not fully scanned for
> correctness when you submit the job. While you may get an immediate error if your
> SBATCH directives are malformed, it is not until the job starts to run that the
> interpreter starts to process the batch script.
>
> NeSI has an easy way for you to test your job submission.  One can employ the debug
> QOS to get a short, high priority test job. Debug jobs have to run within 15
> minutes and cannot use more that 2 nodes. To use debug QOS, add or change the
> following in your batch submit script
>
>```
>#SBATCH --qos=debug 
>#SBATCH --time=15:00
> ``` 
>{: .language-bash}
>
> Adding these SBATCH directives will provide your job with the highest priority
> possible, meaning it should start to run within a few minutes, provided
> your resource request is not too large.
{: .callout}

## Initial Resource Requirements

As we have just discussed, the best and most reliable method of determining resource requirements is from testing,
but before we run our first test there are a couple of things you can do to start yourself off in the right area.

### Read the Documentation

NeSI maintains documentation  that does have some guidance on using resources for some software
However, as you noticed in the Modules lessons, we have a lot of software.  So it is also advised to search
the web for others that may have written up guidance for getting the most out of your specific software.

### Ask Other Users

If you know someone who has used the software before, they may be able to give you a ballpark figure.

<!-- Now that you know the efficiency of your small test job what next? Throw 100 more CPUs at the problem for 100x speedup? -->

> ## Next Steps
>
> You can use this knowledge to set up the
> next job with a closer estimate of its load on the system.
> A good general rule
> is to ask the scheduler for **30%** more time and memory than you expect the
> job to need.
{: .callout}

{% include links.md %}
