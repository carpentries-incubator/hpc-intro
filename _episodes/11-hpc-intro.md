---
title: "Why Use a Cluster?"
teaching: 15
exercises: 5
questions:
- "Why would I be interested in High Performance Computing (HPC)?"
- "What can I expect to learn from this course?"
objectives:
- "Be able to describe what an HPC system is"
- "Identify how an HPC system could benefit you."  
keypoints:
- "High Performance Computing (HPC) typically involves connecting to very large computing systems
  elsewhere in the world."
- "These other systems can be used to do work that would either be impossible or much slower or
  smaller systems."
- "The standard method of interacting with such systems is via a command line interface called
  Bash."
---

## Why Use These Computers?

Frequently, research problems that use computing can outgrow the desktop or laptop computer where
they started:

* A statistics student wants to cross-validate their model. This involves running the model 1000
  times -- but each run takes an hour. Running on their laptop will take over a month!

* A genomics researcher has been using small datasets of sequence data, but soon will be receiving a
  new type of sequencing data that is 10 times as large. It's already challenging to open the
  datasets on their computer -- analyzing these larger datasets will probably crash it.

* An engineer is using a fluid dynamics package that has an option to run in parallel. So far, they
  haven't used this option on their desktop, but in going from 2D to 3D simulations, simulation time
  has more than tripled and it might be useful to take advantage of that feature.

In all these cases, what is needed is access to more computers than can be used at the same time.

> # And what do you do?
> 
> Talk to your neighbour, office mate or [rubber duck](https://rubberduckdebugging.com/) about your research. How does computing help you do your research? 
> How could more computing help you do more or better research?
{: .callout }


## All these Computers

Today, people coding or analysing data typically work with laptops.

![A laptop](fig/laptop-openclipartorg-aoguerrero.svg)

For programs to run on a laptop, the keyboard that is directly attached to it is used. The laptop also has a disk to store data and display results by means of the monitor. To achieve a long runtime on battery, laptops are typically made up of energy efficient components. 

![A server in a server rack](fig/servers-openclipartorg-ericlemerdy.svg)

If computations are getting too long or data too big, a laptop or workstation is not enough. Then a server is used to offer more resources, be it the ability to perform more computations or to store more data or both. Servers typically have neither a keyboard, monitor or mouse attached to them. They can only be reached by a network (the internet or a local network in a building or on campus).


## The Story


Through out this material, we will assist Lola Curious and look over her shoulder while she is starting to work at the Institute of Things as a side job to earn some extra money. 

On the first day, her supervisor greets her friendly and welcomes her to the job. She explains what her task is and suggests her that she will need to use the cluster on the campus. Lola has so far used her Laptop at home for her studies, so the idea of using a super computer appears a bit intimidating to her. Her supervisor notices her anxiety and tells her that she will receive an introduction to the super computer after she has requested an account on the cluster. 

Lola walks to the IT department and finishes the paper work to get an account. One of the admins promises to sit down with her in the morning to show her the way around the machine. The admin explains that Lola will use a small to mid-range HPC cluster.
