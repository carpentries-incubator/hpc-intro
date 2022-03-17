---
title: "Exploring the cluster"
teaching: 45
exercises: 30
questions:
- "What do you actually connect to?"
- "What big differences are there between your laptop, the head node,
  and compute nodes?"
- "What is a scheduler and why are they used?"
- "How do I launch a program to run on a compute node in the cluster?"
- "How do I capture the output of a program that is run on a node in the
  cluster?"
objectives:
- "Find the right place to put large datasets on the cluster."
- "Inspect the memory and processors available on the cluster."
- "Run a simple Hello World style program on the cluster."
- "Submit a simple Hello World style script to the cluster."
- "Use the batch system command line tools to monitor the execution of your
  job."
- "Inspect the output and error files of your jobs."
keypoints:
- "Cluster nodes have more cores and more memory than your local
  machine or the head node."
- "The scheduler handles how compute resources are shared between users."
- "Everything you do should be run through the scheduler."
- "A job is just a shell script."
- "If in doubt, request more resources than you will need."
---

## Look Around the Rest of the System

Most high-performance computing systems run the Linux operating system, which
is built around the UNIX [Filesystem Hierarchy Standard][fshs]. Instead of
having a separate root for each hard drive or storage medium, all files and
devices are anchored to the "root" directory, which is `/`:

```
{{ site.remote.prompt }} ls /
```
{: .language-bash}
```
bin   etc   lib64  proc  sbin     sys  var
boot  {{ site.remote.homedir | replace: "/", "" }}  mnt    root  scratch  tmp  working
dev   lib   opt    run   srv      usr
```
{: .output}

The "{{ site.remote.homedir | replace: "/", "" }}" directory is the one where
we generally want to keep all of our files. Other folders on a UNIX OS contain
system files, and get modified and changed as you install new software or
upgrade your OS.

> ## Using HPC filesystems
>
> On HPC systems, you have a number of places where you can store your files.
> These differ in both the amount of space allocated and whether or not they
> are backed up.
>
> * **Home** -- often a *network filesystem*, data stored here is available
>   throughout the HPC system, and often backed up periodically. Files stored
>   here are typically slower to access, the data is actually stored on another
>   computer and is being transmitted and made available over the network!
> * **Scratch** -- typically faster than the networked home directory, but not
>   usually backed up, and should not be used for long term storage.
> * **Work** -- sometimes provided as an alternative to Scratch space, Work is
>   a fast file system accessed over the network. Typically, this will have
>   higher performance than your home directory, but lower performance than
>   Scratch; it may not be backed up. It differs from Scratch space in that
>   files in a work file system are not automatically deleted for you: you must
>   manage the space yourself.
{: .callout}

## Nodes

Individual computers that compose a cluster are typically called *nodes*
(although you will also hear people call them *servers*, *computers* and
*machines*). On a cluster, there are different types of nodes for different
types of tasks. The node where you are right now is called the *head node*,
*login node*, *landing pad*, or *submit node*. A login node serves as an access
point to the cluster.

As a gateway, it is well suited for uploading and downloading files, setting up
software, and running quick tests. Generally speaking, the login node should
not be used for time-consuming or resource-intensive tasks. You should be alert
to this, and check with your site's operators or documentation for details of
what is and isn't allowed. In these lessons, we will avoid running jobs on the
head node.

> ## Dedicated Transfer Nodes
>
> If you want to transfer larger amounts of data to or from the cluster, some
> systems offer dedicated nodes for data transfers only. The motivation for
> this lies in the fact that larger data transfers should not obstruct
> operation of the login node for anybody else. Check with your cluster's
> documentation or its support team if such a transfer node is available. As a
> rule of thumb, consider all transfers of a volume larger than 500 MB to 1 GB
> as large. But these numbers change, e.g., depending on the network connection
> of yourself and of your cluster or other factors.
{: .callout}

The real work on a cluster gets done by the *worker* (or *compute*) *nodes*.
Worker nodes come in many shapes and sizes, but generally are dedicated to long
or hard tasks that require a lot of computational resources.

All interaction with the worker nodes is handled by a specialized piece of
software called a scheduler (the scheduler used in this lesson is called
{{ site.sched.name }}). We'll learn more about how to use the
scheduler to submit jobs next, but for now, it can also tell us more
information about the worker nodes.

For example, we can view all of the worker nodes by running the command
`{{ site.sched.info }}`.

```
{{ site.remote.prompt }} {{ site.sched.info }}
```
{: .language-bash}

{% include {{ site.snippets }}/cluster/queue-info.snip %}

There are also specialized machines used for managing disk storage, user
authentication, and other infrastructure-related tasks. Although we do not
typically logon to or interact with these machines directly, they enable a
number of key features like ensuring our user account and files are available
throughout the HPC system.

## What's in a Node?

All of the nodes in an HPC system have the same components as your own laptop
or desktop: *CPUs* (sometimes also called *processors* or *cores*), *memory*
(or *RAM*), and *disk* space. CPUs are a computer's tool for actually running
programs and calculations. Information about a current task is stored in the
computer's memory. Disk refers to all storage that can be accessed like a file
system. This is generally storage that can hold data permanently, i.e. data is
still there even if the computer has been restarted. While this storage can be
local (a hard drive installed inside of it), it is more common for nodes to
connect to a shared, remote fileserver or cluster of servers.

{% include figure.html url="" max-width="40%"
   file="/fig/node_anatomy.png"
   alt="Node anatomy" caption="" %}

> ## Explore Your Computer
>
> Try to find out the number of CPUs and amount of memory available on your
> personal computer.
>
> Note that, if you're logged in to the remote computer cluster, you need to
> log out first. To do so, type `Ctrl+d` or `exit`:
>
> ```
> {{ site.remote.prompt }} exit
> {{ site.local.prompt }}
> ```
> {: .language-bash}
>
> > ## Solution
> >
> > There are several ways to do this. Most operating systems have a graphical
> > system monitor, like the Windows Task Manager. More detailed information
> > can be found on the command line:
> >
> > * Run system utilities
> >   ```
> >   {{ site.local.prompt }} nproc --all
> >   {{ site.local.prompt }} free -m
> >   ```
> >   {: .language-bash}
> >
> > * Read from `/proc`
> >   ```
> >   {{ site.local.prompt }} cat /proc/cpuinfo
> >   {{ site.local.prompt }} cat /proc/meminfo
> >   ```
> >   {: .language-bash}
> >
> > * Run system monitor
> >   ```
> >   {{ site.local.prompt }} htop
> >   ```
> >   {: .language-bash}
> {: .solution}
{: .challenge}

> ## Explore the Head Node
>
> Now compare the resources of your computer with those of the head node.
>
> > ## Solution
> >
> > ```
> > {{ site.local.prompt }} ssh {{ site.remote.user }}@{{ site.remote.login }}
> > {{ site.remote.prompt }} nproc --all
> > {{ site.remote.prompt }} free -m
> > ```
> > {: .language-bash}
> >
> > You can get more information about the processors using `lscpu`,
> > and a lot of detail about the memory by reading the file `/proc/meminfo`:
> >
> > ```
> > {{ site.remote.prompt }} less /proc/meminfo
> > ```
> > {: .language-bash}
> >
> > You can also explore the available filesystems using `df` to show **d**isk
> > **f**ree space. The `-h` flag renders the sizes in a human-friendly format,
> > i.e., GB instead of B. The **t**ype flag `-T` shows what kind of filesystem
> > each resource is.
> >
> > ```
> > {{ site.remote.prompt }} df -Th
> > ```
> > {: .language-bash}
> >
> > > ## Different results from `df`
> > >
> > > * The local filesystems (ext, tmp, xfs, zfs) will depend on whether
> > >   you're on the same login node (or compute node, later on).
> > > * Networked filesystems (beegfs, cifs, gpfs, nfs, pvfs) will be similar
> > >   -- but may include {{ site.remote.user }}, depending on how it
> > >   is [mounted](https://en.wikipedia.org/wiki/Mount_(computing)).
> > {: .discussion}
> >
> > > ## Shared Filesystems
> > >
> > > This is an important point to remember: files saved on one node
> > > (computer) are often available everywhere on the cluster!
> > {: .callout}
> {: .solution}
{: .challenge}

{% include {{ site.snippets }}/cluster/specific-node-info.snip %}

> ## Compare Your Computer, the Head Node and the Worker Node
>
> Compare your laptop's number of processors and memory with the numbers you
> see on the cluster head node and worker node. What implications do
> you think the differences might have on running your research work on the
> different systems and nodes?
>
> > ## Solution
> >
> > Compute nodes are usually built with processors that have *higher
> > core-counts* than the head node or personal computers in order to support
> > highly parallel tasks. Compute nodes usually also have substantially *more
> > memory (RAM)* installed than a personal computer. More cores tends to help
> > jobs that depend on some work that is easy to perform in *parallel*, and
> > more, faster memory is key for large or *complex numerical tasks*.
> {: .solution}
{: .discussion}

> ## Differences Between Nodes
>
> Many HPC clusters have a variety of nodes optimized for particular workloads.
> Some nodes may have larger amount of memory, or specialized resources such as
> Graphics Processing Units (GPUs or "video cards").
{: .callout}

With all of this in mind, we will now cover how to talk to the cluster's
scheduler, and use it to start running our scripts and programs!

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

The scheduler used in this lesson is {{ site.sched.name }}. Although
{{ site.sched.name }} is not used everywhere, running jobs is quite similar
regardless of what software is being used. The exact syntax might change, but
the concepts remain the same.

## Running a Batch Job

The most basic use of the scheduler is to run a command non-interactively. Any
command (or series of commands) that you want to run on the cluster is called a
*job*, and the process of using a scheduler to run the job is called *batch job
submission*.

In this case, the job we want to run is a shell script -- essentially a
text file containing a list of UNIX commands to be executed in a sequential
manner. Our shell script will have three parts:

* On the very first line, add `{{ site.remote.bash_shebang }}`. The `#!`
  (pronounced "hash-bang" or "shebang") tells the computer what program is
  meant to process the contents of this file. In this case, we are telling it
  that the commands that follow are written for the command-line shell (what
  we've been doing everything in so far). If we wanted our script to be run
  with something else -- Python, for example -- we could change this line to
  read `#!/usr/bin/python3`.
* Anywhere below the first line, we'll add an `echo` command with a friendly
  greeting. When run, the shell script will print whatever comes after `echo`
  in the terminal.
  * `echo -n` will print everything that follows, *without* ending
    the line by printing the new-line character.
* On the last line, we'll invoke the `hostname` command, which will print the
  name of the machine the script is run on.

```
{{ site.remote.prompt }} nano example-job.sh
```
{: .language-bash}
```
{{ site.remote.bash_shebang }}

echo -n "This script is running on "
hostname
```
{: .output}

Let's try running it:

```
$ example-job.sh 
```
{: .language-bash}

```
bash: example-job.sh: command not found...
```
{: .error}

Strangely enough, Bash can't find our script. As it turns out, Bash will only
look in certain directories for scripts to run. To run anything else, we need
to tell Bash exactly where to look. To run a script that we wrote ourselves, we
need to tell Bash where it is explicitly, so it doesn't go searching. We could
do this one of two ways: either with the absolute path 
`{{ site.workshop_host_homedir }}/yourUserName/example-job.sh` (equivalently,
`~/example-job.sh`), or with the relative path `./example-job.sh`
(where "." stands for "the current working directory").

```
$ ./example-job.sh
```
{: .language-bash}

```
bash: ./example-job.sh: Permission denied
```
{: .error}

There's one last thing we need to do. Before a file can be run, it needs
"permission" to execute. Let's look at the permissions for every file in this
directory using the "long" format option with `ls`:

```
$ ls -l
```
{: .language-bash}

```
...
-rw-rw-r-- 1 yourUsername yourGroup  40 Jan 16 19:41 example-job.sh
...
```
{: .output}

Let's see if we can understand **what each field of a given row represents**,
working left to right.

1. **Permissions:** to the far left, there are 10 single-character columns with
   some or all of the following symbols:
   * `d` indicates whether something is a directory
   * `r` indicates permission to **r**ead the file or directory
   * `w` indicates permission to **w**rite to the file or directory
   * `x` indicates permission to e**x**ecute the file or directory
   * `-` is used where permission has not been granted.

   There are three fields of `rwx` permissions following the spot for `d`:
  
   * The first set of `rwx` are the permissions that the `u`ser who owns the
     file has (in this case the owner is `yourUsername`).
   * The second set of `rwx`s are permissions that other members of the owner's
     `g`roup share (in this case, the group is named `yourGroup`); shorthand is `g`.
   * The third set of `rwx`s are permissions that all `o`ther users can do with
     a file.
   * Although files are typically created with read permissions for
     everyone, typically the permissions on your home directory prevent others
     from being able to access the file in the first place.
2. **References:** This counts the number of references ([hard links](
   https://en.wikipedia.org/wiki/Hard_link)) to the item (file, folder,
   symbolic link or "shortcut").
3. **Owner:** This is the username of the user who owns the file. Their
   permissions are indicated in the first permissions field.
4. **Group:** This is the user group of the user who owns the file. Members of
   this user group have permissions indicated in the second permissions field.
5. **Size of item:** This is the number of bytes in a file, or the number of
   [filesystem blocks](https://en.wikipedia.org/wiki/Block_(data_storage))
   occupied by the contents of a folder. (We can use the `-h` option here to
   get a human-readable file size in megabytes, gigabytes, etc.)
6. **Time last modified:** This is the last time the file was modified.
7. **Filename:** This is the filename.

Changing permissions is done with `chmod`. To add executable permissions for
our own **u**sername, we'll enter:

```
$ chmod u+x example-job.sh
$ ls -l example-job.sh
```
{: .language-bash}
```
...
-rwxrw-r-- 1 yourUsername yourGroup  40 Jan 16 19:41 example-job.sh
```
{: .output}


> ## Creating Our Test Job
>
> Run the script. Does it execute on the cluster or just our login node?
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} ./example-job.sh
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
"running it". To submit this job to the scheduler, we use the
`{{ site.sched.submit.name }}` command.

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {% if site.sched.submit.options != '' %}{{ site.sched.submit.options }} {% endif %}example-job.sh
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/basic-job-script.snip %}

And that's all we need to do to submit a job. Our work is done -- now the
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
> On the login node, this script printed output to the terminal -- but
> when we exit `watch`, there's nothing. Where'd it go?
>
> Cluster job output is typically redirected to a file in the directory you
> launched it from. Use `ls` to find and read the file.
{: .discussion}

## Customising a Job

The job we just ran used all of the scheduler's default options. In a
real-world scenario, that's probably not what we want. The default options
represent a reasonable minimum. Chances are, we will need more cores, more
memory, more time, among other special considerations. To get access to these
resources we must customize our job script.

Comments in UNIX shell scripts (denoted by `#`) are typically ignored, but
there are exceptions. For instance the special `#!` comment at the beginning of
scripts specifies what program should be used to run it (you'll typically see
`{{ site.local.bash_shebang }}`). Schedulers like {{ site.sched.name }} also
have a special comment used to denote special scheduler-specific options.
Though these comments differ from scheduler to scheduler,
{{ site.sched.name }}'s special comment is `{{ site.sched.comment }}`. Anything
following the `{{ site.sched.comment }}` comment is interpreted as an
instruction to the scheduler.

Let's illustrate this by example. By default, a job's name is the name of the
script, but the `{{ site.sched.flag.name }}` option can be used to change the
name of a job. Add an option to the script:

```
{{ site.remote.prompt }} cat example-job.sh
```
{: .language-bash}

```
{{ site.remote.bash_shebang }}
{{ site.sched.comment }} {{ site.sched.flag.name }} new_name

echo -n "This script is running on "
hostname
echo "This script has finished successfully."
```
{: .output}

Submit the job and monitor its status:

```
{{ site.remote.prompt }} {{ site.sched.submit.name }} {% if site.sched.submit.options != '' %}{{ site.sched.submit.options }} {% endif %}example-job.sh
{{ site.remote.prompt }} {{ site.sched.status }} {{ site.sched.flag.user }}
```
{: .language-bash}

{% include {{ site.snippets }}/scheduler/job-with-name-status.snip %}

Fantastic, we've successfully changed the name of our job!

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
