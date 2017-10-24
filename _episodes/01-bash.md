---
title: "UNIX fundamentals: Connecting & BASH Basics"
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

Type your password and press ENTER to access the system.

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

For those logging in with PuTTY it would likely be best to cover the terminal basics already mentioned above before moving on to navigating the remote system.

## Telling the Difference between the Local Terminal and the Remote Terminal

You may have noticed that the prompt changed when you logged into the remote system using the terminal (if you logged in using PuTTY this will not apply because it does not offer a local terminal).  This change is important because it makes it clear on which system the commands you type will be run when you pass them into the terminal.  This change is also a small complication that we will need to navigate throughout the workshop.  Exactly what is reported before the `$` in the terminal when it is connected to the local system and the remote system will typically be different for every user.  We still need to indicate which system we are entering commands on though so we will adopt the following convention:

`[local]$` when the command is to be entered on a terminal connected to your local computer

`[remote]$` when the command is to be entered on a terminal connected to the remote system

`$` when it really doesn't matter which system the terminal is connected to.

> ## Keep Two Terminal Windows Open
> It is strongly recommended that you have two terminals open, one connected to the local system and one connected to the remote system, that you can switch back and forth between.  If you only use one terminal window then you will need to reconnect to the remote system using one of the methods above when you see a change from `[local]$` to `[remote]$` and disconnect when you see the reverse.
{: .callout}

## Navigating the Remote System

Now let's learn the command that will let us see the contents of the remote filesystem.  We can see what's in our home directory by running `ls`,
which stands for "listing":

~~~
[remote]$ ls
~~~
{: .bash}

~~~
project  projects  scratch
~~~
{: .output}

(Again, your results may be slightly different depending on the operating
system and how the remote system has been customized.)


`ls` prints the names of the files and directories in the current directory in
alphabetical order,
arranged neatly into columns.

Running `ls` on the remote system is likely significantly different from what you would see if you ran `ls` from your laptop or home computer.

 where 
{: .output}

> ## Differences between remote and local system
>
> Open a second terminal window on your local computer and run the `ls` command without logging in remotely.
>  What differences do you see?
> > you would likely see something more like this:
> > ~~~
> > Applications Documents    Library      Music        > > Public
> > Desktop      Downloads    Movies       Pictures
> > ~~~
> > In addition you should also note that the preamble before the prompt (`$`) is different.  This is very important for making sure you know what system you are issuing commands on when in the shell.
> {: .solution}
{: .challenge}

We can make its output more comprehensible by using the **flag** `-F`,
which tells `ls` to add a trailing `/` to the names of directories:

~~~
[remote]$ ls -F
~~~
{: .bash}

~~~
project/  projects/  scratch/
~~~
{: .output}

# **FROM HERE DOWN NEEDS TWEAKING TO FIT WITH A REMOTE HPC SYSTEM.  PROJECT, SCRATCH, etc. NEED DESCRIBING.** 

`ls` has lots of other options. To find out what they are, we can type:

~~~
[remote]$ ls --help
~~~
{: .bash}

~~~
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      scale sizes by SIZE before printing them; e.g.,
                               '--block-size=M' prints sizes in units of
                               1,048,576 bytes; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
  -c                         with -lt: sort by, and show, ctime (time of last
                               modification of file status information);
                               with -l: show ctime and sort by name;
                               otherwise: sort by ctime, newest first
  -C                         list entries by columns
      --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                               if omitted), 'auto', or 'never'; more info below
  -d, --directory            list directories themselves, not their contents
  -D, --dired                generate output designed for Emacs' dired mode
  -f                         do not sort, enable -aU, disable -ls --color
  -F, --classify             append indicator (one of */=>@|) to entries
      --file-type            likewise, except do not append '*'
      --format=WORD          across -x, commas -m, horizontal -x, long -l,
                               single-column -1, verbose -l, vertical -C
      --full-time            like -l --time-style=full-iso
  -g                         like -l, but do not list owner
      --group-directories-first
                             group directories before files;
                               can be augmented with a --sort option, but any
                               use of --sort=none (-U) disables grouping
  -G, --no-group             in a long listing, don't print group names
  -h, --human-readable       with -l and/or -s, print human readable sizes
                               (e.g., 1K 234M 2G)
      --si                   likewise, but use powers of 1000 not 1024
  -H, --dereference-command-line
                             follow symbolic links listed on the command line
      --dereference-command-line-symlink-to-dir
                             follow each command line symbolic link
                               that points to a directory
      --hide=PATTERN         do not list implied entries matching shell PATTERN
                               (overridden by -a or -A)
      --indicator-style=WORD  append indicator with style WORD to entry names:
                               none (default), slash (-p),
                               file-type (--file-type), classify (-F)
  -i, --inode                print the index number of each file
  -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
  -k, --kibibytes            default to 1024-byte blocks for disk usage
  -l                         use a long listing format
  -L, --dereference          when showing file information for a symbolic
                               link, show information for the file the link
                               references rather than for the link itself
  -m                         fill width with a comma separated list of entries
  -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
  -N, --literal              print raw entry names (don't treat e.g. control
                               characters specially)
  -o                         like -l, but do not list group information
  -p, --indicator-style=slash
                             append / indicator to directories
  -q, --hide-control-chars   print ? instead of nongraphic characters
      --show-control-chars   show nongraphic characters as-is (the default,
                               unless program is 'ls' and output is a terminal)
  -Q, --quote-name           enclose entry names in double quotes
      --quoting-style=WORD   use quoting style WORD for entry names:
                               literal, locale, shell, shell-always,
                               shell-escape, shell-escape-always, c, escape
  -r, --reverse              reverse order while sorting
  -R, --recursive            list subdirectories recursively
  -s, --size                 print the allocated size of each file, in blocks
  -S                         sort by file size, largest first
      --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                               time (-t), version (-v), extension (-X)
      --time=WORD            with -l, show time as WORD instead of default
                               modification time: atime or access or use (-u);
                               ctime or status (-c); also use specified time
                               as sort key if --sort=time (newest first)
      --time-style=STYLE     with -l, show times using style STYLE:
                               full-iso, long-iso, iso, locale, or +FORMAT;
                               FORMAT is interpreted like in 'date'; if FORMAT
                               is FORMAT1<newline>FORMAT2, then FORMAT1 applies
                               to non-recent files and FORMAT2 to recent files;
                               if STYLE is prefixed with 'posix-', STYLE
                               takes effect only outside the POSIX locale
  -t                         sort by modification time, newest first
  -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
  -u                         with -lt: sort by, and show, access time;
                               with -l: show access time and sort by name;
                               otherwise: sort by access time, newest first
  -U                         do not sort; list entries in directory order
  -v                         natural sort of (version) numbers within text
  -w, --width=COLS           set output width to COLS.  0 means no limit
  -x                         list entries by lines instead of by columns
  -X                         sort alphabetically by entry extension
  -Z, --context              print any security context of each file
  -1                         list one file per line.  Avoid '\n' with -q or -b
      --help     display this help and exit
      --version  output version information and exit

The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

Using color to distinguish file types is disabled both by default and
with --color=never.  With --color=auto, ls emits color codes only when
standard output is connected to a terminal.  The LS_COLORS environment
variable can change the settings.  Use the dircolors command to set it.

Exit status:
 0  if OK,
 1  if minor problems (e.g., cannot access subdirectory),
 2  if serious trouble (e.g., cannot access command-line argument).

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/ls>
or available locally via: info '(coreutils) ls invocation'
~~~
{: .output}

Many bash commands, and programs that people have written that can be
run from within bash, support a `--help` flag to display more
information on how to use the commands or programs.

> ## Unsupported command-line options
> If you try to use an option that is not supported, `ls` and other programs
> will print an error message similar to this:
>
> ~~~
> [remote]$ ls -j
> ~~~
> {: .bash}
> 
> ~~~
> ls: invalid option -- 'j'
> Try 'ls --help' for more information.
> ~~~
> {: .error}
{: .callout}

For more information on how to use `ls` we can type `man ls`.
`man` is the Unix "manual" command:
it prints a description of a command and its options,
and (if you're lucky) provides a few examples of how to use it.

To navigate through the `man` pages,
you may use the up and down arrow keys to move line-by-line,
or try the "b" and spacebar keys to skip up and down by full page.
Quit the `man` pages by typing "q".

Here,
we can see that our home directory contains mostly **sub-directories**.
Any names in your output that don't have trailing slashes,
are plain old **files**.
And note that there is a space between `ls` and `-F`:
without it,
the shell thinks we're trying to run a command called `ls-F`,
which doesn't exist.

> ## Parameters vs. Arguments
>
> According to [Wikipedia](https://en.wikipedia.org/wiki/Parameter_(computer_programming)#Parameters_and_arguments),
> the terms **argument** and **parameter**
> mean slightly different things.
> In practice,
> however,
> most people use them interchangeably
> to refer to the input term(s) given to a command.
> Consider the example below:
> ```
> [remote]$ ls -lh Documents
> ```
> {: .bash}
> `ls` is the command, `-lh` are the flags (also called options),
> and `Documents` is the argument.
{: .callout}

We can also use `ls` to see the contents of a different directory.  Let's take a
look at our `Desktop` directory by running `ls -F Desktop`,
i.e.,
the command `ls` with the **arguments** `-F` and `Desktop`.
The second argument --- the one *without* a leading dash --- tells `ls` that
we want a listing of something other than our current working directory:

~~~
[remote]$ ls -F Desktop
~~~
{: .bash}

~~~
data-shell/
~~~
{: .output}

Your output should be a list of all the files and sub-directories on your
Desktop, including the `data-shell` directory you downloaded at
the start of the lesson.  Take a look at your Desktop to confirm that
your output is accurate.  

As you may now see, using a bash shell is strongly dependent on the idea that
your files are organized in an hierarchical file system.  
Organizing things hierarchically in this way helps us keep track of our work:
it's possible to put hundreds of files in our home directory,
just as it's possible to pile hundreds of printed papers on our desk,
but it's a self-defeating strategy.

Now that we know the `data-shell` directory is located on our Desktop, we
can do two things.  

First, we can look at its contents, using the same strategy as before, passing
a directory name to `ls`:

~~~
[remote]$ ls -F Desktop/data-shell
~~~
{: .bash}

~~~
creatures/          molecules/          notes.txt           solar.pdf
data/               north-pacific-gyre/ pizza.cfg           writing/
~~~
{: .output}

Second, we can actually change our location to a different directory, so
we are no longer located in
our home directory.  

The command to change locations is `cd` followed by a
directory name to change our working directory.
`cd` stands for "change directory",
which is a bit misleading:
the command doesn't change the directory,
it changes the shell's idea of what directory we are in.

Let's say we want to move to the `data` directory we saw above.  We can
use the following series of commands to get there:

~~~
[remote]$ cd Desktop
[remote]$ cd data-shell
[remote]$ cd data
~~~
{: .bash}

These commands will move us from our home directory onto our Desktop, then into
the `data-shell` directory, then into the `data` directory.  `cd` doesn't print anything,
but if we run `pwd` after it, we can see that we are now
in `/Users/nelle/Desktop/data-shell/data`.
If we run `ls` without arguments now,
it lists the contents of `/Users/nelle/Desktop/data-shell/data`,
because that's where we now are:

~~~
[remote]$ pwd
~~~
{: .bash}

~~~
/Users/nelle/Desktop/data-shell/data
~~~
{: .output}

~~~
[remote]$ ls -F
~~~
{: .bash}

~~~
amino-acids.txt   elements/     pdb/	        salmon.txt
animals.txt       morse.txt     planets.txt     sunspot.txt
~~~
{: .output}

We now know how to go down the directory tree, but
how do we go up?  We might try the following:

~~~
[remote]$ cd data-shell
~~~
{: .bash}

~~~
-bash: cd: data-shell: No such file or directory
~~~
{: .error}

But we get an error!  Why is this?  

With our methods so far,
`cd` can only see sub-directories inside your current directory.  There are
different ways to see directories above your current location; we'll start
with the simplest.  

There is a shortcut in the shell to move up one directory level
that looks like this:

~~~
[remote]$ cd ..
~~~
{: .bash}

`..` is a special directory name meaning
"the directory containing this one",
or more succinctly,
the **parent** of the current directory.
Sure enough,
if we run `pwd` after running `cd ..`, we're back in `/Users/nelle/Desktop/data-shell`:

~~~
[remote]$ pwd
~~~
{: .bash}

~~~
/Users/nelle/Desktop/data-shell
~~~
{: .output}

The special directory `..` doesn't usually show up when we run `ls`.  If we want
to display it, we can give `ls` the `-a` flag:

~~~
[remote]$ ls -F -a
~~~
{: .bash}

~~~
./                  creatures/          notes.txt
../                 data/               pizza.cfg
.bash_profile       molecules/          solar.pdf
Desktop/            north-pacific-gyre/ writing/
~~~
{: .output}

`-a` stands for "show all";
it forces `ls` to show us file and directory names that begin with `.`,
such as `..` (which, if we're in `/Users/nelle`, refers to the `/Users` directory)
As you can see,
it also displays another special directory that's just called `.`,
which means "the current working directory".
It may seem redundant to have a name for it,
but we'll see some uses for it soon.

Note that in most command line tools, multiple arguments can be combined 
with a single `-` and no spaces between the arguments: `ls -F -a` is 
equivalent to `ls -Fa`.

> ## Other Hidden Files
>
> In addition to the hidden directories `..` and `.`, you may also see a file
> called `.bash_profile`. This file usually contains shell configuration
> settings. You may also see other files and directories beginning
> with `.`. These are usually files and directories that are used to configure
> different programs on your computer. The prefix `.` is used to prevent these
> configuration files from cluttering the terminal when a standard `ls` command
> is used.
{: .callout}

> ## Orthogonality
>
> The special names `.` and `..` don't belong to `cd`;
> they are interpreted the same way by every program.
> For example,
> if we are in `/Users/nelle/data`,
> the command `ls ..` will give us a listing of `/Users/nelle`.
> When the meanings of the parts are the same no matter how they're combined,
> programmers say they are **orthogonal**:
> Orthogonal systems tend to be easier for people to learn
> because there are fewer special cases and exceptions to keep track of.
{: .callout}

These then, are the basic commands for navigating the filesystem on your computer:
`pwd`, `ls` and `cd`.  Let's explore some variations on those commands.  What happens
if you type `cd` on its own, without giving
a directory?  

~~~
[remote]$ cd
~~~
{: .bash}

How can you check what happened?  `pwd` gives us the answer!  

~~~
[remote]$ pwd
~~~
{: .bash}

~~~
/Users/nelle
~~~
{: .output}

It turns out that `cd` without an argument will return you to your home directory,
which is great if you've gotten lost in your own filesystem.  

Let's try returning to the `data` directory from before.  Last time, we used
three commands, but we can actually string together the list of directories
to move to `data` in one step:

~~~
[remote]$ cd Desktop/data-shell/data
~~~
{: .bash}

Check that we've moved to the right place by running `pwd` and `ls -F`  

If we want to move up one level from the data directory, we could use `cd ..`.  But
there is another way to move to any directory, regardless of your
current location.  

So far, when specifying directory names, or even a directory path (as above),
we have been using **relative paths**.  When you use a relative path with a command
like `ls` or `cd`, it tries to find that location  from where we are,
rather than from the root of the file system.  

However, it is possible to specify the **absolute path** to a directory by
including its entire path from the root directory, which is indicated by a
leading slash.  The leading `/` tells the computer to follow the path from
the root of the file system, so it always refers to exactly one directory,
no matter where we are when we run the command.

This allows us to move to our `data-shell` directory from anywhere on
the filesystem (including from inside `data`).  To find the absolute path
we're looking for, we can use `pwd` and then extract the piece we need
to move to `data-shell`.  

~~~
[remote]$ pwd
~~~
{: .bash}

~~~
/Users/nelle/Desktop/data-shell/data
~~~
{: .output}

~~~
[remote]$ cd /Users/nelle/Desktop/data-shell
~~~
{: .bash}

Run `pwd` and `ls -F` to ensure that we're in the directory we expect.  

> ## Two More Shortcuts
>
> The shell interprets the character `~` (tilde) at the start of a path to
> mean "the current user's home directory". For example, if Nelle's home
> directory is `/Users/nelle`, then `~/data` is equivalent to
> `/Users/nelle/data`. This only works if it is the first character in the
> path: `here/there/~/elsewhere` is *not* `here/there/Users/nelle/elsewhere`.
>
> Another shortcut is the `-` (dash) character.  `cd` will translate `-` into
> *the previous directory I was in*, which is faster than having to remember,
> then type, the full path.  This is a *very* efficient way of moving back
> and forth between directories. The difference between `cd ..` and `cd -` is
> that the former brings you *up*, while the latter brings you *back*. You can
> think of it as the *Last Channel* button on a TV remote.
{: .callout}

### Nelle's Pipeline: Organizing Files

Knowing just this much about files and directories,
Nelle is ready to organize the files that the protein assay machine will create.
First,
she creates a directory called `north-pacific-gyre`
(to remind herself where the data came from).
Inside that,
she creates a directory called `2012-07-03`,
which is the date she started processing the samples.
She used to use names like `conference-paper` and `revised-results`,
but she found them hard to understand after a couple of years.
(The final straw was when she found herself creating
a directory called `revised-revised-results-3`.)

> ## Sorting Output
>
> Nelle names her directories "year-month-day",
> with leading zeroes for months and days,
> because the shell displays file and directory names in alphabetical order.
> If she used month names,
> December would come before July;
> if she didn't use leading zeroes,
> November ('11') would come before July ('7'). Similarly, putting the year first
> means that June 2012 will come before June 2013.
{: .callout}

Each of her physical samples is labelled according to her lab's convention
with a unique ten-character ID,
such as "NENE01729A".
This is what she used in her collection log
to record the location, time, depth, and other characteristics of the sample,
so she decides to use it as part of each data file's name.
Since the assay machine's output is plain text,
she will call her files `NENE01729A.txt`, `NENE01812A.txt`, and so on.
All 1520 files will go into the same directory.

Now in her current directory `data-shell`,
Nelle can see what files she has using the command:

~~~
[remote]$ ls north-pacific-gyre/2012-07-03/
~~~
{: .bash}

This is a lot to type,
but she can let the shell do most of the work through what is called **tab completion**.
If she types:

~~~
[remote]$ ls nor
~~~
{: .bash}

and then presses tab (the tab key on her keyboard),
the shell automatically completes the directory name for her:

~~~
[remote]$ ls north-pacific-gyre/
~~~
{: .bash}

If she presses tab again,
Bash will add `2012-07-03/` to the command,
since it's the only possible completion.
Pressing tab again does nothing,
since there are 19 possibilities;
pressing tab twice brings up a list of all the files,
and so on.
This is called **tab completion**,
and we will see it in many other tools as we go on.

> ## Absolute vs Relative Paths
>
> Starting from `/Users/amanda/data/`,
> which of the following commands could Amanda use to navigate to her home directory,
> which is `/Users/amanda`?
>
> 1. `cd .`
> 2. `cd /`
> 3. `cd /home/amanda`
> 4. `cd ../..`
> 5. `cd ~`
> 6. `cd home`
> 7. `cd ~/data/..`
> 8. `cd`
> 9. `cd ..`
>
> > ## Solution
> > 1. No: `.` stands for the current directory.
> > 2. No: `/` stands for the root directory.
> > 3. No: Amanda's home directory is `/Users/amanda`.
> > 4. No: this goes up two levels, i.e. ends in `/Users`.
> > 5. Yes: `~` stands for the user's home directory, in this case `/Users/amanda`.
> > 6. No: this would navigate into a directory `home` in the current directory if it exists.
> > 7. Yes: unnecessarily complicated, but correct.
> > 8. Yes: shortcut to go back to the user's home directory.
> > 9. Yes: goes up one level.
> {: .solution}
{: .challenge}

> ## Relative Path Resolution
>
> Using the filesystem diagram below, if `pwd` displays `/Users/thing`,
> what will `ls -F ../backup` display?
>
> 1.  `../backup: No such file or directory`
> 2.  `2012-12-01 2013-01-08 2013-01-27`
> 3.  `2012-12-01/ 2013-01-08/ 2013-01-27/`
> 4.  `original/ pnas_final/ pnas_sub/`
>
> ![File System for Challenge Questions](../fig/filesystem-challenge.svg)
>
> > ## Solution
> > 1. No: there *is* a directory `backup` in `/Users`.
> > 2. No: this is the content of `Users/thing/backup`,
> >    but with `..` we asked for one level further up.
> > 3. No: see previous explanation.
> > 4. Yes: `../backup/` refers to `/Users/backup/`.
> {: .solution}
{: .challenge}

> ## `ls` Reading Comprehension
>
> Assuming a directory structure as in the above Figure
> (File System for Challenge Questions), if `pwd` displays `/Users/backup`,
> and `-r` tells `ls` to display things in reverse order,
> what command will display:
>
> ~~~
> pnas_sub/ pnas_final/ original/
> ~~~
> {: .output}
>
> 1.  `ls pwd`
> 2.  `ls -r -F`
> 3.  `ls -r -F /Users/backup`
> 4.  Either #2 or #3 above, but not #1.
>
> > ## Solution
> >  1. No: `pwd` is not the name of a directory.
> >  2. Yes: `ls` without directory argument lists files and directories
> >     in the current directory.
> >  3. Yes: uses the absolute path explicitly.
> >  4. Correct: see explanations above.
> {: .solution}
{: .challenge}

> ## Exploring More `ls` Arguments
>
> What does the command `ls` do when used with the `-l` and `-h` arguments?
>
> Some of its output is about properties that we do not cover in this lesson (such
> as file permissions and ownership), but the rest should be useful
> nevertheless.
>
> > ## Solution
> > The `-l` arguments makes `ls` use a **l**ong listing format, showing not only
> > the file/directory names but also additional information such as the file size
> > and the time of its last modification. The `-h` argument makes the file size
> > "**h**uman readable", i.e. display something like `5.3K` instead of `5369`.
> {: .solution}
{: .challenge}

> ## Listing Recursively and By Time
>
> The command `ls -R` lists the contents of directories recursively, i.e., lists
> their sub-directories, sub-sub-directories, and so on in alphabetical order
> at each level. The command `ls -t` lists things by time of last change, with
> most recently changed files or directories first.
> In what order does `ls -R -t` display things? Hint: `ls -l` uses a long listing
> format to view timestamps.
>
> > ## Solution
> > The directories are listed alphabetical at each level, the files/directories
> > in each directory are sorted by time of last change.
> {: .solution}
{: .challenge}