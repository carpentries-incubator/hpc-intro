---
title: "Working on a remote HPC system"
teaching: 10
exercises: 0
start: true
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
- "Files saved on shared storage are available on all nodes."
- "The login node is a shared machine: be considerate of other users."
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

As access points, both the login node and JupyterHub are well suited for uploading and downloading files, setting up software, and running quick tests. Generally speaking, the login node *should
not* be used for time-consuming or resource-intensive tasks.   In other words, do not run jobs directly on the login node.  We will learn how to properly run jobs on the cluster in an upcoming lesson.


The real work on a cluster gets done by the *compute nodes*.
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

> ## Differences Between Nodes
>
> Many HPC clusters have a variety of nodes optimized for particular workloads.
> Some nodes may have larger amount of memory, or specialized resources such as
> Graphical Processing Units (GPUs).
{: .callout}
> ## Dedicated Transfer Nodes
>
> If you want to transfer larger amounts of data to or from the cluster, NeSI
> offers dedicated transfer nodes using the Globus service.  More information on using Globus for large data transfer to and from the 
> cluster can be found here: [Globus Transfer Service](https://support.nesi.org.nz/hc/en-gb/sections/360000040596)
{: .callout}

{% include links.md %}

[fshs]: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard