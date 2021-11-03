---
layout: page
title: Setup
root: .
---


## NeSI JupyterHub Login

The easiest method for accessing the NeSI cluster is to use our JupyterHub service.  Below are the 
login and troubleshooting instructions for NeSI JupyterHub:

1. Follow this link: [https://jupyter.nesi.org.nz](https://jupyter.nesi.org.nz)
2. Enter your NeSI username, HPC password your 6 digit second factor token ![Login](/img/Login_jupyterhubNeSI.png)
3. Choose server options: the session project code should be *NeSI Training (nesi99991)*, Number of CPUs and memory size will remain unchanged. However, select the appropriate **Wall time** based on the projected length of a session ![Options](/img/ServerOptions_jupyterhubNeSI.png)
4. From Jupyter Launcher screen, choose Terminal (highlighted in red box) ![Terminal](/img/jupyterLauncher.png)

<br>

## Accessing the Cluster and Running Jobs

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

**Advantages:** Most flexible.  
