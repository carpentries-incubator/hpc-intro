---
layout: page
title: HPC Carpentry Lesson Outline
---

This is the tentative list of tasks and topics for each lesson.
Lesson writers are indicated with first/last initials (e.g. AR).
Feel free to edit the topics for your section.

## [hpc-shell](https://github.com/hpc-carpentry/hpc-shell): UNIX fundamentals on HPC installations

This lesson is hosted in the [hpc-shell](https://github.com/hpc-carpentry/hpc-shell) repo.

* SSH to a cluster 
* Bash fundamentals (`cd`, `ls`, ..., aliases, functions, ~/.bashrc)
* Transferring files (`scp`? `sftp`? Maybe only one?)
* Working with the environment (showing the power of changing `PATH`)
* Introducing modules or similar 


## [hpc-intro](https://github.com/hpc-carpentry/hpc-intro): Submitting / running jobs

This lesson is hosted [here](https://github.com/hpc-carpentry/hpc-intro).

### Overview of cluster resources

* [11-hpc-intro.md](_episodes/11-hpc-intro.md) (brief, concentrate on the concepts not details like interconnect type)

    * What is a server? (remote computer, typically no GUI)
	* What is a cluster? (shared resource, interconnected set of computers, local or distributed storage)
	* What is a cloud?
    * user profiles (academic and/or commercial)
    * story introduction

### Scheduling jobs

* Scheduler - lesson will cover SLURM by default, other schedulers are planned.   
  From [hpc-in-a-day](https://github.com/psteinb/hpc-in-a-day) we know that material comprising Slurm, PBS and LSF is possible, but hard already as e.g. PBS doesn't support direct dispatchment as `srun`.


    * [0] Scheduling basics (why scheduling, what is a job)
    
	* [1] Definition of a job and batch processing 
    * [1] Submitting a job to the scheduler
    * [1] Passing options to the scheduler (log files)
    * [1] Callout: Changing a job's name
    * [1] Optional Callout: Send an email once the job completes (not all sites support sending emails)
    * [2] Requesting resources on a compute node
    
    * [2] Checking status of jobs
    * [2] Wall times
    * [2] Cancelling/deleting a job

* Using software and environment modules (a repetition of [hpc-shell](https://github.com/hpc-carpentry/hpc-shell))
* Playing friendly in the cluster (psteinb: the following is very tricky as it is site dependent)

	* Understanding resource utilisation
	* Profiling code - time, size, etc.
	* Getting system stats
	* Consequences of going over

For the above, [1] can be adapted from [hpc-in-a-day/02-01-batch-systems-101.md](https://github.com/psteinb/hpc-in-a-day/blob/gh-pages/_episodes/02-01-batch-systems-101.md) and [2] can be adapted from [hpc-in-a-day/02-02-advanced-job-scheduling.md](https://github.com/psteinb/hpc-in-a-day/blob/gh-pages/_episodes/02-02-advanced-job-scheduling.md) while merging existing content from [this repo](https://github.com/hpc-carpentry/hpc-intro).

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
