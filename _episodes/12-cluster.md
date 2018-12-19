---
title: "Working on a cluster"
teaching: 15
exercises: 10
questions:
- "How do I log on to a cluster?"
- "How do I transfer data to a cluster?"
- "How is a cluster different to my laptop?"
- "How do I run processes on the cluster?"
objectives:
- "Connect to a cluster using ssh."
- "Transfer files to and from the cluster."
- "Run the `hostname` command on a compute node of the cluster." 
keypoints:
- "Clusters (almost always) provide a login node."
- "You connect to the login node by special software using an encrypted connection."
- "Data has to be transferred to and from the cluster using specialized software."
- "A cluster is a shared resource."
- "Running a process on the cluster requires using the scheduler."
---

## The Story

Through out this material, we will assist Lola Curious and look over her shoulder while she is starting to work at the Institute of Things as a side job to earn some extra money. 

On the first day, her supervisor greets her friendly and welcomes her to the job. She explains what her task is and suggests her that she will need to use the cluster on the campus. Lola has so far used her Laptop at home for her studies, so the idea of using a super computer appears a bit intimidating to her. Her supervisor notices her anxiety and tells her that she will receive an introduction to the super computer after she has requested an account on the cluster. 

Lola walks to the IT department and finishes the paper work to get an account. One of the admins promises to sit down with her in the morning to show her the way around the machine. The admin explains that Lola will use a small to mid-range HPC cluster.

## Going remote

First of all, the admin asks Lola to connect to the super computer. She mentions that in the past, compute clusters were named after planets or moons as they often presented distant somewhat mythological places. One of the admin's first instructors then often said, that they would use the Space Shuttle (or `ssh` briefly) to reach that planet or moon. So the admin asks Lola to open a terminal on her laptop and type in the following commands:

~~~ 
$ ssh lola@{{ site.workshop_login_host }}
~~~
{: .language-bash}

> ## Logging in
> 
> If you do this material on your own, be sure to replace `lola` with the username that is attributed to you on {{ site.workshop_login_host }}. When you hit enter, a prompt like this might appear:
>
> ~~~
> lola@{{ site.workshop_login_host }}'s password:
> ~~~
> {: .output}
> 
> Now is your chance to type in your password. But watch out, the characters you type are not displayed on the screen.
{: .callout}

~~~ 
Last login: Fri Dec 14 14:13:14 2018 from lolas_laptop
$ 
~~~
{: .output}

The admin explains to Lola that she is using a program known as the secure shell or `ssh`. This establishes a temporary encrypted connection between Lola's laptop and `{{ site.workshop_login_host }}`. The word before the `@` symbol, e.g. `lola` here, is the user account name that Lola has access permissions for on the cluster. 

> ## Where do I get this `ssh` from ?
> On Linux and/or macOS, the `ssh` command line utility is almost always pre-installed. Open a terminal and type `ssh --help` to check if that is the case. 
> 
> At the time of writing, the openssh support on Microsoft is still very [recent](https://blogs.msdn.microsoft.com/powershell/2017/12/15/using-the-openssh-beta-in-windows-10-fall-creators-update-and-windows-server-1709/). Alternatives to this are [putty](http://www.putty.org), [bitvise SSH](https://www.bitvise.com/ssh-client-download), [mRemoteNG](https://mremoteng.org/) or [MobaXterm](https://mobaxterm.mobatek.net/). Download it, install it and open the GUI. The GUI asks for your user name and the destination address or IP of the computer you want to connect to. Once provided, you will be queried for your password just like in the example above.
{: .callout}

Lola is asked to use a UNIX command called `ls` (for list directory contents) to have a look around. 

~~~ 
$ ls
~~~
{: .language-bash}

~~~ 
~~~
{: .output}

There is nothing displayed. To prove, that Lola is really logged in to another machine, Lola issues a command that prints the name of the machine she is currently working on:

~~~ 
$ hostname
~~~
{: .language-bash}

~~~ 
{{ site.workshop_login_host }}
~~~
{: .output}

The admin explains that Lola has to work with this remote shell session in order to run programs on the cluster. Launching programs that open a Graphical User Interface (GUI) is possible, but the interaction with the GUI will be slow as everything will have to get transferred through the WiFi network her laptop is currently logged into. Before Rob continues, he suggests to leave the cluster node again. For this, Lola can type in `logout` or `exit`.

~~~ 
$ logout
~~~
{: .language-bash}

## Looking around more

The admin continues to encourage Lola to look around. She explains that all of a cluster's nodes have similar components as Lola's laptop or workstation. 

- every cluster node offers a certain amount of CPU (Central Processing Unit) cores. To see how many, Lola can run

~~~
$ nproc --all
~~~
{: .language-bash}

- every cluster node has a certain amount of memory or [RAM](https://en.wikipedia.org/wiki/Random-access_memory) (Random-access memory). To see much memory `{{ site.workshop_login_host }}` in units of [Gigabyte](https://en.wikipedia.org/wiki/Gigabyte) has, Lola can run

~~~
$ free -g
~~~
{: .language-bash}

> ## Units and Language
> 
> A computer's memory and disk are measured in units called *Bytes* (one Byte are bits). As today's files and memory have grown to be large given historic standards, volumes are noted using the [SI](https://en.wikipedia.org/wiki/International_System_of_Units) prefixes. So 1000 Bytes is a Kilobyte (kB), 1000 Kilobytes is a Megabyte, 1000 Megabytes is a Gigabyte etc. 
> 
> History and common language have however mixed this notation with a different meaning. When people say "Kilobyte", they mean 1024 Bytes instead. In that spirit, a Megabyte are 1024 Kilobytes. To address this ambiguity, the [International System of Quantities](https://en.wikipedia.org/wiki/International_System_of_Quantities) standardizes the binary prefixes (with base of 1024) by the prefixes kibi, mibi, gibi, etc. For more details, see [here](https://en.wikipedia.org/wiki/Binary_prefix)
{: .callout}

> ## Relative to your Laptop
> 
> Note down the number of CPU cores, the amount of RAM and the total disk space available on `{{ site.workshop_login_host }}`. Compare it to your laptop!
> 
> Bonus: Divide the values obtained from `{{ site.workshop_login_host }}` by the numbers obtained for your laptop. How much more powerful is the login node of the cluster compared to your laptop?
{: .challenge}


## Transferring Data

The admin continues to explain, that typically people perform computationally heavy tasks on the cluster and prepare files that contain the results or a subset of data to create final results on the individuals laptop. So communication to and from the cluster is done mostly by transferring files. For example, Lola is asked to use a [file of her liking]({{page.root}}/filesystem/home/admin/this_weeks_canteen_menus/todays_canteen_menu.pdf) and transfer it over. For this, he advises her to use the secure copy command, `scp`. As before, this establishes a secure encrypted temporary connection between Lola's laptop and the cluster just for the sake of transferring the files. After the transfer has completed, scp will close the connection again.

~~~ 
$ scp todays_canteen_menu.pdf lola@{{ site.workshop_login_host }}:todays_canteen_menu.pdf
~~~
{: .language-bash}

~~~ 
todays_canteen_menu.pdf                                              100%   28KB  27.6KB/s   00:00
~~~
{: .output}

She can now `ssh` into the cluster again and check, if the file has arrived after she just uploaded it:

~~~ 
$ ssh lola@{{ site.workshop_login_host }}
Last login: Tue Mar 14 14:17:44 2017 from lolas_laptop
$ ls
~~~
{: .language-bash}

~~~ 
todays_canteen_menu.pdf
~~~
{: .output}

Now, let's try the other way around, i.e. downloading a file from the cluster to Lola's laptop. For this, Lola has to swap the two arguments of the `scp` command she just issued.

~~~ 
$ scp lola@{{ site.workshop_login_host }}:todays_canteen_menu.pdf todays_canteen_menu_downloaded.pdf
~~~
{: .language-bash}

Lola notices how the command line changed. First, she has to enter the source (`lola@{{ site.workshop_login_host }}`) then put a `:` and continue with the path of the file she wants to download. After that, separated by a space, the destination has to be provided, which in this case is a file `todays_canteen_menu_downloaded.pdf` in the current directory.

~~~
todays_canteen_menu.pdf                                                100%   28KB  27.6KB/s   00:00
~~~
{: .output}

Lola has a look in the current directory and indeed `todays_canteen_menu_downloaded.pdf`. She opens it with her pdf reader and can tell that it contains indeed the same content as the original one. The admin explains that if she would have used the same name as the destination, i.e. `todays_canteen_menu.pdf`, `scp` would have overwritten her local copy.

To finish, The admin asks Lola that she can also transfer entire directories. She prepared a temporary directory on the cluster for her under `/tmp/this_weeks_canteen_menus`. She asks Lola to obtain a copy of the entire directory onto her laptop.

~~~ 
$ scp -r lola@{{ site.workshop_login_host }}:/tmp/this_weeks_canteen_menus .
~~~
{: .language-bash}

~~~ 
canteen_menu_day_2.pdf                                                 100%   28KB  27.6KB/s   00:00    
canteen_menu_day_3.pdf                                                 100%   28KB  27.6KB/s   00:00    
canteen_menu_day_5.pdf                                                 100%   28KB  27.6KB/s   00:00    
canteen_menu_day_4.pdf                                                 100%   28KB  27.6KB/s   00:00    
canteen_menu_day_1.pdf                                                 100%   28KB  27.6KB/s   00:00
~~~
{: .output}

The trailing `.` is a short-hand to represent the current working directory that Lola currently calls `scp` from. When inspecting this directory, Lola sees the transferred directory:

~~~ 
$ ls
~~~
{: .language-bash}

~~~
this_weeks_canteen_menus/  todays_canteen_menu_downloaded.pdf  todays_canteen_menu.pdf
~~~
{: .output}

A closer look into that directory using the relative path with respect to the current one:

~~~ 
$ ls this_weeks_canteen_menus/
~~~
{: .language-bash}

reveals the transferred files.

~~~ 
canteen_menu_day_1.pdf  canteen_menu_day_2.pdf  canteen_menu_day_3.pdf  canteen_menu_day_4.pdf  canteen_menu_day_5.pdf
~~~
{: .output}

Rob suggests to Lola to consult the man page of `scp` for further details by calling:

~~~ 
$ man scp
~~~
{: .language-bash}

## Using the login node is not using the cluster

As a final word on this lesson, the admin tells Lola that she should never execute long running processes or applications on `{{ site.workshop_login_host }}`. This is a server that is used by many users of `{{ site.workshop_cluster_name }}`. If Lola starts a lot of long running processes, other users may start seeing their commands taking longer to complete. To actually to do science and complete the tasks Lola is meant to complete, a software called __the scheduler__ has to be used. 

> ## All mixed up
>
> Lola needs to obtain a file called `results.data` from a remote machine that is called `safe-store-1`. This machine is hidden behind the login node `{{ site.workshop_login_host }}`. However she mixed up the commands somehow that are needed to get the file onto her laptop. Help her and rearrange the following commands into the right order!
>
> ~~~
> $ ssh lola@`{{ site.workshop_login_host }}`
> $ logout
> $ scp lola@`{{ site.workshop_login_host }}`:results.data .
> $ scp lola@safe-store-1:results.data .
> ~~~
> {: .language-bash}
>
> > ## Solution
> > ~~~
> > $ ssh lola@`{{ site.workshop_login_host }}`
> > $ scp lola@safe-store-1:results.data .
> > $ logout
> > $ scp lola@`{{ site.workshop_login_host }}`:results.data .
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}


> ## Who is hanging around ?
>
> The `w` utility displays a list logged-in users and what they are currently doing. Use it to check:
>
> 1. that nobody but yourself is logged into your laptop/desktop
> 2. that a lot of people use the login node of your cluster `{{ site.workshop_login_host }}`
{: .challenge}

> ## Where did they go ?
>
> Rob has a zip file stored under `/tmp/passwords.zip` on the login node of the cluster `{{ site.workshop_login_host }}`. He wants to unzip it on his laptop under `/important/passwords`. How does he do that?
>
> 
> 1.
> ~~~
> $ ssh rob@{{ site.workshop_login_host }}
> $ unzip /tmp/passwords.zip
> ~~~
> {: .language-bash}
> 
> 2.
> ~~~
> $ scp {{ site.workshop_login_host }}@rob:/tmp/passwords.zip .
> $ unzip passwords.zip
> ~~~
> {: .language-bash}
> 
> 3.
> ~~~
> $ cd /important/passwords
> $ scp rob@{{ site.workshop_login_host }}:passwords.zip .
> $ unzip passwords.zip
> ~~~
> {: .language-bash}
> 
> 4.
> ~~~
> $ cd /important/passwords
> $ scp rob@{{ site.workshop_login_host }}:/tmp/passwords.zip .
> $ unzip passwords.zip
> ~~~
> {: .language-bash}
> 
> > ## Solution
> > 
> > 1. No: Rob only unpacks the zip file, but does not transfer the unpacked files onto his laptop
> > 2. No: Rob mixed up the syntax for `scp`
> > 3. No: Rob did not specify the correct path of `/tmp/passwords.zip` on the login node of the cluster `{{ site.workshop_login_host }}`
> > 4. Yes: you may also use `unzip foo.zip -d /somewhere` if you want to omit the first command
> {: .solution}
{: .challenge}



{% include links.md %}

