---
title: "Working on a remote HPC system"
teaching: 10
exercises: 0
questions:
- "What is an HPC system?"
- "How does an HPC system work?"
- "How do I log in to a remote HPC system?"
objectives:
- "Connect to a remote HPC system."
- "Understand the general HPC system architecture."
keypoints:
- "An HPC system is a set of networked machines."
- "HPC systems typically provide login nodes and a set of compute nodes."
- "The resources found on independent (compute) nodes can vary in volume and
  type (amount of RAM, processor architecture, availability of network mounted
  filesystems, etc.)."
- "Files saved on one node are available on all nodes."
---

## What Is an HPC System?

The words "cloud", "cluster", and the phrase "high-performance computing" or
"HPC" are used a lot in different contexts and with various related meanings.
So what do they mean? And more importantly, how do we use them in our work?

The *cloud* refers to computing resources
that are provisioned to users on demand or as needed.
Cloud resources may refer to machines performing relatively simple tasks such as
serving websites, providing shared storage, providing web services (such as
e-mail or social media platforms), as well as more traditional compute
intensive tasks such as running a simulation.

*HPC*, *High Performance Computer*, *High Performance Computing* or *Supercomputer* are all general terms for a large or powerful computing resource.


*Cluster* is a more specific term describing a type of supercomputer comprised of multiple smaller computers (nodes) working together. Almost all supercomputers are clusters.

## Nodes

Individual computers that compose a cluster are typically called *nodes*
(although you will also hear people call them *servers*, *computers* or
*hosts*). On a cluster, there are different types of nodes for different
types of tasks. The node where you are now will be different depending on 
how you accessed the cluster.  Most of you (using JupyterHub) will be on an interactive *compute node*. 
This is because Jupyter sessions are launched as a job.  If you are using SSH to connect to the cluster, you will be on a
*login node*. Both JupyterHub and SSH login nodes serve as an access point to the cluster.

As access points, both the login node and JupyterHub are well suited for uploading and downloading files, setting up
software, and running quick tests. Generally speaking, the login node *should
not* be used for time-consuming or resource-intensive tasks.   In other words, do not run jobs directly on the login node.  We will learn how to properly run jobs on the cluster in an upcoming lesson.


The real work on a cluster gets done by the *compute* *nodes*.
Compute nodes come in many shapes and sizes, but generally are dedicated to long
or hard tasks that require a lot of computational resources.

All interaction with the compute nodes is handled by a specialized piece of
software called a scheduler (the scheduler used in this lesson is called
{{ site.sched.name }}). We'll learn more about how to use the {{ site.sched.name }}
scheduler to submit jobs in an upcoming lesson, but for now, it can also tell us more
information about the compute nodes.

For example, we can view all of the compute nodes by running the command
`{{ site.sched.info }}`.

```
{{ site.remote.prompt }} {{ site.sched.info }}
```
{: .language-bash}

{% include {{ site.snippets }}/cluster/queue-info.snip %}

## What's in a Node?

All of the nodes in an HPC system have the same components as your own laptop
or desktop: *CPUs* (sometimes also called *processors* or *cores*), *memory*
(or *RAM*), and *disk* space. CPUs are a computer's tool for actually running
programs and calculations. Information about a current task is stored in the
computer's memory. Disk refers to all storage that can be accessed like a file
system. This is generally storage that can hold data permanently, i.e. data is
still there even if the computer has been restarted. While this storage can be
local (a hard drive installed inside of it), it is more common for nodes to
connect to a shared, remote fileserver or cluster of servers.  You will learn more about disk storage in an upcoming lesson.

{% include figure.html url="" max-width="40%"
   file="/fig/node_anatomy.png"
   alt="Node anatomy" caption="" %}

<!-- > ## Explore Your Computer
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
> > > The local filesystems (ext, tmp, xfs, zfs) will depend on whether you're
> > > on the same login node (or compute node, later on). Networked filesystems
> > > (beegfs, cifs, gpfs, nfs, pvfs) will be similar &mdash; but may include
> > > {{ site.remote.user }}, depending on how it is [mounted](
> > > https://en.wikipedia.org/wiki/Mount_(computing)).
> > {: .discussion}
> >
> > > ## Shared Filesystems
> > >
> > > This is an important point to remember: files saved on one node
> > > (computer) are often available everywhere on the cluster!
> > {: .callout}
> {: .solution}
{: .challenge}

{% include {{ site.snippets }}/cluster/specific-node-info.snip %} -->

> ## Differences Between Nodes
>
> Many HPC clusters have a variety of nodes optimized for particular workloads.
> Some nodes may have larger amount of memory, or specialized resources such as
> Graphical Processing Units (GPUs).
{: .callout}
> ## Dedicated Transfer Nodes
>
> If you want to transfer larger amounts of data to or from the cluster, NeSI
> offers dedicated transfer nodes using the Globus service.  More infromation on using Globus for large data transfer to and from the 
> cluster can be found here: [Globus Transfer Service](https://support.nesi.org.nz/hc/en-gb/sections/360000040596)
{: .callout}

{% include links.md %}

[fshs]: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
[putty-gen]: https://tartarus.org/~simon/putty-prerel-snapshots/htmldoc/Chapter8.html#pubkey-puttygen
[putty-agent]: https://tartarus.org/~simon/putty-prerel-snapshots/htmldoc/Chapter9.html#pageant
[ssh-agent]: https://www.ssh.com/academy/ssh/agent
[ssh-flags]: https://stribika.github.io/2015/01/04/secure-secure-shell.html
[wiki-rsa]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[wiki-dsa]: https://en.wikipedia.org/wiki/EdDSA
