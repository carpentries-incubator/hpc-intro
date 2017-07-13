---
title: "Python introduction: Hello world!"
teaching: 15
exercises: 5
questions:
- "Getting started with Python"
objectives:
- "Learn what Python is and what it is good at"
- "Learn what Anaconda is"
- "Understand the concept of a 'working directory'"
- "Know how to start a new project"
keypoints:
- "Anaconda is a Python software bundle"
- "Python 2 and 3 are incompatible" 
- "We are learning Python 3"
- "Spyder is a coding tool that makes coding in Python easier"
- "A project is simply a folder with your files in it"
- "print()"
---

> ## Somewhat inspirational quote
>
> "Laziness is a programmer's main virtue."
>
> \-- Larry Wall (the guy who wrote Perl)
{: .testimonial}

Programming languages are time-saving devices.
They allow you to you do more work with less effort. 
In many cases, programming languages allow you to do new things!
You've likely run into situations where software doesn't do quite what you want it to, 
or perhaps the software you need doesn't even exist yet.
Python is a tool that will make your life easier.

Python is one of the most widely-used languages in use today.
It owes this success to many factors, but we've listed the most important ones here:

* It's free
* (Relatively) easy to learn
* Runs on any computer, anywhere
* No need to compile anything
* Versatile - most anything involving a computer can be done with Python
* It's open-source. You can see exactly how it works and what's going on behind the scenes.

## Anaconda

[Anaconda](https://www.continuum.io/downloads) is a distribution of Python.
There are a lot of competing versions of Python out there, and Anaconda is one of them.
We've chosen to use Anaconda for this workshop for two reasons: 
it behaves the same regardless of operating system, 
and it includes the most important add-ons to the language by default.
Anaconda also includes a "package manager" which lets you install new add-ons ("packages") with minimal effort.

### Python 2 vs. Python 3

When Python 3 was released, it broke compatibility with Python 2. 
There are no good reasons to learn Python 2 instead of Python 3 aside from backwards compatibility.
This workshop focuses on teaching Python 3, as it is what modern programmers use. 

## Spyder

Spyder is what's known as an IDE ("Integrated Development Environment"). 
IDE's are tools that make your life easier while you program. 
In particular, Spyder will let us write and run code more easily, 
view suggestions & help as we type, and let us "see" what we are doing (this will make more sense later).

> ## Other Python IDEs
> 
> There are a lot of different ways to program in Python.
> If you don't like Spyder, you may like one of these:
>
> * [PyCharm](https://www.jetbrains.com/pycharm/) - PyCharm checks your code for errors as you type (called "code linting") and includes a fantastic debugger. Probably overkill for most projects, but it's a great tool.
> * [Visual Studio Code (with Python extension)](http://code.visualstudio.com) - VSCode is a lightweight editor with great autocomplete and code linting. Works great.
> * [Jupyter Notebook](https://jupyter.org) - If you'd rather write code as a report, Jupyter Notebooks may be the tool for you.
{: .callout}

To start Spyder, just type `spyder` at a command-prompt.
Upon opening Spyder, you will see a screen that looks something like this. 

`image should go here`

There are 3 main "panes" to the interface (you can drag the panes to resize them):

* IPython console (bottom right) - This is an interactive Python command-line. You can type whatever you want here, and it will be run.
* Editor (left side) - This is where we will write Python scripts and programs. Pressing, `Ctrl+Enter` (`Cmd+Enter` on OSX) will run the currently-selected line of code in the terminal below.
* Variable Explorer/Project Explorer/Help - As we define variable and functions (more on this later!), they will appear in the "Variable Explorer" tab. "Project Explorer" lets you view your current directory, and "Help" displays documentation as we look things up!

> ## Configuring 
>
> There is a toolbar along the top and a sidebar with tutorials and settings along the right side. 
> See if you can figure out how to change Rodeo's editor theme and font size in the settings (can be done using either the top toolbar or sidebar).
> 
> Hint: the editor colors are found under `Editor -> Theme` and the font size is found under `Global`.
{: .challenge}

## Our first line of code

In the "Terminal" (lower-left side), enter the following command:

```
print('Everything works!')
```
{: .python}

```
Everthing works!
```
{: .output}

So what did we just do?

We just ran the `print()` command. 
`print()` simply takes whatever text or code is between the parentheses and prints it back to us.
The apostrophes are used to mark text as a word in Python. 
We will cover this more in-depth in the next section.

> ## Instructor's Note
>
> Do not proceed to the next section until *everyone* has successfully run `print('Everything works!')` in Spyder.
>
{: .callout}


