---
title: "Why use a Cluster?"
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
- "These other systems can be used to do work that would either be impossible or much slower on
  smaller systems."
- "The standard method of interacting with such systems is via a command line interface called
  Bash."
---

Frequently, research problems that use computing can outgrow the capabilities of the desktop or laptop computer where
they started:

* A statistics student wants to cross-validate a model. This involves running the model 1000
  times -- but each run takes an hour. Running the model on a laptop will take over a month!

* A genomics researcher has been using small datasets of sequence data, but soon will be receiving
  a new type of sequencing data that is 10 times as large. It's already challenging to open the
  datasets on a computer -- analyzing these larger datasets will probably crash it.

* An engineer is using a fluid dynamics package that has an option to run in parallel. So far, this option was not utilized on a desktop. In going from 2D to 3D simulations, the simulation time has more than tripled. It might be useful to take advantage of that option or feature.

In all these cases, access to more computers is needed. Those computers should be usable at the same time.

> ## And what do you do?
> 
> Talk to your neighbour, office mate or [rubber duck](https://rubberduckdebugging.com/) about your
> research.
>
> - How does computing help you do your research? 
> - How could more computing help you do more or better research?
{: .discussion }


## A standard Laptop for standard tasks

Today, people coding or analysing data typically work with laptops.

{% include figure.html url="" max-width="20%" file="/fig/200px-laptop-openclipartorg-aoguerrero.svg"
 alt="A standard laptop" caption="" %}

Let's dissect what resources programs running on a laptop require:
- the keyboard and/or touchpad is used to tell the computer what to do (**Input**)
- the internal computing resources **Central Processing Unit** and **Memory** perform calculation
- the display depicts progress and results (**Output**)

Schematically, this can be reduced to the following:

{% include figure.html url="" max-width="30%" file="/fig/Simple_Von_Neumann_Architecture.svg" 
alt="Schematic of how a computer works" caption="" %}


## When tasks take too long

When the task to solve becomes heavy on computations, the operations are typically out-sourced from
the local laptop or desktop to elsewhere. Take for example the task to find the directions for your
next vacation. The capabilities of your laptop are typically not enough to calculate that route
spontaneously: [finding the shortest path](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
through a network runs on the order of (*v* log *v*) time, where *v* (vertices) represents the
number of intersections in your map. Instead of doing this yourself, you use a website, which in
turn runs on a server, that is almost definitely not in the same room as you are.

{% include figure.html url="" max-width="20%" file="/fig/servers-openclipartorg-ericlemerdy.svg" 
alt="A rack half full with servers" caption="" %}

Note here, that a server is mostly a noisy computer mounted into a rack cabinet which in turn
resides in a data center. The internet made it possible that these data centers do not require to be
nearby your laptop. What people call **the cloud** is mostly a web-service where you can rent such
servers by providing your credit card details and requesting remote resources that satisfy your
requirements. This is often handled through an online, browser-based interface listing the various
machines available and their capacities in terms of processing power, memory, and storage.

The server itself has no direct display or input methods attached to it. But most importantly, it 
has much more storage, memory and compute capacity than your laptop will ever have. In any case,
you need a local device (laptop, workstation, mobile phone or tablet) to interact with this remote 
machine, which people typically call 'a server'. 

## When one server is not enough

If the computational task or analysis to complete is daunting for a single server, larger 
agglomerations of servers are used. These go by the name of "clusters" or "super computers".

{% include figure.html url="" max-width="20%" 
file="/fig/serverrack-openclipartorg-psteinb-basedon-ericlemerdy.svg" alt="A rack with servers"
caption="" %}

The methodology of providing the input data, configuring the program options, and retrieving the
results is quite different to using a plain laptop. Moreover, using a graphical interface is often
discarded in favor of using the command line. This imposes a double paradigm shift for prospective
users asked to

1. work with the command line interface (CLI), rather than a graphical user interface (GUI)
2. work with a distributed set of computers (called nodes) rather than the machine attached to their
   keyboard & mouse

> ## I've never used a server, have I?
> 
> Take a minute and think about which of your daily interactions with a computer may require a 
> remote server or even cluster to provide you with results. 
>
> > ## Some Ideas
> > 
> > - Checking email: your computer (possibly in your pocket) contacts a remote machine,
> >   authenticates, and downloads a list of new messages; it also uploads changes to message
> >   status, such as whether you read, marked as junk, or deleted the message. Since yours is
> >   not the only account, the mail server is probably one of many in a data center.
> > - Searching for a phrase online involves comparing your search term against a massive database
> >   of all known sites, looking for matches. This "query" operation can be straightforward, but
> >   building that database is a [monumental task](https://en.wikipedia.org/wiki/MapReduce)!
> >   Servers are involved at every step. 
> > - Searching for directions on a mapping website involves connecting your (A) starting and 
> >   (B) end points by [traversing a graph](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
> >   in search of the "shortest" path by distance, time, expense, or another metric. Converting
> >   a map into the right form is relatively simple, but calculating all the possible routes 
> >   between A and B is expensive. 
> >
> > Checking email could be serial: your machine connects to one server and exchanges data. Searching
> > by querying the database for your search term (or endpoints) could also be serial, in that one machine
> > receives your query and returns the result. However, assembling and storing the full database
> > is far beyond the capability of any one machine. Therefore, these functions are served in
> > parallel by a large, ["hyperscale"](https://en.wikipedia.org/wiki/Hyperscale_computing)
> > collection of servers working together.
> {: .solution}
{: .challenge }

{% include links.md %}
