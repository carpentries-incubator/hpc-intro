---
title: "Scripts, variables, and loops"
teaching: 45
exercises: 10
questions:
- "How do I turn a set of commands into a program?"
objectives:
- "Write a shell scripts"
- "Understand and manipulate UNIX permissions"
- "Understand shell variables and how to use them"
- "Write a simple for loop"
keypoints:
- "A shell script is just a list of bash commands in a text file."
- "`chmod +x script.sh` will give it permission to execute."
---

We now know a whole bunch of UNIX commands. Wouldn't it be great if we could save certain commands so that we could run them later or not have to type them out again? As it turns out, this is extremely easy to do. Saving a list of commands to a file is called a "shell script". These shell scripts can be run whenever we want, and are a great way to automate our work.

So how do we write a shell script, exactly? It turns out we can do this with a simple text editor. Start editing a file called "demo.sh" (`nano demo.sh`). The ".sh" is simply the standard file extension for shell scripts that people use.

Our shell script will have two parts:  

* On the very first line, add `#!/bin/bash`. The `#!` (pronounced "hash-bang") tells our computer what program to run our script with. In this case, we are telling it to run our script with our command-line shell (what we've been doing everything in so far). If we wanted our script to be run with something else, like Python, we could add `#!/usr/bin/python`

* Now, anywhere below the first line, add `echo "Our script worked!"`. When our script runs, `echo` will happily print out `Our script worked!`.

Our file should now look like this:

```
#!/bin/bash

echo "Our script worked!"
```

Ready to run our program? There's one last thing we need to do. Before a file can be run, it needs "permission" to run. Let's look at our file's permissions with `ls -l` (remember this from earlier?).

```
$ ls -l
```
{: .bash}
```
-rw-r--r--. 1 jeff jeff        39 Jan 27 10:45 demo.sh
-rw-r-----. 1 jeff jeff    721242 Jan 25 11:09 dmel_unique_protein_isoforms_fb_2016_01.tsv
-rw-r--r--. 1 jeff jeff 159401627 Jan 20 14:32 Drosophila_melanogaster.BDGP5.77.gtf
drwxr-xr-x. 2 jeff jeff        18 Jan 25 13:53 fastq
-rw-r-----. 1 jeff jeff  56654230 Jan 25 11:09 fb_synonym_fb_2016_01.tsv
-rw-r-----. 1 jeff jeff   1830516 Jan 25 11:09 gene_association.fb.gz
-rw-r--r--. 1 jeff jeff        15 Jan 25 13:56 test.txt
-rw-r--r--. 1 jeff jeff       270 Jan 25 14:40 word_counts.txt
```
{: .output}

That's a huge amount of output. Let's see if we can understand what it is, working left to right.

+ **1st column - Permissions:** On the very left side, there is a string of the characters `d`, `r`, `w`, `x`, and `-`. The `d` simply indicates if something is a directory (there is a `-` in that spot if it is not a directory). The other `r`, `w`, `x` bits indicates permission to **R**ead **W**rite and e**X**ecute a file.**** There are three columns of `rwx` permissions following the spot for `d`. If a user is missing a permission to do something, it's indicated by a `-`.
    + The first column of `rwx` are the permissions that the owner has (the owner is indicated by jeff in the next column).
    + The second set of `rwx`s are permissions that other members of the owner's group share (indicated by jeff).
    + The third set of `rwx`s are permissions that anyone else with access to this computer can do with a file.

+ **2nd column - Owner:** This is the username of the user who owns the file. Their permissions are indicated in the first permissions column.

+ **3rd column - Group:** This is the user group of the user who owns the file. Members of this user group have permissions indicated in the second permissions column.

+ **4th column - Size of file:** This is simply the size of a file in bytes, or the number of files/subdirectories if we are looking at a directory.

+ **5th column - Date last modified:** This is the last date the file was modified.

+ **6th column - Filename:** Pretty self explanatory- this is the filename.

So how do we change permissions? As I mentioned earlier, we need permission to execute our script.

Changing permissions is done with `chmod`. To add executable permissions for all users we could use this:

```
$ chmod +x demo.sh
$ ls -l
```
{: .bash}
```
-rwxr-xr-x. 1 jeff jeff        39 Jan 27 10:45 demo.sh
-rw-r-----. 1 jeff jeff    721242 Jan 25 11:09 dmel_unique_protein_isoforms_fb_2016_01.tsv
-rw-r--r--. 1 jeff jeff 159401627 Jan 20 14:32 Drosophila_melanogaster.BDGP5.77.gtf
drwxr-xr-x. 2 jeff jeff        18 Jan 25 13:53 fastq
-rw-r-----. 1 jeff jeff  56654230 Jan 25 11:09 fb_synonym_fb_2016_01.tsv
-rw-r-----. 1 jeff jeff   1830516 Jan 25 11:09 gene_association.fb.gz
-rw-r--r--. 1 jeff jeff        15 Jan 25 13:56 test.txt
-rw-r--r--. 1 jeff jeff       270 Jan 25 14:40 word_counts.txt
```
{: .output}

Now that we have executable permissions for that file, we can run it. To run a script that we wrote ourselves, we need to specify the full path to the file, followed by the filename. We could do this one of two ways: either with our absolute path `/home/jeff/demo.sh`, or with the relative path `./demo.sh`.

```
$ ./demo.sh
```
{: .bash}
```
Our script worked!
```
{: .output}

Fantastic, we've written our first program! Before we go any further, let's learn how to take notes inside our program using comments. A comment is indicated by the `#` character, followed by whatever we want. Comments do not get run. Let's try out some comments in the console, then add one to our script!

```
# This wont show anything
```

Now lets try adding this to our script with `nano`. Edit your script to look something like this:

```
#!/bin/bash

# This is a comment... they are nice for making notes!
echo "Our script worked!"
```

When we run our script, the output should be unchanged from before!

## Shell variables

One important concept that we'll need to cover are shell variables. Variables are a great way of saving information under a name you can access later. In programming languages like Python and R, variables can store pretty much anything you can think of. In the shell, they usually just store text. The best way to understand how they work is to see them in action.

To set a variable, simply type in a name containing only letters, numbers, and underscores, followed by an `=` and whatever you want to put in the variable. Shell variable names are typically uppercase by convention.

```
$ VAR="This is our variable"
```
{: .bash}

To use a variable, prefix its name with a `$` sign. Note that if we want to simply check what a variable is, we should use echo (or else the shell will try to run the contents of a variable).

```
$ echo $VAR
```
{: .bash}
```
This is our variable
```
{: .output}

Let's try setting a variable in our script and then recalling its value as part of a command. We're going to make it so our script runs `wc -l` on whichever file we specify with `FILE`.

Our script:
```
#!/bin/bash

# set our variable to the name of our GTF file
FILE=Drosophila_melanogaster.BDGP5.77.gtf

# call wc -l on our file
wc -l $FILE
```

```
$ ./demo.sh
```
{: .bash}
```
471308 Drosophila_melanogaster.BDGP5.77.gtf
```
{: .output}

What if we wanted to do our little `wc -l` script on other files without having to change `$FILE` every time we want to use it? There is actually a special shell variable we can use in scripts that allows us to use arguments in our scripts (arguments are extra information that we can pass to our script, like the `-l` in `wc -l`).

To use the first argument to a script, simply use `$1` (the second argument is `$2`, and so on). Let's change our script to run `wc -l` on `$1` instead of `$FILE`. Note that we can also pass all of the arguments using `$@` (not going to use it in this lesson, but it's something to be aware of).

Our script:
```
#!/bin/bash

# call wc -l on our first argument
wc -l $1
```

```
$ ./demo.sh fb_synonym_fb_2016_01.tsv
```
{: .bash}
```
1304914 fb_synonym_fb_2016_01.tsv
```
{: .output}

Nice! One thing to be aware of when using variables: they are all treated as pure text. How do we save the output of an actual command like `ls -l`?

A demonstration of what doesn't work:
```
$ TEST=ls -l
```
```
-bash: -l: command not found
```
{: .error}

What does work:
```
TEST=$(ls -l)
echo $TEST
```
{: .bash}
```
total 214132 -rwxr-xr-x. 1 jeff jeff 57 Feb 1 12:20 demo.sh -rw-r-----. 1 jeff jeff 721242 Jan 25 11:09 dmel_unique_protein_isoforms_fb_2016_01.tsv -rw-r--r--. 1 jeff jeff 159401627 Jan 20 14:32 Drosophila_melanogaster.BDGP5.77.gtf drwxr-xr-x. 2 jeff jeff 18 Jan 25 13:53 fastq -rw-r-----. 1 jeff jeff 56654230 Jan 25 11:09 fb_synonym_fb_2016_01.tsv -rw-r-----. 1 jeff jeff 1830516 Jan 25 11:09 gene_association.fb.gz -rw-r--r--. 1 jeff jeff 15 Jan 25 13:56 test.txt -rw-r--r--. 1 jeff jeff 270 Jan 25 14:40 word_counts.txt
```
{: .output}

Note that everything got printed on the same line. This is a feature, not a bug, as it allows us to use $(commands) inside lines of script without triggering line breaks (which would end our line of code and execute it prematurely).

## Loops

To end our lesson on scripts, we are going to learn how to write a simple for-loop. This will let us do the same string of commands on every file in a directory (or other stuff of that nature).

for-loops generally have the following syntax:
```
#!/bin/bash

for VAR in first second third
do
    echo $VAR
done
```

When a for-loop gets run, the loop will run once for everything following the word `in`. In each iteration, the variable `$VAR` is set to a particular value for that iteration. In this case it will be set to `first` during the first iteration, `second` on the second, and so on. During each iteration, the code between `do` and `done` is performed.

Let's run the script we just wrote (I saved mine as `loop.sh`).
```
$ chmod +x loop.sh
$ ./loop.sh
```
{: .bash}
```
first
second
third
```
{: .output}

What if we wanted to loop over a shell variable, such as every file in the current directory? Shell variables work perfectly in for-loops.

```
#!/bin/bash

FILES=$(ls)
for VAR in $FILES
do
        echo $VAR
done
```
{: .bash}
```
demo.sh
dmel_unique_protein_isoforms_fb_2016_01.tsv
Drosophila_melanogaster.BDGP5.77.gtf
fastq
fb_synonym_fb_2016_01.tsv
gene_association.fb.gz
loop.sh
test.txt
word_counts.txt
```
{: .output}

There's actually even a shortcut to run on all files of a particular type, say all .tsv files:
```
#!/bin/bash

for VAR in *.tsv
do
        echo $VAR
done
```
{: .bash}
```
dmel_unique_protein_isoforms_fb_2016_01.tsv
fb_synonym_fb_2016_01.tsv
```
{: .output}

> ## Writing our own scripts and loops
> `cd` to our `fastq` directory from earlier and write a loop to print off the name and first read (top 4 lines) of every fastq file in that directory.
>
> Is there a way to only run the loop on fastq files ending in `_1.fastq`?
{: .challenge}

> ## Concatenating variables
> Concatenating (i.e. mashing together) variables is quite easy to do. Simply add whatever you want to concatenate to the beginning or end of the shell variable after enclosing it in `{}` characters.
>
> ```{.bash}
> FILE=stuff.txt
> echo ${FILE}.processed
> ```
> ```{.output}
> stuff.txt.processed
> ```
>
> Can you write a script that prints off the name of every file in a directory with ".example" added to it?
{: .challenge}

> ## Tricks for working with file extensions {.callout}
> Working with file extensions can be tough sometimes. Here are a couple examples that demonstrate how to retrieve various parts of a filename. You're not required to memorize these or anything, although they come in useful from time to time.
>
> ```
> FILE="example.tar.gz"
> echo "${FILE%%.*}"
> example
> echo "${FILE%.*}"
> example.tar
> echo "${FILE#*.}"
> tar.gz
> echo "${FILE##*.}"
> gz
> ```
> {: .bash}
{: .challenge}

> ## Special permissions {.challenge}
> What if we want to give different sets of users different permissions. `chmod` actually accepts special numeric codes instead of stuff like `chmod +x`. The numeric codes are as follows: read = 4, write = 2, execute = 1. For each user we will assign permissions based on the sum of these permissions (must be between 7 and 0).
>
> Let's make an example file and give everyone permission to do everything with it.
> ```
> touch example
> ls -l example
> chmod 777 example
> ls -l example
> ```
> {: .bash}
>
> How might we give ourselves permission to do everything with a file, but allow no one else to do anything with it.
{: .challenge}
