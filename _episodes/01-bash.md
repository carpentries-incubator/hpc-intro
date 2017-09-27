---
title: "UNIX fundamentals: Connecting & BASH Basics 1"
teaching: 0
exercises: 0
questions:
- "How do I connect to an HPC system?"
- "How do I view files and move around on the system?"
- "Where can I store my files/data?"
objectives:
- "Be able to connect to a remote HPC system"
- "Be able to navigate the remote filesystem."
keypoints:
- "`ssh` is a common and powerful method for connecting to remote HPC systems."
- "`ls` is used to view the content of directories and `cd` is used to move around the directory structure."
- "scratch storage is temporary and should not be relied on for crucial data beyond a short period of time."
---

## Opening a Terminal

Connecting to an HPC system is most often done through a tool known as "SSH" (Secure SHell) and usually SSH is run through a terminal.  So, to begin using an HPC system we need to begin by opening a terminal.  Different operating systems have different terminals, none of which are exactly the same in terms of their features and abilities while working on the operating system.  When connected to the remote system the experience between terminals will be identical as each will faithfully present the same experience of using that system.

Here is the process for opening a terminal in each operating system.

### Linux  
There are many different versions (aka "flavours") of Linux and how to open a terminal window can change between flavours.  Fortunately most Linux users already know how to open a terminal window since it is a common part of the workflow for Linux users.  If this is something that you do not know how to do then a quick search on the Internet for "how to open a terminal window in" with your particular Linux flavour appended to the end should quickly give you the directions you need.

A very popular version of Linux is Ubuntu.  There are many ways to open a terminal window in Ubuntu but a very fast way is to use the terminal shortcut key sequence: Ctrl+Alt+T.

### Mac
Macs have had a terminal built in since the first version of OSX since it is built on a Linux flavour known as BSD (Berkeley Systems Designs).  The terminal can be quickly opened through the use of the Searchlight tool.  Hold down the command key and press the spacebar.  In the search bar that shows up type "terminal", choose the terminal app from the list of results (it will look like a tiny, black computer screen) and you will be presented with a terminal window.

### Windows
While Windows does have a command-line interface known as the "Command Prompt" that has its roots in MS-DOS (Microsoft Disk Operating System) it does not have an SSH tool built into it and so one needs to be installed.  There are a variety of programs that can be used for this, two common ones we describe here, as follows:

#### MobaXterm
MobaXterm is a terminal window emulator for Windows and the home edition can be downloaded for free from [mobatek.net](https://mobaxterm.mobatek.net/download-home-edition.html).  If you follow the link you will note that there are two editions of the home version available: Portable and Installer.  The portable edition puts all MobaXterm content in a folder on the desktop (or anywhere else you would like it) so that it is easy add plug-ins or remove the software.  The installer edition adds MobaXterm to your Windows installation as any other program you might install.  If you are not sure that you will continue to use MobaXterm in the future you are likely best to choose the portable edition.

Download the version that you would like to use and install it as you would any other software on your Windows installation.  Once the software is installed you can run it by either opening the folder installed with the portable edition and double-clicking on the file named *MobaXterm_Personal_10.2* or, if the installer edition was used, finding the executable through either the start menu or the Windows search option.

Once the MobaXterm window is open you should see a large button in the middle of that window with the text "Start Local Terminal".  Click this button and you will have a terminal window at your disposal.

## Terminal Basics

The part of the operating system responsible for managing files and directories
is called the **file system**.
It organizes our data into files,
which hold information,
and directories (also called "folders"),
which hold files or other directories.

Several commands are frequently used to create, inspect, rename, and delete files and directories.
To start exploring them,
let's open a shell window:

> ## Preparation Magic
>
> If you type the command:
> `PS1='$ '`
> into your shell, followed by pressing the 'enter' key,
> your window should look like our example in this lesson.  
> This isn't necessary to follow along (in fact, your prompt may have
> other helpful information you want to know about).  This is up to you!  
{: .callout}

~~~
$
~~~
{: .bash}

The dollar sign is a **prompt**, which shows us that the shell is waiting for input;
your shell may use a different character as a prompt and may add information before
the prompt. When typing commands, either from these lessons or from other sources,
do not type the prompt, only the commands that follow it.

Type the command `whoami`,
then press the Enter key (sometimes marked Return) to send the command to the shell.
The command's output is the ID of the current user,
i.e.,
it shows us who the shell thinks we are:

~~~
$ whoami
~~~
{: .bash}

~~~
nelle
~~~
{: .output}

More specifically, when we type `whoami` the shell:

1.  finds a program called `whoami`,
2.  runs that program,
3.  displays that program's output, then
4.  displays a new prompt to tell us that it's ready for more commands.


> ## Username Variation
>
> In this lesson, we have used the username `nelle` (associated
> with our hypothetical scientist Nelle) in example input and output throughout.  
> However, when
> you type this lesson's commands on your computer,
> you should see and use something different,
> namely, the username associated with the user account on your computer.  This
> username will be the output from `whoami`.  In
> what follows, `nelle` should always be replaced by that username.  
{: .callout}

> ## Unknown commands
> Remember, the Shell is a program that runs other programs rather than doing
> calculations itself. So the commands you type must be the names of existing
> programs.
> If you type the name of a program that does not exist and hit enter, you
> will see an error message similar to this:
> 
> ~~~
> $ mycommand
> ~~~
> {: .bash}
> 
> ~~~
> -bash: mycommand: command not found
> ~~~
> {: .error}
> 
> The Shell (Bash) tells you that it cannot find the program `mycommand`
> because the program you are trying to run does not exist on your computer.
> We will touch on quite a few commands in the course of this tutorial, but there
> are actually many more than we can cover here.
{: .callout}

Next,
let's find out where we are by running a command called `pwd`
(which stands for "print working directory").
At any moment,
our **current working directory**
is our current default directory,
i.e.,
the directory that the computer assumes we want to run commands in
unless we explicitly specify something else.
Here,
the computer's response is `/Users/nelle`,
which is Nelle's **home directory**:

~~~
$ pwd
~~~
{: .bash}

~~~
/Users/nelle
~~~
{: .output}

> ## Home Directory Variation
>
> The home directory path will look different on different operating systems.
> On Linux it may look like `/home/nelle`,
> and on Windows it will be similar to `C:\Documents and Settings\nelle` or
> `C:\Users\nelle`.  
> (Note that it may look slightly different for different versions of Windows.)
> In future examples, we've used Mac output as the default - Linux and Windows
> output may differ slightly, but should be generally similar.  
{: .callout}

To understand what a "home directory" is,
let's have a look at how the file system as a whole is organized.  For the
sake of this example, we'll be
illustrating the filesystem on our scientist Nelle's computer.  After this
illustration, you'll be learning commands to explore your own filesystem,
which will be constructed in a similar way, but not be exactly identical.  

On Nelle's computer, the filesystem looks like this:

![The File System](../fig/filesystem.svg)

At the top is the **root directory**
that holds everything else.
We refer to it using a slash character `/` on its own;
this is the leading slash in `/Users/nelle`.

Inside that directory are several other directories:
`bin` (which is where some built-in programs are stored),
`data` (for miscellaneous data files),
`Users` (where users' personal directories are located),
`tmp` (for temporary files that don't need to be stored long-term),
and so on.  

We know that our current working directory `/Users/nelle` is stored inside `/Users`
because `/Users` is the first part of its name.
Similarly,
we know that `/Users` is stored inside the root directory `/`
because its name begins with `/`.

> ## Slashes
>
> Notice that there are two meanings for the `/` character.
> When it appears at the front of a file or directory name,
> it refers to the root directory. When it appears *inside* a name,
> it's just a separator.
{: .callout}

Underneath `/Users`,
we find one directory for each user with an account on Nelle's machine,
her colleagues the Mummy and Wolfman.  

![Home Directories](../fig/home-directories.svg)

The Mummy's files are stored in `/Users/imhotep`,
Wolfman's in `/Users/larry`,
and Nelle's in `/Users/nelle`.  Because Nelle is the user in our
examples here, this is why we get `/Users/nelle` as our home directory.  
Typically, when you open a new command prompt you will be in
your home directory to start.  

As part of going further with exploring the Bash Shell we'll move to connecting to a remote system.  This will allow us to see some new commands, ensure that the experience of each user from here on with the file system they are interacting with is (mostly) uniform, and let us begin to get familiar with the HPC system that we will be working with.

## Connecting to a Remote HPC System

### SSH from Terminal Window
`ssh` is the "Secure SHell" command and is used to open a connection with another computer system and use the current terminal window to interact with that system *as if* it was the local system.  There are many options available with the `ssh` command from passing a username up front to passing graphical display content to using special keys (very long strings of seemingly random numbers) for authentication.  We will set aside such options because while they are important they are in addition to using `ssh` in the simplest way possible, which we'll look at now.

Unlike the commands that we have issued so far `ssh` requires both the command (`ssh`) *and* and an input.  The input in this case is the location of the remote system that we are looking to connect to.  This input is passed to the `ssh` command by placing one or more spaces *after* the `ssh` command and then typing in the address for the remote system either in alpha-numeric format, like most web addresses, or by giving an IP address.  If the name of the remote system was `cedar.computecanada.ca` then the full command would look like the following:

~~~
$ ssh cedar.computecanada.ca
~~~
{: .bash}

If this was the first time we had ever connected to `cedar.computecanada.ca	` then we will see a note declaring that our computer has no way to know that this is the system that we want to connect to and it will ask us if we are sure about connecting.

~~~
The authenticity of host 'graham.computecanada.ca (199.241.166.2)' can't be established.
ECDSA key fingerprint is SHA256:JRj286Pkqh6aeO5zx1QUkS8un5fpcapmezusceSGhok.
Are you sure you want to continue connecting (yes/no)?
~~~
{: .output}

It is always worth double checking the address/IP address to make sure that it is indeed the system that we intend to connect to.  If you are really concerned about the authenticity of the system then you will need to contact someone like a system administrator on that system and ask them for the IP address of the system (if you were not using it to connect already) and/or the fingerprint (the long string of alpha-numeric digits above).  If these match then you can continue.  If they do not matche then you'll need to either correct your address or, if it is already correct, then contact a system administrator on the system for advice on how to proceed.

Assuming that all is well you just need to type "yes" and press ENTER to move on.

~~~
$ yes
~~~
{: .bash}

This will give you what the system considers to be a warning.  Note that it is not necessarily a bad thing to receive a warning like this, it is just something to take note of.  In this case the warning is telling us that our computer is going to remember the remote system, matching its name/IP to the fingerprint.  As long as these continue to match then in the future we'll be taken directly to the part where we put in our username and password.  If they fail to match in the future then we'll be given a more serious warning and will be unable to connect until we fix the problem.

~~~
Warning: Permanently added 'graham.computecanada.ca,199.241.166.2' (ECDSA) to the list of known hosts.
~~~
{: .output}

Beneath the warning it will prompt for a password.

~~~
carpentry@graham.computecanada.ca's password:
~~~
{: .output}

Type your password and press ENTER to access the system.  Note two

~~~
Password123
~~~
{: .bash}

~~~
Welcome to the ComputeCanada/SHARCNET cluster Graham.

Please refer to the following page:
https://docs.computecanada.ca/wiki/Graham

Email support@computecanada.ca for assistance.

***


intel/2016.4: 
============================================================================================
The software listed above is available for non-commercial usage only. By
continuing, you
accept that you will not use the software for commercial purposes.

Le logiciel listé ci-dessus est disponible pour usage non commercial
seulement. En
continuant, vous acceptez de ne pas l'utiliser pour un usage commercial.
============================================================================================
~~~
{: .output}

### PuTTY

It is strictly speaking not necessary to have a terminal running on your local computer in order to access and use a remote system, only a window into the remote system once connected.  PuTTy is likely the oldest, most well-known, and widely used software solution to take this approach.

PuTTY is available for free download from [www.putty.org](http://www.putty.org/).  Download the version that is correct for your operating system and install it as you would other software on you Windows system.  Once installed it will be available through the start menu or similar.

Running PuTTY will not initially produce a terminal but intsead a window full of connection options.  Putting the address of the remote system in the "Host Name (or IP Address)" box and either pressing enter or clicking the "Open" button should begin the connection process.

If this works you will see a terminal window open that prompts you for a username through the "login as:" prompt and then for a password.  If both of these are passed correctly then you will be given access to the system and will see a message saying so within the terminal.  If you need to escape the authentication process you can hold the control/ctrl key and press the c key to exit and start again.

Note that you may want to paste in your password rather than typing it.  Use control/ctrl plus a right-click of the mouse to paste content from the clipboard to the PuTTY terminal.

For those logging in with PuTTY it would likely be best to cover the terminal basics already mentioned, above.

## Navigating the Remote System

ls

cd

home, scratch, and project