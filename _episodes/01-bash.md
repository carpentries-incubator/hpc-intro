---
title: "UNIX fundamentals: Connecting & BASH Basics 1"
teaching: 0
exercises: 0
questions:
- "How do I connect to an HPC system?"
- "How do I view files and move around on the system?"
- "Where can I store my files/data?"
objectives:
- "Be able to connect to a remote HPC system"
- "Be able to navigate the remote filesystem."
keypoints:
- "`ssh` is a common and powerful method for connecting to remote HPC systems."
- "`ls` is used to view the content of directories and `cd` is used to move around the directory structure."
- "scratch storage is temporary and should not be relied on for crucial data beyond a short period of time."
---

## Opening a Terminal

Connecting to an HPC system is most often done through a tool known as "SSH" (Secure SHell) and usually SSH is run through a terminal.  So, to begin using an HPC system we need to begin by opening a terminal.  Different operating systems have different terminals, none of which are exactly the same in terms of their features and abilities while working on the operating system.  When connected to the remote system the experience between terminals will be identical as each will faithfully present the same experience of using that system.

Here is the process for opening a terminal in each operating system.

### Linux  
There are many different versions (aka "flavours") of Linux and how to open a terminal window can change between flavours.  Fortunately most Linux users already know how to open a terminal window since it is a common part of the workflow for Linux users.  If this is something that you do not know how to do then a quick search on the Internet for "how to open a terminal window in" with your particular Linux flavour appended to the end should quickly give you the directions you need.

A very popular version of Linux is Ubuntu.  There are many ways to open a terminal window in Ubuntu but a very fast way is to use the terminal shortcut key sequence: Ctrl+Alt+T.

### Mac
Macs have had a terminal built in since the first version of OSX since it is built on a Linux flavour known as BSD (Berkeley Systems Designs).  The terminal can be quickly opened through the use of the Searchlight tool.  Hold down the command key and press the spacebar.  In the search bar that shows up type "terminal", choose the terminal app from the list of results (it will look like a tiny, black computer screen) and you will be presented with a terminal window.

### Windows
While Windows does have a command-line interface known as the "Command Prompt" that has its roots in MS-DOS (Microsoft Disk Operating System) it does not have an SSH tool built into it and so one needs to be installed.  There are a variety of programs that can be used for this, two common ones we describe here, as follows:

#### MobaXterm
MobaXterm is a terminal window emulator for Windows so 


#### PuTTy

ctrl-right-click to paste

## Terminal Basics

whoami

whereami

pwd

## Connecting to a Remote HPC System

SSH

PuTTy

## Navigating the System

pwd

ls

cd

home, scratch, and project