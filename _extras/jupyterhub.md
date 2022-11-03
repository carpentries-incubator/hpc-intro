---
layout: page
title: "JupyterHub"
permalink: /jupyter/
---

## NeSI JupyterHub Login

The easiest method for accessing the NeSI cluster is to use our JupyterHub service.  Below are the 
login and troubleshooting instructions for NeSI JupyterHub:

1. Follow this link: [https://jupyter.nesi.org.nz](https://jupyter.nesi.org.nz)
2. Enter your NeSI username, HPC password your 6 digit second factor token ![Login](/fig/Login_jupyterhubNeSI.png)
3. Choose server options: the session project code should be *NeSI Training ({{site.sched.project}})*, Number of CPUs and memory size will remain unchanged. However, select the appropriate **Wall time** based on the projected length of a session ![Options](/fig/ServerOptions_jupyterhubNeSI.png)
4. From Jupyter Launcher screen, choose Terminal (highlighted in red box) ![Terminal](/fig/jupyterLauncher.png)

<br>

<!-- ## SLURM and JupyterHub

All JupyterHub sessions run inside of a SLURM job, however as the sessions are interactive the resources available this way are very limited. In onder to access more resources you will still have to submit a SLURM job.

### Jupyter for Interactive work.
![Terminal](/fig/UsingJupyterHub2.svg)
In a web browser, navigate to [https://jupyter.nesi.org.nz](https://jupyter.nesi.org.nz), select the resource requirements *for your job*. Jobs are run interactively.  

**Best For:** New Users, Job and code tests and Jobs using < 4 CPUs and < 128GB

**Advantages:** Interactive, file explorer, no local setup required.
### Jupyter and SBATCH
![Terminal](/fig/UsingJupyterHub3.svg)
In a web browser, navigate to [https://jupyter.nesi.org.nz](https://jupyter.nesi.org.nz), select the resource requirements *for your session* (should only need minimal memory and CPU).  Jobs scripts are submitted using the `sbatch` command (non-interactive).  

**Best For:** New Users, Windows Users.  

**Advantages:** File explorer, no local setup required.
### SSH and SBATCH
![Terminal](/fig/UsingJupyterHub1.svg)
From your local computer, using an SSH client to connect to a shell session (interactive), running on the NeSI login Node. Jobs scripts are submitted using the `sbatch` command (non-interactive).  Instructions for SSH and command-line setup can be found in our documentation: [Accessing the HPCs](https://support.nesi.org.nz/hc/en-gb/sections/360000034315)

**Best For:** Users familiar with command line, Linux/Mac users.  

**Advantages:** Most flexible.   -->

## Plugins

### Rstudio

### MATLAB

### Virtual Desktop

### Queue Manager

## File transfer window

![Terminal](/fig/jupyter_ftw.png)

By default the file browser will be in a temporary hidden directory containing links to all of you projects and your home directory. Do-not create files here as they will be difficult to find later!

Note, the file browser is not linked at all to your terminal, changing your directory in one will not affect the other.

Files can be uploaded to the cluster by dragging from your local machine into the file transfer window.

## Text Editor

<kbd>ctrl</kbd> + <kbd>s</kbd> to save.