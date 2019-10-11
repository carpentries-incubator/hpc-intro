---
title: "Style Guide"
teaching: 10
exercises: 0
questions:
- "How are keyboard key combinations written?"
objectives:
- "Explain keyboard key combination."
keypoints:
- "Keyboard keys need to use `<kbd>` HTML tag."
---

## Emphasis

Markdown treats asterisks (_*_) indicators of emphasis,
and renders text marked up like this in italics.
We use emphasis

- to highlight a word, phrase, or character where it is itself the object of discussion.

  For example,

  ~~~
  We want to output the lines that do not contain the word *the*.
  ~~~
  {: .source}

  This is preferable instead of the use of quotation marks.

  See the "Keyboard Key" section for characters or keyboard keys that the learn should type.

- for words and phrases that are still regarded as unfamiliar.
- for titles of books, periodicals, plays, films, TV, radio series, and music albums.

  For example,

  ~~~
  We will use a file that contains three haikus taken from a 1998 competition in *Salon* magazine.
  ~~~
  {: .source}

## Strong Emphasis

Markdown treats double asterisks (_**_) as indicators of strong emphasis,
and renders text marked up like this in boldface.
We use strong emphasis

- to highlight a newly introduced term, often one that is going to be defined or explained.
  For example,

  ~~~
  We are all familiar with **graphical user interfaces**
  ~~~
  {: .source}

## Span of Code

Markdown treats backtick quotes (_\`_) as indicators of a span of code.
We use span of code

- to highlight part of some code where it is itself the object of discussion.

  For example,

  ~~~
  For example, `range(3, 10, 2)` produces
  ~~~
  {: .source}
- to highlight one command where it is itself the object of discussion.

  For example,

  ~~~
  you can run it by opening a terminal and typing `bash`.
  ~~~
  {: .source}

  When the object of discussion is the program or language in a broad sense,
  we don't use span of code. For example,

  ~~~
  The most popular Unix shell is Bash.
  ~~~
  {: .source}
- to highlight one function where it is itself the object of discussion.

  For example,

  ~~~
  `len` is much faster than any function we could write ourselves.
  ~~~
  {: .source}
- to highlight one file name where it is itself the object of discussion.

  For example,

  ~~~
  `my_file.txt` can also be viewed in your GUI file explorer.
  ~~~
  {: .source}
- to highlight any sequence of character that the user is expected to type.

## Keyboard Key

When making reference to a keyboard key that the reader should press
the HTML tag `<kbd>` **must** be used to enclose the key label.
For example, "to delete the cell press <kbd>D</kbd>" should be write as

~~~
to delete the cell press <kbd>D</kbd>
~~~
{: .html}

The table below covers most of the keyboard key labels.

|-------------------+--------------------------------------------------------------------+--------------------------|
|   Keyboard key    |                             Style Note                             |         Example          |
|-------------------+--------------------------------------------------------------------+--------------------------|
|      Letters      |                          Always capital.                           |      `<kbd>A</kbd>`      |
|-------------------+--------------------------------------------------------------------+--------------------------|
|      Numbers      |                                                                    |      `<kbd>1</kbd>`      |
|-------------------+--------------------------------------------------------------------+--------------------------|
|  Punctuation mark |                                                                    |      `<kbd>*</kbd>`      |
|-------------------+--------------------------------------------------------------------+--------------------------|
|     Function      |                 Capital F followed by the number.                  |     `<kbd>F12</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|        Alt        |                     Only first letter capital.                     |     `<kbd>Alt</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|     Backspace     |                     Only first letter capital.                     |  `<kbd>Backspace</kbd>`  |
|-------------------+--------------------------------------------------------------------+--------------------------|
|      Command      |                     Only first letter capital.                     |   `<kbd>Command</kbd>`   |
|-------------------+--------------------------------------------------------------------+--------------------------|
|       Ctrl        |                     Only first letter capital.                     |    `<kbd>Ctrl</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|      Delete       |                     Only first letter capital.                     |   `<kbd>Delete</kbd>`    |
|-------------------+--------------------------------------------------------------------+--------------------------|
|        End        |                     Only first letter capital.                     |     `<kbd>End</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|        Esc        |                     Only first letter capital.                     |     `<kbd>Esc</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|       Home        |                     Only first letter capital.                     |    `<kbd>Home</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|      Insert       |                     Only first letter capital.                     |   `<kbd>Insert</kbd>`    |
|-------------------+--------------------------------------------------------------------+--------------------------|
|     Page Down     |                            Use "PgDn".                             |    `<kbd>PgDn</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|      Page Up      |                            Use "PgUp".                             |    `<kbd>PgUp</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|   Print Screen    |                           Use "PrtScr".                            |   `<kbd>PrtScr</kbd>`    |
|-------------------+--------------------------------------------------------------------+--------------------------|
|      Return       |   Only first letter capital. We use "Return" instead of "Enter".   |   `<kbd>Return</kbd>`    |
|-------------------+--------------------------------------------------------------------+--------------------------|
|       Shift       |                     Only first letter capital.                     |    `<kbd>Shift</kbd>`    |
|-------------------+--------------------------------------------------------------------+--------------------------|
|      Spacebar     |                     Only first letter capital.                     |  `<kbd>Spacebar</kbd>`   |
|-------------------+--------------------------------------------------------------------+--------------------------|
|        Tab        |                     Only first letter capital.                     |     `<kbd>Tab</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|    Down arrow     |               Use Unicode "Downwards arrow" (8595).                |      `<kbd>↓</kbd>`      |
|-------------------+--------------------------------------------------------------------+--------------------------|
|    Left arrow     |               Use Unicode "Leftwards arrow" (8592).                |      `<kbd>←</kbd>`      |
|-------------------+--------------------------------------------------------------------+--------------------------|
|    Right arrow    |               Use Unicode "Rightwards arrow" (8594).               |      `<kbd>→</kbd>`      |
|-------------------+--------------------------------------------------------------------+--------------------------|
|     Up arrow      |                Use Unicode "Upwards arrow" (8593).                 |      `<kbd>↑</kbd>`      |
|-------------------+--------------------------------------------------------------------+--------------------------|

## Keyboard Key Combination

When making reference to a keyboard key combination that the reader should press,
insert a plus sign **without space** between each one of the keys.
For example, "press <kbd>Ctrl</kbd>+<kbd>X</kbd> to quit nano" should be written as:

~~~
press <kbd>Ctrl</kbd>+<kbd>X</kbd> to quit nano.
~~~
{: .html}


## Links

Please label links with meaningful texts, in order to [improve
accessibility](https://webaccess.berkeley.edu/ask-pecan/click-here). Please avoid
`click here` or similar.

## Menu Items

Use double quotes for menu and submenu items. For multiple menu and submenu options in a sequence, use the right angle bracket or greater than sign.

e.g.:

"Help" > "Check for updates"  

## Title Casing

Lesson and episode titles should be written in title case e.g.

> Saving the World, One Commit at a Time

An exception should be made where the title includes the name of a tool/library/command that must be typed in lower case when used, e.g.

> Data Visualisation with `matplotlib`

(In HTML files, such as the workshop schedule and syllabus files in the [workshop webpage template](https://github.com/carpentries/workshop-template), tool/command/library names such as `matplotlib` in the example above can be correctly formatted using `<code></code>` tags.)

{% include links.md %}
