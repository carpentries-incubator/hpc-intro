# Jargon Buster Presentation Files

## What is this?

The material in this directory is meant to comprise a 
short presentation to familiarize learners with a few
ways in which computing can be scaled up.

The idea is to present a variety of scale-up schemes,
and clarify the use of terms like "server" and "node"
in these various contexts.

## Mechanics

The material here is not intended to be rendered into the 
lesson, rather it's meant to be stand-alone.

The current version just consists of a few slides, with
some notes for the presenter. 

The scheme is meant to work with the `pdfpc` presentation
tool.  The idea is that you would create a PDF presentation
from the source `hpc_jargon.txt` file, and then present it
with `pdfpc` and read the notes.

In the below workflow example, the `pdfpc` tool is used 
in "windowed" mode, with the idea that the audience window
would be shared to a video teleconference presentattion,
and the presenter console would be viewable by the presenter,
with the timer and notes so that content does not get missed.

```
$ pandoc -t beamer hpc_jargon.txt -o hpc_jargon.pdf
$ pdfpc -w hpc_jargon.pdf
```
