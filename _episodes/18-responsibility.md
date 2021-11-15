---
title: "Using shared resources responsibly"
teaching: 15
exercises: 5
questions:
- "How can I be a responsible user?"
- "How can I protect my data?"
- "How can I best get large amounts of data off an HPC system?"
objectives:
- "Learn how to be a considerate shared system citizen."
- "Understand how to protect your critical data."
- "Appreciate the challenges with transferring large amounts of data off HPC
  systems."
- "Understand how to convert many files to a single archive file using tar."
keypoints:
- "Be careful how you use the login node."
- "Your data on the system is your responsibility."
- "Plan and test large data transfers."
- "It is often best to convert many files to a single archive file before
  transferring."
- "Again, don't run stuff on the login node."
---

One of the major differences between using remote HPC resources and your own
system (e.g. your laptop) is that remote resources are shared. How many users
the resource is shared between at any one time varies from system to system but
it is unlikely you will ever be the only user logged into or using such a
system.

The widespread usage of scheduling systems where users submit jobs on HPC
resources is a natural outcome of the shared nature of these resources. There
are other things you, as an upstanding member of the community, need to
consider.

## Be Kind to the Login Nodes

The login node is often busy managing all of the logged in users, creating and
editing files and compiling software. If the machine runs out of memory or
processing capacity, it will become very slow and unusable for everyone. While
the machine is meant to be used, be sure to do so responsibly &mdash; in ways
that will not adversely impact other users' experience.

Login nodes are always the right place to launch jobs. Cluster policies vary,
but they may also be used for proving out workflows, and in some cases, may
host advanced cluster-specific debugging or development tools. The cluster may
have modules that need to be loaded, possibly in a certain order, and paths or
library versions that differ from your laptop, and doing an interactive test
run on the head node is a quick and reliable way to discover and fix these
issues.

> ## Login Nodes Are a Shared Resource
>
> Remember, the login node is shared with all other users and your actions
> could cause issues for other people. Think carefully about the potential
> implications of issuing commands that may use large amounts of resource.
>
> Unsure? Ask your friendly systems administrator ("sysadmin") if the thing
> you're contemplating is suitable for the login node, or if there's another
> mechanism to get it done safely.
{: .callout}

You can always use the commands `top` and `ps ux` to list the processes that
are running on the login node along with the amount of CPU and memory they are
using. If this check reveals that the login node is somewhat idle, you can
safely use it for your non-routine processing task. If something goes wrong
&mdash; the process takes too long, or doesn't respond &mdash; you can use the
`kill` command along with the *PID* to terminate the process.

> ## Login Node Etiquette
>
> Which of these commands would be a routine task to run on the login node?
>
> 1. `python physics_sim.py`
> 2. `make`
> 3. `create_directories.sh`
> 4. `molecular_dynamics_2`
> 5. `tar -xzf R-3.3.0.tar.gz`
>
> > ## Solution
> >
> > Building software, creating directories, and unpacking software are common
> > and acceptable > tasks for the login node: options #2 (`make`), #3
> > (`mkdir`), and #5 (`tar`) are probably OK. Note that script names do not
> > always reflect their contents: before launching #3, please
> > `less create_directories.sh` and make sure it's not a Trojan horse.
> >
> > Running resource-intensive applications is frowned upon. Unless you are
> > sure it will not affect other users, do not run jobs like #1 (`python`)
> > or #4 (custom MD code). If you're unsure, ask your friendly sysadmin for
> > advice.
> {: .solution}
{: .challenge}

If you experience performance issues with a login node you should report it to
the system staff (usually via the helpdesk) for them to investigate.

> ## Test Job Submission Scripts That Use Large Amounts of Resources
>
> Before submitting a large run of jobs, submit one as a test first to make
> sure everything works as expected.
>
> Before submitting a very large or very long job submit a short truncated test
> to ensure that the job starts as expected.
{: .callout}

## Have a Backup Plan

Although many HPC systems keep backups, it does not always cover all the file
systems available and may only be for disaster recovery purposes (i.e. for
restoring the whole file system if lost rather than an individual file or
directory you have deleted by mistake). Protecting critical data from
corruption or deletion is primarily your responsibility: keep your own backup
copies.

Version control systems (such as Git) often have free, cloud-based offerings
(e.g., GitHub and GitLab) that are generally used for storing source code. Even
if you are not writing your own programs, these can be very useful for storing
job scripts, analysis scripts and small input files.

For larger amounts of data, you should make sure you have a robust system in
place for taking copies of critical data off the HPC system wherever possible
to backed-up storage. Tools such as `rsync` can be very useful for this.

Your access to the shared HPC system will generally be time-limited so you
should ensure you have a plan for transferring your data off the system before
your access finishes. The time required to transfer large amounts of data
should not be underestimated and you should ensure you have planned for this
early enough (ideally, before you even start using the system for your
research).

In all these cases, the helpdesk of the system you are using should be able to
provide useful guidance on your options for data transfer for the volumes of
data you will be using.

> ## Your Data Is Your Responsibility
>
> Make sure you understand what the backup policy is on the file systems on the
> system you are using and what implications this has for your work if you lose
> your data on the system. Plan your backups of critical data and how you will
> transfer data off the system throughout the project.
{: .callout}