---
title: "Working with the scheduler"
teaching: 45
exercises: 30
questions:
- "What is a scheduler and why are they used?"
- "How do I launch a program to run on any one node in the cluster?"
- "How do I capture the output of a program that is run on a node in the cluster?"
objectives:
- "Run a simple Hello World style program on the cluster."
- "Submit a simple Hello World style script to the cluster."
- "Use the batch system command line tools to monitor the execution of your job."
- "Inspect the output and error files of your jobs."
keypoints:
- "The scheduler handles how compute resources are shared between users."
- "Everything you do should be run through the scheduler."
- "A job is just a shell script."
- "If in doubt, request more resources than you will need."
---

## Job scheduler

An HPC system might have thousands of nodes and thousands of users. How do we decide who gets what
and when? How do we ensure that a task is run with the resources it needs? This job is handled by a
special piece of software called the scheduler. On an HPC system, the scheduler manages which jobs
run where and when.

The following illustration compares these tasks of a job scheduler to a waiter in a restaurant.
If you can relate to an instance where you had to wait for a while in a queue to get in to a 
popular restaurant, then you may now understand why sometimes your job do not start instantly
as in your laptop.

{% include figure.html max-width="75%" file="/fig/restaurant_queue_manager.svg"
alt="Compare a job scheduler to a waiter in a restaurant" caption="" %}

> ## Job scheduling roleplay (optional)
> 
> Your instructor will divide you into groups taking on different roles in the cluster (users,
> compute nodes and the scheduler). Follow their instructions as they lead you through this
> exercise. You will be emulating how a job scheduling system works on the cluster.
> 
> > ## Instructions
> >
> > To do this exercise, you will need about 50-100 pieces of paper or sticky notes.
> >
> > 1. Divide the room into groups, with specific roles. 
> >    * Pick three or four people to be the "scheduler."
> >    * Select one-third of the room be "users", given several slips of paper (or post-it notes)
> >       and pens.
> >    * Have the remaining two thirds of the room be "compute nodes."
> >    * Have the "users" go to the front of the room (or the back, wherever there's space for them
> >      to stand) and the "schedulers" stand between the users and "compute nodes" (who should 
> >      remain at their seats).
> >
> > 2. Divide the pieces of paper / sticky notes among the "users" and have them fill out all the
> >    pages with simple math problems and their name. Tell everyone that these are the jobs that
> >    need to be done and correspond to their computing research problems.
> >
> > 3. Point out that we now have jobs and we have "compute nodes" (the people still sitting down)
> >    that can solve these problems. How are the jobs going to get to the nodes? The answer is the
> >    scheduling program that will take the jobs from the users and deliver them to open compute
> >    nodes.
> >
> > 4. Have all the "compute nodes" raise their hands. Have the users "submit" their jobs by handing
> >    them to the schedulers. Schedulers should then deliver them to "open" (hands-raised) compute
> >    nodes and collect finished problems and return them to the appropriate user.
> >
> > 5. Wait until most of the problems are done and then re-seat everyone.
> >
> > > ## Discussion
> > > 
> > > A "node" might be unable to solve the assigned problem for a variety of reasons.
> > > 
> > > * Ran out of time.
> > > * Ran out of memory.
> > > * Ran out of storage space, or could not load an input file or dataset.
> > > * Doesn't know where to start: nobody "taught" it, i.e., the program can't be loaded.
> > > * Gets stuck on a hard part: the program has the wrong algorithm, or was never told to load
> > >   the library containing the right algorithm.
> > > * Was busy thinking about something else, and didn't get to the problem yet.
> > {: .discussion}
> {: .challenge}
{: .callout}

The scheduler used in this lesson is {{ site.sched.name }}. Although {{ site.sched.name }} is not
used everywhere, running jobs is quite similar regardless of what software is being used. The exact
syntax might change, but the concepts remain the same.

## Running a batch job

The most basic use of the scheduler is to run a command non-interactively. Any command (or series 
of commands) that you want to run on the cluster is called a *job*, and the process of using a
scheduler to run the job is called *batch job submission*.

In this case, the job we want to run is just a shell script. Let's create a demo shell script to
run as a test. The landing pad will have a number of terminal-based text editors installed. Use
whichever you prefer. Unsure? `nano` is a pretty good, basic choice.

```
{{ site.remote.prompt }} nano example-job.sh
{{ site.remote.prompt }} chmod +x example-job.sh
{{ site.remote.prompt }} cat example-job.sh
```
{: .bash}

```
#!/bin/bash

echo -n "This script is running on "
hostname
```
{: .output}

> ## Creating our test job
> 
> Run the script. Does it execute on the cluster or just our login node?
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} ./example-job.sh
> > ```
> > {: .bash}
> > ```
> > This script is running on {{ site.remote.host }}
> > ```
> > {: .output}
> > 
> > This job runs on the login node.
> {: .solution}
{: .challenge}

If you completed the previous challenge successfully, you probably realise that there is a
distinction between running the job through the scheduler and just "running it". To submit this job
to the scheduler, we use the `{{ site.sched.submit.name }}` command.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh
```
{: .bash}

{% include {{ site.snippets }}/scheduler/basic-job-script.snip %}

And that's all we need to do to submit a job. Our work is done &mdash; now the scheduler takes over and
tries to run the job for us. While the job is waiting to run, it goes into a list of jobs called 
the *queue*. To check on our job's status, we check the queue using the command
`{{ site.sched.status }} {{ site.sched.flag.user }}`.

```
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .bash}

{% include {{ site.snippets }}/scheduler/basic-job-status.snip %}

The best way to check our job's status is with `{{ site.sched.status }}`. Of course, running 
`{{ site.sched.status }}` repeatedly to check on things can be a little tiresome. To see a real-time
view of our jobs, we can use the `watch` command. `watch` reruns a given command at 2-second
intervals. This is too frequent, and will likely upset your system administrator. You can change
the interval to a more reasonable value, for example 15 seconds, with the `-n 15` parameter. Let's
try using it to monitor another job.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh
{{ site.remote.prompt }} watch -n 15 {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .bash}

You should see an auto-updating display of your job's status. When it finishes, it will disappear
from the queue. Press `Ctrl-C` when you want to stop the `watch` command.

> ## Where's the output?
>
> On the login node, this script printed output to the terminal &mdash; but when we exit `watch`,
> there's nothing. Where'd it go?
>
> Cluster job output is typically redirected to a file in the directory you launched it from.
> Use `ls` to find and read the file.
{: .discussion}

## Customising a job

The job we just ran used all of the scheduler's default options. In a real-world scenario, that's
probably not what we want. The default options represent a reasonable minimum. Chances are, we will
need more cores, more memory, more time, among other special considerations. To get access to these
resources we must customize our job script.

Comments in UNIX shell scripts (denoted by `#`) are typically ignored, but there are exceptions.
For instance the special `#!` comment at the beginning of scripts specifies what program should be
used to run it (you'll typically see `#!/bin/bash`). Schedulers like {{ site.sched.name }} also
have a special comment used to denote special scheduler-specific options. Though these comments
differ from scheduler to scheduler, {{ site.sched.name }}'s special comment is 
`{{ site.sched.comment }}`. Anything following the `{{ site.sched.comment }}` comment is interpreted
as an instruction to the scheduler.

Let's illustrate this by example. By default, a job's name is the name of the script, but the 
`{{ site.sched.flag.name }}` option can be used to change the name of a job. Add an option to the
script:

```
{{ site.remote.prompt }} cat example-job.sh
```
{: .bash}

```
#!/bin/bash
{{ site.sched.comment }} {{ site.sched.flag.name }} new_name

echo -n "This script is running on "
hostname
echo "This script has finished successfully."
```
{: .output}

Submit the job (using `{{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh`)
and monitor it:

```
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .bash}

{% include {{ site.snippets }}/scheduler/job-with-name-status.snip %}

Fantastic, we've successfully changed the name of our job!

> ## Setting up email notifications
> 
> Jobs on an HPC system might run for days or even weeks. We probably have better things to do than
> constantly check on the status of our job with `{{ site.sched.status }}`. Looking at the
> manual page for `{{ site.sched.submit.name }}`, can you set up our test job to send you an email
> when it finishes?
>
> > ## Hint
> >
> > You can use the *manual pages* for {{ site.sched.name }} utilities to find more about their
> > capabilities. On the command line, these are accessed through the `man` utility: run 
> > `man <program-name>`. You can find the same information online by searching 
> > "man <program-name>".
> >
> > ```
> > {{ site.remote.prompt }} man {{ site.sched.submit.name }}
> > ```
> > : .bash}
> {: .solution}
{: .challenge}

### Resource requests

But what about more important changes, such as the number of cores and memory for our jobs? One 
thing that is absolutely critical when working on an HPC system is specifying the resources 
required to run a job. This allows the scheduler to find the right time and place to schedule our 
job. If you do not specify requirements (such as the amount of time you need), you will likely be
stuck with your site's default resources, which is probably not what you want.

The following are several key resource requests:

{% include {{ site.snippets }}/scheduler/option-flags-list.snip %}

Note that just *requesting* these resources does not make your job run faster, nor does it 
necessarily mean that you will consume all of these resources. It only means that these are
made available to you.  Your job may end up using less memory, or less time, or fewer tasks
or nodes, than you have requested, and it will still run.

It's best if your requests accurately reflect your job's requirements.  We'll talk more 
about how to make sure that you're using resources effectively in a later episode of this lesson.

> ## Submitting resource requests
>
> Modify our `hostname` script so that it runs for a minute, then submit a job for it on
> the cluster.
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} cat example-job.sh
> > ```
> > {: .bash}
> >
> > ```
> > #!/bin/bash
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
> > {{ site.remote.prompt }} {{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh
> > ```
> > {: .bash}
> >
> > Why are the {{ site.sched.name }} runtime and `sleep` time not identical?
> {: .solution}
{: .challenge}

{% include {{ site.snippets }}/scheduler/print-sched-variables.snip %}

Resource requests are typically binding. If you exceed them, your job will be killed. Let's use
walltime as an example. We will request 30 seconds of walltime, and attempt to run a job for two
minutes.

```
{{ site.remote.prompt }} cat example-job.sh
```
{: .bash}

```
#!/bin/bash
{{ site.sched.comment }} {{ site.sched.flag.name }} long_job
{{ site.sched.comment }} {{ site.sched.flag.time }} 00:00:30

echo "This script is running on ... "
sleep 120 # time in seconds
hostname
echo "This script has finished successfully."
```
{: .output}

Submit the job and wait for it to finish. Once it is has finished, check the log file.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh
{{ site.remote.prompt }} watch -n 15 {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .bash}

{% include {{ site.snippets }}/scheduler/runtime-exceeded-job.snip %}

{% include {{ site.snippets }}/scheduler/runtime-exceeded-output.snip %}

Our job was killed for exceeding the amount of resources it requested. Although this appears harsh,
this is actually a feature. Strict adherence to resource requests allows the scheduler to find the
best possible place for your jobs. Even more importantly, it ensures that another user cannot use
more resources than they've been given. If another user messes up and accidentally attempts to use
all of the cores or memory on a node, {{ site.sched.name }} will either restrain their job to the
requested resources or kill the job outright. Other jobs on the node will be unaffected. This means
that one user cannot mess up the experience of others, the only jobs affected by a mistake in
scheduling will be their own.

## Cancelling a job

Sometimes we'll make a mistake and need to cancel a job. This can be done with the 
`{{ site.sched.del }}` command. Let's submit a job and then cancel it using its job number (remember
to change the walltime so that it runs long enough for you to cancel it before it is killed!).

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .bash}

{% include {{ site.snippets }}/scheduler/terminate-job-begin.snip %}

Now cancel the job with its job number (printed in your terminal). A clean return of your command
prompt indicates that the request to cancel the job was successful.

```
{{ site.remote.prompt }} {{site.sched.del }} 38759
# ... Note that it might take a minute for the job to disappear from the queue ...
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .bash}

{% include {{ site.snippets }}/scheduler/terminate-job-cancel.snip %}

{% include {{ site.snippets }}/scheduler/terminate-multiple-jobs.snip %}

## Other types of jobs

Up to this point, we've focused on running jobs in batch mode. {{ site.sched.name }}
also provides the ability to start an interactive session.

There are very frequently tasks that need to be done interactively. Creating an entire job
script might be overkill, but the amount of resources required is too much for a login node to
handle. A good example of this might be building a genome index for alignment with a tool like
[HISAT2](https://ccb.jhu.edu/software/hisat2/index.shtml). Fortunately, we can run these types of
tasks as a one-off with `{{ site.sched.interactive }}`.

{% include {{ site.snippets }}/scheduler/using-nodes-interactively.snip %}
