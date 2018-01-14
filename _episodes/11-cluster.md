---
title: "Working on a cluster"
teaching: 15
exercises: 10
questions:
- "What is a cluster?"
- "How does a cluster work?"
- "How do I log on to a cluster?"
objectives:
- "Connect to a cluster."
- "Understand the general cluster architecture."
keypoints:
- "A cluster is a set of networked machines."
- "Clusters typically provide a login node and a set of worker nodes."
- "Files saved on one node are available everywhere."
---

The words "cloud", "cluster", and "high-performance computing" get thrown around a lot.
So what do they mean exactly?
And more importantly, how do we use them for our work?

The "cloud" is a generic term commonly used to refer to remote computing resources.
Cloud can refer to webservers, remote storage, API endpoints, and as well as more traditional "raw compute" resources. 
A cluster on the other hand, is a term used to describe a network of compters.
Machines in a cluster typically share a common purpose, 
and are used to accomplish tasks that might otherwise be too substantial for any one machine. 

![The cloud is made of Linux](../files/linux-cloud.jpg)

## Where are we? 

Very often, many users are tempted to think of a high-performance computing installation as one giant, magical machine.
Sometimes, people even assume that the machine they've logged onto is the entire computing cluster.
So what's really happening? What machine have we logged on to?
The name of the current computer we are logged onto can be checked with the `hostname` command.
(Clever users will notice that the current hostname is also part of our prompt!)

```
hostname
```
{: .bash}
```
gra-login3
```
{: .output}

Clusters have different types of machines customized for different types of tasks.
In this case, we are on a login node.
A login node serves as a gateway to the cluster and serves as a single point of access.
As a gateway, it is well suited for uploading and downloading files, setting up software, and running quick tests.
It should never be used for doing actual work.

The real work on a cluster gets done by the "worker" nodes.
Worker nodes come in many shapes and sizes, but generally are dedicated to doing all of the heavy lifting that needs doing. 
All interaction with the worker nodes is handled by a specialized piece of software called a scheduler (called SLURM, in this case). 
We can view all of the worker nodes with the `sinfo` command.

```
sinfo
```
{: .bash}
```
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
compute*     up 7-00:00:00      1 drain* gra259
compute*     up 7-00:00:00     11  down* gra[8,99,211,268,376,635,647,803,852,966,986]
compute*     up 7-00:00:00      1   drng gra272
compute*     up 7-00:00:00     31   comp gra[988-991,994-1002,1006-1007,1015,1017,1021-1022,1028-1033,1037-1041,1043]
compute*     up 7-00:00:00     33  drain gra[225-251,253-256,677,1026]
compute*     up 7-00:00:00    323    mix gra[7,13,25,41,43-44,56,58-77,107-108,112-113,117,125-126,163,168-169,173,180-203,205-210,220,224,257-258,300-317,320,322-349,385-387,398,400-428,448,452,460,528-529,540-541,565-601,603-606,618,622-623,628,643-646,652,657,660,665,678-699,710-711,713-728,734-735,737,741-751,753-755,765,767,774,776,778,796-798,802,805-812,827,830,832,845-846,853,856,865-866,872,875,912,914,916-917,925,928,930,934,953-954,959-960,965,969-971,973,1004,1008-1009,1011,1013-1014,1023-1025]
compute*     up 7-00:00:00    464  alloc gra[1-6,9-12,14-19,21-24,26-40,42,45-55,57,100-106,109-111,114-116,118-122,127,164-167,174-179,204,212-219,221-223,252,260-267,269-271,273-284,318-319,321,350-375,377-384,388-397,399,453-459,461-501,526-527,530-539,542-564,607-608,629-634,636-642,648-651,653-656,658-659,661-664,666-676,700-703,738,756-764,766,768-773,804,813-826,828-829,831,833-844,847-851,854-855,857-864,867-871,873-874,876-911,913,915,918-924,926-927,929,931-933,935-936,938-952,955-958,961-964,967-968,972,974-985,987,992-993,1003,1005,1010,1012,1016,1018-1020,1027,1034-1036,1042]
compute*     up 7-00:00:00    176   idle gra[78-98,123-124,128-162,170-172,285-299,429-447,449-451,502-525,602,609-617,619-621,624-627,704-709,712,729-733,736,739-740,752,775,777,779-795,799-800]
compute*     up 7-00:00:00      3   down gra[20,801,937]
```
{: .output}

There are also specialized machines used for managing disk storage, user authentication, 
and other infrastructure-related tasks. 
Although we do not interact with these directly, 
but these enable a number of key features like ensuring our user account and files are available throughout the cluster.
This is an important point to remember: 
files saved on one node (computer) are available everywhere on the cluster!
