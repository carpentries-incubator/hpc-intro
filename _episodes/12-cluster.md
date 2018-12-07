---
title: "Working on a cluster"
teaching: 15
exercises: 10
questions:
- "What is a cluster?"
- "How does a cluster work?"
- "How do I log on to a cluster?"
objectives:
- "Connect to a cluster."
- "Understand the general cluster architecture."
keypoints:
- "A cluster is a set of networked machines."
- "Clusters typically provide a login node and a set of worker nodes."
- "Files saved on one node are available everywhere."
---

## The Story

Through out this material, we will assist Lola Curious and look over her shoulder while she is starting to work at the Institute of Things as a side job to earn some extra money. 

On the first day, her supervisor greets her friendly and welcomes her to the job. She explains what her task is and suggests her that she will need to use the cluster on the campus. Lola has so far used her Laptop at home for her studies, so the idea of using a super computer appears a bit intimidating to her. Her supervisor notices her anxiety and tells her that she will receive an introduction to the super computer after she has requested an account on the cluster. 

Lola walks to the IT department and finishes the paper work to get an account. One of the admins promises to sit down with her in the morning to show her the way around the machine. The admin explains that Lola will use a small to mid-range HPC cluster.

{% include links.md %}

## Where are we?

Go ahead and log in to the cluster.
```
[user@laptop]$ ssh remote
```
{: .bash}


Very often, many users are tempted to think of a high-performance computing installation as one
giant, magical machine. Sometimes, people will assume that the computer they've logged onto is the
entire computing cluster. So what's really happening? What computer have we logged on to? The name
of the current computer we are logged onto can be checked with the `hostname` command. (Clever users
will notice that the current hostname is also part of our prompt!)

```
[remote]$ hostname
```
{: .bash}
```
gra-login3
```
{: .output}

Individual computers that compose a cluster are typically called *nodes* (although you will also
hear people call them *servers*, *computers* and *machines*). On a cluster, there are different
types of nodes for different types of tasks. The node where you are right now is called the *head
node*, *login node* or *submit node*. A login node serves as an access point to the cluster. As a
gateway, it is well suited for uploading and downloading files, setting up software, and running
quick tests. It should never be used for doing actual work.

The real work on a cluster gets done by the *worker* (or *execute*) *nodes*. Worker nodes come in
many shapes and sizes, but generally are dedicated to doing all of the heavy lifting that needs
doing.

All interaction with the worker nodes is handled by a specialised piece of software called a
scheduler (the scheduler used in this lesson is called SLURM). We'll learn more about how to use the
scheduler to submit jobs next, but for now, it can also tell us more information about the worker
nodes.

For example, we can view all of the worker nodes with the `sinfo` command.

```
[remote]$ sinfo
```
{: .bash}
```
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
compute*     up 7-00:00:00      1 drain* gra259
compute*     up 7-00:00:00     11  down* gra[8,99,211,268,376,635,647,803,852,966,986]
compute*     up 7-00:00:00      1   drng gra272
compute*     up 7-00:00:00     31   comp gra[988-991,994-1002,1006-1007,1015,1017,1021-1022,1028-...
compute*     up 7-00:00:00     33  drain gra[225-251,253-256,677,1026]
compute*     up 7-00:00:00    323    mix gra[7,13,25,41,43-44,56,58-77,107-108,112-113,117,125-12...
compute*     up 7-00:00:00    464  alloc gra[1-6,9-12,14-19,21-24,26-40,42,45-55,57,100-106,109-1...
compute*     up 7-00:00:00    176   idle gra[78-98,123-124,128-162,170-172,285-299,429-447,449-45...
compute*     up 7-00:00:00      3   down gra[20,801,937]
```
{: .output}

There are also specialised machines used for managing disk storage, user authentication, and other
infrastructure-related tasks. Although we do not typically logon to or interact with these machines
directly, they enable a number of key features like ensuring our user account and files are
available throughout the cluster. This is an important point to remember: files saved on one node
(computer) are available everywhere on the cluster!

## What's in a node? 

All of a cluster's nodes have the same components as your own laptop or desktop: *CPUs* (sometimes
also called *processors* or *cores*), *memory* (or *RAM*), and *disk* space. CPUs are a computer's
tool for actually running programs and calculations. Information about a current task is stored in
the computer's memory. Disk is a computer's long-term storage for information it will need later.

> ## Explore Your Computer
>
> Try to find out the number of CPUs and amount of memory available on your personal computer.
{: .challenge}

> ## Explore The Head Node
>
> Now we'll compare the size of your computer with the size of the head node: To see the number of
> processors, run:
>
> ```
> nproc --all
> ```
> {: .bash}
>
> or
>
> ```
> cat /proc/cpuinfo
> ```
> {: .bash}
>
> to see full details.
> 
> How about memory? Try running: 
>
> ```
> free -m
> ```
> {: .bash}
>
> or for more details: 
>
> ```
> cat /proc/meminfo
> ```
> {: .bash}
{: .challenge}

> ## Explore a Worker Node
> 
> Finally, let's look at the resources available on the worker nodes where your jobs will actually
> run. Try running this command to see the name, CPUs and memory available on the worker nodes:
>
> ```
> sinfo -n aci-377 -o "%n %c %m"
> ```
> {: .bash}
{: .challenge}

> ## Differences Between Nodes
> Many HPC clusters have a variety of nodes optimized for particular workloads. Some nodes may have larger amount of memory, or specialized resources such as Graphical Processing Units.
{: .callout}

> ## Units
> 
> A computer's memory and disk are measured in units called *bytes*. The magnitude of a file or
> memory use is measured using the same prefixes of the metric system: kilo, mega, giga, tera. So
> 1024 bytes is a kilobyte, 1024 kilobytes is a megabyte, and so on.
{: .callout}

With all of this in mind, we will now cover how to talk to the cluster's scheduler, and use it to
start running our scripts and programs!

{% include links.md %}
