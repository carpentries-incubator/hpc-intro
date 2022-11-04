---
title: "Writing good code"
teaching: 5
exercises: 5
questions:
- "How do we write a good job script."
objectives:
- "Write a script that can be run serial or parallel."
- "Write a script that using SLURM environment variables."
- "Understand the limitations of random number generation."
keypoints:
- "Write your script in a way that is independent of data or environment. (elaborate)"
---

When talking about 'a script' we could be referring to multiple things.

* Slurm/Bash script - Almost everyone will be using one of these to submit their Slurm jobs.
* Work script - If your work involves running another script (usually in a langage other than Bash, Python, R, MATLAB, etc) that will have to be invoked in your bash script.

This section will cover best practice for both types of script. 

```
python python_script.py
```

```
rscript r_script.r
```

```
matlab -r matlab_script
```

## Paralellism

Understand where this is happeing. High level, low level?

## Use environment variables

In this lesson we will take a look at a few of the things to watch out for when writing scripts for use on the cluster.
This will be most relevant to people writing their own code, but covers general practices applicable to everyone.

Lets have a look at the script we ran before, `array_sum.r`, 

> ## Using R commands
>
> If you are unfamiliar with R, don't worry there are equivalent operations in any language you choose to use.
{: .callout}

```
{% include example_scripts/array_sum.r %}
```
{: .language-r}

Starting from the top;

```
num_cpus <- 2
```
{: .language-r}

The number of CPU's being used is fixed in the script. We can save time and reduce chances for making mistakes by replacing this static value with an environment variable. 
We can use the environment variable `SLURM_CPUS_PER_TASK`.

```
num_cpus <- strtoi(Sys.getenv('SLURM_CPUS_PER_TASK')) 
```
{: .language-r}

Slurm sets many environment variables when starting a job, see [Slurm Documentation for the full list](https://slurm.schedmd.com/sbatch.html). 

The problem with this approach however, is our code will throw an error if we run it on the login node, or on our local machine or anywhere else that `SLURM_CPUS_PER_TASK` is not set.

Generally it is best not to diverge your codebase especially if you don't have it under version control, so lets add some compatibility for those use cases.

```
num_cpus <- strtoi(Sys.getenv('SLURM_CPUS_PER_TASK', unset = "1")) 
```
{: .language-r}


Now if `SLURM_CPUS_PER_TASK` variable is not set, 1 CPU will be used. You could also use some other method of detecting CPUs, like `detectCores()`.

## Interoperability

windows + mac + linux
headless + interactive

## Verbose 


Having a printout of job progress is fine for an interactive terminal, but when you aren't seeing the updates in real time anyway, it's just bloat for your output files.

Let's add an option to mute the updates.

```
print_progress <- FALSE
```
{: .language-r}


```
if (print_progress && percent_complete%%1==0){

```
{: .language-r}

## Reproduceability 

As this script uses [Pseudorandom number generation](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) there are a few additional factors to consider.
It is desirable that our output be reproducible so we can confirm that changes to the code have not affected it. 

We can do this by setting the seed of the PRNG. That way we will get the same progression of 'random' numbers.

We are using the environment variable `SLURM_ARRAY_TASK_ID` for reasons we will get to later. We also need to make sure a default seed is set for the occasions when `SLURM_ARRAY_TASK_ID` is not set.

```
seed <- strtoi(Sys.getenv('SLURM_ARRAY_TASK_ID', unset = "0"))
set.seed(seed)
```
{: .language-r}


Now your script should look something like this;

```
{% include example_scripts/array_sum2.r %}
```
{: .language-r}

## Readability

Comments!

## Debugging

```
#!/bin/bash -e
```

Exit bash script on error

```
#!/bin/bash -x
```

Print everything.

```
env
```

Print environment, if someone else has problems replicating the problem, it will likely come down to differences in your enviroment. 

```
cat $0
```

Will print your input Slurm script to you output, this can help identify when changes in your submission script leads to errors.

## Version control

In many cases you may be using the same peice of code across multiple enviroments, in these situations it can be difficult to keep track of changes made and your code can begin to diverge. Setting up version control like Git can save a lot of time.

## Testing

More often than not, problems come in the form of typos, or other small errors that become apparent within the first few seconds/minutes of script. 

Running on login node?

Control + c to kill.

{% include links.md %}
