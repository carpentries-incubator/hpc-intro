---
title: "Working on a remote HPC system"
teaching: 25
exercises: 10
questions:
- "What is an HPC system?"
- "How does an HPC system work?"
- "How do I log on to a remote HPC system?"
objectives:
- "Connect to a remote HPC system."
- "Understand the general HPC system architecture."
keypoints:
- "An HPC system is a set of networked machines."
- "HPC systems typically provide login nodes and a set of worker nodes."
- "The resources found on independent (worker) nodes can vary in volume and type 
  (amount of RAM, processor architecture, availability of network mounted file systems, etc.)."
- "Files saved on one node are available on all nodes."
---

## What is an HPC system?

The words "cloud", "cluster", and the phrase "high-performance computing" or "HPC" are used a
lot in different contexts and with various related meanings. So what do they mean? And more
importantly, how do we use them in our work?

The *cloud* is a generic term commonly used to refer to computing resources that are
a) *provisioned* to users on demand or as needed and b) represent real or *virtual* resources
that may be located anywhere on Earth. For example, a large company with computing resources in
Brazil, Zimbabwe and Japan may manage those resources as its own *internal* cloud and that same
company may also utilize commercial cloud resources provided by Amazon or Google. Cloud resources
may refer to machines performing relatively simple tasks such as serving websites, providing
shared storage, providing webservices (such as e-mail or social media platforms), as well as more
traditional compute intensive tasks such as running a simulation.

The term *HPC system*, on the other hand, describes a stand-alone resource for computationally
intensive workloads. They are typically comprised of a multitude of integrated processing and
storage elements, designed to handle high volumes of data and/or large numbers of floating-point
operations ([FLOPS](https://en.wikipedia.org/wiki/FLOPS)) with the highest possible performance.
For example, all of the machines on the [Top-500](https://www.top500.org) list are HPC systems. To
support these constraints, an HPC resource must exist in a specific, fixed location: networking
cables can only stretch so far, and electrical and optical signals can travel only so fast.

The word "cluster" is often used for small to moderate scale HPC resources less impressive than the
[Top-500](https://www.top500.org). Clusters are often maintained in computing centers that support
several such systems, all sharing common networking and storage to support common compute intensive
tasks.


## Logging in
The first step in using a cluster is to establish a connection from our laptop to the cluster,
via the Internet and/or your organisation's network. We use a program called the 
Secure SHell (or ssh) client for this. Make sure you have a SSH client installed on your
laptop. Refer to the [setup]({{ page.root }}/setup) section for more details.

{% include figure.html url="" max-width="50%" file="/fig/connect-to-remote.svg"
 alt="Connect to cluster" caption="" %}


Go ahead and log in to the cluster: {{ site.remote.name }} at {{ site.remote.location }}.
```
{{ site.local.prompt }} ssh {{ site.remote.user }}@{{ site.remote.login }}
```
{: .bash}

Remember to replace `{{ site.remote.user }}` with the username supplied by the instructors. You may be asked
for your password. Watch out: the characters you type after the password prompt are not displayed on
the screen. Normal output will resume once you press `Enter`.

You are logging in using a program known as the secure shell or `ssh`. This establishes a temporary
encrypted connection between your laptop and `{{ site.remote.login }}`. The word before the `@`
symbol, e.g. `{{ site.remote.user }}` here, is the user account name that you have permission to use on the
cluster.


## Where are we?

Very often, many users are tempted to think of a high-performance computing installation as one
giant, magical machine. Sometimes, people will assume that the computer they've logged onto is the
entire computing cluster. So what's really happening? What computer have we logged on to? The name
of the current computer we are logged onto can be checked with the `hostname` command. (You may also
notice that the current hostname is also part of our prompt!)

```
{{ site.remote.prompt }} hostname
```
{: .bash}

```
{{ site.remote.name }}
```
{: .output}

> ## What's in your home directory?
>
> The system administrators may have configured your home directory with some helpful files,
> folders, and links (shortcuts) to space reserved for you on other filesystems. Take a look around
> and see what you can find.
>
> Home directory contents vary from user to user. Please discuss any differences you spot with your
> neighbors.
>
> *Hint:* The shell commands `pwd` and `ls` may come in handy.
>
> > ## Solution
> >
> > Use `pwd` to **p**rint the **w**orking **d**irectory path:
> >
> > ```
> > {{ site.remote.prompt }} pwd
> > ```
> > {: .bash}
> >
> > > The deepest layer should differ: {{ site.remote.user }} is uniquely yours. Are there
> > > differences in the path at higher levels?
> > {: .discussion}
> >
> > You can run `ls` to **l**i**s**t the directory contents, though it's possible nothing will show
> > up (if no files have been provided). To be sure, use the `-a` flag to show hidden files, too.
> >
> > ```
> > {{ site.remote.prompt }} ls -a
> > ```
> > {: .bash}
> >
> > At a minimum, this will show the current directory as `.`, and the parent directory as `..`.
> >
> > > If both of you have empty directories, they will look identical. If you or your neighbor has
> > > used the system before, there may be differences. What are you working on?
> > {: .discussion}
> {: .solution}
{: .discussion}

## Nodes

Individual computers that compose a cluster are typically called *nodes* (although you will also
hear people call them *servers*, *computers* and *machines*). On a cluster, there are different
types of nodes for different types of tasks. The node where you are right now is called the *head
node*, *login node*, *landing pad*, or *submit node*. A login node serves as an access point to the
cluster. As a gateway, it is well suited for uploading and downloading files, setting up software,
and running quick tests. It should never be used for doing actual work.

The real work on a cluster gets done by the *worker* (or *compute*) *nodes*. Worker nodes come in
many shapes and sizes, but generally are dedicated to long or hard tasks that require a lot of
computational resources.

All interaction with the worker nodes is handled by a specialized piece of software called a
scheduler (the scheduler used in this lesson is called {{ site.workshop.sched.name }}). We'll learn
more about how to use the scheduler to submit jobs next, but for now, it can also tell us more
information about the worker nodes.

For example, we can view all of the worker nodes with the `{{ site.sched.info }}` command.

```
{{ site.remote.prompt }} {{ site.sched.info }}
```
{: .bash}

{% include {{ site.snippets }}/cluster/queue-info.snip %}

There are also specialized machines used for managing disk storage, user authentication, and other
infrastructure-related tasks. Although we do not typically logon to or interact with these machines
directly, they enable a number of key features like ensuring our user account and files are
available throughout the HPC system.

## What's in a node? 

All of the nodes in an HPC system have the same components as your own laptop or desktop: *CPUs*
(sometimes also called *processors* or *cores*), *memory* (or *RAM*), and *disk* space. CPUs are a
computer's tool for actually running programs and calculations. Information about a current task is
stored in the computer's memory. Disk refers to all storage that can be accessed like a file system.
This is generally storage that can hold data permanently, i.e. data is still there even if the
computer has been restarted. While this storage can be local (a hard drive installed inside of it),
it is more common for nodes to connect to a shared, remote fileserver or cluster of servers.

{% include figure.html url="" max-width="40%" file="/fig/node_anatomy.png" alt="Node anatomy" caption="" %}

> ## Explore Your Computer
>
> Try to find out the number of CPUs and amount of memory available on your personal computer.
>
> Note that, if you're logged in to the remote computer cluster, you need to log out first. To
> do so, type `Ctrl+d` or `exit`:
>
> ```
> {{ site.remote.prompt }} exit
> {{ site.local.prompt }}
> ```
> {: .bash}
>
> > ## Solution
> >
> > There are several ways to do this. Most operating systems have a graphical system monitor,
> > like the Windows Task Manager. More detailed information can be found on the command line:
> >
> > * Run system utilities
> >   ```
> >   {{ site.local.prompt }} nproc --all
> >   {{ site.local.prompt }} free -m
> >   ```
> >   {: .bash}
> >
> > * Read from `/proc`
> >   ```
> >   {{ site.local.prompt }} cat /proc/cpuinfo
> >   {{ site.local.prompt }} cat /proc/meminfo
> >   ```
> >   {: .bash}
> >
> > * Run system monitor
> >   ```
> >   {{ site.local.prompt }} htop
> >   ```
> >   {: .bash}
> {: .solution}
{: .challenge}

> ## Explore The Head Node
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
> > {: .bash}
> >
> > You can get more information about the processors using `lscpu`,
> > and a lot of detail about the memory by reading the file `/proc/meminfo`:
> >
> > ```
> > {{ site.remote.prompt }} less /proc/meminfo
> > ```
> > {: .bash}
> >
> > You can also explore the available filesystems using `df` to show **d**isk **f**ree space.
> > The `-h` flag renders the sizes in a human-friendly format, i.e., GB instead of B. The **t**ype
> > flag `-T` shows what kind of filesystem each resource is.
> >
> > ```
> > {{ site.remote.prompt }} df -Th
> > ```
> > {: .bash}
> >
> > > The local filesystems (ext, tmp, xfs, zfs) will depend on whether you're on the same login
> > > node (or compute node, later on). Networked filesystems (beegfs, cifs, gpfs, nfs, pvfs) will
> > > be similar -- but may include yourUserName, depending on how it is [mounted](
> > > https://en.wikipedia.org/wiki/Mount_(computing)).
> > {: .discussion}
> > 
> > > ## Shared file systems
> > > 
> > > This is an important point to remember: files saved on one node (computer) are often available
> > > everywhere on the cluster!
> > {: .callout}
> {: .solution}
{: .challenge}

{% include {{ site.snippets }}/cluster/specific-node-info.snip %}

> ## Compare Your Computer, the Head Node and the Worker Node
>
> Compare your laptop's number of processors and memory with the numbers you see on the cluster 
> head node and worker node. Discuss the differences with your neighbor. 
>
> What implications do you think the differences might have on running your research work on the
> different systems and nodes?
{: .discussion}

> ## Differences Between Nodes
>
> Many HPC clusters have a variety of nodes optimized for particular workloads. Some nodes
> may have larger amount of memory, or specialized resources such as Graphical Processing Units
> (GPUs).
{: .callout}

With all of this in mind, we will now cover how to talk to the cluster's scheduler, and use it to
start running our scripts and programs!
