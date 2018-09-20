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
* Transferring files (`scp`? `sftp`? Maybe only one?), maybe adapt [15-transferring-files.md](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_episodes/15-transferring-files.md)
* Working with the environment (showing the power of changing `PATH`)
* Introducing modules or similar 


## [hpc-intro](https://github.com/hpc-carpentry/hpc-intro): Submitting / running jobs

This lesson is hosted [here](https://github.com/hpc-carpentry/hpc-intro).

### Overview of cluster resources

* [11-hpc-intro.md](_episodes/11-hpc-intro.md) (brief, concentrate on the concepts not details like interconnect type etc)

    * What is a laptop/desktop? (sketches of a von-Neumann architecture without calling it that)
	* What is a server? (remote computer, typically no GUI)
	* What is a cluster? (shared resource, interconnected set of computers, local or distributed storage)
	* What is a cloud?
    * user profiles (academic and/or commercial)
    * story introduction

### Scheduling jobs

* Scheduler - lesson will cover SLURM by default, other schedulers are planned.   
  From [hpc-in-a-day](https://github.com/psteinb/hpc-in-a-day) we know that material comprising Slurm, PBS and LSF is possible, but hard already as e.g. PBS doesn't support direct dispatchment as `srun`.

    * [12-cluster.md](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_episodes/12-cluster.md)
        * logging in with ssh
        * looking around (compare with your laptop)
        * now what? Scheduling basics (why scheduling, what is a job), see for example [here](https://psteinb.github.io/hpc-in-a-day/02-01-batch-systems-101/) on trying to illustrate the fair share problem
    
    * [13-scheduler.md](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_episodes/13-scheduler.md)
	    * submit a `echo Hello World` on the command line (`srun`, `bsub`, etc.)
        * check the automagically log file for output
        * submit a batch script (`sbatch`, `bsub`, etc)
        * NB: do not dive into options yet
        * for a starting point, see [the bottom half of this](https://psteinb.github.io/hpc-in-a-day/02-01-batch-systems-101/) for reference
        
    * `14-advanced-jobs.md` (doesn't exist yet)
        * Checking status of jobs (`squeue`, `bjobs` etc.), explain different job states and relate to scheduler basics
        * Cancelling/deleting a job (`scancel`, `bkill` etc.)
        * Passing options to the scheduler (log files)
        * Callout: Changing a job's name
        * Optional Callout: Send an email once the job completes (not all sites support sending emails)
        * for a starting point, see [this](https://psteinb.github.io/hpc-in-a-day/02-02-advanced-job-scheduling/) for reference
        
        
    * `15-filesystem-zoo.md` (doesn't exist yet)
        * execute a job that collects node information and stores the output to `/tmp`
        * ask participants where the output went and why they can't see it
        * execute a job that collects node information and stores the output to `/shared` or however your shared file system is called
        * for a starting point, see [this](https://psteinb.github.io/hpc-in-a-day/02-03-shared-filesystem/) for reference
        
* Using software and environment modules (a repetition of [hpc-shell](https://github.com/hpc-carpentry/hpc-shell))

* Playing friendly in the cluster (psteinb: the following is very tricky as it is site dependent, I personally would like to see it in [_extras](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_extras))

	* Understanding resource utilisation
	* Profiling code - time, size, etc.
	* Getting system stats
	* Consequences of going over

## Language refresher / introduction ([Python](https://github.com/hpc-carpentry/hpc-python), [Chapel](https://github.com/hpc-carpentry/hpc-python))

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

## Intro to parallel programming ([Python](https://github.com/hpc-carpentry/hpc-python), [Chapel](https://github.com/hpc-carpentry/hpc-python))

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
