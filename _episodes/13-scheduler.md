---
title: "Working with the scheduler"
teaching: 45
exercises: 30
questions:
- "What is a scheduler and why are they used?"
- "How do I launch a program to run on any one node in the cluster?"
- "How do I capture the output of a program that is run on a node in the
  cluster?"
objectives:
- "Run a simple Hello World style program on the cluster."
- "Submit a simple Hello World style script to the cluster."
- "Use the batch system command line tools to monitor the execution of your
  job."
- "Inspect the output and error files of your jobs."
keypoints:
- "The scheduler handles how compute resources are shared between users."
- "Everything you do should be run through the scheduler."
- "A job is just a shell script."
- "If in doubt, request more resources than you will need."
---
## Job Scheduler

An HPC system might have thousands of nodes and thousands of users. How do we
decide who gets what and when? How do we ensure that a task is run with the
resources it needs? This job is handled by a special piece of software called
the scheduler. On an HPC system, the scheduler manages which jobs run where and
when.

The following illustration compares these tasks of a job scheduler to a waiter
in a restaurant. If you can relate to an instance where you had to wait for a
while in a queue to get in to a popular restaurant, then you may now understand
why sometimes your job do not start instantly as in your laptop.

{% include figure.html max-width="75%" caption=""
   file="/fig/restaurant_queue_manager.svg"
   alt="Compare a job scheduler to a waiter in a restaurant" %}



## Interactive vs Batch

Sofar, whenever we have entered a command into our terminals, we have received the response immediately in the same terminal, this is said to be an _interactive session_.

??Diagram??

This is all well for doing small tasks, but what if we want to do several things one after another without without waiting in-between? Or what if we want to repeat the same series of command again later?

This is where _batch processing_ becomes useful, this is where instead of entering commands directly to the terminal we write them down in a text file or _script_. Then, the script can be _executed_ by calling it with `bash`.

??Diagram??

Lets try this now, create and open a new file in your current directory called `example-job.sh`.
(If you prefer another text editor than nano, feel free to use that), and enter the following.


<!-- The most basic use of the scheduler is to run a command non-interactively. Any
command (or series of commands) that you want to run on the cluster is called a
*job*, and the process of using a scheduler to run the job is called *batch job
submission*. -->

```
{{ site.remote.prompt }} nano example-job.sh
```
{: .language-bash}

?? I dont like introducing comments here. Must be better place.


```
{{ site.remote.bash_shebang }}

# This is a comment. 
# Anything after a '#' is not read by the interpreter.
echo "This script is running on $HOSTNAME"
date
```
{: .language-bash}

> ## Shebang
>
> Say something about shebang
{: .callout}

We can now run this script using
{{ site.remote.prompt }} bash example-job.sh
```
{: .language-bash}

{{ site.remote.bash_shebang }}

This script is running on {{ site.remote.host }}
{{ site.time }}
```
{: .output}

You will get the output printed to your terminal as if you had just run it.

> ## Creating Our Test Job
>
> Run the script. Does it execute on the cluster or just our login node?
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} bash example-job.sh
> > ```
> > {: .language-bash}
> > ```
> > This script is running on {{ site.remote.host }}
> > ```
> > {: .output}
> >
> > This job runs on the login node.
> {: .solution}
{: .challenge}

If you completed the previous challenge successfully, you probably realise that
there is a distinction between running the job through the scheduler and just
"running it". To submit this job to the scheduler, we use the `{{
site.sched.submit.name }}` command.

## Scheduled Batch Job

Up until now the scheduler has not been involved, our batch scripts were run directly on the login node (or equivalent).

Lets first take a copy of our batch script.

```
cp example-job.sh example-job.sl
```
> ## File Extensions
>
> A files extension in this case does not in any way affect how a script is read,
> it is just another part of the name used to remind users what type of file it is.
> Some common file extensions
> `.sh`: **Sh**ell Script.
> `.sl`: **Sl**urm Script, a shell script that includes a *slurm header* and is indented to be run using slurm.
> `.out`: Commonly used to indicate the file contains the std**out** of some process.
> `.err`: Same as `.out` but for std**err**.
{: .callout}

One of the key ways a scheduler allows us to be more efficient with resources, is by taking into account additional 'real world' factors that are not easily determined by looking at a piece of code, things like estimated runtime, memory requirements, number of CPUs required. We can provide that extra information by adding a _slurm header_ to our script.

```
{{ site.remote.bash_shebang }}

# This is a comment. 
# Anything after a '#' is not read by the interpreter.
echo "This script is running on $HOSTNAME"
date
```
{: .language-bash}

?? Diagram, slurm anatomy ??

> ## Comments
>
> Comments in UNIX shell scripts (denoted by `#`) are ignored by the bash interpreter.
> Why is it that we start our slurm parameters with `#` if it is going to be ignored?
> > Commented lines are ignored by the bash interpreter, but they are _not_ ignored by slurm.
> > The `{{ site.sched.comment }}` parameters are read by slurm when we _submit_ the job. When the job starts,
> > the bash interpreter will ignore all lines starting with `#`.
> >
> > This is very similar to the _shebang_ mentioned earlier,
> > when you run your script, the system looks at the `#!`, then uses the program at the subsequent
> > path to interpret the script, in our case `/bin/bash` (the program 'bash' found in the 'bin' directory).
> {: .solution}
{: .challenge}


Then rather than running our script with `bash` we _submit_ it to the scheduler using the command `sbatch` (**S**lurm **batch**).

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {% if site.sched.submit.options != '' %}{{ site.sched.submit.options }} {% endif %}example-job.sh
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/basic-job-script.snip %}


And that's all we need to do to submit a job. Our work is done &mdash; now the
scheduler takes over and tries to run the job for us. While the job is waiting
to run, it goes into a list of jobs called the *queue*. To check on our job's
status, we check the queue using the command
`{{ site.sched.status }} {{ site.sched.flag.user }}`.

```
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/basic-job-status.snip %}

The best way to check our job's status is with `{{ site.sched.status }}`. Of
course, running `{{ site.sched.status }}` repeatedly to check on things can be
a little tiresome. To see a real-time view of our jobs, we can use the `watch`
command. `watch` reruns a given command at 2-second intervals. This is too
frequent, and will likely upset your system administrator. You can change the
interval to a more reasonable value, for example 15 seconds, with the `-n 15`
parameter. Let's try using it to monitor another job.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {% if site.sched.submit.options != '' %}{{ site.sched.submit.options }} {% endif %}example-job.sh
{{ site.remote.prompt }} watch -n 15 {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .language-bash}

You should see an auto-updating display of your job's status. When it finishes,
it will disappear from the queue. Press `Ctrl-c` when you want to stop the
`watch` command.

> ## Where's the Output?
>
> On the login node, this script printed output to the terminal &mdash; but
> when we exit `watch`, there's nothing. Where'd it go?
>
> Cluster job output is typically redirected to a file in the directory you
> launched it from. Use `ls` to find and read the file.
{: .discussion}

> ## Setting up Email Notifications
>
> Jobs on an HPC system might run for days or even weeks. We probably have
> better things to do than constantly check on the status of our job with
> `{{ site.sched.status }}`. Looking at the manual page for
> `{{ site.sched.submit.name }}`, can you set up our test job to send you an email
> when it finishes?
>
> > ## Hint
> >
> > You can use the *manual pages* for {{ site.sched.name }} utilities to find
> > more about their capabilities. On the command line, these are accessed
> > through the `man` utility: run `man <program-name>`. You can find the same
> > information online by searching > "man <program-name>".
> >
> > ```
> > {{ site.remote.prompt }} man {{ site.sched.submit.name }}
> > ```
> > {: .language-bash}
> {: .solution}
{: .challenge}

### Resource Requests

But what about more important changes, such as the number of cores and memory
for our jobs? One thing that is absolutely critical when working on an HPC
system is specifying the resources required to run a job. This allows the
scheduler to find the right time and place to schedule our job. If you do not
specify requirements (such as the amount of time you need), you will likely be
stuck with your site's default resources, which is probably not what you want.

The following are several key resource requests:

{% include {{ site.snippets }}/scheduler/option-flags-list.snip %}

Note that just *requesting* these resources does not make your job run faster,
nor does it necessarily mean that you will consume all of these resources. It
only means that these are made available to you. Your job may end up using less
memory, or less time, or fewer tasks or nodes, than you have requested, and it
will still run.

It's best if your requests accurately reflect your job's requirements. We'll
talk more about how to make sure that you're using resources effectively in a
later episode of this lesson.

> ## Submitting Resource Requests
>
> Modify our `hostname` script so that it runs for a minute, then submit a job
> for it on the cluster.
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} cat example-job.sh
> > ```
> > {: .language-bash}
> >
> > ```
> > {{ site.remote.bash_shebang }}
> > {{ site.sched.comment }} {{ site.sched.flag.time }} 00:01:15
> >
> > echo -n "This script is running on "
> > sleep 60 # time in seconds
> > hostname
> > echo "This script has finished successfully."
> > ```
> > {: .output}
> >
> > ```
> > {{ site.remote.prompt }} {{ site.sched.submit.name }} {% if site.sched.submit.options != '' %}{{ site.sched.submit.options }} {% endif %}example-job.sh
> > ```
> > {: .language-bash}
> >
> > Why are the {{ site.sched.name }} runtime and `sleep` time not identical?
> {: .solution}
{: .challenge}

{% include {{ site.snippets }}/scheduler/print-sched-variables.snip %}

Resource requests are typically binding. If you exceed them, your job will be
killed. Let's use walltime as an example. We will request 30 seconds of
walltime, and attempt to run a job for two minutes.

```
{{ site.remote.prompt }} cat example-job.sh
```
{: .language-bash}

```
{{ site.remote.bash_shebang }}
{{ site.sched.comment }} {{ site.sched.flag.name }} long_job
{{ site.sched.comment }} {{ site.sched.flag.time }} 00:00:30

echo "This script is running on ... "
sleep 120 # time in seconds
hostname
echo "This script has finished successfully."
```
{: .output}

Submit the job and wait for it to finish. Once it is has finished, check the
log file.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {% if site.sched.submit.options != '' %}{{ site.sched.submit.options }} {% endif %}example-job.sh
{{ site.remote.prompt }} watch -n 15 {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/runtime-exceeded-job.snip %}

{% include {{ site.snippets }}/scheduler/runtime-exceeded-output.snip %}

Our job was killed for exceeding the amount of resources it requested. Although
this appears harsh, this is actually a feature. Strict adherence to resource
requests allows the scheduler to find the best possible place for your jobs.
Even more importantly, it ensures that another user cannot use more resources
than they've been given. If another user messes up and accidentally attempts to
use all of the cores or memory on a node, {{ site.sched.name }} will either
restrain their job to the requested resources or kill the job outright. Other
jobs on the node will be unaffected. This means that one user cannot mess up
the experience of others, the only jobs affected by a mistake in scheduling
will be their own.

## Cancelling a Job

Sometimes we'll make a mistake and need to cancel a job. This can be done with
the `{{ site.sched.del }}` command. Let's submit a job and then cancel it using
its job number (remember to change the walltime so that it runs long enough for
you to cancel it before it is killed!).

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {% if site.sched.submit.options != '' %}{{ site.sched.submit.options }} {% endif %}example-job.sh
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/terminate-job-begin.snip %}

Now cancel the job with its job number (printed in your terminal). A clean
return of your command prompt indicates that the request to cancel the job was
successful.

```
{{ site.remote.prompt }} {{site.sched.del }} 38759
# It might take a minute for the job to disappear from the queue...
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/terminate-job-cancel.snip %}

{% include {{ site.snippets }}/scheduler/terminate-multiple-jobs.snip %}

## Other Types of Jobs

Up to this point, we've focused on running jobs in batch mode.
{{ site.sched.name }} also provides the ability to start an interactive session.

There are very frequently tasks that need to be done interactively. Creating an
entire job script might be overkill, but the amount of resources required is
too much for a login node to handle. A good example of this might be building a
genome index for alignment with a tool like
[HISAT2](https://ccb.jhu.edu/software/hisat2/index.shtml). Fortunately, we can
run these types of tasks as a one-off with `{{ site.sched.interactive }}`.

{% include {{ site.snippets }}/scheduler/using-nodes-interactively.snip %}

{% include links.md %}
