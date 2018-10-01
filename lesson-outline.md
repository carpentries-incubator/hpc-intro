---
layout: page
title: Introduction to HPC Lesson Outline
---

# Fundamentals of cluster resources

* [11-hpc-intro.md](_episodes/11-hpc-intro.md) (brief, concentrate on the concepts not details like interconnect type etc)

    * What is a laptop/desktop? (sketches of a von-Neumann architecture without calling it that)
	* What is a server? (remote computer, typically no GUI)
	* What is a cluster? (shared resource, interconnected set of computers, local or distributed storage)
	* What is a cloud?
    * user profiles (academic and/or commercial)
    * story introduction

# Jobs

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
