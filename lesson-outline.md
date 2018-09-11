---
layout: page
title: Lesson outline and todo list
---
# Lesson outline and todo list

This is the tentative list of tasks and topics for each lesson.
Lesson writers are indicated with first/last initials (e.g. AR).
Feel free to edit the topics for your section.

## 1. UNIX fundamentals

This lesson is hosted in the [hpc-shell](https://github.com/hpc-carpentry/hpc-shell) repo.

* SSH to a cluster
* Bash fundamentals (`cd`, `ls`, ..., aliases, functions, ~/.bashrc)
* Transferring files (`scp`? `sftp`? Maybe only one?)
* Working with the environment
* Overview of HPC resources

	* What is a cloud?
	* What is a cluster? Different cluster types
	* Overview of services available (Compute Canada, Amazon EC2, etc.)

## 2. Submitting / running jobs

This lesson is hosted in the [hpc-intro](https://github.com/hpc-carpentry/hpc-intro) repo.

* Scheduler - lesson will cover SLURM by default (which can also run PBS scripts/commands natively)

	* Submitting jobs
	* Checking status of jobs
	* Deleting jobs
	* Job size consequences
	* GUI vs. batch programs (X-forwarding, SSH tunnels?)

* Using software and environment modules
* Playing friendly in the cluster

	* Understanding resource utilisation
	* Profiling code - time, size, etc.
	* Getting system stats
	* Consequences of going over

## 3. Language refresher / introduction (Python - JB, Chapel - JZ+AR)

* Programming language concepts

	* Compiled vs. interpreted languages
	* How does a program work?
	* Quick intro of programming language of choice

		* Major features + pros/cons
		* What is it good at? 

* Actual language overview

	* Basic syntax (arithmetic, variables, etc.)
	* Basic data structures (lists, arrays, etc.)
	* Defining functions
	* Conditional expressions
	* For-loops
	* Reading/writing data

Some side notes: 
perhaps a quick refresh of key concepts right before use in parallel section,
certain concepts could get mixed in right before they're needed by the parallel lesson.

## 4. Intro to parallel programming (Python - JB, Chapel - JZ+AR)

* Pipelining / automatic job submission / serial farming
* Shared memory programming
* Distributed memory programming
* Overview of good parallel design

	* Dependencies within own code
	* Race conditions

* Typical problems and bottlenecks

	* running in parallel (parallel scaling)
	* parallel I/O (don't write a 1GB file from one processor if data is already distributed, etc.)
	* Storage limitations (millions of files, compression, text vs. binary storage)
	* Filesystem choice (home, scratch, tmp, etc.)


Good luck!
