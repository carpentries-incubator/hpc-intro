---
title: "Scaling"
teaching: 25
exercises: 15
questions:
- "How do we go from running a job on a small number of CPUs to a larger one."
objectives:
- "Understand scaling procedure."
keypoints:
- Start small.
- Test one thing at a time (unit tests).
- Record everything.
---

<!-- TODO: Add scaling example
Currently the rest of this lesson Not ready yet.  Too little info to go on without some sort of easy to grok exercise. -->


The aim of these tests will be to establish how a jobs requirements change with size (CPUs, inputs) and ultimately figure out the best way to run your jobs.

Unfortunately we cannot assume speedup will be linear (e.g. double CPUs won't usually half runtime, doubling the size of your input data won't necessarily double runtime) therefore more testing is required. This is called *scaling testing*.

## Scaling Test

Last time we submitted a job, we did not specify a number of CPUs, and therefore got the default of `2` (1 'core').

As a reminder, our slurm script `example-job.sl` should currently look like this.

```
{% include example_scripts/example-job.sl.1 %}
```
{: .language-bash}


Using the information we collected from the previous job (`nn_seff <job-id>`), we will submit the same job again with more CPUs and our best estimates of required resources.
We ask for more CPUs using by adding `#SBATCH --cpus-per-task 4` to our script.

Your script should now look like this:

```
{% include example_scripts/example-job.sl.2 %}
```
{: .language-bash}

And then submit using `sbatch` as we did before.

> ## acctg-freq
>
> We will also add the argument `--acctg-freq 1`.
> By default SLURM records job data every 30 seconds. This means any job running for less than 30 
> seconds will not have it's memory use recorded.
> This is the same as specifying `#SBATCH --acctg-freq 1` inside the script.
{: .callout}

```
{{ site.remote.prompt }} sbatch --acctg-freq 1 example-job.sl
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/basic-job-script.snip %}

> ## Watch
>
> We can prepend any command with `watch` in order to periodically (default 2 seconds) run a command. e.g. `watch 
> squeue --me` will give us up to date information on our running jobs. 
> Care should be used when using `watch` as repeatedly running a command can have adverse effects.  
{: .callout}

Checking on our job with `sacct`.
Oh no! 
{% include {{ site.snippets }}/scaling/OOM.snip %}

> ## OOM Error
> 
> 1. What went wrong?
> 2. What should be our next steps? 
> 3. How can we avoid this happening again in the future.
>
> > ## Solution
> >
> > The job failed due to an out of "OUT_OF_ME+(MORY)" error. This is because we doubled the number of 
> > CPUs over our previous job, but did not adjust memory.
> > The job running on 2 CPUs used ≈ 200Mb of RAM, extrapolating linearly, we want to give a 4 CPU job 400 Mb + small buffer, say 500Mb to be safe.
> > 
> {: .solution}
{: .challenge}

In order to establish an understanding of the scaling properties we may have to repeat this test several times, giving more resources each iteration.
> ## Scaling Exercise
>
> 1. Find your name in the [spreadsheet]({{ site.exersice }}) and modify your `example-job.sl` to request 
> "x" `--cpus-per-task`. For example `#SBATCH --cpus-per-task 10`.
> 2. Estimate memory requirement based on our previous runs and the cpus requested, memory 
> is specified with the `--mem ` flag, it does not accept decimal values, however you may 
> specify a unit (`K`|`M`|`G`), if no unit is specified it is assumed to be `M`. 
> For example `#SBATCH --mem 1200`. 
> 3. Submit the job with `sbatch --acctg-freq 1 example-job.sl`. 
> 4. Watch the job with `squeue --me` or `watch squeue --me`.
> 5. On completion of job, use `nn_seff <job-id>`.
> 6. Record the jobs "Elapsed", "TotalCPU", and "Memory" values in the spreadsheet. (Hint: They are the first 
> numbers after the percentage efficiency in output of `nn_seff`). Make sure you have entered the values in the correct format and there is a tick next to each entry. ![Correctly entered data in spreadsheet.](../fig/correct-spreadsheet-entry.png)
>
> > ## Solution
> > [spreadsheet]({{ site.exersice }})
> {: .solution}
{: .challenge}

## Scaling Behavior

### Diminishing Returns

Running code in parallel rarely comes for free, there are usually computational overheads. 
Whatever method is being used to distribute the workload usually require some computation, as well as communication between processes.

<!-- ![Fraction of CPU doing useful computation decreases due to overheads.](../fig/DimReturns.svg) -->

This usually leads to diminishing returns when it comes to performance.

![Fraction of CPU doing useful computation decreases due to overheads.](../fig/DimReturns2.png)


### Amdahl's Law

Most computational tasks will have a certain amount of work that must be computed serially.

<!-- ![The blue components can be run in parallel, red cannot.](../fig/AmdahlsLaw.svg)

As only the parallel portion of the job is sped up by scaling, the ratio of parallel to serial is an important factor in job scaling.  -->

![Larger fractions of parallel code will have closer to linear scaling performance.](../fig/AmdahlsLaw2.svg)

Eventually your performance gains will plateau.


The fraction of the task that can be run in parallel determines the point of this plateau.
Code that has no serial components is said to be "embarrassingly parallel".




<!-- > > ## Solution
> >
> >  1. No: `pwd` is not the name of a directory.
> >  2. Yes: `ls` without directory argument lists files and directories
> >     in the current directory.
> >  3. Yes: uses the absolute path explicitly.
> {: .solution}
{: .challenge} -->

{% include links.md %}
