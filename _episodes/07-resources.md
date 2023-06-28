---
title: "Using resources effectively"
#teaching: 25
teaching: 20
exercises: 5
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

In previous episodes we covered *how* to request resources, but what you may not know is *what* resources you need to request. The solution to this problem is testing!
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

## Estimating Required Resources

How do we know what resources to ask for in our scripts? In general, unless the software
documentation or user testimonials provide some idea, we won't know how much
memory or compute time a program will need.

> ## Read the Documentation
>
> NeSI maintains documentation  that does have some guidance on using resources for some software
> However, as you noticed in the Modules lessons, we have a lot of software.  So it is also advised to search
> the web for others that may have written up guidance for getting the most out of your specific software.
{: .callout}

## Running Test Jobs

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
Testing allows you to become more more precise with your resource requests.  We will cover a bit more on running tests in the last lesson.

## Efficient way to run tests jobs using debug QOS (Quality of Service)

Before submitting a large job, first submit one as a test to make
sure everything works as expected.  Often, users discover typos in their submit
scripts, incorrect module names or possibly an incorrect pathname after their job
has queued for many hours.  Be aware that your job is not fully scanned for
correctness when you submit the job.  While you may get an immediate error if your
SBATCH directives are malformed, it is not until the job starts to run that the
interpreter starts to process the batch script.

NeSI has an easy way for you to test your job submission.  One can employ the debug
QOS to get a short, very high priority test job.  Debug jobs have to run within 15 
minutes and cannot use more that 2 nodes.  To use debug QOS, add or change the
following in your batch submit script  
`#SBATCH --qos=debug`  
`#SBATCH --time=15:00`  

Adding these SBATCH directives will provide your job with the highest priority
possible, meaning it should start to run within a few minutes, provided
your resource request is not too large.

## Measuring Resource Usage of a Finished Job

If we check the status of our finished job using the `sacct` command we learned earlier.

```
{{ site.remote.prompt }} sacct
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/basic-job-status-sacct.snip %}

<!-- Put big formulas here. -->

With this information, we may determine a couple of things.

Memory efficiency can be determined by comparing **ReqMem** (requested memory) with **MaxRSS** (maximum used memory), MaxRSS is  given in KB, so a unit conversion is usually required.

So for the above example we see that **0.1GB** (102048K) of our requested **1GB** meaning the memory efficincy was about 10%.

CPU efficiency can be determined by comparing **TotalCPU** (CPU time), with the maximum possible CPU time. The maximum possible CPU time equal to **Alloc** (number of allocated CPUs) multiplied by **Elapsed** (Walltime, actual time passed).

For the above example **33 seconds** of computation was done where the maximum possible computation time was **96 seconds** (2 CPUs multiplied by 00:00:48), meaning the CPU efficiency was about 35%.

For convenience, NeSI has provided the command `nn_seff <jobid>` to calculate **S**lurm **Eff**iciency (all NeSI commands start with `nn_`, for **N**eSI **N**IWA). 
```
{{ site.remote.prompt }} nn_seff <jobid>
```
{: .language-bash}

{% include {{ site.snippets }}/resources/seff.snip %}

If you were to submit this same job again what resources would you request?

## Measuring the System Load From Currently Running Tasks

On Mahuika, we allow users to connect directly to compute nodes from the
login node. This is useful to check on a running job and see how it's doing, however, we
only allow you to connect to nodes on which you have running jobs. 

### Monitor System Processes With `htop`

The most reliable way to check current system stats is with `htop`. Some sample
output might look like the following (type `q` to exit `htop`):

```
{{ site.remote.prompt }} htop -u <yourUsername>
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

Running this command as is will show us information on tasks running on the login nod (where we should not be running resource intensive jobs anyway), in order to get information on a running job we will need to run htop on a compute node.

#### Finding job node

Running the command `sacct` we can see where our currently located jobs are located.

```
{{ site.remote.prompt }} squeue --me
```
{: .language-bash}


{% include  {{ site.snippets }}/resources/get-job-node.snip %}

Now that we know the location of the job (wbn189) we can use SSH to run htop there.

```
{{ site.remote.prompt }} ssh wbn189 -t htop -u $USER
```
{: .language-bash}


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
