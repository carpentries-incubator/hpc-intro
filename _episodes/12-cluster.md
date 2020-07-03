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
- "HPC systems typically provides login nodes and a set of worker nodes."
- "The resources found on independent (worker) nodes can vary in volume and type (amount of RAM, processor architecture, availability of network mounted file systems, etc.)."
- "Files saved on one node are available on all nodes."
---

## What is an HPC system?

The words "cloud", "cluster", and "high-performance computing" are used a lot in different contexts
and with varying degrees of correctness. So what do they mean exactly? And more importantly, how do
we use them for our work?

The *cloud* is a generic term commonly used to refer to remote computing resources of any kind --
that is, any computers that you use but are not right in front of you. Cloud can refer to
machines serving websites, providing shared storage, providing webservices (such as e-mail or social
media platforms), as well as more traditional "compute" resources. An *HPC system* on the other hand,
is a term used to describe a network of computers. The computers in a cluster typically share a common
purpose, and are used to accomplish tasks that might otherwise be too big for any one computer.

## Logging in

Go ahead and log in to the cluster: {{ site.remote.name }} at {{ site.remote.location }}.
```
{{ site.local.prompt }} ssh yourUsername@{{ site.remote.login }}
```
{: .bash}

Remember to replace `yourUsername` with the username supplied by the instructors. You will be asked for
your password. But watch out, the characters you type are not displayed on the screen.

You are logging in using a program known as the secure shell or `ssh`. 
This establishes a temporary encrypted connection between your laptop and `{{ site.remote.login }}`.
The word before the `@` symbol, e.g. `yourUsername` here, is the user account name that Lola has access 
permissions for on the cluster. 

> ## Where do I get this `ssh` from ?
>
> On Linux and/or macOS, the `ssh` command line utility is almost always pre-installed. Open a
> terminal and type `ssh --help` to check if that is the case. 
> 
> At the time of writing, the openssh support on Microsoft is still very 
> [recent](https://blogs.msdn.microsoft.com/powershell/2017/12/15/using-the-openssh-beta-in-windows-10-fall-creators-update-and-windows-server-1709/). 
> Alternatives to this are [putty](http://www.putty.org), 
> [bitvise SSH](https://www.bitvise.com/ssh-client-download), 
> [mRemoteNG](https://mremoteng.org/) or [MobaXterm](https://mobaxterm.mobatek.net/). 
> Download it, install it and open the GUI. The GUI asks for your user name and the destination
> address or IP of the computer you want to connect to. Once provided, you will be queried for 
> your password just like in the example above.
{: .callout}

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

## Nodes

Individual computers that compose a cluster are typically called *nodes* (although you will also
hear people call them *servers*, *computers* and *machines*). On a cluster, there are different
types of nodes for different types of tasks. The node where you are right now is called the *head
node*, *login node* or *submit node*. A login node serves as an access point to the cluster. As a
gateway, it is well suited for uploading and downloading files, setting up software, and running
quick tests. It should never be used for doing actual work.

The real work on a cluster gets done by the *worker* (or *compute*) *nodes*. Worker nodes come in
many shapes and sizes, but generally are dedicated to long or hard tasks that require a lot of
computational resources.

All interaction with the worker nodes is handled by a specialized piece of software called a
scheduler (the scheduler used in this lesson is called {{ site.workshop_shed_name }}). We'll
learn more about how to use the scheduler to submit jobs next, but for now, it can also tell us
more information about the worker
nodes.

For example, we can view all of the worker nodes with the `{{ site.sched.info }}` command.

```
{{ site.remote.prompt }} {{ site.sched.info }}
```
{: .bash}

```
{% include {{ site.snippets }}/12/info.snip %}
```
{: .output}

There are also specialized machines used for managing disk storage, user authentication, and other
infrastructure-related tasks. Although we do not typically logon to or interact with these machines
directly, they enable a number of key features like ensuring our user account and files are
available throughout the HPC system.

> ## Shared file systems
>
> This is an important point to remember: files saved on one node (computer) are often available
> everywhere on the cluster!
{: .callout}

## What's in a node? 

All of a HPC system's nodes have the same components as your own laptop or desktop: *CPUs* (sometimes
also called *processors* or *cores*), *memory* (or *RAM*), and *disk* space. CPUs are a computer's
tool for actually running programs and calculations. Information about a current task is stored in
the computer's memory. Disk refers to all storage that can be accessed like a file system. This is
generally storage that can hold data permanently, i.e. data is still there even if the computer has
been restarted.

{% include figure.html url="" max-width="40%" file="/fig/node_anatomy.png" alt="Node anatomy" caption="" %}

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
> {{ site.remote.prompt }} nproc --all
> ```
> {: .language-bash}
> 
> How about memory? Try running: 
>
> ```
> {{ site.remote.prompt }} free -m
> ```
> {: .language-bash}
{: .challenge}



> ## Getting more information
>
> You can get more detailed information on both the processors and memory by using different commands.
>
> For more information on processors use `lscpu`
>
> ```
> {{ site.remote.prompt }} lscpu
> ```
> {: .language-bash}
>
> For more information on memory you can look in the `/proc/meminfo` file:
>
> ```
> {{ site.remote.prompt }} cat /proc/meminfo
> ```
> {: .language-bash}
{: .callout}

{% include {{ site.snippets }}/12/explore.snip %}

> ## Compare Your Computer, the Head Node and the Worker Node
>
> Compare your laptop's number of processors and memory with the numbers you see on the cluster 
> head node and worker node. Discuss the differences with your neighbor. What implications do
> you think the differences might have on running your research work on the different systems
> and nodes?
{: .challenge}

> ## Units and Language
> 
> A computer's memory and disk are measured in units called *Bytes* (one Byte is 8 bits). 
> As today's files and memory have grown to be large given historic standards, volumes are 
> noted using the [SI](https://en.wikipedia.org/wiki/International_System_of_Units) prefixes. 
> So 1000 Bytes is a Kilobyte (kB), 1000 Kilobytes is a Megabyte, 1000 Megabytes is a 
> Gigabyte etc. 
> 
> History and common language have however mixed this notation with a different meaning. 
> When people say "Kilobyte", they mean 1024 Bytes instead. In that spirit, a Megabyte are 
> 1024 Kilobytes. To address this ambiguity, the [International System of 
> Quantities](https://en.wikipedia.org/wiki/International_System_of_Quantities) 
> standardizes the binary prefixes (with base of 1024) by the prefixes kibi, mibi, gibi,
>  etc. For more details, see [here](https://en.wikipedia.org/wiki/Binary_prefix)
{: .callout}

> ## Differences Between Nodes
>
> Many HPC clusters have a variety of nodes optimized for particular workloads. Some nodes
> may have larger amount of memory, or specialized resources such as Graphical Processing Units
> (GPUs).
{: .callout}

With all of this in mind, we will now cover how to talk to the cluster's scheduler, and use it to
start running our scripts and programs!

{% include links.md %}
