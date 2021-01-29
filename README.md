# Intro to HPC 

This lesson teaches the basics of interacting with high-performance computing (HPC) clusters
through the command line

[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fhpc-carpentry%2Fhpc-intro%2Fbadge%3Fref%3Dgh-pages&style=flat)](https://actions-badge.atrox.dev/hpc-carpentry/hpc-intro/goto?ref=gh-pages)

## Using this material

NOTE: This is *not* Carpentries boilerplate! Please read carefully.

1. Follow the instructions found in The Carpentries' [example lesson](
   https://github.com/carpentries/lesson-example/) to create a repository for your lesson. Install
   Ruby, Make, and Jekyll following the instructions
   [here](http://carpentries.github.io/lesson-example/setup.html).

2. For easier portability, we use snippets of text and code to capture inputs and outputs that are
   host- or site-specific and cannot be scripted. These are stored in a library,
   [_includes/snippets_library](_includes/snippets_library), with subdirectories matching the
   pattern `InstitutionName_ClusterName_scheduler`. If your cluster is not already present, 
   please copy (`cp -r`) the *closest match* as a new folder under `snippets_library`.

   - We have placed snippets in files with the `.snip` extension, to make tracking easier. These
     files contain Markdown-formatted text, and will render to HTML when the lesson is built.
   - Code snippets are placed in subdirectories that are named according to the episode they
     appear in. For example, if the snippet is for episode 12, then it will be in a 
     subdirectory called `12`.
   - In the episodes source, snippets are included using [Liquid](
     https://shopify.github.io/liquid/) scripting  `include` statements. For example, the first
     snippet in episode 12 is included using `{% include /snippets/12/info.snip %}`.

3. Edit `_config_options.yml` in your snippets folder. These options set such things as the address
   of the host to login to, definitions of the command prompt, and scheduler names.

4. Set the environment variable `HPC_JEKYLL_CONFIG` to the relative path of the configuration file
   in your snippets folder:
   `export HPC_JEKYLL_CONFIG=_includes/snippets_library/Site_Cluster_scheduler/_config_options.yml`.

5. Preview the lesson locally, by running `make serve`. You can then view the website in your
   browser, following the links in the output (usually, <https://localhost:4000>). Pages will be
   automatically regenerated every time you write to them.
   
6. If there are discrepancies in the output, edit the snippet file containing it, or create a new
   one and customize.

7. Add your snippet directory name to the GitHub Actions configuration file,
   [.github/workflows/test_and_build.yml](.github/workflows/test_and_build.yml).

8. Check out a new branch, commit your changes, and push to your fork of the repository. If you're
   comfortable sharing, please file a Pull Request against our [upstream repo](
   https://github.com/carpentries-incubator/hpc-intro). We would love to have your site config for
   the Library.
   
9. *TODO:* Document deploying the site-specific branch on GitHub (and maybe GitLab).


## Lesson Outlines

The following list of items is meant as a guide on what content should go where in this repo. This
should work as a guide where you can contribute. If a bullet point is prefixed by a file name, this
is the lesson where the listed content should go into. This document is meant as a concept map
converted into a flow of learning goals and questions.

* Prelude
    * User profiles (academic and/or commercial) of cluster users
    * Narrative introduction

* [11-hpc-intro.md: Intro to Cluster Computing](_episodes/11-hpc-intro.md): Fundamentals of
  clusters and their resources resources (brief, concentrate on the concepts not details like
  interconnect type etc)
    * Be able to describe what a compute cluster (HPC/HTC system) is
    * Explain how a cluster differs from a laptop, desktop, cloud, or "server"
    * Identify how an compute cluster could benefit you.
    * Jargon busting

* [12-cluster.md: Accessing the Cluster](_episodes/12-cluster.md)
    * Understand the purpose of using a terminal program and SSH
    * Learn the basics of working on a remote system
    * Know the differences of between login and compute nodes
    * Objectives: Connect to a cluster using ssh; Transfer files to and from the cluster; Run the
      hostname command on a compute node of the cluster.
    * Potential tools: `ssh`, `ls`, `hostname`, `logout`, `nproc`, `free`, `scp`, `man`, `wget`

* [13-scheduler.md: Working with the Scheduler](_episodes/13-scheduler.md): Lesson will cover Slurm
  by default, other schedulers are planned. From
  [hpc-in-a-day](https://github.com/psteinb/hpc-in-a-day) we know that material comprising Slurm,
  PBS and LSF is possible, but hard already as e.g. PBS doesn't support direct dispatching as
  `srun`.
    * Know how to submit a program and batch scrip to the cluster (interactive & batch)
    * Use the batch system command line tools to monitor the execution of your job.
    * Inspect the output and error files of your jobs.
    * Potential tools: shell script, `sbatch`, `squeue -u`, `watch`, `-N`, `-n`, `-c`, `--mem`,
      `--time`, `scancel`, `srun`, `--x11 --pty`,
    * Extras: `--mail-user`, `--mail-type`, 
    * Remove? `watch` 
    * Later lessons? `-N` `-n` `-c`

* [14-modules.md: Accessing Software](_episodes/14-modules.md)
    * Understand the runtime environment at login
    * Learn how software modules can modify your environment
    * Learn how modules prevent problems and promote reproducibility
    * Objectives: how to load and use a software package.
    * Tools: `module avail`, `module load`, `which`, `echo $PATH`, `module list`, `module unload`,
      `module purge`, `.bashrc`, `.bash_profile`, `git clone`, `make`
    * Remove: `make`, `git clone`, 
    * Extras: `.bashrc`, `.bash_profile`

* [15-transferring-files.md: Transferring Files](_episodes/15-transferring-files.md)
    * Understand the (cognitive) limitations that remote systems don't necessarily have local
      Finder/Explorer windows
    * Be mindful of network and speed restrictions (e.g. cannot push from cluster; many files vs
      one archive)
    * Know what tools can be used for file transfers, and transfer modes (binary vs text)
    * Objective: Be able to transfer files to and from a computing cluster.
    * Tools: `wget`, `scp`, `rsync` (callout), `mkdir`, FileZilla, 
    * Remove: `dos2unix`, `unix2dos`,
    * Bonus: `gzip`, `tar`, `dos2unix`, `cat`, `unix2dos`, `sftp`, `pwd`, `lpwd`, `put`, `get`, 
    * Later:

* [16-resources.md: Using Resources Effectively](_episodes/16-resources.md)
    * Understand how to look up job statistics
    * Learn how to use job statistics to understand the health of your jobs
    * Learn some very basic techniques to monitor / profile code execution.
    * Understand job size and resource request implications.
    * Tools: `fastqc`, `sacct`, `ssh`, `top`, `free`, `ps`, `kill`, `killall` (note that some of
      these may not be appropriate on shared systems)


### Nascent lesson ideas

* Playing friendly in the cluster (psteinb: the following is very tricky as it is site dependent, I
  personally would like to see it in
  [_extras](https://github.com/hpc-carpentry/hpc-intro/tree/gh-pages/_extras))
	* Understanding resource utilisation
	* Profiling code - time, size, etc.
	* Getting system stats
	* Consequences of going over

* Filesystems and Storage: objectives likely include items from @psteinb's [Shared Filesystem lesson](
  https://github.com/psteinb/hpc-in-a-day/blob/gh-pages/_episodes/01-04-shared-filesystem.md):
    * Understand the difference between a local and shared / network filesystem
    * Learn about high performance / scratch filesystems
    * Raise attention that misuse (intentional or not) of a common file system negatively
      affects all users very quickly.
    * Possible tools: `echo $TEMP`, `ls -al /tmp`, `df`, `quota`

* Advanced Job Scripting and Submission:
	* Checking status of jobs (`squeue`, `bjobs` etc.), explain different job states and relate to
      scheduler basics
	* Cancelling/deleting a job (`scancel`, `bkill` etc.)
	* Passing options to the scheduler (log files)
	* Callout: Changing a job's name
	* Optional Callout: Send an email once the job completes (not all sites support sending emails)
	* for a starting point, see [this](
      https://psteinb.github.io/hpc-in-a-day/02-02-advanced-job-scheduling/) for reference

* Filesystem Zoo:
    * execute a job that collects node information and stores the output to `/tmp`
    * ask participants where the output went and why they can't see it
    * execute a job that collects node information and stores the output to `/shared` or however
      your shared file system is called
    * for a starting point, see [this](
      https://psteinb.github.io/hpc-in-a-day/02-03-shared-filesystem/)
