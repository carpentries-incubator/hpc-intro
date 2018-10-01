---
layout: page
title: Introduction to HPC Lesson Outline
---

# How to use this outline

The following list of items is meant as a guide on what content should go where in this repo. This should work as a guide where you can contribute. If a bullet point is prefixed by a file name, this is the lesson where the listed content should go into. This document is meant as a concept map converted into a flow learning goals and questions.

# Fundamentals of cluster resources

* [11-hpc-intro.md](_episodes/11-hpc-intro.md) (brief, concentrate on the concepts not details like interconnect type etc)

    * What is a laptop/desktop? 
        * sketches of a von-Neumann architecture without calling it that
        * machine is mostly controlled through keyboard/mouse inputs
        
	* What is a server? 
        * remote computer
        * typically no GUI
        * only reachable by some form of network
        
	* What is a cluster? 
        * shared resource
        * interconnected set of computers by means of a network
        * local or distributed storage, only reachable by some form of network
        
	* What is a cloud?  
        * on-demand virtualized resource with exclusive usage permissions by the user
        
    * user profiles (academic and/or commercial) of clusters
    * story introduction (in the following 

# Using a cluster for science

* Scheduler - lesson will cover SLURM by default, other schedulers are planned.   
  From [hpc-in-a-day](https://github.com/psteinb/hpc-in-a-day) we know that material comprising Slurm, PBS and LSF is possible, but hard already as e.g. PBS doesn't support direct dispatchment as `srun`.

    * [12-cluster.md](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_episodes/12-cluster.md)
        * logging in with ssh
        * looking around (compare with your laptop)
        * now what? Scheduling basics (why scheduling, what is a job), see for example [here](https://psteinb.github.io/hpc-in-a-day/02-01-batch-systems-101/) on trying to illustrate the fair share problem
    
    * [13-scheduler.md](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_episodes/13-scheduler.md)
	    * submit a `echo Hello World` on the command line (`srun`, `bsub`, etc.)
        * second iteration of `srun` et al, use `hostname` to illustrate that the process is not running on the login node
        * check the automagically created log file for output
        * submit a batch script (`sbatch`, `bsub`, etc) doing the same as above or alternatively use `hostname`
        * NB: do not dive into options yet of the submit command
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
