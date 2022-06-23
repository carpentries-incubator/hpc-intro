---
title: "Why use a Cluster?"
teaching: 15
exercises: 5
questions:
- "Why would I be interested in High Performance Computing (HPC)?"
- "What can I expect to learn from this course?"
objectives:
- "Describe what an HPC system is"
- "Identify how an HPC system could benefit you."
keypoints:
- "High Performance Computing (HPC) typically involves connecting to very large
  computing systems elsewhere in the world."
- "These other systems can be used to do work that would either be impossible
  or much slower on smaller systems."
- "HPC resources are shared by multiple users."
- "The standard method of interacting with such systems is via a command line
  interface."
---

Frequently, research problems that use computing can outgrow the capabilities
of the desktop or laptop computer where they started:

* A statistics student wants to cross-validate a model. This involves running
  the model 1000 times -- but each run takes an hour. Running the model on
  a laptop will take over a month! In this research problem, final results are
  calculated after all 1000 models have run, but typically only one model is
  run at a time (in __serial__) on the laptop. Since each of the 1000 runs is
  independent of all others, and given enough computers, it's theoretically
  possible to run them all at once (in __parallel__).
* A genomics researcher has been using small datasets of sequence data, but
  soon will be receiving a new type of sequencing data that is 10 times as
  large. It's already challenging to open the datasets on a computer --
  analyzing these larger datasets will probably crash it. In this research
  problem, the calculations required might be impossible to parallelize, but a
  computer with __more memory__ would be required to analyze the much larger
  future data set.
* An engineer is using a fluid dynamics package that has an option to run in
  parallel. So far, this option was not used on a desktop. In going from 2D
  to 3D simulations, the simulation time has more than tripled. It might be
  useful to take advantage of that option or feature. In this research problem,
  the calculations in each region of the simulation are largely independent of
  calculations in other regions of the simulation. It's possible to run each
  region's calculations simultaneously (in __parallel__), communicate selected
  results to adjacent regions as needed, and repeat the calculations to
  converge on a final set of results. In moving from a 2D to a 3D model, __both
  the amount of data and the amount of calculations increases greatly__, and
  it's theoretically possible to distribute the calculations across multiple
  computers communicating over a shared network.

In all these cases, access to more (and larger) computers is needed. Those
computers should be usable at the same time, __solving many researchers'
problems in parallel__.

## Jargon Busting Presentation

Open the [HPC Jargon Buster]({{ site.url }}{{ site.baseurl }}/files/jargon.html#p1)
in a new tab. To present the content, press `C` to open a **c**lone in a
separate window, then press `P` to toggle **p**resentation mode.

> ## I've Never Used a Server, Have I?
>
> Take a minute and think about which of your daily interactions with a
> computer may require a remote server or even cluster to provide you with
> results.
>
> > ## Some Ideas
> >
> > * Checking email: your computer (possibly in your pocket) contacts a remote
> >   machine, authenticates, and downloads a list of new messages; it also
> >   uploads changes to message status, such as whether you read, marked as
> >   junk, or deleted the message. Since yours is not the only account, the
> >   mail server is probably one of many in a data center.
> > * Searching for a phrase online involves comparing your search term against
> >   a massive database of all known sites, looking for matches. This "query"
> >   operation can be straightforward, but building that database is a
> >   [monumental task][mapreduce]! Servers are involved at every step.
> > * Searching for directions on a mapping website involves connecting your
> >   (A) starting and (B) end points by [traversing a graph][dijkstra] in
> >   search of the "shortest" path by distance, time, expense, or another
> >   metric. Converting a map into the right form is relatively simple, but
> >   calculating all the possible routes between A and B is expensive.
> >
> > Checking email could be serial: your machine connects to one server and
> > exchanges data. Searching by querying the database for your search term (or
> > endpoints) could also be serial, in that one machine receives your query
> > and returns the result. However, assembling and storing the full database
> > is far beyond the capability of any one machine. Therefore, these functions
> > are served in parallel by a large, ["hyperscale"][hyperscale] collection of
> > servers working together.
> {: .solution}
{: .challenge }

{% include links.md %}

[dijkstra]: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
[hyperscale]: https://en.wikipedia.org/wiki/Hyperscale_computing
[mapreduce]: https://en.wikipedia.org/wiki/MapReduce
