---
layout: page
title: Introduction to HPC Lesson Outline
---

# How to use this outline

The following list of items is meant as a guide on what content should go where in this repo. This should work as a guide where you can contribute. If a bullet point is prefixed by a file name, this is the lesson where the listed content should go into. This document is meant as a concept map converted into a flow learning goals and questions.

# Using a cluster for science

* Prelude
    * User profiles (academic and/or commercial) of clusters
    * Narrative introduction

* [11-hpc-intro.md](_episodes/11-hpc-intro.md): Fundamentals of clusters and their resources resources (brief, concentrate on the concepts not details like interconnect type etc)
    * Be able to describe what an HPC system is
        * And how is this different from a laptop, desktop, cloud, or "server"
    * Identify how an HPC system could benefit you.
    * Jargon busting

* [12-cluster.md](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_episodes/12-cluster.md)
    * Connect to a cluster using ssh: 
    * Transfer files to and from the cluster
    * Run the hostname command on a compute node of the cluster.
    * Potential tools: ssh, ls, hostname, logout, nproc, free, scp, man, w
        
    

* Scheduler - 
  
* [13-scheduler.md](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_episodes/13-scheduler.md)
Lesson will cover SLURM by default, other schedulers are planned.  From [hpc-in-a-day](https://github.com/psteinb/hpc-in-a-day) we know that material comprising Slurm, PBS and LSF is possible, but hard already as e.g. PBS doesn't support direct dispatchment as `srun`.
    * Know how to submit a program and batch scrip to the cluster (interactive & batch)
    * Use the batch system command line tools to monitor the execution of your job.
    * Inspect the output and error files of your jobs.
    * Potential tools: shell script, sbatch, squeue -u, watch, -N, -n, -c, --mem, --time, scancel, srun, --x11 --pty, 
    * Extras: --mail-user, --mail-type, 
    * Remove? watch, 
    * Later lessons? -N -n -c
    
* [14-Accessing Software]
    * Understand how to load and use a software package.
    * Tools: module avail, module load, which, echo $PATH, module list, module unload, module purge, .bashrc, .bash_profile, git clone, make, 
    * Remove: make, git clone, 
    * Extras: .bashrc, .bash_profile

* [15-Filesystems and Storage]

* [16- Transferring Files]
    * Be able to transfer files to and from a computing cluster.
    * Tools: wget, scp, rsync (callout), mkdir, FileZilla, 
    * Remove: dos2unix, unix2dos,
    * Bonus: gzip, tar, dos2unix, cat, unix2dos, sftp, pwd, lpwd, put, get, 
    * Later:

* [17- Using Resources Effectively]
    * Understand how to look up job statistics and profile code.
    * Understand job size implications.
    * Tools: fastqc, sacct, ssh, top, free, ps, kill, killall

# Lesson ideas up for debate

* Using software and environment modules (a repetition of [hpc-shell](https://github.com/hpc-carpentry/hpc-shell) potentially)

* Playing friendly in the cluster (psteinb: the following is very tricky as it is site dependent, I personally would like to see it in [_extras](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_extras))

	* Understanding resource utilisation
	* Profiling code - time, size, etc.
	* Getting system stats
	* Consequences of going over
	

* `Advanced-jobs.md` (doesn't exist yet)
        * Checking status of jobs (`squeue`, `bjobs` etc.), explain different job states and relate to scheduler basics
        * Cancelling/deleting a job (`scancel`, `bkill` etc.)
        * Passing options to the scheduler (log files)
        * Callout: Changing a job's name
        * Optional Callout: Send an email once the job completes (not all sites support sending emails)
        * for a starting point, see [this](https://psteinb.github.io/hpc-in-a-day/02-02-advanced-job-scheduling/) for reference
        
        
* `Filesystem-zoo.md` (doesn't exist yet)
    * execute a job that collects node information and stores the output to `/tmp`
    * ask participants where the output went and why they can't see it
    * execute a job that collects node information and stores the output to `/shared` or however your shared file system is called
    * for a starting point, see [this](https://psteinb.github.io/hpc-in-a-day/02-03-shared-filesystem/) for reference

