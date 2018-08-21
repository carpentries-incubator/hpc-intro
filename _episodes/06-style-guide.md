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

  This is preferable instead of the use of quotation marks.

  See the "Keyboard Key" section for characters or keyboard keys that the learn should type.
  
- for words and phrases that are still regarded as unfamiliar.
- for titles of books, periodicals, plays, films, TV, radio series, and music albums.

  For example,

  ~~~
  We will use a file that contains three haikus taken from a 1998 competition in *Salon* magazine.
  ~~~

## Strong Emphasis

Markdown treats double asterisks (_**_) as indicators of strong emphasis,
and renders text marked up like this in boldface.
We use strong emphasis

- to highlight a newly introduced term, often one that is going to be defined or explained.
  For example,

  ~~~
  We are all familiar with **graphical user interfaces**
  ~~~

## Span of Code

Markdown treats backtick quotes (_\`_) as indicators of a span of code.
We use span of code

- to highlight part of some code where it is itself the object of discussion.

  For example,

  ~~~
  For example, `range(3, 10, 2)` produces
  ~~~
- to highlight one command where it is itself the object of discussion.

  For example,

  ~~~
  you can run it by opening a terminal and typing `bash`.
  ~~~

  When the object of discussion is the program or language in a broad sense,
  we don't use span of code. For example,

  ~~~
  The most popular Unix shell is Bash.
  ~~~
- to highlight one function where it is itself the object of discussion.

  For example,

  ~~~
  `len` is much faster than any function we could write ourselves.
  ~~~
- to highlight one file name where it is itself the object of discussion.

  For example,

  ~~~
  `my_file.txt` can also be viewed in your GUI file explorer.
  ~~~
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
|   Print Screen    |                           Use "PtrScr".                            |   `<kbd>PtrScr</kbd>`    |
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

{% include links.md %}
