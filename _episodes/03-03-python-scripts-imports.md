---
title: "Python introduction: Writing our first program"
teaching: 15
exercises: 5
questions:
- "Scripts and imports"
objectives:
- "Learn how to create and run our first Python programs"
- "Understand the concept of a working directory"
- "Understand how to import a library"
- "Learn several basic ipython commands"
keypoints:
- "A Python program is any text file with valid Python syntax"
- "`Ctrl+Enter` executes a line in Spyder"
- "ipython provides several extra commands to make things easier"
---

## What is a program?

Everything we've learned so far is pretty cool. 
But if we want to run a set of commands more than once?
How do we write a program in Python?

Python programs are simply a set of Python commands saved in a file.
No compiling required!
To demonstrate this, let's write our first program! 
In Rodeo, open a new file (File -> New) - 
You will notice a new file is opened in a pane that we have previously ignored: the editor (top-left).
Enter the following text in the editor and save it under any name you like 
(Python files are typically given the extension `.py`).

```
print('it works!!!')
```
{: .python}

We can now run this program in several ways.
The easiest, of course, is to click the `Run Script` button.

```
it works!!!
```
{: .output}

Note that we can run things line-by-line.
If we were to change our program to the following, we can run each line with `Ctrl+Enter`

```
print('it works!!!')
print('this is line 2')
```
{: .python}
```
it works!!!
this is line 2
```
{: .output}

> ## What's the point of `print()`?
>
> We saw earlier that there was no difference between printing something with `print()`
> and just entering a command on the command line.
> But is this really the case?
> Is there a difference after all?
>
> Try executing the following code:
> 
> ```
> print('this involves print')
> 'this does not'
> ```
> {: .python}
>
> What gets printed if you execute this as a script?
> What gets printed if you execute things line by line in Rodeo?
> Using this information, what's the point of `print()`?
>
{: .challenge}

## `import`-ing things

We can also run our script from the command line. 
If we were to open up a terminal in the folder where we had saved our program, 
we could run the command `python3 our-script-name.py` to run it.
IPython (what is running in Rodeo's consol) 
has a neat trick we can use to test this out.
Any command that begins with `!` gets run on your computer's command line,
and not the IPython terminal.

We can use this fact to run the command `python3 our-script-name.py`.
I've called my script `test.py` as an example.

```
!python3 test.py
```
{: .python}

```
it works!!!
this is line 2
```
{: .output}

What if we wanted to pass additional information to Python?
For example, what if we want Python to print whatever we type back at us?
To do this, we'll need to use a bit of extra functionality:
the `sys` package.

Python includes a lot of extra features in the form of packages, 
but not all of them get loaded by default.
To access a package, we need to `import` it.

```
import sys
```
{: .python}

You'll notice that there's no output.
Only one thing is changed:
We can now use the bonuses provided by the `sys` package.
For now, all we will use is `sys.argv`.
`sys.argv` is a special variable 
that stores any additional arguments we provide on the command-line
after `python3 our-script-name.py`.
Let's make a new script called `command-args.py` to try this out.

{% highlight python %}
import sys

print('we typed: ', sys.argv)
{% endhighlight %}

What happens when we run this script?

```
!python3 test.py word1 word2 3
```
{: .python}

```
we typed: ['test.py', 'word1', 'word2', '3']
```
{: .output}

You'll notice that sys.argv looks different from other data types we've seen so far.
`sys.argv` is a list (more about this in the next session).
