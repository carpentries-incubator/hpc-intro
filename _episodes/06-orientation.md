---
title: "Getting Oriented"
teaching: 10
exercises: 20
questions:
- "How is a cluster laid out?"
objectives:
- "Identify your home directory."
- "Describe the three main components of any computer and what they do."
- "Draw a diagram of your system."
keypoints:
- "All computers have CPUs, memory and disk to perform operations."
- "All large scale computing systems have a log in point and worker nodes."
---

Now that we've logged in, we're going to go for a short tour of the cluster
and talk about some common computing terms.  

## Cluster Orientation

Some useful commands for managing files and directories are:

du -h

ls -lh

ncdu

> ## More directories
>
> If your system has additional directories that are used for running jobs,
> add them here.  

## Terms

Before we do any work on the cluster, we are going to clarify some of the
terms that are being used.  

All computers have three major parts -- their *CPUs* (sometimes also called
  *processors* or *cores*), *memory* (or *RAM*), and *disk* space.  

> ## Explore Your Computer
>
> Find this information

CPUs are a computer's tool for actually running programs and calculations.
Information about a current task is stored in the computer's memory.  Disk
is a computer's long-term storage for information it will need later.

All clusters are essentially a collection of many computers that are
configured in special ways.  These computers, frequently called *nodes*,
have the same pieces (CPU, memory, disk) as your computer but
are larger and instead of being accessed using a screen and graphic interface,
have to be accessed remotely using the command line, as you're doing right now.  

> ## Explore The Head Node
>
> Cpu, proc, stuff
>
> How does this compare to

 The node where you log in (where you are right now)  is
usually called the *head node* (sometimes also *log-in node* or *submit node*).
The nodes that make up the majority of the cluster are called *worker nodes*
(or *execute* nodes).

Go to the next lesson to learn more about the cluster nodes.
