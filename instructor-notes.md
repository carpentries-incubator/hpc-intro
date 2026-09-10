---
title: Glossary
permalink: /guide/
---

## Glossary

The following list captures terms that need to be added to this glossary. This is a great way to contribute.

---

[Accelerator](#accelerator)  
[Central Processing Unit](#cpu)  
[Cloud Computing](#cloud-computing)  
[Cluster](#cluster)  
[Compute Node](#compute-node)  
[Coupling Loose vs. Tight](#coupling-loose-vs-tight)  
[Compute Unified Device Architecture](#cuda)  
[Distributed Memory](#distributed-memory)  
[Execution Node](#execution-node)  
[Flynn's Taxonomy](#flynns-taxonomy)  
[Graphics Processing Unit](#gpu)  
[Grid Computing](#grid-computing)  
[Grid Engine](#grid-engine)  
[High-Performance Computing](#hpc)  
[Hyper-Threading](#hyper-threading)  
[InfiniBand](#infiniband)  
[Interconnect](#interconnect)  
[Massively Parallel](#massively-parallel)  
[Message Passing Interface](#mpi)  
[Node](#node)  
[Open Multi-Processing](#openmp)  
[Parallel](#parallel)  
[Serial](#serial)  
[Server](#server)  
[Shared Memory](#shared-memory)  
[Single Instruction, Multiple Data](#simd)  
[Single Instruction, Multiple Threads](#simt)  
[Simple Linux Utility for Resource Management](#slurm)  
[Symmetric Multiprocessing](#smp)  
[Simultaneous Multithreading](#smt)  
[Supercomputer](#supercomputer)  
[Worker Node](#worker-node)  
[Workstation](#workstation)


### Accelerator {#accelerator}

An **accelerator** in [high-performance computing (HPC)](#hpc) is a specialized hardware component designed to offload compute-intensive and parallelizable tasks from the [central processing unit](#cpu), enabling higher performance, energy efficiency, and throughput, particularly for highly parallel workloads.

More info: [Hardware Acceleration](https://en.wikipedia.org/wiki/Hardware_acceleration)

See also: [Graphics Processing Unit](#gpu)

### Central Processing Unit (CPU) {#cpu}

A **central processing unit (CPU)** or simply *processor* is the hardware component of a computer that executes the instructions provided by software. 

Most systems use multi-core processors (e.g., dual-core, quad-core, and so on), where each **core** is an independent execution unit. Systems may also have multiple CPUs (sockets), each containing multiple cores.

More info: [CPU](https://en.wikipedia.org/wiki/CPU)

### Cloud Computing {#cloud-computing}

**Cloud computing** is the on-demand delivery of computing resources such as physical or virtual servers, data storage, networking, software, and analytics over the internet, typically using a pay-per-use pricing model, enabling scalable and elastic workloads.

More info: [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing)

### Cluster {#cluster}

A **cluster** is a collection of computers ([nodes](#node)) connected via a high-speed [interconnect](#interconnect), working together as a unified system to execute parallel workloads.

More info:  [Cluster](https://en.wikipedia.org/wiki/Computer_cluster)

### Compute Node {#compute-node}

A **compute node** is a [server](#server) within a [cluster](#cluster) that is dedicated to executing computational jobs. 
It provides processing power (CPU/GPU), memory, and other resources required to run user workloads, typically managed by a job scheduler (e.g., [Slurm](#slurm)).

### Coupling, Loose vs. Tight {#coupling-loose-vs-tight}

- **Coupling** refers to the degree of interdependence between components (e.g., processes or nodes) in a computing system, particularly in how frequently they communicate and synchronize.
- **Tightly coupled systems** have components that frequently communicate and share data, often with low-latency interconnects and shared memory or fast message passing.
- **Loosely coupled systems** have components that operate more independently, communicating less frequently, typically through higher-latency networks or asynchronous exchanges.

More info: [Loosely vs. Tightly Coupled Multiprocessor System](https://techdifferences.com/difference-between-loosely-coupled-and-tightly-coupled-multiprocessor-system.html)

### Compute Unified Device Architecture (CUDA) {#cuda}

**CUDA** is a proprietary parallel computing platform and application programming interface that allows software to use certain types of [graphics processing units](#gpu) for accelerated general-purpose processing, significantly broadening their utility in scientific and [high-performance computing](#hpc).

More info: [CUDA](https://en.wikipedia.org/wiki/CUDA)

### Distributed Memory {#distributed-memory}

**Distributed memory** is a parallel computer architecture where each processor ([node](#node)) has its own private, local memory, and nodes communicate (e.g., using [MPI](#mpi)) by sending messages over a network [interconnect](#interconnect).

More info: [Distributed memory](https://en.wikipedia.org/wiki/Distributed_memory)

### Execution Node {#execution-node}

An **execution node** is a node on which a job or task is actively running within a cluster environment. 
It is typically a [compute node](#compute-node) allocated by the scheduler to execute a specific workload.

### Flynn's Taxonomy {#flynns-taxonomy}

**Flynn's taxonomy** classifies computing architectures into:
- Single instruction stream, single data stream (SISD)
- Single instruction stream, multiple data streams ([SIMD](#simd))
- Multiple instruction streams, single data stream (MISD)
- Multiple instruction streams, multiple data streams (MIMD)

This taxonomy is a coarse model, as many parallel processors are hybrids of the SISD, SIMD, and MIMD classes.

More info: [Flynn's Taxonomy](https://en.wikipedia.org/wiki/Flynn%27s_taxonomy) ([SIMD](#simd), [SIMT](#simt))

### Graphics Processing Unit (GPU) {#gpu}

A **graphics processing unit (GPU)** is a specialized [accelerator](#accelerator) optimized for high-throughput parallel computation using many lightweight parallel cores.

More info: [Graphics processing unit](https://en.wikipedia.org/wiki/Graphics_processing_unit)

### Grid Computing {#grid-computing}

**Grid computing** is a distributed system that connects geographically dispersed computers, often aggregating heterogeneous and possibly idle resources to act as a virtual [supercomputer](#supercomputer).

More info: [Grid computing](https://en.wikipedia.org/wiki/Grid_computing)

### Grid Engine {#grid-engine}

**Grid engine** is typically used on a compute cluster or [high-performance computing](#hpc) system and is responsible for accepting, scheduling, dispatching, and managing the remote and distributed execution of large numbers of standalone, parallel or interactive user jobs.

More info: [Grid Engine](https://en.wikipedia.org/wiki/Oracle_Grid_Engine)

### High-Performance Computing (HPC) {#hpc}

**High-Performance Computing (HPC)** uses clustered, interconnected computing nodes ([cluster](#cluster)) to solve complex, data-intensive problems far beyond the capacity of standard desktop computers, often utilizing [parallel](#parallel) processing.

More info: [High-Performance Computing](https://en.wikipedia.org/wiki/High-performance_computing)

### Hyper-Threading {#hyper-threading}

**Hyper-Threading** technology is a form of [simultaneous-multithreading](#smt) technology introduced by Intel.

Architecturally, a processor with Hyper-Threading technology consists of two logical processors per core, each of which has its own processor architectural state.

More info: [Hyper-Threading](https://en.wikipedia.org/wiki/Hyper-threading)([SMT](#smt))

### InfiniBand {#infiniband}

**InfiniBand** is a computer networking standard used in [high-performance computing](#hpc) that features very high throughput and very low latency. It provides high-speed [interconnect](#interconnect) capabilities within and between computers ([nodes](#node)).

More info: [InfiniBand](https://en.wikipedia.org/wiki/InfiniBand)

### Interconnect {#interconnect}

**Interconnect** components are specialized hardware and communication technologies designed to provide extremely fast, low-latency and high-bandwidth communication between compute nodes, storage, and accelerators in a [cluster](#cluster) (e.g., [InfiniBand](#infiniband)) particularly in [distributed memory](#distributed-memory) systems.

More info: [Interconnect](https://en.wikipedia.org/wiki/Supercomputer_architecture)

### Massively Parallel {#massively-parallel}

The term **massively parallel** means using a large number of processors to simultaneously perform a set of computations in parallel.

More info: [Massively Parallel](https://en.wikipedia.org/wiki/Massively_parallel)

### Message Passing Interface (MPI) {#mpi}

**MPI** is a standardized and portable message-passing interface used for [parallel](#parallel) computing. 
It provides explicit communication, synchronization, and data exchange between processes, typically in [distributed memory](#distributed-memory) systems, often relying on high-performance [interconnect](#interconnect) technologies.

MPI is commonly used for communication between processes across nodes in distributed memory systems, but can also be used within a single node.

More info: [Message passing interface](https://en.wikipedia.org/wiki/Message_Passing_Interface)

### Node {#node}

An HPC **node** is an individual server (computer) within an [HPC](#hpc) [cluster](#cluster).

More info: [Node](https://en.wikipedia.org/wiki/Node_\(computer_science\))

### Open Multi-Processing (OpenMP) {#openmp}

**OpenMP** is an application programming interface which provides a model for parallel programming in [shared memory](#shared-memory) systems within a single node that is portable across architectures from different vendors.

More info: [OpenMP](https://en.wikipedia.org/wiki/OpenMP)

### Parallel {#parallel}

**Parallel** computing or **parallel** programming is a process where large compute problems are broken down into smaller problems that can be solved simultaneously by multiple processors.

More info: [Parallel](https://en.wikipedia.org/wiki/Parallel_computing)

### Serial {#serial}

**Serial** computing refers to a computational model where tasks are executed sequentially, one after another, on a single processing unit.

More info: [Serial](https://en.wikipedia.org/wiki/Serial_computer)

### Server {#server}

A **server** is a computer that provides resources, services, or functionality to other computers (clients) over a network.

More info: [Server](https://en.wikipedia.org/wiki/Server_\(computing\))

### Shared Memory {#shared-memory}

**Shared memory** is a high-performance inter-process communication mechanism that allows multiple processes to access a common memory segment directly.

More info: [Shared Memory](https://en.wikipedia.org/wiki/Shared_memory)

### Single Instruction, Multiple Data (SIMD) {#simd}

**SIMD** is a computer architecture technique that enhances performance by applying one instruction to multiple data points simultaneously using specialized vector registers.

Examples:
- `x86_64` architectures support "SSE", "AVX" and "AVX-512" instructions and
- `aarch64` architectures support "NEON", "SVE" instructions.

More info: [SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)

### Single Instruction, Multiple Threads (SIMT) {#simt}

**SIMT** is a parallel execution model used by [GPU](#gpu)s where a single instruction is applied to multiple threads. 
Threads are grouped (e.g., warps) and execute the same instruction in lockstep, with divergence handled through control flow masking.

More info: [SIMT](https://en.wikipedia.org/wiki/Single_instruction,_multiple_threads)

### Simple Linux Utility for Resource Management (Slurm) {#slurm}

**Slurm** is an open-source, fault tolerant, and highly scalable cluster management and job scheduling system for Linux clusters.

More info: [Slurm](https://en.wikipedia.org/wiki/Slurm_Workload_Manager)

### Symmetric Multiprocessing (SMP) {#smp}

**Symmetric Multiprocessing (SMP)** involves a multiprocessor hardware and software architecture where two or more identical processors are connected to a single shared main memory with equal access to all memory and I/O devices. 
It is controlled by a single operating system and treats all processes equally with no single processor having privileged access.

More info: [Symmetric Multiprocessing](https://en.wikipedia.org/wiki/Symmetric_multiprocessing)

### Simultaneous Multithreading (SMT) {#smt}

**Simultaneous Multithreading (SMT)** is a technique for improving the overall efficiency of superscalar CPUs with hardware multithreading.

More info: [Simultaneous Multithreading](https://en.wikipedia.org/wiki/Simultaneous_multithreading)

### Supercomputer {#supercomputer}

A **supercomputer** is a type of computer with a high level of performance as compared to [general-purpose computers](https://en.wikipedia.org/wiki/Computer).

More info: [Supercomputer](https://en.wikipedia.org/wiki/Supercomputer)

### Worker Node {#worker-node}

A **worker node** is a compute node in a cluster that executes assigned computational tasks as part of a distributed system, typically under the coordination of a scheduler or control node.

### Workstation {#workstation}

A **workstation** is a special computer designed for technical or scientific applications intended to be used by a single user.

More info: [Workstation](https://en.wikipedia.org/wiki/Workstation)
