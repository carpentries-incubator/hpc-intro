---
layout: page
title: Setup
root: .
---

There are several pieces of software you will wish to install before the workshop. Though
installation help will be provided at the workshop, we recommend that these tools are installed (or
at least downloaded) beforehand.

> ## Bash and SSH
>
> This lesson requires a terminal application (`bash`) with the ability to securely connect to a
> remote machine (`ssh`).
{: .prereq}

## Where to type commands: How to open a new shell

The shell is a program that enables us to send commands to the computer and receive output. It is
also referred to as the terminal or command line.

Some computers include a default Unix Shell program. The steps below describe some methods for
identifying and opening a Unix Shell program if you already have one installed. There are also
options for identifying and downloading a Unix Shell program, a Linux/UNIX emulator, or a program
to access a Unix Shell on a server.

### Windows

Computers with Windows operating systems do not automatically have a Unix Shell program installed.
In this lesson, we encourage you to use an emulator included in Git for Windows, which gives you
access to both Bash shell commands and Git. If you have attended a Software Carpentry workshop
session, it is likely you have already received instructions on how to install Git for Windows.

Once installed, you can open a terminal by running the program Git Bash from the Windows start menu.

#### Reference

* [Git for Windows](https://git-for-windows.github.io/) &ndash; *Recommended*
* [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
  &ndash; advanced option for Windows 10

> ## Alternatives to Git for Windows
>
> Other solutions are available for running Bash commands on Windows. There is now a Bash shell
> command-line tool available for Windows 10. Additionally, you can run Bash commands on a remote
> computer or server that already has a Unix Shell, from your Windows machine. This can usually be
> done through a Secure Shell (SSH) client. One such client available for free for Windows computers
> is PuTTY. See the reference below for information on installing and using PuTTY, using the Windows
> 10 command-line tool, or installing and using a Unix/Linux emulator.
>
> For advanced users, you may choose one of the following alternatives: 
>
> * Install the [Windows Subsystem for
>   Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
> * Use the Windows [Powershell](
https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core?view=powershell-7)
> * Read up on [Using a Unix/Linux emulator (Cygwin) or Secure Shell (SSH) client
>   (Putty)](http://faculty.smu.edu/reynolds/unixtut/windows.html)
>
> > ## Warning
> >
> > Commands in the Windows Subsystem for Linux (WSL), Powershell, or Cygwin may differ slightly
> > from those shown in the lesson or presented in the workshop. Please ask if you encounter such
> > a mismatch &ndash; you're probably not alone.
> {: .challenge}
{: .discussion}

### macOS

For a Mac computer running macOS Mojave or earlier releases, the default Unix Shell is Bash. For a
Mac computer running macOS Catalina or later releases, the default Unix Shell is Zsh. Your default
shell is available via the Terminal program within your Utilities folder.

To open Terminal, try one or both of the following:

* In Finder, select the Go menu, then select Utilities. Locate Terminal in the Utilities folder and
  open it.
* Use the Mac ‘Spotlight’ computer search function. Search for: `Terminal` and press
  <kbd>Return</kbd>.

To check if your machine is set up to use something other than Bash, type `echo $SHELL` in your
terminal window. If your machine is set up to use something other than Bash, you can run it by
typing `bash`.

#### Reference 

[How to Use Terminal on a
Mac](http://www.macworld.co.uk/feature/mac-software/how-use-terminal-on-mac-3608274/)

### Linux

The default Unix Shell for Linux operating systems is usually Bash. On most versions of Linux, it
is accessible by running the [(Gnome) Terminal](https://help.gnome.org/users/gnome-terminal/stable/)
or [(KDE) Konsole](https://konsole.kde.org/) or [xterm](https://en.wikipedia.org/wiki/Xterm), which
can be found via the applications menu or the search bar. If your machine is set up to use something
other than Bash, you can run it by opening a terminal and typing `bash`.

### Special cases

If none of the options above address your circumstances, try an online search for: `Unix shell [your
computer model] [your operating system]`.

## SSH for Secure Connections

All students should have an SSH client installed. SSH is a tool that allows us to connect to and
use a remote computer as our own.

### Windows

Git for Windows comes with SSH preinstalled: you do not have to do anything.

> ## GUI Support
>
> If you know that the software you will be running on the cluster requires a graphical user interface (a GUI window needs to open for the application to run properly), please
> install [MobaXterm](http://mobaxterm.mobatek.net) Home Edition.
{: .discussion}

### macOS

macOS comes with SSH pre-installed: you do not have to do anything. 

> ## GUI Support
>
> If you know that the software you will be running requires a graphical user interface, please
> install [XQuartz](www.xquartz.org).
{: .discussion}

### Linux

Linux comes with SSH and X window support preinstalled: you do not have to do anything.
