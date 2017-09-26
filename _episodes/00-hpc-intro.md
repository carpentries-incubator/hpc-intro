---
title: "High Performance Computing Introduction"
teaching: 5
exercises: 0
questions:
- "Why would I be interested in High Performance Computing (HPC)?"
- "What can I expect to learn from this course?"
objectives:
- "Be able to describe what an HPC system is"
- "Explain the difference between a cloud-based and a cluster-based system"
keypoints:
- "High Performance Computing (HPC) typically involves connecting to very large computing systems elsewhere in the world."
- "These other systems can be used to do work that would either be impossible or much slower or smaller systems."
- "Using these systems usually requires submitting tasks, often referred to as \"jobs\" to a program called a scheduler that determines when your turn on the system is."
- "The standard method of interacting with such systems is via a linux-based command line interface called \"The Shell\"."
---

### What is High Performance Computing (HPC)?

High Performance Computing (HPC) is the name given to the use of computers with capabilities well beyond the scope of standard desktop computers.   The computers that qualify as HPC systems are typically seen as being more powerful than other systems, usually because they have more central processing units (CPUs), CPUs that operate at higher speeds, more memory, more storage, and faster connections with other computer systems.  HPC systems are used when the resources of more standard computers, such as most dektops and laptops, are not enough to provide results in a timely fashion, if at all.

Using HPC systems often involves the use of a shell through a command line interface (CLI) and either specialized software or programming techniques.  The shell is a program with the special role of having the job of running other programs rather than doing calculations or similar tasks itself.  
What the user types goes into the shell,
which then figures out what commands to run and orders the computer to execute them.
(Note that the shell is called "the shell" because it encloses the operating system
in order to hide some of its complexity and make it simpler to interact with.)  The most popular Unix shell is Bash,
the Bourne Again SHell
(so-called because it's derived from a shell written by Stephen Bourne).
Bash is the default shell on most modern implementations of Unix
and in most packages that provide Unix-like tools for Windows.

Interacting with the shell is done via a command line interface (CLI) on most HPC systems.  In the earliest days of computers,
the only way to interact with early computers was to rewire them.
From the 1950s to the 1980s 
most people used line printers.
These devices only allowed input and output of the letters, numbers, and punctuation found on a standard keyboard,
so programming languages and software interfaces had to be designed around that constraint and text-based interfaces were the way to do this.  Typing-based interfaces are often called a
**command-line interface**, or CLI,
to distinguish it from a
**graphical user interface**, or GUI,
which most people now use.
The heart of a CLI is a **read-evaluate-print loop**, or REPL:
when the user types a command and then presses the Enter (or Return) key,
the computer reads it,
executes it,
and prints its output.
The user then types another command,
and so on until the user logs off.


### Why HPC?

Learning to use Bash or any other shell
sometimes feels more like programming than like using a mouse.
Commands are terse (often only a couple of characters long),
their names are frequently cryptic,
and their output is lines of text rather than something visual like a graph.
On the other hand,
with only a few keystrokes, the shell allows us to combine existing tools into 
powerful pipelines and handle large volumes of data automatically. This automation
not only makes us more productive but also improves the reproducibility of our workflows by 
allowing us to repeat them with a few simple commands.
In addition, the command line is often the easiest way to interact with remote machines and supercomputers.
Familiarity with the shell is near essential to run a variety of specialized tools and resources
including high-performance computing systems.
As clusters and cloud computing systems become more popular for scientific data crunching,
being able to interact with the shell is becoming a necessary skill.

The benefits of using HPC systems for research often far outweigh the cost of learning to use a Shell and include:

* **Speed.** With many more CPU cores, often with higher performance specs, than the computers most people have access to HPC systems can offer significant speed up.
* **Volume.** Many HPC systems have both the processing memory (RAM) and disk storage to handle very large amounts of data.  Terrabytes of RAM and Petabytes of storage are available for research projects judged to be deserving of such resources.
* **Efficiency.** Many HPC systems operate a pool of resources that are drawn on by a many users.  In most cases when the pool is large and diverse enough the resources on the system are used almost constantly.
* **Cost.** Bulk purchasing and government funding mean that the cost to the research community for using these systems in significantly less that it would be otherwise.
* **Keep personal resources free.** By using an HPC system when required your own personal computer can be used for other things to which it is better suited, like email and spreadsheets.

### Example: Nelle's Pipeline: Starting Point

Consider the case of Nelle Nemo, a marine biologist, who
has returned from a six-month survey of the
[North Pacific Gyre](http://en.wikipedia.org/wiki/North_Pacific_Gyre),
where she has been sampling gelatinous marine life in the
[Great Pacific Garbage Patch](http://en.wikipedia.org/wiki/Great_Pacific_Garbage_Patch).
She collected 10,000 samples in all, and has run each sample through an assay machine
that measures the abundance of 300 different proteins.
The machine's output for a single sample is
a file with one line for each protein.
For example, the file `NENE01812A.csv` looks like this:

~~~
72,0.142961371327
265,0.452337146655
279,0.332503761597
25,0.557135549292
207,0.55632965303
107,0.96031076351
124,0.662827329632
193,0.814807235075
32,1.82402616061
99,0.7060230697
.
.
.
.
200,1.13383446523
264,0.552846392611
268,0.0767025200665
~~~

Each line consists of two "fields", separated by a comma (`,`).
The first field identifies the protein,
and the second field is a measure of the amount of protein in the sample.
Nelle needs to accomplish tasks such as the following:

1.  For any given file, extract the amount of a given protein.
2.  Find the maximum amount of a given protein across all files.
3.  For each file, run a program called `stats.py` that she wrote,
    which produces a graph, and writes some statistics
    (these go in the directories `plots/` and `results/` respectively.)

Suppose that each file takes about a minute to analyze on her desktop system and consuming all of the resources available, so no email or any other work while the program is running.  With 10,000 files in all this means that it will take approximately 166 hours, or just under 7 days to completely process all the files. 

Shifting this work to an HPC system will not only stand to speed up the processig of these files but the processing will importantly allow Nelle to continue to use her own computer for other work.

[Example modified from [clemsonciti](https://github.com/clemsonciti/hpc-workshop/).]

## Cloud vs Cluster

Traditionally "HPC" is used to refer to computer systems known as "clusters" because they are groups of computer cores (or central processing units (CPUs)) and resources like memory and storage joined together by special networks that allow these computers to work together at very high speeds.  Such machines often have tens of thousands---or even hundreds of thousands---of cores.

Clusters often share their resources among a large number of users through a piece of software called a scheduler.  When people want to use such a cluster they have to tell the scheduler that they want to do some work and what that work looks like in terms of the number of cores and the amount of memory that they plan to use.  The scheduler then gives them resources when they are available and when their "priority" (a score or ranking that is increased by how valuable their work is seen as being and decreased as they use resources) is high enough.

Another type of computing resource that is catching attention and that is sometimes included in the term "HPC" is "the cloud".  When understood most broadly      using the cloud amounts to using a computer that is elsewhere and on this understanding most of the Internet and the clusters mentioned earlier are part of the cloud.  Often a narrower understanding is meant though...  

Final point is that we're really focused on cluster-based computing in this course.