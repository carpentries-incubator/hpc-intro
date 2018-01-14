---
title: "Moving around and looking at things"
teaching: 15 
exercises: 5
questions:
- "How do I navigate and look around the system?"
objectives:
- Learn how to navigate around directories and look at their contents
- Explain the difference between a file and a directory.
- Translate an absolute path into a relative path and vice versa.
- Identify the actual command, flags, and filenames in a command-line call.
- Demonstrate the use of tab completion, and explain its advantages.
keypoints:
- "Your current directory is referred to as the working directory."
- "To change directories, use `cd`."
- "To view files, use `ls`."
- "We can view a command's manual with `man command_name`."
---

At the point in this lesson, we've just logged into the system. 
Nothing has happened yet, and we're not going to be able to do anything until we learn a few basic commands. 
By the end of this lesson, you will know how to "move around" the system and look at what's there.

Right now, all we see is something that looks like this:

~~~
$
~~~
{: .bash}

The dollar sign is a **prompt**, which shows us that the shell is waiting for input;
your shell may use a different character as a prompt and may add information before
the prompt. When typing commands, either from these lessons or from other sources,
do not type the prompt, only the commands that follow it.

Type the command `whoami`, then press the Enter key (sometimes marked Return) to send the command to the shell. The command's output is the ID of the current user, i.e., it shows us who the shell thinks we are:

~~~
$ whoami
~~~
{: .bash}
~~~
jeff
~~~
{: .output}

More specifically, when we type `whoami` the shell:

1.  finds a program called `whoami`,
2.  runs that program,
3.  displays that program's output, then
4.  displays a new prompt to tell us that it's ready for more commands.

Next,
let's find out where we are by running a command called `pwd` (which stands for "print working directory"). At any moment, our **current working directory** (where we are) is the directory that the computer assumes we want to run commands in unless we explicitly specify something else.
Here, the computer's response is `/home/jeff`, which is Jeff's **home directory**:
Note that the location of your home directory may differ from system to system.

~~~
$ pwd
~~~
{: .bash}
~~~
/home/jeff
~~~
{: .output}

So, we know where we are. How do we look and see what's in our current directory?
```
$ ls
```
{: .bash}

`ls` prints the names of the files and directories in the current directory in alphabetical order, arranged neatly into columns.

> ## Differences between remote and local system
>
> Open a second terminal window on your local computer and run the `ls` command without logging in remotely.
> What differences do you see?
>
> > You would likely see something more like this:
> > ~~~
> > Applications Documents    Library      Music        Public
> > Desktop      Downloads    Movies       Pictures
> > ~~~
> > In addition you should also note that the preamble before the prompt (`$`) is different.  This is very important for making sure you know what system you are issuing commands on when in the shell.
> {: .solution}
{: .challenge}

If nothing shows up when you run `ls`, it means that nothing's there. Let's make a directory for us to play with.

`mkdir <new directory name>` makes a new directory with that name in your current location. Notice that this command required two pieces of input: the actual name of the command (`mkdir`) and an argument that specifies the name of the directory you wish to create.

```
$ mkdir documents
```
{: .bash}

Let's us `ls` again. What do we see?

Our folder is there, awesome. What if we wanted to go inside it and do stuff there?

We will use the `cd` (change directory) command to move around. Let's `cd` into our new Documents folder.

```
$ cd documents
$ pwd
```
{: .bash}
```
~/documents
```
{: .output}

Now that we know how to use `cd`, we can go anywhere. That's a lot of responsibility. What happens if we get "lost" and want to get back to where we started?

To go back to your home directory, the following two commands will work:

```
cd /home/yourUserName
cd ~
```
{: .bash}

What is the `~` character? When using the shell, `~` is a shortcut that represents `/home/yourUserName`.

A quick note on the structure of a UNIX (Linux/Mac/Android/Solaris/etc) filesystem. Directories and absolute paths (i.e. exact position in the system) are always prefixed with a `/`. `/` is the "root" or base directory.

Let's go there now, look around, and then return to our home directory.
```
cd /
ls
cd ~
```
{: .bash}
```
bin   cvmfs  etc   initrd  lib64  localscratch  mnt  opt   project  root  sbin     srv  tmp  var
boot  dev    home  lib     local  media         nix  proc  ram      run   scratch  sys  usr  work
```
{: .output}

The "home" directory is the one where we generally want to keep all of our files. 
Other folders on a UNIX OS contain system files, and get modified and changed as you install new software or upgrade your OS.

> ## Using HPC filesystems
> On HPC systems, you have a number of places where you can store your files. These differ in both the amount of space allocated and whether or not they are backed up.
>
> File storage locations:  
> **Home directory** - Your home directory (also known as `~`), is usually a great place to store anything, and is typically backed up. The home directory is typically (but not always!) located under `/home`.
> **Network filesystem** - Many systems will have other storage locations besides just your home directory that are typically backed up as well. In the last command, `/project` is an example of one such filesystem.
> **Scratch** - Some systems may offer "scratch" space. Scratch space is typically faster to use than your home directory or network filesystem, but is not usually backed up, and should not be used for long term storage. In the last example, `/scratch` is a scratch drive.
> **Local scratch (job only)** - Some systems may offer local scratch space while executing a job. Such storage is very fast, but will be deleted at the end of your job.
> **Ramdisk (job only)** - Some systems may let you store files in a "ramdisk" while running a job, where files are stored directly in the computer's memory. This extremely fast, but files stored here will count against your job's memory usage and be deleted at the end of your job. 
{: .callout}

There are several other useful shortcuts you should be aware of.  

+ `.` represents your current directory   

+ `..` represents the "parent" directory of your current location

+ While typing nearly *anything*, you can have bash try to autocomplete what you are typing by pressing the `tab` key.  

Let's try these out now:
```
$ cd ./documents
$ pwd
$ cd ..
$ pwd
```
{: .bash}
```
/home/jeff/documents
/home/jeff
```

Many commands also have multiple behaviors that you can invoke with command
line 'flags.' What is a flag? It's generally just your command followed by a
'-' and the name of the flag (sometimes it's '--' followed by the name of the
flag. You follow the flag(s) with any additional arguments you might need.

We're going to demonstrate a couple of these "flags" using `ls`.

Show hidden files with `-a`. Hidden files are files that begin with `.`,
these files will not appear otherwise, but that doesn't mean they aren't there!
"Hidden" files are not hidden for security purposes, 
they are usually just config files and other tempfiles 
that the user doesn't necessarily need to see all the time.

```
$ ls -a
```
{: .bash}
```
.   .bash_history  .bash_profile  documents  .oracle_jre_usage  .Xauthority
..  .bash_logout   .bashrc        .licenses  .pki
```
{: .output}

Notice how both `.` and `..` are visible as hidden files.
Show files, their size in bytes, date last modified, permissions, and other things with `-l`.

```
$ ls -l
```
{: .bash}
```
drwxr-xr-x 2 jeff jeff 4096 Jan 14 17:31 documents
```
{: .output}

This is a lot of information to take in at once, but we will explain this later! `ls -l` is *extremely* useful, and tells you almost everything you need to know about your files without actually looking at them.

We can also use multiple flags at the same time!
```
$ ls -l -a
```
{: .bash}
```
drwx------.    6 jeff jeff  4096 Jan 14 17:31 .
drwxrwxr-x  2805 root root 98304 Jan 12 12:03 ..
-rw-------     1 jeff jeff    63 Jan  3 11:32 .bash_history
-rw-r--r--.    1 jeff jeff    18 Jan  2 14:20 .bash_logout
-rw-r--r--.    1 jeff jeff   193 Jan  2 14:20 .bash_profile
-rw-r--r--.    1 jeff jeff   231 Jan  2 14:20 .bashrc
drwxr-xr-x     2 jeff jeff  4096 Jan 14 17:31 documents
drwxr-xr-x     2 jeff jeff  4096 Jan 14 17:31 .licenses
drwxr-xr-x     2 jeff jeff  4096 Jan  3 11:30 .oracle_jre_usage
drwxr-----     3 jeff jeff  4096 Jan  3 11:32 .pki
-rw-------     1 jeff jeff   106 Jan 14 17:31 .Xauthority
```
{: .output}

Flags generally precede any arguments passed to a UNIX command. `ls` actually takes an extra argument that specifies a directory to look into.
When you use flags and arguments together, they syntax (how it's supposed to be typed) generally looks something like this:

```
$ command <flags/options> <arguments>
```
{: .bash}

So using `ls -l -a` on a different directory than the one we're in would look something like:

```
$ ls -l -a ~/documents
```
{: .bash}
```
drwx------  6 jeff jeff 4096 Jan 14 17:31 .
drwxrwxr-x. 2 jeff jeff 4096 Jan 14 17:31 ..
```
{: .output}

## Where to go for help?

How did I know about the `-l` and `-a` options? Is there a manual we can look at for help when we need help?
There is a very helpful manual for most UNIX commands: `man` (if you've ever heard of a "man page" for something, this is what it is).

```
$ man ls
```
{: .bash}
```
LS(1)                                                   User Commands                                                  LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about the FILEs (the current directory by default).  Sort entries alphabetically if none of -cftu‐
       vSUX nor --sort is specified.

       Mandatory arguments to long options are mandatory for short options too.
Manual page ls(1) line 1 (press h for help or q to quit)
```
{: .output}

To navigate through the `man` pages,
you may use the up and down arrow keys to move line-by-line,
or try the spacebar and "b" keys to skip up and down by full page.
Quit the `man` pages by typing "q".

Alternatively, most commands you run will have a 
`--help` option that displays addition information 
For instance, with `ls`:

```
$ ls --help
```
{: .bash}
```
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

# further output omitted for clarity
```
{: .output}

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


> ## Looking at documentation
> Looking at the man page for `ls` or using `ls --help`, what does the `-h` (`--human-readable`) option do?
{: .challenge}

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
