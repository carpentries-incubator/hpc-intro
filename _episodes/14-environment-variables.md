---
title: Environment Variables
teaching: 10
exercises: 5
questions:
- "How are variables set and accessed in the Unix shell?"
- "How can I use variables to change how a program runs?"
objectives:
- "Understand how variables are implemented in the shell"
- "Read the value of an existing variable"
- "Create new variables and change their values"
- "Change the behaviour of a program using an environment variable"
- "Explain how the shell uses the `PATH` variable to search for executables"
keypoints:
- "Shell variables are by default treated as strings"
- "Variables are assigned using \"`=`\" and recalled using the variable's name prefixed by \"`$`\""
- "Use \"`export`\" to make an variable available to other programs"
- "The `PATH` variable defines the shell's search path"
---

> ## Episode provenance
>
> This episode has been remixed from the
> [Shell Extras episode on Shell Variables](https://github.com/carpentries-incubator/shell-extras/blob/gh-pages/_episodes/08-environment-variables.md)
> and the [HPC Shell episode on scripts](https://github.com/hpc-carpentry/hpc-shell/blob/gh-pages/_episodes/05-scripts.md)
{: .callout}

The shell is just a program, and like other programs, it has variables.
Those variables control its execution,
so by changing their values
you can change how the shell behaves (and with a little more effort how other
programs behave).

Variables
are a great way of saving information under a name you can access later. In
programming languages like Python and R, variables can store pretty much
anything you can think of. In the shell, they usually just store text. The best
way to understand how they work is to see them in action.

Let's start by running the command `set` and looking at some of the variables
in a typical shell session:

~~~
$ set
~~~
{: .language-bash}

~~~
COMPUTERNAME=TURING
HOME=/home/vlad
HOSTNAME=TURING
HOSTTYPE=i686
NUMBER_OF_PROCESSORS=4
PATH=/Users/vlad/bin:/usr/local/git/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin
PWD=/home/vlad
UID=1000
USERNAME=vlad
...
~~~
{: .output}

As you can see, there are quite a few — in fact,
four or five times more than what's shown here.
And yes, using `set` to *show* things might seem a little strange,
even for Unix, but if you don't give it any arguments,
it might as well show you things you *could* set.

Every variable has a name.
All shell variables' values are strings,
even those (like `UID`) that look like numbers.
It's up to programs to convert these strings to other types when necessary.
For example, if a program wanted to find out how many processors the computer
had, it would convert the value of the `NUMBER_OF_PROCESSORS` variable from a
string to an integer.

## Showing the Value of a Variable

Let's show the value of the variable `HOME`:

~~~
$ echo HOME
~~~
{: .language-bash}

~~~
HOME
~~~
{: .output}

That just prints "HOME", which isn't what we wanted
(though it is what we actually asked for).
Let's try this instead:

~~~
$ echo $HOME
~~~
{: .language-bash}

~~~
/home/vlad
~~~
{: .output}

The dollar sign tells the shell that we want the *value* of the variable
rather than its name.
This works just like wildcards:
the shell does the replacement *before* running the program we've asked for.
Thanks to this expansion, what we actually run is `echo /home/vlad`,
which displays the right thing.

## Creating and Changing Variables

Creating a variable is easy — we just assign a value to a name using "="
(we just have to remember that the syntax requires that there are _no_ spaces
around the `=`!):

~~~
$ SECRET_IDENTITY=Dracula
$ echo $SECRET_IDENTITY
~~~
{: .language-bash}

~~~
Dracula
~~~
{: .output}

To change the value, just assign a new one:

~~~
$ SECRET_IDENTITY=Camilla
$ echo $SECRET_IDENTITY
~~~
{: .language-bash}

~~~
Camilla
~~~
{: .output}

## Environment variables

When  we ran the `set` command we saw there were a lot of variables whose names
were in upper case. That's because, by convention, variables that are also
available to use by _other_ programs are given upper-case names. Such variables
are called _environment variables_ as they are shell variables that are defined
for the current shell and are inherited by any child shells or processes.

To create an environment variable you need to `export` a shell variable. For
example, to make our `SECRET_IDENTITY` available to other programs that we call
from our shell we can do:

~~~
$ SECRET_IDENTITY=Camilla
$ export SECRET_IDENTITY
~~~
{: .language-bash}

You can also create and export the variable in a single step:

~~~
$ export SECRET_IDENTITY=Camilla
~~~
{: .language-bash}

> ## Using environment variables to change program behaviour
>
> Set a shell variable `TIME_STYLE` to have a value of `iso` and check this
> value using the `echo` command.
>
> Now, run the command `ls` with the option `-l` (which gives a long format).
>
> `export` the variable and rerun the `ls -l` command. Do you notice any
> difference?
>
> > ## Solution
> >
> > The `TIME_STYLE` variable is not _seen_ by `ls` until is exported, at which
> > point it is used by `ls` to decide what date format to use when presenting
> > the timestamp of files.
> >
> {: .solution}
{: .challenge}

You can see the  complete set of environment variables in your current shell
session with the command `env` (which returns a subset of what the command
`set` gave us). **The complete set of environment variables is called
your _runtime environment_ and can affect the behaviour of the programs you
run**.

{% include {{ site.snippets }}/scheduler/print-sched-variables.snip %}

To remove a variable or environment variable you can use the `unset` command,
for example:

~~~
$ unset SECRET_IDENTITY
~~~
{: .language-bash}

## The `PATH` Environment Variable

Similarly, some environment variables (like `PATH`) store lists of values.
In this case, the convention is to use a colon ':' as a separator.
If a program wants the individual elements of such a list,
it's the program's responsibility to split the variable's string value into
pieces.

Let's have a closer look at that `PATH` variable.
Its value defines the shell's search path for executables,
i.e., the list of directories that the shell looks in for runnable programs
when you type in a program name without specifying what directory it is in.

For example, when we type a command like `analyze`,
the shell needs to decide whether to run `./analyze` or `/bin/analyze`.
The rule it uses is simple:
the shell checks each directory in the `PATH` variable in turn,
looking for a program with the requested name in that directory.
As soon as it finds a match, it stops searching and runs the program.

To show how this works,
here are the components of `PATH` listed one per line:

~~~
/Users/vlad/bin
/usr/local/git/bin
/usr/bin
/bin
/usr/sbin
/sbin
/usr/local/bin
~~~
{: .output}

On our computer,
there are actually three programs called `analyze`
in three different directories:
`/bin/analyze`,
`/usr/local/bin/analyze`,
and `/users/vlad/analyze`.
Since the shell searches the directories in the order they're listed in `PATH`,
it finds `/bin/analyze` first and runs that.
Notice that it will *never* find the program `/users/vlad/analyze`
unless we type in the full path to the program,
since the directory `/users/vlad` isn't in `PATH`.

This means that I can have executables in lots of different places as long as
I remember that I need to to update my `PATH` so that my shell can find them.

What if I want to run two different versions of the same program?
Since they share the same name, if I add them both to my `PATH` the first one
found will always win.
In the next episode we'll learn how to use helper tools to help us manage our
runtime environment to make that possible without us needing to do a lot of
bookkeeping on what the value of `PATH` (and other important environment
variables) is or should be.

{% include links.md %}
