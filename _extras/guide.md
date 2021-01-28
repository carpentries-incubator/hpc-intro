---
layout: page
title: "Instructor Notes"
permalink: /guide/
---

## "No such file or directory" or symbol `0096` errors

`scp` and `rsync` may throw a perplexing error about files that very much do exist. One source of
these errors is copy-and-paste of command line arguments from Web browsers, where the double-dash
string `--` is rendered as an em-dash character `—` (or en-dash `–`, or horizontal bar `―`). For
example, instead of showing the transfer rate in real time, the following command fails mysteriously.

```
{{ site.local.prompt }} rsync —progress my_precious_data.txt {{ site.remote.user }}@{{ site.remote.login }}
rsync: link_stat "/home/{{ site.local.user }}/—progress" failed: No such file or directory (2)
rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1207) [sender=3.1.3]
```
{: .bash}

The correct command, different only by two characters, succeeds:

```
{{ site.local.prompt }} rsync --progress my_precious_data.txt {{ site.remote.user }}@{{ site.remote.login }}
```
{: .bash}

We have done our best to wrap all commands in code blocks, which prevents this subtle conversion. If
you encounter this error, please open an issue or pull request on the lesson repository to help
others avoid it.


## Cluster roleplay instructions (from 13-scheduler)

To do this exercise, you will need about 50-100 pieces of paper or sticky notes.

1. Divide the room into groups, with specific roles. 
 * Pick three-four people to be the "scheduler"
 * Have the remaining one-third of the room be "users", given several slips of paper (or post-it
   notes) and pens
 * Have the remaining two thirds of the room be "compute nodes" Make sure everyone knows what their
   roles are. Have the "users" go to the front of the room (or the back, wherever there's space for
   them to stand) and the "schedulers" stand between the users and "compute nodes" (who should
   remain at their seats).

2. Divide the pieces of paper / sticky notes among the "users" and have them fill out all the pages
   with simple math problems and their name. Tell everyone that these are the jobs that need to be
   done and correspond to their computing research problems.

3. Point out that we now have jobs and we have "compute nodes" (the people still sitting down) that
   can solve these problems. How are the jobs going to get to the nodes? The answer is the
   scheduling program that will take the jobs from the users and deliver them to open compute nodes.

4. Have all the "compute nodes" raise their hands. Have the users "submit" their jobs by handing
   them to the schedulers. Schedulers should then deliver them to "open" (hands-raised) compute
   nodes and collect finished problems and return them to the appropriate user.

5. Wait until most of the problems are done and then re-seat everyone.

6. Follow-up discussion: what would happen if a node couldn't solve the math problem? It might be
   important to indicate the *resources* that your job needs to run. Add other parallels that will
   be coming up in the next section of the lesson.
