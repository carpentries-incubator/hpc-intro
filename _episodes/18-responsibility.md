---
title: "Using shared resources responsibly"
teaching: 10
exercises: 5
questions:
- "How can I be a responsible user?"
- "How can I protect my data?"
objectives:
- "Learn how to be a considerate shared system citizen."
- "Understand how to protect your critical data."
keypoints:
- "Be careful how you use the login node."
- "Your data on the system is your responsibility."
---

One of the major differences between using the {{ site.remote.name }} cluster and your own system (e.g. your laptop) is that {{ site.remote.name }} is shared. How many users
the resource is shared between at any one time varies from day to day but
it is unlikely you will ever be the only user logged into or using {{ site.remote.name }}.

## Be Kind to the Login Nodes (and your fellow researchers)

The {{ site.remote.name }} login node is a shared resource for researchers. 
Common activities on the login node include transferring data, creating/editing 
files and compiling software.   If the login node runs out of memory or
processing capacity, it will become very slow and unusable for everyone, it may even crash. While the login node is meant to be a common resource, be sure to use it responsibly and in ways that will not adversely impact your fellow users.

Login nodes are the right place to submit jobs but do not run jobs directly on the login node, this is not allowed.   Your workflows will likely include
loading environment modules, possibly in a certain order, and paths or
library versions that differ from your laptop, and doing an interactive test
of these types of tasks on the login node is a quick and reliable way to discover and fix these issues.

> ## Login Nodes Are a Shared Resource
>
> Remember, the login node is shared with all other users and your actions
> could cause issues for other people. Think carefully about the potential
> implications of issuing commands that may use large amounts of resource.
>
> Unsure? Please ask us at {{ site.email }}  if the thing
> you're contemplating is suitable for the login node, or if there's another
> mechanism to accomplish your task.
{: .callout}

> ## Login Node Etiquette
>
> Which of these commands would be a routine task to run on the login node?
>
> 1. `python physics_sim.py`
> 2. `make test`
> 3. `sbatch genome_seq.sl`
> 4. `molecular_dynamics_2`
> 5. `tar xzf nz-geodata.tar.gz`
>
> > ## Solution
> >
> > Building software, submitting jobs, and unpacking software are common
> > and acceptable tasks for the login node: options #2 (`make`), #3
> > (`sbatch`), and #5 (`tar`) are OK.  Running a Python script or a molecular 
> > dynamics software are not appropriate commands to run on the login node. 
> >
> > If unsure, please feel free to contact us at {{ site.email }}
> >
> {: .solution}
{: .challenge}

> ## How to Test Job Submission Scripts - Debug QOS!
>
> Before submitting a large job, first submit one as a test to make
> sure everything works as expected.  Often, users discover typos in their submit
> scripts, incorrect module names or possibly an incorrect pathname after their job
> has queued for many hours.  Be aware that your job is not fully scanned for
> correctness when you submit the job.  While you may get an immediate error if your
> SBATCH directives are malformed, it is not until the job starts to run that the
> interpreter starts to process the batch script.
>
> NeSI has an easy way for you to test your job submission.  One can employ the debug
> QOS to get a short, very high priority test job.  Debug jobs have to run within 15 
> minutes and cannot use more that 2 nodes.  To use debug QOS, add or change the
> following in your batch submit script  
> `#SBATCH --qos=debug`  
> `#SBATCH --time=15:00`  
> 
> Adding these SBATCH directives will provide your job with the highest priority
> possible, meaning it should start to run within a few minutes, provided
> your resource request is not too large.
{: .callout}

<!--Let's edit our Slurm submit script one last time: (TODO:need to get from latest)-->


## Have a Backup Plan

NeSI does perform backups of the `/home` and `/nesi/project` filesystems.  However, backups are only captured once per day.  So, if you edit or change code or data and then immediately delete it, it likely cannot be recovered.  Note, as the name suggests, NeSI does **not** backup the `/nesi/nobackup` filesystem.

Protecting critical data from corruption or deletion is primarily your 
responsibility. Ensure you have a data management plan and stick to the plan to reduce the chance of data loss.

Version control systems (such as Git) often have free, cloud-based offerings
(e.g., BitBucket, GitHub and GitLab) that are generally used for storing source code. Even
if you are not writing your own programs, these can be very useful for storing
job submit scripts, notes and other files.  Git is not an appropriate solution for storing data.


> ## Your Data Is Your Responsibility
> 
> For more information on NeSI backup and retention policy, please see the following
> webpage: [NeSI File Systems and Quotas](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas)
{: .callout}