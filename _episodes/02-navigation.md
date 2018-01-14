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
ls
```
{: .bash}

`ls` prints the names of the files and directories in the current directory in alphabetical order, arranged neatly into columns.

If nothing shows up, it means that nothing's there. Let's make a directory for us to play with.

`mkdir <new directory name>` makes a new directory with that name in your current location. Notice that this command required two pieces of input: the actual name of the command (`mkdir`) and an argument that specifies the name of the directory you wish to create.

```
mkdir Documents
```
{: .bash}

Let's us `ls` again. What do we see?

Our folder is there, awesome. What if we wanted to go inside it and do stuff there?

We will use the `cd` (change directory) command to move around. Let's `cd` into our new Documents folder.

```
cd Documents
pwd
```
{: .bash}
```
~/Documents
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

Our "home" directory is the one where we generally want to keep all of our files. Other folders on a UNIX OS contain system files, and get modified and changed as you install new software or upgrade your OS.

> ## Using HPC filesystems
> On HPC systems, you have a number of places where you can store your files. These differ in both the amount of space allocated and whether or not they are backed up.
>
> File storage locations:  
> **Home directory** - Your home directory (also known as `~`), is usually a great place to store anything, and is typically backed up.
> **Network filesystem** - Many systems will have other storage locations besides just your home directory that are typically backed up as well.
> **Scratch** - Some systems may offer "scratch" space. Scratch space is typically faster to use than your home directory or network filesystem, but is not usually backed up, and should not be used for long term storage.
> **Local scratch (job only)** - Some systems may offer local scratch space while executing a job. Such storage is very fast, but will be deleted at the end of your job.
> **Ramdisk (job only)** - Some systems may let you store files in a "ramdisk" while running a job, where files are stored directly in the computer's memory. This extremely fast, but files stored here will count against your job's memory usage and be deleted at the end of your job. 
{: .callout}

There are several other useful shortcuts you should be aware of.  

+ `.` represents your current directory   

+ `..` represents the "parent" directory of your current location

+ While typing nearly *anything*, you can have bash try to autocomplete what you are typing by pressing the `tab` key.  


Let's try these out now:
```
cd ./Documents
pwd

cd ..
pwd
```
{: .bash}

Many commands also have multiple behaviors that you can invoke with command line 'flags.' What is a flag? It's generally just your command followed by a '-' and the name of the flag (sometimes it's '--' followed by the name of the flag. You follow the flag(s) with any additional arguments you might need.

We're going to demonstrate a couple of these "flags" using `ls`.

Show hidden files with `-a`. Hidden files are files that begin with `.`, these files will not appear otherwise, but that doesn't mean they aren't there!
```
ls -a
```
{: .bash}

Show files, their size in bytes, date last modified, permissions, and other things with `-l`.
```
ls -l
```
{: .bash}

This is a lot of information to take in at once, but we will explain this later! `ls -l` is *extremely* useful, and tells you almost everything you need to know about your files without actually looking at them.

We can also use multiple flags at the same time!
```
ls -l -a
```
{: .bash}

Flags generally precede any arguments passed to a UNIX command. `ls` actually takes an extra argument that specifies a directory to look into.

When you use flags and arguments together, they syntax (how it's supposed to be typed) generally looks something like this:
```
command <flags/options> <arguments>
```
{: .bash}

So using `ls -l` on a different directory than the one we're in would look something like:
```
ls -l ~/Documents
```
{: .bash}

How did I know about the `-l` and `-a` options? Is there a manual we can look at for help when we need help?
There is a very helpful manual for most UNIX commands: `man` (if you've ever heard of a "man page" for something, this is what it is).
```
man ls
```
{: .bash}

You can scroll through this manual using the arrow keys. To close the manual, press the `q` to exit.
