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

<iframe src="https://www.icloud.com/keynote/067s-LrA5QLZiEbKde8qe5QHA?embed=true" width="100%" height="720" frameborder="0" allowfullscreen="1" referrer="no-referrer"></iframe>

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
