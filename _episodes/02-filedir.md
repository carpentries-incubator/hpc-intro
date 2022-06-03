---
title: "Navigating Files and Directories"
teaching: 30
exercises: 10
questions:
- "How can I move around the cluster filesystem"
- "How can I see what files and directories I have?"
- "How can I make new files and directories."
objectives:
- "Create, edit, manipulate and remove files from command line"
- "Translate an absolute path into a relative path and vice versa."
- "Use options and arguments to change the behaviour of a shell command."
- "Demonstrate the use of tab completion and explain its advantages."
keypoints:
- "The file system is responsible for managing information on the disk."
- "Information is stored in files, which are stored in directories (folders)."
- "Directories can also store other directories, which then form a directory tree."
- "`cd [path]` changes the current working directory."
- "`ls [path]` prints a listing of a specific file or directory; `ls` on its own lists the current working directory."
- "`pwd` prints the user's current working directory."
- "`cp [file] [path]` copies [file] to [path]"
- "`mv [file] [path]` moves [file] to [path]"
- "`rm [file]` deletes [file]"
- "`/` on its own is the root directory of the whole file system."
- "Most commands take options (flags) that begin with a `-`."
- "A relative path specifies a location starting from the current location."
- "An absolute path specifies a location from the root of the file system."
- "Directory names in a path are separated with `/` on Unix, but `\\` on Windows."
- "`..` means 'the directory above the current one'; `.` on its own means 'the current directory'."
---
> ## The Unix Shell
>
> This episode will be a quick introduction to the Unix shell, only the bare minimum required to use the cluster.
>
> The Software Carpentry '[Unix Shell](https://swcarpentry.github.io/shell-novice/)' lesson covers the subject in more depth, we recommend you check it out.
>
{: .callout}

The part of the operating system responsible for managing files and directories
is called the **file system**.
It organizes our data into files,
which hold information,
and directories (also called 'folders'),
which hold files or other directories.

Understanding how to navigate the file system using command line is essential for using an HPC.

Directories are like *places* — at any time
while we are using the shell, we are in exactly one place called
our **current working directory**.
Commands mostly read and write files in the
current working directory, i.e. 'here', so knowing where you are before running
a command is important.

First, let's find out where we are by running the command `pwd` for '**p**rint **w**orking **d**irectory'. 

```
{{ site.remote.prompt }} pwd
```
{: .language-bash}

```
/home/<username>
```
{: .output}

The output we see is what is known as a 'path'.
The path can be thought of as a series of directions given to navigate the file system.

At the top is the **root directory**
that holds all the files in a filesystem.

We refer to it using a slash character, `/`, on its own.
This is what the leading slash in `/home/<username>` is referring to, it is telling us our path starts at the root directory.

Next is `home`, as it is the next part of the path we know it is inside the root directory,
we also know that home is another directory as the path continues.
Finally, stored inside `home` is the directory with your username.

The NeSI filesystem looks something like this:

![The file system is made up of a root directory that contains sub-directories
titled home, nesi, and system files](../fig/NesiFiletree.svg)

The directories that are relevant to us are.

<table style="width: 100%; height: 90px;">
<tbody>
<tr>
<td style="width: 300px;"></td>
<td style="width: 250px;">Location</td>
<td style="width: 167.562px;">Default Storage</td>
<td style="width: 142.734px;">Default Files</td>
<td style="width: 89.3594px;">Backup</td>
<td style="width: 155.188px;">Access Speed</td>
</tr>
<tr>
<td style="width: 300px;"><strong>Home</strong> is for user-specific files such as configuration files, environment setup, source code, etc.</td>
<td style="width: 250px;"><code>/home/&lt;username&gt;</code></td>
<td style="width: 167.562px;">20GB</td>
<td style="width: 142.734px;">1,000,000</td>
<td style="width: 89.3594px;">Daily</td>
<td style="width: 155.188px;">Normal</td>
</tr>
<tr>
<td style="width: 300px;"><strong>Project</strong> is for persistent project-related data, project-related software, etc.</td>
<td style="width: 250px;"><code>/nesi/project/&lt;projectcode&gt;</code></td>
<td style="width: 167.562px;">100GB</td>
<td style="width: 142.734px;">100,000</td>
<td style="width: 89.3594px;">Daily</td>
<td style="width: 155.188px;">Normal</td>
</tr>
<tr>
<td style="width: 300px;"><strong>Nobackup</strong> is a 'scratch space', for data you don't need to keep long term. Old data is periodically deleted from nobackup</td>
<td style="width: 250px;"><code>/nesi/nobackup/&lt;projectcode&gt;</code></td>
<td style="width: 167.562px;">10TB</td>
<td style="width: 142.734px;">1,000,000</td>
<td style="width: 89.3594px;">None</td>
<td style="width: 155.188px;">Fast</td>
</tr>
</tbody>
</table>

#### Have a Backup Plan

NeSI performs backups of the `/home` and `/nesi/project` (persistent) filesystems.  However, backups are only captured once per day.  So, if you edit or change code or data and then immediately delete it, it likely cannot be recovered.  Note, as the name suggests, NeSI does **not** backup the `/nesi/nobackup` filesystem.

Protecting critical data from corruption or deletion is primarily your 
responsibility. Ensure you have a data management plan and stick to the plan to reduce the chance of data loss.  Also important is managing your storage quota.  To check your quotas, use the `nn_storage_quota` command, eg

```
$ nn_storage_quota
Quota Location                    Available         Used      Use%     State       Inodes        IUsed     IUse%    IState
home_johndoe                            20G       14.51G    72.57%        OK      1000000       112084    11.21%        OK
project_nesi99999                      100G         101G    101.00%       LOCKED  100000           194     0.19%        OK
nobackup_nesi99999                      10T            0     0.00%        OK      1000000           14     0.00%        OK
```

Notice that the project space for this user is over quota and has been locked, meaning no more data can be added.  When your space is locked you will need to move or remove data.  Also note that none of the nobackup space is being used.  Likely data from project can be moved to nobackup.

For more details on our persistent and nobackup storage systems, including data retention and the nobackup autodelete schedule, please see our [Filesystem and Quota](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas) documentation.

#### Version Control

Version control systems (such as Git) often have free, cloud-based offerings
(e.g., BitBucket, GitHub and GitLab) that are generally used for storing source code. Even
if you are not writing your own programs, these can be very useful for storing
job submit scripts, notes and other files.  Git is not an appropriate solution for storing data.
> ## Slashes
>
> Notice that there are two meanings for the `/` character.
> When it appears at the front of a file or directory name,
> it refers to the root directory. When it appears *inside* a path,
> it's just a separator.
{: .callout}

As you may now see, using a bash shell is strongly dependent on the idea that
your files are organized in a hierarchical file system.
Organizing things hierarchically in this way helps us keep track of our work:
it's possible to put hundreds of files in our home directory,
just as it's possible to pile hundreds of printed papers on our desk,
but it's a self-defeating strategy.
## Listing the contents of directories

To **l**i**s**t the contents of a directory, we use the command `ls` followed by the path to the directory whose contents we want listed.

We will now list the contents of the `project` directory we we will be working from. We can
use the following command to do this:

```
{{ site.remote.prompt }} ls {{ site.working_dir[0] }}
```
{: .language-bash}

{% include {{ site.snippets }}/filedir/working-dir.snip %}


You should see a directory called `{{ site.working_dir[1] }}`, and possibly several other directories. For the purposes of this workshop you will be working within `{{ site.working_dir[0] }}/{{ site.working_dir[1] }}`

> ## `ls` Reading Comprehension
>
> Using the filesystem diagram below,
> if `pwd` displays `/Users/backup`,
> and `-r` tells `ls` to display things in reverse order,
> what command(s) will result in the following output:
>
> ```
> pnas_sub pnas_final original
> ```
> {: .output}
>
> ![A directory tree below the Users directory where "/Users" contains the
directories "backup" and "thing"; "/Users/backup" contains "original",
"pnas_final" and "pnas_sub"; "/Users/thing" contains "backup"; and
"/Users/thing/backup" contains "2012-12-01", "2013-01-08" and
"2013-01-27"](../fig/filesystem-challenge.svg)
>
> 1.  `ls pwd`
> 2.  `ls -r`
> 3.  `ls -r /Users/backup`
>
> > ## Solution
> >
> >  1. No: `pwd` is not the name of a directory.
> >  2. Yes: `ls` without directory argument lists files and directories
> >     in the current directory.
> >  3. Yes: uses the absolute path explicitly.
> {: .solution}
{: .challenge}
## Moving about

Currently we are still in our home directory, we want to move into the`project` directory from the previous command.

The command to **c**hange **d**irectory is `cd` followed by the path to the directory we want to move to.

The `cd` command is akin to double clicking a folder in a graphical interface.

We will use the following command:

```
{{ site.remote.prompt }} cd {{ site.working_dir[0] }}/{{ site.working_dir[1] }}
```
{: .language-bash}

You will notice that `cd` doesn't print anything. This is normal. Many shell commands will not output anything to the screen when successfully executed.
We can check we are in the right place by running `pwd`.

```
{{ site.remote.prompt }} pwd
```
{: .language-bash}

```
{{ site.working_dir[0] }}/{{ site.working_dir[1] }}
```
{: .output}

## Creating directories

<!-- NOTE: This bit uses relative paths even though the convept hasn't been introduced yet. -->

As previously mentioned, it is general useful to organise your work in a hierarchical file structure to make managing and finding files easier. It is also is especially important when working within a shared directory with colleagues, such as a project, to minimise the chance of accidentally effecting your colleagues work. So for this workshop you will each make a directory using the `mkdir` command within the workshops directory for you to personally work from.

```
{{ site.remote.prompt }} mkdir <username>
```
{: .language-bash}

You can then your new directory is there using `ls`.

```
{{ site.remote.prompt }} ls {{ site.working_dir[0] }}
```
{: .language-bash}
```
  array_sum.r   usr123   usr234
```
{: .output}
## General Syntax of a Shell Command

We are now going to use `ls` again but with a twist, this time we will also use what are known as **options**, **flags** or **switches**.
These options modify the way that the command works, for this example we will add the flag `-l` for "long listing format".

```
{{ site.remote.prompt }} ls -l {{ site.working_dir[0] }}/{{ site.working_dir[1] }}
```
{: .language-bash}

```
total 1
-rw-r-----+ 1 cwal219 nesi99991  460 Nov 18 17:03 array_sum.r
drwxrws---+ 2 usr123  nesi99991 4096 Nov 15 09:01 usr123
drwxrws---+ 2 usr345  nesi99991 4096 Nov 15 09:01 usr345
```
{: .output}

We can see that the `-l` option has modified the command and now our output has listed all the files in alphanumeric order, which can make finding a specific file easier.
It also includes information about the file size, time of its last modification, and permission and ownership information.

Most unix commands follow this basic structure.
![Structure of a Unix command](../fig/Unix_Command_Struc.svg)

The **prompt** tells us that the terminal is accepting inputs, prompts can be customised to show all sorts of info.

The **command**, what are we trying to do.

**Options** will modify the behavior of the command, multiple options can be specified.
Options will either start with a single dash (`-`) or two dashes (`--`)..
Often options will have a short and long format e.g. `-a` and `--all`.

**Arguments** tell the command what to operate on (usually files and directories).

Each part is separated by spaces: if you omit the space
between `ls` and `-l` the shell will look for a command called `ls-l`, which
doesn't exist. Also, capitalization can be important.
For example, `ls -s` will display the size of files and directories alongside the names,
while `ls -S` will sort the files and directories by size.

Another useful option for `ls` is the `-a` option, lets try using this option together with the -l option:

```
{{ site.remote.prompt }} ls -la
```
{: .language-bash}

```
total 1
drwxrws---+  4 usr001  nesi99991   4096 Nov 15 09:00 .
drwxrws---+ 12 root    nesi99991 262144 Nov 15 09:23 ..
-rw-r-----+  1 cwal219 nesi99991    460 Nov 18 17:03 array_sum.r
drwxrws---+  2 usr123  nesi99991   4096 Nov 15 09:01 usr123
drwxrws---+  2 usr345  nesi99991   4096 Nov 15 09:01 usr345
```
{: .output}

You might notice that we now have two extra lines for directories `.` and `..`. These are hidden directories which the `-a` option has been used to reveal, you can make any file or directory hidden by beginning their filenames with a `.`.

These two specific hidden directories are special as they will exist hidden inside every directory, with the `.` hidden directory representing your current directory and the `..` hidden directory representing the **parent** directory above your current directory.

> ## Exploring More `ls` Flags
>
> You can also use two options at the same time. What does the command `ls` do when used
> with the `-l` option? What about if you use both the `-l` and the `-h` option?
>
> Some of its output is about properties that we do not cover in this lesson (such
> as file permissions and ownership), but the rest should be useful
> nevertheless.
>
> > ## Solution
> > The `-l` option makes `ls` use a **l**ong listing format, showing not only
> > the file/directory names but also additional information, such as the file size
> > and the time of its last modification. If you use both the `-h` option and the `-l` option,
> > this makes the file size '**h**uman readable', i.e. displaying something like `5.3K`
> > instead of `5369`.
> {: .solution}
{: .challenge}

> ## Unsupported command-line options
>
> If you try to use an option (flag) that is not supported, `ls` and other commands
> will usually print an error message similar to:
>
> ```
> $ ls -j
> ```
> {: .language-bash}
>
> ```
> ls: invalid option -- 'j'
> Try 'ls --help' for more information.
> ```
> {: .error}
{: .callout}

## Relative paths

You may have noticed in the last command we did not specify an argument for the directory path.
Until now, when specifying directory names, or even a directory path (as above),
we have been using what are know **absolute paths**, which work no matter where you are currently located on the machine
since it specifies the full path from the top level root directory.

An **absolute path** always starts at the root directory, which is indicated by a
leading slash. The leading `/` tells the computer to follow the path from
the root of the file system, so it always refers to exactly one directory,
no matter where we are when we run the command.

Any path without a leading `/` is a **relative path**.

When you use a relative path with a command
like `ls` or `cd`, it tries to find that location from where we are,
rather than from the root of the file system.

In the previous command, since we did not specify an **absolute path** it ran the command on the relative path from our current directory
(implicitly using the `.` hidden directory), and so listed the contents of our current directory.

We will now navigate to the parent directory, the simplest way do do this is to use the relative path `..`.

```
{{ site.remote.prompt }} cd ..
```
{: .language-bash}

We should now be back in `{{ site.working_dir[0] }}`.

```
{{ site.remote.prompt }} pwd
```
{: .language-bash}

```
{{ site.working_dir[0] }}
```
{: .output}

> ## Two More Shortcuts
>
> The shell interprets a tilde (`~`) character at the start of a path to
> mean "the current user's home directory". For example, if Nelle's home
> directory is `/home/nelle`, then `~/data` is equivalent to
> `/home/nelle/`. This only works if it is the first character in the
> path: `here/there/~/elsewhere` is *not* `here/there/Users/nelle/elsewhere`.
>
> Another shortcut is the `-` (dash) character. `cd` will translate `-` into
> *the previous directory I was in*, which is faster than having to remember,
> then type, the full path.  This is a *very* efficient way of moving
> *back and forth between two directories* -- i.e. if you execute `cd -` twice,
> you end up back in the starting directory.
>
> The difference between `cd ..` and `cd -` is
> that the former brings you *up*, while the latter brings you *back*.
>
{: .callout}
> ## Absolute vs Relative Paths
>
> Starting from `/Users/amanda/data`,
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
> > 4. No: this command goes up two levels, i.e. ends in `/Users`.
> > 5. Yes: `~` stands for the user's home directory, in this case `/Users/amanda`.
> > 6. No: this command would navigate into a directory `home` in the current directory if it exists.
> > 7. Yes: unnecessarily complicated, but correct.
> > 8. Yes: shortcut to go back to the user's home directory.
> > 9. Yes: goes up one level.
> {: .solution}
{: .challenge}

> ## Relative Path Resolution
>
> Using the filesystem diagram below, if `pwd` displays `/Users/thing`,
> what will `ls ../backup` display?
>
> 1. `../backup: No such file or directory`
> 2. `2012-12-01 2013-01-08 2013-01-27`
> 3. `original pnas_final pnas_sub`
>
> ![A directory tree below the Users directory where "/Users" contains the
directories "backup" and "thing"; "/Users/backup" contains "original",
"pnas_final" and "pnas_sub"; "/Users/thing" contains "backup"; and
"/Users/thing/backup" contains "2012-12-01", "2013-01-08" and
"2013-01-27"](../fig/filesystem-challenge.svg)
>
> > ## Solution
> >
> > 1. No: there *is* a directory `backup` in `/Users`.
> > 2. No: this is the content of `Users/thing/backup`,
> >    but with `..`, we asked for one level further up.
> > 3. Yes: `../backup/` refers to `/Users/backup/`.
> >
> {: .solution}
{: .challenge}

> ## Clearing your terminal
>
> If your screen gets too cluttered, you can clear your terminal using the
> `clear` command. You can still access previous commands using <kbd>↑</kbd>
> and <kbd>↓</kbd> to move line-by-line, or by scrolling in your terminal.
{: .callout}

> ## Listing in Reverse Chronological Order
>
> By default, `ls` lists the contents of a directory in alphabetical
> order by name. The command `ls -t` lists items by time of last
> change instead of alphabetically. The command `ls -r` lists the
> contents of a directory in reverse order.
> Which file is displayed last when you combine the `-t` and `-r` flags?
> Hint: You may need to use the `-l` flag to see the
> last changed dates.
>
> > ## Solution
> >
> > The most recently changed file is listed last when using `-rt`. This
> > can be very useful for finding your most recent edits or checking to
> > see if a new output file was written.
> {: .solution}
{: .challenge}

## Tab completion

Sometimes file paths can also be very long, making typing out the path tedious.
One trick you can use to save yourself time is to use something called **tab completion**.
If you start typing the path in a command and their is only one possible match,
if you hit tab the path will autocomplete (until there are more than one possible matches).

For example, if you type:

```
{{ site.remote.prompt }} cd {{ site.working_dir[1] | slice: 0,3 }}
```
{: .language-bash}

and then press <kbd>Tab</kbd> (the tab key on your keyboard),
the shell automatically completes the directory name for you (since there is only one possible match):

```
{{ site.remote.prompt }} cd {{ site.working_dir[1] }}/
```
{: .language-bash}

However, that command would only take you `{{ working_dir[0] }}/{{ working_dir[0] }}`.
You want to move to your personal working directory. If you hit <kbd>Tab</kbd> once you will
likely see nothing change, as there are more than one possible options. Hitting <kbd>Tab</kbd>
a second time will print all possible autocomplete options.

```
cwal219/    riom/    harrellw/
```
{: .output}

Now entering in the first few characters of the path (just enough that the possible options are no longer ambiguous) and pressing <kbd>Tab</kbd> again, should complete the path.

Now press <kbd>Enter</kbd> to execute the command.

```
{{ site.remote.prompt }} cd {{ site.working_dir[1] }}/<username>
```
{: .language-bash}

Check that we've moved to the right place by running `pwd`.

```
{{ site.working_dir[0] }}/{{ site.working_dir[1] }}/<username>
```
{: .output}

## Create a text file

Now let's create a file. To do this we will use a text editor called Nano to create a file called `draft.txt`:

```
{{ site.remote.prompt }} nano draft.txt
```
{: .language-bash}

> ## Which Editor?
>
> When we say, '`nano` is a text editor' we really do mean 'text': it can
> only work with plain character data, not tables, images, or any other
> human-friendly media. We use it in examples because it is one of the
> least complex text editors. However, because of this trait, it may
> not be powerful enough or flexible enough for the work you need to do
> after this workshop. On Unix systems (such as Linux and macOS),
> many programmers use [Emacs](http://www.gnu.org/software/emacs/) or
> [Vim](http://www.vim.org/) (both of which require more time to learn),
> or a graphical editor such as
> [Gedit](http://projects.gnome.org/gedit/). On Windows, you may wish to
> use [Notepad++](http://notepad-plus-plus.org/).  Windows also has a built-in
> editor called `notepad` that can be run from the command line in the same
> way as `nano` for the purposes of this lesson.
>
> No matter what editor you use, you will need to know where it searches
> for and saves files. If you start it from the shell, it will (probably)
> use your current working directory as its default location. If you use
> your computer's start menu, it may want to save files in your desktop or
> documents directory instead. You can change this by navigating to
> another directory the first time you 'Save As...'
{: .callout}

Let's type in a few lines of text.
Once we're happy with our text, we can press <kbd>Ctrl</kbd>+<kbd>O</kbd>
(press the <kbd>Ctrl</kbd> or <kbd>Control</kbd> key and, while
holding it down, press the <kbd>O</kbd> key) to write our data to disk
(we'll be asked what file we want to save this to:
press <kbd>Return</kbd> to accept the suggested default of `draft.txt`).

<div style="width:80%; margin: auto;"><img alt="screenshot of nano text editor in action"
src="../fig/nano-screenshot.png"></div>

Once our file is saved, we can use <kbd>Ctrl</kbd>+<kbd>X</kbd> to quit the editor and
return to the shell.

> ## Control, Ctrl, or ^ Key
>
> The Control key is also called the 'Ctrl' key. There are various ways
> in which using the Control key may be described. For example, you may
> see an instruction to press the <kbd>Control</kbd> key and, while holding it down,
> press the <kbd>X</kbd> key, described as any of:
>
> * `Control-X`
> * `Control+X`
> * `Ctrl-X`
> * `Ctrl+X`
> * `^X`
> * `C-x`
>
> In nano, along the bottom of the screen you'll see `^G Get Help ^O WriteOut`.
> This means that you can use `Control-G` to get help and `Control-O` to save your
> file.
{: .callout}

`nano` doesn't leave any output on the screen after it exits,
but `ls` now shows that we have created a file called `draft.txt`:

```
{{ site.remote.prompt }} ls
```
{: .language-bash}

```
draft.txt
```
{: .output}
## Copying files and directories

In a future lesson, we will be running the R script ```{{ site.working_dir[0] }}/{{ site.working_dir[1] }}/array_sum.r```, but as we can't all work on the same file at once you will need to take your own copy. This can be done with the **c**o**p**y command `cp`, two arguments are needed the file (or directory) you want to copy, and the directory (or file) where you want the copy to be created. We will be copying the file into the directory we made previously, as this should be your current directory the second argument can be a simple `.`.

```
{{ site.remote.prompt }} cp {{ site.working_dir[0] }}/{{ site.working_dir[1] }}/array_sum.r .
```

We can check that it did the right thing using `ls`

```
{{ site.remote.prompt }} ls
```
{: .language-bash}

```
draft.txt   array_sum.r
```
{: .output}

We can also copy a directory and all its contents by using the
[recursive](https://en.wikipedia.org/wiki/Recursion) option `-r`,
e.g. to back up a directory:

Alternatively, if in the future you wish to move a file, rather than copy it, you can replace the `cp` command with `mv`.
If you wish to permanently delete a file or directory you can use the `rm` command, but be careful, as once the file or directory is deleted it cannot be recovered.

> ## Unsupported command-line options
>
> If you try to use an option (flag) that is not supported, `ls` and other commands
> will usually print an error message similar to:
>
> ```
> $ ls -j
> ```
> {: .language-bash}
>
> ```
> ls: invalid option -- 'j'
> Try 'ls --help' for more information.
> ```
> {: .error}
{: .callout}
## Getting help

Commands will often have many **options**. Most commands have a `--help` flag, as can be seen in the error above.  You can also use the manual pages (aka manpages) by using the `man` command. The manual page provides you with all the available options and their use in more detail. For example, for thr `ls` command:

```
{{ site.remote.prompt }} man ls
```
{: .language-bash}

```
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if neither -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options, too.
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
...        ...        ...
```
{: .output}

To navigate through the `man` pages,
you may use <kbd>↑</kbd> and <kbd>↓</kbd> to move line-by-line,
or try <kbd>B</kbd> and <kbd>Spacebar</kbd> to skip up and down by a full page.
To search for a character or word in the `man` pages,
use <kbd>/</kbd> followed by the character or word you are searching for.
Sometimes a search will result in multiple hits. If so, you can move between hits using <kbd>N</kbd> (for moving forward) and <kbd>Shift</kbd>+<kbd>N</kbd> (for moving backward).

To **quit** the `man` pages, press <kbd>Q</kbd>.
> ## Manual pages on the web
>
> Of course, there is a third way to access help for commands:
> searching the internet via your web browser.
> When using internet search, including the phrase `unix man page` in your search
> query will help to find relevant results.
>
> GNU provides links to its
> [manuals](http://www.gnu.org/manual/manual.html) including the
> [core GNU utilities](http://www.gnu.org/software/coreutils/manual/coreutils.html),
> which covers many commands introduced within this lesson.
{: .callout}

[Arguments]: https://swcarpentry.github.io/shell-novice/reference.html#argument
