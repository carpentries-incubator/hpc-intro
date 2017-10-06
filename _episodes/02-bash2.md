---
title: "UNIX fundamentals: BASH Basics 2"
teaching: 0
exercises: 0
questions:
- "How do I move files on and off the remote system?"
- "How do I control who has access to my files?"
- "How do I write and run a simple script?"
objectives:
- "Be able to move files to and from the remote system."
- "Be able to read and change file permissions."
- "Be able to write and edit simple scripts
keypoints:
- "`scp` (The Secure Copy Program) is a standard way to securely transfer data to remote HPC systems."
- "File ownership is an important component of a shared computing space and can be controlled with `chgrp` and `chown`."
- "Scripts are *mostly* just lists of commands from the command line in the order they are to be performed."
---

## Moving Files Around

`mv` and `cp`

These will be an important setup for `scp` since the syntax is basically the same before adding the server components.


## Moving files to the remote system

It is often necessary to move data from a local computer to the remote compute and vice versa.  There are many ways to do this but since we are on the command line we will explore the principal command line tool for this, secure copy or `scp`.

`scp` behaves similarily to `ssh` but with one additional input, the name of the file to be copied.  If we were in the shell on our local computer, the file we wanted to move was in our current directory, named "globus.tgz", and Nelle wanted to move it to her home directory on cedar.computecanada.ca then the command would be

	$ scp globus.tgz nelle@cedar.computecanada.ca:
	
It should be expected that a password will be asked for and you should be prepared to provide it.

Once the transfer is complete you should be able to use `ssh` to login to the remote system and see your file in your home directory.

WHAT IF YOU WANTED THE FILE SOMEWHERE OTHER THAN THE HOME DIRECTORY?

> ## Remember the `:`
> Note the colon (`:`) at the end of the command.  This is a very important modifier to include.  If it isn't included then running `scp` will result in a copy of the file that was to be moved being created in the current directory with the name of the remote system.  In the case of the globus.tgz example above it would look like the following:
> 
> ~~~
> $ scp globus.tgz nelle@cedar.computecanada.ca: 
> $ ls
> ~~~
> {: .bash}
> 
> ~~~
> globus.tgz
> nelle@cedar.computecanada.ca
> ~~~
> {: .output}
> 
> If this does happen then the extra file can be removed with `rm`.
> 
> ~~~
> $ rm nelle@cedar.computecanada.ca
> ~~~
> {: .bash}
{: .callout}

NEED AN EXERCISE.  OPEN A SECOND TERMINAL WINDOW ON LOCAL SYSTEM AND USE `scp` TO PUSH A FILE TO THE REMOTE SYSTEM

## Moving Files to the Local System

Moving files from the remote system to the local system will also be necessary.  This is also done from the local system so instead of pushing content we'll be pulling it.  This is achieved by changing the order of the inputs passed to the `scp` command and specifying the exact location of the file that we want from the remote system.

scp simpson@cedar.computecanada.ca:junk junk

> ## Copying entire directories
> 
> HIGHLIGHT the `-r` flag here.
> 
{: .callout}


## Controlling File Ownership

List with `ls -l`

Change ownership with `chown`

## Groups

## Changing Group Association

chgrp

## Scripting

nano

## Making Scripts Executable / Changing Permissions

chmod

p. 195