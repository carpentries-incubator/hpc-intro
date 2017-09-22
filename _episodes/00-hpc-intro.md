---
title: "High Performance Computing Introduction"
teaching: 0
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
- "The standard method of interacting with such systems is via a linux-based command line interface."
---

## Why High Performance Computing (HPC)?

High Performance Computing (HPC) is the name given to the use of computers well beyond the scope of standard desktop computers.  Using HPC systems is needed when the resources of the more standard computers that are avaialable are not enough to provide results in a timely fashion, if at all. 

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

## Interacting with HPC Resources

Interacting with HPC systems is usually done through a text-based interface known as the "command line" that is a standard part of Linux, the operating system (OS) that is deployed on most clusters...