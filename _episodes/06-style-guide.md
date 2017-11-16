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
|  Pontuation mark  |                                                                    |      `<kbd>*</kbd>`      |
|-------------------+--------------------------------------------------------------------+--------------------------|
|     Function      |                 Capital F followed by the number.                  |     `<kbd>F12</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|        Alt        |                     Only first letter capital.                     |     `<kbd>Alt</kbd>`     |
|-------------------+--------------------------------------------------------------------+--------------------------|
|     Backspace     |                     Only first letter capital.                     |  `<kbd>Backspace</kbd>`  |
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
insert a plus sign **without sapce** between each one of the keys.
For example, "press <kbd>Ctrl</kbd>+<kbd>X</kbd> to quit nano" should be write as

~~~
press <kbd>Ctrl</kbd>+<kbd>X</kbd> to quit nano.
~~~
{: .html}

{% include links.md %}
