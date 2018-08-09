---
title: "Using resources effectively"
teaching: 10
exercises: 5
questions:
- "How can I be a responsible cluster user?"
objectives:
- "Be a good person and be nice to other users."
keypoints:
- "Don't run stuff on the login node."
- "Again, don't run stuff on the login node."
- "Don't be a bad person and run stuff on the login node."
---

You now have everything you need to run jobs, transfer files, use/install software,
and monitor how many resources your jobs are using.

So here are a couple final words to live by:

## Be kind to the login node

* The login node is very busy managing lots and lots of jobs! It doesn’t have any 
extra space to run computational work.  Don’t run jobs on the login node, though 
quick tests are generally fine. A “quick test” is generally anything that uses 
less than 10GB of memory, 4 CPUs, and 15 minutes of time. 
Remember, the login node is to be shared with other users.

> ## Login Node Etiquette
> 
> Which of these commands would probably be okay to run on the login node?
> python physics_sim.py
> make
> create_directories.sh
> molecular_dynamics_2
> tar -xzf R-3.3.0.tar.gz
> 
{: .challenge}

* If someone is being inappropriate and using the login node to run all of their stuff, 
  message an administrator to take a look at things and deal with them.

## Test before scaling

* Before submitting a large run of jobs, submit one as a test first to make sure everything works.

## Have a backup plan

* Use a Version Control system like git to keep track of your code. Though most systems have some form
  of backup/archival system, you shouldn't rely on it for something as key as your research code.
  The best backup system is one you manage yourself.

* Eventually, your data will need to leave the cluster.  You should have a plan of 
where you’ll store all your results *before* you run jobs.  

## Save time

* Compress files before transferring to save file transfer times with large datasets.  

* The less resources you ask for, the faster your jobs will find a slot in which to run.
  Lots of small jobs generally beat a couple big jobs.

## Software tips

* You can generally install software yourself, but if you want a shared installation of some kind,
  it might be a good idea to message an administrator.

* Always use the default compilers if possible. Newer compilers are great, but older stuff generally
  has less compatibility issues.

