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

First of all, the admin asks Lola to connect to the cluster. She mentions that in the past, compute clusters were named after planets or moons as they often presented distant somewhat mythological places. Her first instructors then often said, that they would use the Space Shuttle (or `ssh` briefly) to reach that planet or moon. So she asks Lola to open a terminal on her laptop and type in the following commands:

~~~ 
$ ssh lola@{{ site.workshop_login_host }}
~~~
{: .bash}

~~~ 
Last login: Tue Mar 14 14:13:14 2018 from lolas_laptop
-bash-4.1$ 
~~~
{: .output}

The admin explains to Lola that she is using the secure shell or `ssh`. This establishes a temporary secure connection between Lola's laptop and `{{ site.workshop_login_host }}`. The word before the `@` symbol, e.g. `lola` here, is the user account name that Lola has access permissions for on the cluster. 

> ## Where do I get this `ssh` from ?
> On Linux and/or macOS, the `ssh` command line utility is typically pre-installed. Just open a terminal and you are good to go. At the time of writing, the openssh support on microsoft is still pretty [recent](https://blogs.msdn.microsoft.com/powershell/2017/12/15/using-the-openssh-beta-in-windows-10-fall-creators-update-and-windows-server-1709/). Alternatives to this are [putty](http://www.putty.org), [bitvise SSH](https://www.bitvise.com/ssh-client-download) or [mRemoteNG](https://mremoteng.org/). Download it, install it and open the GUI. They typically ask for your user name and the destination address or IP. Once provided, you will be queried for your password just like in the example above.
{: .callout}

Rob tells her to use a UNIX command called `ls` (for list directory contents) to have a look around. 

~~~ 
$ ls
~~~
{: .bash}

~~~ 
~~~
{: .output}

To no surprise, there is nothing in there. Rob asks Lola to issue a command to see on what machine she currently is on.

~~~ 
$ hostname
~~~
{: .bash}

~~~ 
{{ site.workshop_login_host }}
~~~
{: .output}

Lola wonders a bit what this may be about, that you need a dedicated command to tell you where you are, but the admin explains to her that he has so many machines under her responsibility, that the output of `hostname` is very valuable.

The admin explains to Lola that she has to work with this remote shell session in order to run programs on the HPC cluster. Launching programs that open a Graphical User Interface (GUI) is possible, but the interaction with the GUI will be slow as everything will have to get transferred through the WiFi network her laptop is currently logged into. Before continuing, she suggests to leave the cluster node again for the sake of practise. For this, Lola can type in `logout` or `exit`.

~~~ 
$ logout
~~~
{: .bash}


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
