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
{: .challenge }


# Doing Analysis or Running Code

## A standard Laptop for standard tasks

Today, people coding or analysing data typically work with laptops.
 
{% include figure.html url="" max-width="20%" file="/fig/200px-laptop-openclipartorg-aoguerrero.svg" alt="A standard laptop"
caption="" %}

Let's dissect what resources programs running on a laptop require:
- the keyboard and/or touchpad is used to tell the the computer what to do (**Input**)
- the internal computing resources **Central Processing Unit** and **Memory** perform calculation
- the display depicts progress and results (**Output**)

Schematically, this can be reduced to the following:

{% include figure.html url="" max-width="30%" file="/fig/Simple_Von_Neumann_Architecture.svg" alt="Schematic of how a computer works"
caption="" %}


## When tasks take too long

When the task to solve become more heavy on computations, the operations are typically out-sourced from the local laptop or desktop to elsewhere. Take for example the task to find the directions for your next business trip. The capabilities of your laptop are typically not enough to calculate that route spontaneously. So you use website, which in turn runs on a server that is almost exclusively no in the same room than you are.

{% include figure.html url="" max-width="20%" file="/fig/servers-openclipartorg-ericlemerdy.svg" alt="A rack half full with servers"
caption="" %}

Note here, that a server is mostly a noisy computer mounted into a rack cabinet which in turn resides in a data center. The internet made it possible that these data centers do not require to be nearby your laptop. 
What people call **the cloud** is mostly a web-service where you can rent such servers by providing your credit card details and by clicking together the specs of this remote resource.

The server itself has no direct display or input methods attached to it. But most importantly, it has much more storage, memory and compute capacity than your laptop will ever have. In any case, you need a local device (laptop, workstation, mobile phone or tablet) to interact with this remote machine, people typically call 'a server'. 

## When one server is not enough

If the computational task or analysis to complete is daunting for a single server, larger agglomerations of servers are used. These go by the name of clusters or super computers.

{% include figure.html url="" max-width="20%" file="/fig/serverrack-openclipartorg-psteinb-basedon-ericlemerdy.svg" alt="A rack full with servers"
caption="" %}

The methodology of providing the input data, communicating options and flags as well as retrieving the results is quite opposite to using a plain laptop. Moreover, using a GUI style interface is often discarded in favor of using the command line. This imposes a double paradigm shift for prospect users:

1. they work with the command line (not a GUI style user interface)
2. they work with a distributed set of computers (called nodes)

> # I've never used a server, did I?
> 
> Take a minute and think about which of your daily interactions with a computer may require a remote server or even cluster to provide you with results. 
{: .challenge }

{% include links.md %}
