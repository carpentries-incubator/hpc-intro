---
title: "What is High Performance Computing?"
teaching: 15 
exercises: 5
questions:
- "Why would I be interested in High Performance Computing (HPC)?"
- "What can I expect to learn from this course?"
objectives:
- "Be able to describe what an HPC system is"
- "Identify how an HPC system could benefit you."  
keypoints:
- "High Performance Computing (HPC) typically involves connecting to very large computing systems elsewhere in the world."
- "These other systems can be used to do work that would either be impossible or much slower or smaller systems."
- "The standard method of interacting with such systems is via a command line interface called Bash."
---

## What is High Performance Computing (HPC)?

High Performance Computing (HPC) is the name given to the use of computers with
capabilities well beyond the scope of standard desktop computers.   The
computers that qualify as HPC systems are typically seen as being more powerful
than other systems, usually because they have more central processing units
(CPUs), CPUs that operate at higher speeds, more memory, more storage, and
faster connections with other computer systems.  HPC systems are used when the
resources of more standard computers, such as most dektops and laptops, are not
enough to provide results in a timely fashion, if at all.

Using HPC systems often involves the use of a shell through a command line
interface (CLI) and either specialized software or programming techniques.  The
shell is a program with the special role of having the job of running other
programs rather than doing calculations or similar tasks itself.  What the user
types goes into the shell, which then figures out what commands to run and
orders the computer to execute them.  (Note that the shell is called "the
shell" because it encloses the operating system in order to hide some of its
complexity and make it simpler to interact with.)  The most popular Unix shell
is Bash, the Bourne Again SHell (so-called because it's derived from a shell
written by Stephen Bourne).  Bash is the default shell on most modern
implementations of Unix and in most packages that provide Unix-like tools for
Windows.

Interacting with the shell is done via a command line interface (CLI) on most
HPC systems.  In the earliest days of computers, the only way to interact with
early computers was to rewire them.  From the 1950s to the 1980s most people
used line printers.  These devices only allowed input and output of the
letters, numbers, and punctuation found on a standard keyboard, so programming
languages and software interfaces had to be designed around that constraint and
text-based interfaces were the way to do this.  Typing-based interfaces are
often called a **command-line interface**, or CLI, to distinguish it from a
**graphical user interface**, or GUI, which most people now use.  The heart of
a CLI is a **read-evaluate-print loop**, or REPL: when the user types a command
and then presses the Enter (or Return) key, the computer reads it, executes it,
and prints its output.  The user then types another command, and so on until
the user logs off.

## Why HPC?

Of course, the important question to ask is why learn how to do all this?
Learning to use Bash or any other shell sometimes feels more like programming
than like using a mouse.  Commands are terse (often only a couple of characters
long), their names are frequently cryptic, and their output is lines of text
rather than something visual like a graph. 

Where's the payoff?

The benefits of using HPC systems often far outweigh the cost of
learning to use them, including:

* **Speed.** With many more CPU cores, often with higher performance specs,
  than the computers most people have access to HPC systems can offer
  significant speed up.
* **Volume.** Many HPC systems have both the processing memory (RAM) and disk
  storage to handle very large amounts of data. Terabytes of RAM and
  petabytes of storage are available for research projects.
* **Efficiency.** Many HPC systems operate a pool of resources that are drawn
  on by a many users.  In most cases when the pool is large and diverse enough
  the resources on the system are used almost constantly.
* **Cost.** Bulk purchasing and government funding mean that the cost to the
  research community for using these systems in significantly less that it
  would be otherwise.
* **Convenience.** Maybe your calculations just take a long time to run or are
  otherwise inconvenient to run on your personal computer. There's no need to
  tie up your own computer for hours when you can use someone else's instead.

## The rest of this lesson

The only way to use these types of resources is by learning to use the command line.
This introduction to HPC systems has two parts:

* We will learn to use the UNIX command line (also known as Bash).
* We will use our new Bash skills to connect to and operate a high-performance computing supercomputer.

The skills we learn here have other uses beyond just HPC - 
Bash and UNIX skills used everywhere, be it for web development, running software, or operating servers.
It's become so essential that Microsoft 
[now ships it as part of Windows](https://www.microsoft.com/en-us/store/p/ubuntu/9nblggh4msv6)!
Knowing how to use Bash and HPC systems will allow you to operate virtually any modern device.
Wit all of this in mind, let's connect to a cluster and get started!
