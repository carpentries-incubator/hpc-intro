---
title: Learner Reference
---

### Quick Reference or "Cheat Sheets" for Queuing System Commands

Search online for the one that fits you best, but here's some to start:

- [Slurm summary](https://slurm.schedmd.com/pdfs/summary.pdf) from SchedMD
- [Torque/PBS
  summary](https://gif.biotech.iastate.edu/torque-pbs-job-management-cheat-sheet)
  from Iowa State
- [Translating between Slurm and
  PBS](https://www.msi.umn.edu/slurm/pbs-conversion) from University of
  Minnesota

### Units and Language

A computer's memory and disk are measured in units called *Bytes* (one Byte is
8 bits). As today's files and memory have grown to be large given historic
standards, volumes are noted using the
[SI](https://en.wikipedia.org/wiki/International_System_of_Units) prefixes. So
1000 Bytes is a Kilobyte (kB), 1000 Kilobytes is a Megabyte (MB), 1000
Megabytes is a Gigabyte (GB), etc.

History and common language have however mixed this notation with a different
meaning. When people say "Kilobyte", they mean 1024 Bytes instead. In that
spirit, a Megabyte is 1024 Kilobytes.

To address this ambiguity, the [International System of
Quantities](https://en.wikipedia.org/wiki/International_System_of_Quantities)
standardizes the *binary* prefixes (with base of 2<sup>10</sup>\=1024) by the
prefixes Kibi (ki), Mebi (Mi), Gibi (Gi), etc. For more details, see
[an explanation on Wikipedia](https://en.wikipedia.org/wiki/Binary_prefix).

### "No such file or directory" or "symbol 0096" Errors

`scp` and `rsync` may throw a perplexing error about files that very much do
exist. One source of these errors is copy-and-paste of command line arguments
from Web browsers, where the double-dash string `--` is rendered as an em-dash
character "—" (or en-dash "–", or horizontal bar `―`). For example,
instead of showing the transfer rate in real time, the following command fails
mysteriously.

```bash
$ rsync —progress my_precious_data.txt user@host
rsync: link_stat "/home/user/—progress" failed:
No such file or directory (2)
rsync error: some files/attrs were not transferred (see previous errors)
(code 23) at main.c(1207) [sender=3.1.3]
```

The correct command, different only by two characters, succeeds:

```bash
$ rsync --progress my_precious_data.txt user@host
```

We have done our best to wrap all commands in code blocks, which prevents this
subtle conversion. If you encounter this error, please open an issue or pull
request on the lesson repository to help others avoid it.

### Transferring Files Interactively With `sftp`

`scp` is useful, but what if we don't know the exact location of what we want
to transfer? Or perhaps we're simply not sure which files we want to transfer
yet. `sftp` is an interactive way of downloading and uploading files. Let's
connect to a cluster, using `sftp` -- you'll notice it works the same way
as SSH:

```bash
$ sftp user@host
```

This will start what appears to be a bash shell (though our prompt says
`sftp>`). However we only have access to a limited number of commands. We can
see which commands are available with `help`:

```bash
sftp> help
```

```output
Available commands:
bye                                Quit sftp
cd path                            Change remote directory to 'path'
chgrp grp path                     Change group of file 'path' to 'grp'
chmod mode path                    Change permissions of file 'path' to 'mode'
chown own path                     Change owner of file 'path' to 'own'
df [-hi] [path]                    Display statistics for current directory or
                                   filesystem containing 'path'
exit                               Quit sftp
get [-afPpRr] remote [local]       Download file
reget [-fPpRr] remote [local]      Resume download file
reput [-fPpRr] [local] remote      Resume upload file
help                               Display this help text
lcd path                           Change local directory to 'path'
lls [ls-options [path]]            Display local directory listing
lmkdir path                        Create local directory
ln [-s] oldpath newpath            Link remote file (-s for symlink)
lpwd                               Print local working directory
ls [-1afhlnrSt] [path]             Display remote directory listing

# omitted further output for clarity
```

Notice the presence of multiple commands that make mention of local and remote.
We are actually connected to two computers at once (with two working
directories!).

To show our remote working directory:

```bash
sftp> pwd
```

```output
Remote working directory: /global/home/yourUsername
```

To show our local working directory, we add an `l` in front of the command:

```bash
sftp> lpwd
```

```output
Local working directory: /home/jeff/Documents/teaching/hpc-intro
```

The same pattern follows for all other commands:

- `ls` shows the contents of our remote directory, while `lls` shows our local
  directory contents.
- `cd` changes the remote directory, `lcd` changes the local one.

To upload a file, we type `put some-file.txt` (tab-completion works here).

```bash
sftp> put config.toml
```

```output
Uploading config.toml to /global/home/yourUsername/config.toml
config.toml                                  100%  713     2.4KB/s   00:00
```

To download a file we type `get some-file.txt`:

```bash
sftp> get config.toml
```

```output
Fetching /global/home/yourUsername/config.toml to config.toml
/global/home/yourUsername/config.toml        100%  713     9.3KB/s   00:00
```

And we can recursively put/get files by just adding `-r`. Note that the
directory needs to be present beforehand.

```bash
sftp> mkdir content
sftp> put -r content/
```

```output
Uploading content/ to /global/home/yourUsername/content
Entering content/
content/scheduler.md              100%   11KB  21.4KB/s   00:00
content/index.md                  100% 1051     7.2KB/s   00:00
content/transferring-files.md     100% 6117    36.6KB/s   00:00
content/.transferring-files.md.sw 100%   24KB  28.4KB/s   00:00
content/cluster.md                100% 5542    35.0KB/s   00:00
content/modules.md                100%   17KB 158.0KB/s   00:00
content/resources.md              100% 1115    29.9KB/s   00:00
```

To quit, we type `exit` or `bye`.


## Glossary

[Accelerator]{#accelerator}
: An **accelerator** in [high-performance computing (HPC)](#hpc) is a specialized hardware component designed to
  offload compute-intensive and parallelizable tasks from the [central processing unit (CPU)](#cpu), enabling higher
  performance, energy efficiency, and throughput, particularly for highly parallel workloads.

  More info: [Hardware Acceleration](https://en.wikipedia.org/wiki/Hardware_acceleration)

  See also: [Graphics Processing Unit (GPU)]

[Central Processing Unit (CPU)]{#cpu}
: A **central processing unit (CPU)** or simply *processor* is the hardware component of a computer that executes
  the instructions provided by software.

  Most systems use multi-core processors (e.g., dual-core, quad-core, and so on), where each **core** is an
  independent execution unit. Systems may also have multiple CPUs (sockets), each containing multiple cores.

  More info: [CPU](https://en.wikipedia.org/wiki/CPU)

[Cloud Computing]{#cloud}
: **Cloud computing** is the on-demand delivery of computing resources such as physical or virtual servers, data
  storage, networking, software, and analytics over the internet, typically using a pay-per-use pricing model,
  enabling scalable and elastic workloads.

  More info: [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing)

[Cluster]{#cluster}
: A **cluster** is a collection of computers ([nodes](#node)) connected via a high-speed [interconnect](#interconnect),
  working together as a unified system to execute parallel workloads.

  More info: [Cluster](https://en.wikipedia.org/wiki/Computer_cluster)

[Compute Node]{#compute-node}
: A **compute node** is a [server](#server) within a [cluster](#cluster) that is dedicated to executing computational
  jobs.

  It provides processing power (CPU/GPU), memory, and other resources required to run user workloads, typically managed
  by a job scheduler (e.g., [Slurm](#slurm)).

[Coupling, Loose vs. Tight]{#coupling}
: - **Coupling** refers to the degree of interdependence between components (e.g., processes or nodes) in a computing
    system, particularly in how frequently they communicate and synchronize.
  - **Tightly coupled systems** have components that frequently communicate and share data, often with low-latency
    interconnects and shared memory or fast message passing.
  - **Loosely coupled systems** have components that operate more independently, communicating less frequently,
    typically through higher-latency networks or asynchronous exchanges.

  More info: [Loosely vs. Tightly Coupled Multiprocessor System](https://techdifferences.com/difference-between-loosely-coupled-and-tightly-coupled-multiprocessor-system.html)

[Compute Unified Device Architecture (CUDA)]{#cuda}
: **CUDA** is a proprietary parallel computing platform and application programming interface that allows software to
  use certain types of [graphics processing units (GPU)](#gpu) for accelerated general-purpose processing,
  significantly broadening their utility in scientific and [high-performance computing (HPC)](#hpc).

  More info: [CUDA](https://en.wikipedia.org/wiki/CUDA)

[Distributed Memory]{#distributed-memory}
: **Distributed memory** is a parallel computer architecture where each processor ([node](#node)) has its own private,
  local memory, and nodes communicate (e.g., using [MPI]) by sending messages over a network
  [interconnect](#interconnect).

  More info: [Distributed memory](https://en.wikipedia.org/wiki/Distributed_memory)

[Execution Node]{#execution-node}
: An **execution node** is a node on which a job or task is actively running within a cluster environment.

  It is typically a [compute node](#compute-node) allocated by the scheduler to execute a specific workload.

[Flynn's Taxonomy]{#flynn}
: **Flynn's taxonomy** classifies computing architectures into:

  - Single instruction stream, single data stream (SISD)
  - Single instruction stream, multiple data streams ([SIMD])
  - Multiple instruction streams, single data stream (MISD)
  - Multiple instruction streams, multiple data streams (MIMD)

  This taxonomy is a coarse model, as many parallel processors are hybrids of the SISD, SIMD, and MIMD classes.

  More info: [Flynn's Taxonomy](https://en.wikipedia.org/wiki/Flynn%27s_taxonomy)

[Graphics Processing Unit (GPU)]{#gpu}
: A **graphics processing unit (GPU)** is a specialized [accelerator](#accelerator) optimized for high-throughput
  parallel computation using many lightweight parallel cores.

  More info: [Graphics processing unit](https://en.wikipedia.org/wiki/Graphics_processing_unit)

[Grid Computing]{#grid}
: **Grid computing** is a distributed system that connects geographically dispersed computers, often aggregating
  heterogeneous and possibly idle resources to act as a virtual [supercomputer](#supercomputer).

  More info: [Grid computing](https://en.wikipedia.org/wiki/Grid_computing)

[Grid Engine]{#grid-engine}
: **Grid engine** is typically used on a compute cluster or [high-performance computing (HPC)](#hpc) system and is
  responsible for accepting, scheduling, dispatching, and managing the remote and distributed execution of large
  numbers of standalone, parallel or interactive user jobs.

  More info: [Grid Engine](https://en.wikipedia.org/wiki/Oracle_Grid_Engine)

[High-Performance Computing (HPC)]{#hpc}
: **High-Performance Computing (HPC)** uses clustered, interconnected computing nodes ([cluster](#cluster)) to solve
  complex, data-intensive problems far beyond the capacity of standard desktop computers, often utilizing
  [parallel](#parallel) processing.

  More info: [High-Performance Computing](https://en.wikipedia.org/wiki/High-performance_computing)

[Hyper-Threading]{#hyper-threading}
: **Hyper-Threading** technology is a form of [simultaneous multithreading (SMT)](#smt) technology introduced by Intel.

  Architecturally, a processor with Hyper-Threading technology consists of two logical processors per core, each
  of which has its own processor architectural state.

  More info: [Hyper-Threading](https://en.wikipedia.org/wiki/Hyper-threading)

[InfiniBand]{#infiniband}
: **InfiniBand** is a computer networking standard used in [high-performance computing (HPC)](#hpc) that features very
  high throughput and very low latency. It provides high-speed [interconnect] capabilities within and between computers
  ([nodes](#node)).

  More info: [InfiniBand](https://en.wikipedia.org/wiki/InfiniBand)

[Interconnect]{#interconnect}
: **Interconnect** components are specialized hardware and communication technologies designed to provide extremely
  fast, low-latency and high-bandwidth communication between compute nodes, storage, and accelerators in a
  [cluster](#cluster) (e.g., [InfiniBand](#infiniband)) particularly in [distributed memory](#distributed-memory)
  systems.

  More info: [Interconnect](https://en.wikipedia.org/wiki/Supercomputer_architecture)

[Massively Parallel]{#massively-parallel}
: The term **massively parallel** means using a large number of processors to simultaneously perform a set of
  computations in parallel.

  More info: [Massively Parallel](https://en.wikipedia.org/wiki/Massively_parallel)

[Message Passing Interface (MPI)]{#mpi}
: **MPI** is a standardized and portable message-passing interface used for [parallel](#parallel) computing.

  It provides explicit communication, synchronization, and data exchange between processes, typically in
  [distributed memory] systems, often relying on high-performance [interconnect](#interconnect) technologies.

  MPI is commonly used for communication between processes across nodes in distributed memory systems, but can also be
  used within a single node.

  More info: [Message passing interface](https://en.wikipedia.org/wiki/Message_Passing_Interface)

[Node]{#node}
: An HPC **node** is an individual server (computer) within an [HPC](#hpc) [cluster](#cluster).

  More info: [Node](https://en.wikipedia.org/wiki/Node_\(computer_science\))

[Open Multi-Processing (OpenMP)]{#openmp}
: **OpenMP** is an application programming interface which provides a model for parallel programming in
  [shared memory](#shared-memory)
  systems within a single node that is portable across architectures from different vendors.

  More info: [OpenMP](https://en.wikipedia.org/wiki/OpenMP)

[Parallel]{#parallel}
: **Parallel** computing or **parallel** programming is a process where large compute problems are broken down into
  smaller problems that can be solved simultaneously by multiple processors.

  More info: [Parallel](https://en.wikipedia.org/wiki/Parallel_computing)

[Serial]{#serial}
: **Serial** computing refers to a computational model where tasks are executed sequentially, one after another, on a
  single processing unit.

  More info: [Serial](https://en.wikipedia.org/wiki/Serial_computer)

[Server]{#server}
: A **server** is a computer that provides resources, services, or functionality to other computers (clients) over a
  network.

  More info: [Server](https://en.wikipedia.org/wiki/Server_\(computing\))

[Shared Memory]{#shared-memory}
: **Shared memory** is a high-performance inter-process communication mechanism that allows multiple processes to
  access a common memory segment directly.

  More info: [Shared Memory](https://en.wikipedia.org/wiki/Shared_memory)

[Single Instruction, Multiple Data (SIMD)]{#simd}
: **SIMD** is a computer architecture technique that enhances performance by applying one instruction to multiple data
  points simultaneously using specialized vector registers.

  Examples:

  - `x86_64` architectures support "SSE", "AVX" and "AVX-512" instructions
  - `aarch64` architectures support "NEON", "SVE" instructions

  More info: [SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)

[Single Instruction, Multiple Threads (SIMT)]{#simt}
: **SIMT** is a parallel execution model used by [GPU](#gpu)s where a single instruction is applied to multiple threads.

  Threads are grouped (e.g., warps) and execute the same instruction in lockstep, with divergence handled through
  control flow masking.

  More info: [SIMT](https://en.wikipedia.org/wiki/Single_instruction,_multiple_threads)

[Simple Linux Utility for Resource Management (Slurm)]{#slurm}
: **Slurm** is an open-source, fault tolerant, and highly scalable cluster management and job scheduling system for
  Linux clusters.

  More info: [Slurm](https://en.wikipedia.org/wiki/Slurm_Workload_Manager)

[Symmetric Multiprocessing (SMP)]{#smp}
: **Symmetric Multiprocessing (SMP)** involves a multiprocessor hardware and software architecture where two or more
  identical processors are connected to a single shared main memory with equal access to all memory and I/O devices.

  It is controlled by a single operating system and treats all processes equally with no single processor having
  privileged access.

  More info: [Symmetric Multiprocessing](https://en.wikipedia.org/wiki/Symmetric_multiprocessing)

[Simultaneous Multithreading (SMT)]{#smt}
: **Simultaneous Multithreading (SMT)** is a technique for improving the overall efficiency of superscalar CPUs with
  hardware multithreading.

  More info: [Simultaneous Multithreading](https://en.wikipedia.org/wiki/Simultaneous_multithreading)

[Supercomputer]{#supercomputer}
: A **supercomputer** is a type of computer with a high level of performance as compared to
  [general-purpose computers](https://en.wikipedia.org/wiki/Computer).

  More info: [Supercomputer](https://en.wikipedia.org/wiki/Supercomputer)

[Worker Node]{#worker_node}
: A **worker node** is a compute node in a cluster that executes assigned computational tasks as part of a distributed
  system, typically under the coordination of a scheduler or control node.

[Workstation]{#workstation}
: A **workstation** is a special computer designed for technical or scientific applications intended to be used by a
  single user.

  More info: [Workstation](https://en.wikipedia.org/wiki/Workstation)
