---
title: "HPC Jargon Buster"
author: "HPC Carpentry Team"
theme: "Copenhagen"
colortheme: "dolphin"
date: "February 1, 2022"
urlcolor: Blue
linkstyle: bold
---

# Your Personal Computer

![Standalone computers (banana for scale)](img/standalone_b_c.png){height=45%}

- Familiar starting point, accessed locally
- Good for local computational tasks
- Highly flexible, easy to reconfigure for new tasks

# Shared Computing Resources

![An HPC resource (img: [Julian Herzog](https://commons.wikimedia.org/wiki/File:High_Performance_Computing_Center_Stuttgart_HLRS_2015_07_Cray_XC40_Hazel_Hen_IO.jpg))](img/High_Performance_Computing_Center_Stuttgart_HLRS_2015_07_Cray_XC40_Hazel_Hen_IO.jpg){height=40%}

<!-- Image: https://commons.wikimedia.org/wiki/File:High_Performance_Computing_Center_Stuttgart_HLRS_2015_07_Cray_XC40_Hazel_Hen_IO.jpg, Julian Herzog. -->

- Large-scale computation is different
- It has a rich history, and confusing terminology
- Many terms overloaded

# A large computer

![A large computer (banana for scale)](img/large_computer_b_c.png){height=45%}

- More powerful "compute server"
- Accessed remotely, likely shared by a small group
- Less flexible -- need to accommodate other users


# Cloud Systems

![Cloud computers (bananas for scale)](img/multi_cluster_b.png){height=50%}

- Generally quite heterogeneous
- Many types of servers

# A cluster or supercomputer

![A cluster (banana for scale)](img/cluster_b_c.png){height=45%}

- Special "login node" or "head node" accessed remotely by users
- Compute service accessed via resource manager
- Some flexibility on local accounts
- Specially-built software for best performance

# HPC workflow

![Schematic HPC workflow](img/workflow_a.png){height=50%}

- You talk to the cluster head node
- The cluster head node distributes compute tasks
- You view results
