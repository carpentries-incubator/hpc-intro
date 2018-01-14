---
title: "Connecting to the cluster"
teaching: 15 
exercises: 5
questions:
- "How do I open a terminal?"
- "How do I connect to a remote computer?"
objectives:
- "Connect to a cluster."
keypoints:
- "To connect to a cluster using SSH: `ssh yourUsername@remote.computer.address`"
---

## Opening a Terminal

Connecting to an HPC system is most often done through a tool known as "SSH"
(Secure SHell) and usually SSH is run through a terminal. So, to begin using
an HPC system we need to begin by opening a terminal. Different operating
systems have different terminals, none of which are exactly the same in terms
of their features and abilities while working on the operating system. When
connected to the remote system the experience between terminals will be
identical as each will faithfully present the same experience of using that
system.

Here is the process for opening a terminal in each operating system.

### Linux
There are many different versions (aka "flavours") of Linux and how to open a
terminal window can change between flavours. Fortunately most Linux users
already know how to open a terminal window since it is a common part of the
workflow for Linux users. If this is something that you do not know how to do
then a quick search on the Internet for "how to open a terminal window in"
with your particular Linux flavour appended to the end should quickly give
you the directions you need.

A very popular version of Linux is Ubuntu. There are many ways to open a
terminal window in Ubuntu but a very fast way is to use the terminal shortcut
key sequence: Ctrl+Alt+T.

### Mac

Macs have had a terminal built in since the first version of OSX since it is
built on a Linux flavour known as BSD (Berkeley Systems Designs). The
terminal can be quickly opened through the use of the Searchlight tool. Hold
down the command key and press the spacebar. In the search bar that shows up
type "terminal", choose the terminal app from the list of results (it will
look like a tiny, black computer screen) and you will be presented with a
terminal window.

### Windows

While Windows does have a command-line interface known as the "Command
Prompt" that has its roots in MS-DOS (Microsoft Disk Operating System) it
does not have an SSH tool built into it and so one needs to be installed.
There are a variety of programs that can be used for this, two common ones we
describe here, as follows:

#### MobaXterm

MobaXterm is a terminal window emulator for Windows and the home edition can
be downloaded for free from
[mobatek.net](https://mobaxterm.mobatek.net/download-home-edition.html). If
you follow the link you will note that there are two editions of the home
version available: Portable and Installer. The portable edition puts all
MobaXterm content in a folder on the desktop (or anywhere else you would like
it) so that it is easy add plug-ins or remove the software. The installer
edition adds MobaXterm to your Windows installation as any other program you
might install. If you are not sure that you will continue to use MobaXterm in
the future you are likely best to choose the portable edition.

Download the version that you would like to use and install it as you would
any other software on your Windows installation. Once the software is
installed you can run it by either opening the folder installed with the
portable edition and double-clicking on the file named
*MobaXterm_Personal_10.2* or, if the installer edition was used, finding the
executable through either the start menu or the Windows search option.

Once the MobaXterm window is open you should see a large button in the middle
of that window with the text "Start Local Terminal". Click this button and
you will have a terminal window at your disposal.

## Logging onto the system

With all of this in mind, let's connect to a cluster. 
For these examples, we will connect to Graham - a high-performance cluster located at the University of Waterloo.
Although it's unlikely that every system will be exactly like Graham, 
it's a very good example of what you can expect from a supercomputing installation.
To connect to our example computer, we will use SSH. 

SSH allows us to connect to UNIX computers remotely, and use them as if they were our own.
The general syntax of the connection command follows the format `ssh yourUsername@some.computer.address`
Let's attempt to connect to the cluster now:

```
ssh yourUsername@graham.computecanada.ca
```
{: .bash}

```{.output}
The authenticity of host 'graham.computecanada.ca (199.241.166.2)' can't be established.
ECDSA key fingerprint is SHA256:JRj286Pkqh6aeO5zx1QUkS8un5fpcapmezusceSGhok.
ECDSA key fingerprint is MD5:99:59:db:b1:3f:18:d0:2c:49:4e:c2:74:86:ac:f7:c6.
Are you sure you want to continue connecting (yes/no)?  # type "yes"!
Warning: Permanently added the ECDSA host key for IP address '199.241.166.2' to the list of known hosts.
yourUsername@graham.computecanada.ca's password:  # no text appears as you enter your password
Last login: Wed Jun 28 16:16:20 2017 from s2.n59.queensu.ca

Welcome to the ComputeCanada/SHARCNET cluster Graham.
```

If you've connected successfully, you should see a prompt like the one below. 
This prompt is informative, and lets you grasp certain information at a glance:
in this case `[yourUsername@computerName workingDirectory]$`.
(If you don't understand what these things are, don't worry! 
We will cover things in depth as we explore the system further.)

```{.output}
[yourUsername@gra-login1 ~]$
```
