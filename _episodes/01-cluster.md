---
title: "Working on a remote HPC system"
# teaching: 10
teaching: 20
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
- "Files saved on shared storage are available on all nodes."
- "The login node is a shared machine: be considerate of other users."
---

## What Is an HPC System?

The words "cloud", "cluster", and the phrase "high-performance computing" or
"HPC" are used a lot in different contexts and with various related meanings.
So what do they mean? And more importantly, how do we use them in our work?

A *Remote* computer is one you have no access to physically and must connect via a network (as opposed to *Local*)

*Cloud* refers to remote computing resources
that are provisioned to users on demand or as needed.

*HPC*, *High Performance Computer*, *High Performance Computing* or *Supercomputer* are all general terms for a large or powerful computing resource.

*Cluster* is a more specific term describing a type of supercomputer comprised of multiple smaller computers (nodes) working together. Almost all supercomputers are clusters.

## Access

You will connect to a cluster over the internet either with a web client (Jupyter) or with SSH (**S**ecure **Sh**ell). Your main interface with the cluster will be using command line.

## Nodes

Individual computers that compose a cluster are typically called *nodes*
On a cluster, there are different types of nodes for different
types of tasks. The node where you are now will be different depending on
how you accessed the cluster.

Most of you (using JupyterHub) will be on an interactive *compute node*.
This is because Jupyter sessions are launched as a job.  If you are using SSH to connect to the cluster, you will be on a
*login node*. Both JupyterHub and SSH login nodes serve as an access point to the cluster.

<!-- As access points, both the login node and JupyterHub are well suited for uploading and downloading files, setting up software, and running quick tests. Generally speaking, the login node *should
not* be used for time-consuming or resource-intensive tasks. In other words, do not run jobs directly on the login node.  We will learn how to properly run jobs on the cluster in an upcoming lesson. -->

The real work on a cluster gets done by the *compute nodes*.
Compute nodes come in many shapes and sizes, but generally are dedicated to long
or hard tasks that require a lot of computational resources.

## What's in a Node?

A node is similar in makeup to a regular desktop or laptop, composed of *CPUs* (sometimes also called *processors* or *cores*), *memory*
(or *RAM*), and *disk* space. Although, where your laptop might have 8 CPUs and 16GB of memory, a compute node will have hundreds of cores and GB of memory.

* **CPUs** are a computer's tool for running programs and calculations. 

* **Memory** is for short term storage, containing the information currently being operated on by the CPUs.

* **Disk** is for long term storage, data stored here is permanent, i.e. still there even if the computer has been restarted. 
It is common for nodes to connect to a shared, remote disk.

{% include figure.html url="" max-width="40%"
   file="/fig/clusterDiagram.png"
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
> offers dedicated transfer nodes using the Globus service.  More information on using Globus for large data transfer to and from 
> the cluster can be found here: [Globus Transfer Service](https://support.nesi.org.nz/hc/en-gb/sections/360000040596)
{: .callout}

{% include links.md %}
[fshs]: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard