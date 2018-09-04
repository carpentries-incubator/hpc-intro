---
title: "Accessing software"
teaching: 30
exercises: 15
questions:
- "How do we load and unload software packages?"
objectives:
- "Understand how to load and use a software package."
keypoints:
- "Load software with `module load softwareName`"
- "Unload software with `module purge`"
- "The module system handles software versioning and package conflicts for you automatically."
- "You can edit your `.bashrc` file to automatically load a software package."
---

On a high-performance computing system, no software is loaded by default. If we want to use a
software package, we will need to "load" it ourselves.

Before we start using individual software packages, however, we should understand the reasoning
behind this approach. The two biggest factors are software incompatibilities and versioning.

Software incompatibility is a major headache for programmers. Sometimes the presence (or absence) of
a software package will break others that depend on it. Two of the most famous examples are Python 2
and 3 and C compiler versions. Python 3 famously provides a `python` command that conflicts with
that provided by Python 2. Software compiled against a newer version of the C libraries and then
used when they are not present will result in a nasty `'GLIBCXX_3.4.20' not found` error, for
instance.

Software versioning is another common issue. A team might depend on a certain package version for
their research project - if the software version was to change (for instance, if a package was
updated), it might affect their results. Having access to multiple software versions allow a set of
researchers to prevent software versioning issues from affecting their results.

## Environment modules (Lmod)

Environment modules are the solution to these problems. A module is a self-contained software
package - it contains all of the files required to run a software package and loads required
dependencies.

To see available software modules, use `module avail`

```
[remote]$ module avail
```
{: .bash}
```
----------------------------- MPI-dependent avx2 modules -------------------------------
   abinit/8.2.2     (chem)      lammps/20170331                    plumed/2.3.0        (chem)
   abyss/1.9.0      (bio)       mrbayes/3.2.6            (bio)     pnetcdf/1.8.1       (io)
   boost-mpi/1.60.0 (t)         ncl/6.4.0                          quantumespresso/6.0 (chem)
   cdo/1.7.2        (geo)       ncview/2.1.7             (vis)     ray/2.3.1           (bio)


[removed most of the output here for clarity]

   t:        Tools for development / Outils de développement
   vis:      Visualisation software / Logiciels de visualisation
   chem:     Chemistry libraries/apps / Logiciels de chimie
   geo:      Geography libraries/apps / Logiciels de géographie
   phys:     Physics libraries/apps / Logiciels de physique
   Aliases:  Aliases exist: foo/1.2.3 (1.2) means that "module load foo/1.2" will load foo/1.2.3
   D:        Default Module

Use "module spider" to find all possible modules.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
```
{: .output}

## Loading and unloading software

To load a software module, use `module load`.
In this example we will use Python 3.

Initially, Python 3 is not loaded. 
We can test this by using the `which` command.
`which` looks for programs the same way that Bash does,
so we can use it to tell us where a particular piece of software is stored.

```
[remote]$ which python3
```
{: .bash}
```
/usr/bin/which: no python3 in
(/opt/software/slurm/16.05.9/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/avx2/Compiler/intel2016.4/openmpi/2.1.1/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/imkl/11.3.4.258/mkl/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/imkl/11.3.4.258/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/ifort/2016.4.258/compilers_and_libraries_2016.4.258/linux/bin/intel64:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/gcc-5.4.0/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/icc/2016.4.258/compilers_and_libraries_2016.4.258/linux/bin/intel64:/opt/software/bin:/opt/puppetlabs/puppet/bin:/opt/software/slurm/current/bin:/opt/software/slurm/bin:/cvmfs/soft.computecanada.ca/easybuild/bin:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/bin:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/sbin:/cvmfs/soft.computecanada.ca/custom/bin:/opt/software/slurm/current/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/yourUsername/.local/bin:/home/yourUsername/bin)
```
{: .output}

We can load the `python3` command with `module load`:

```
[remote]$ module load python
[remote[$ which python3
```
{: .bash}
```
/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/python-3.5.2/bin/python3
```
{: .output}

So what just happened?


To understand the output, first we need to understand the nature of the `$PATH` environment
variable. `$PATH` is a special environment variable that controls where a UNIX system looks for
software. Specifically `$PATH` is a list of directories (separated by `:`) that the OS searches
through for a command before giving up and telling us it can't find it. As with all environment
variables we can print it out using `echo`.

```
[remote]$ echo $PATH
```
{: .bash}
```
/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/python-3.5.2/bin:/opt/software/slurm/16.05.9/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/avx2/Compiler/intel2016.4/openmpi/2.1.1/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/imkl/11.3.4.258/mkl/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/imkl/11.3.4.258/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/ifort/2016.4.258/compilers_and_libraries_2016.4.258/linux/bin/intel64:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/gcc-5.4.0/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/icc/2016.4.258/compilers_and_libraries_2016.4.258/linux/bin/intel64:/opt/software/bin:/opt/puppetlabs/puppet/bin:/opt/software/slurm/current/bin:/opt/software/slurm/bin:/cvmfs/soft.computecanada.ca/easybuild/bin:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/bin:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/sbin:/cvmfs/soft.computecanada.ca/custom/bin:/opt/software/slurm/current/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/yourUsername/.local/bin:/home/yourUsername/bin
```
{: .output}

You'll notice a similarity to the output of the `which` command. In this case, there's only one
difference: the `/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/python-3.5.2/bin` directory at
the beginning. When we ran `module load python/3.5.2`, it added this directory to the beginning of
our `$PATH`. Let's examine what's there:

```
[remote]$ ls /cvmfs/soft.computecanada.ca/nix/var/nix/profiles/python-3.5.2/bin
```
{: .bash}
```
2to3		  idle3    pip3.5    python3	       python3.5m-config  virtualenv
2to3-3.5	  idle3.5  pydoc3    python3.5	       python3-config	  wheel
easy_install	  pip	   pydoc3.5  python3.5-config  pyvenv
easy_install-3.5  pip3	   python    python3.5m        pyvenv-3.5
```
{: .output}

Taking this to it's conclusion, `module load` will add software to your `$PATH`. It "loads"
software. A special note on this - depending on which version of the `module` program that is
installed at your site, `module load` will also load required software dependencies. To demonstrate,
let's use `module list`. `module list` shows all loaded software modules.

```
[remote]$ module list
```
{: .bash}
```
Currently Loaded Modules:
  1) nixpkgs/.16.09  (H,S)   3) gcccore/.5.4.0    (H)   5) intel/2016.4  (t)   7) StdEnv/2016.4 (S)
  2) icc/.2016.4.258 (H)     4) ifort/.2016.4.258 (H)   6) openmpi/2.1.1 (m)   8) python/3.5.2  (t)

  Where:
   S:  Module is Sticky, requires --force to unload or purge
   m:  MPI implementations / Implémentations MPI
   t:  Tools for development / Outils de développement
   H:             Hidden Module
```
{: .output}

```
[remote]$ module load beast
[remote]$ module list
```
{: .bash}
```
Currently Loaded Modules:
  1) nixpkgs/.16.09    (H,S)   5) intel/2016.4  (t)   9) java/1.8.0_121   (t)
  2) icc/.2016.4.258   (H)     6) openmpi/2.1.1 (m)  10) beagle-lib/2.1.2 (bio)
  3) gcccore/.5.4.0    (H)     7) StdEnv/2016.4 (S)  11) beast/2.4.0      (chem)
  4) ifort/.2016.4.258 (H)     8) python/3.5.2  (t)

  Where:
   S:     Module is Sticky, requires --force to unload or purge
   bio:   Bioinformatic libraries/apps / Logiciels de bioinformatique
   m:     MPI implementations / Implémentations MPI
   t:     Tools for development / Outils de développement
   chem:  Chemistry libraries/apps / Logiciels de chimie
   H:                Hidden Module
```
{: .output}

So in this case, loading the `beast` module (a bioinformatics software package), also loaded
`java/1.8.0_121` and `beagle-lib/2.1.2` as well. Let's try unloading the `beast` package.

```
[remote]$ module unload beast
[remote]$ module list
```
{: .bash}
```
Currently Loaded Modules:
  1) nixpkgs/.16.09  (H,S)   3) gcccore/.5.4.0    (H)   5) intel/2016.4  (t)   7) StdEnv/2016.4 (S)
  2) icc/.2016.4.258 (H)     4) ifort/.2016.4.258 (H)   6) openmpi/2.1.1 (m)   8) python/3.5.2  (t)

  Where:
   S:  Module is Sticky, requires --force to unload or purge
   m:  MPI implementations / Implémentations MPI
   t:  Tools for development / Outils de développement
   H:             Hidden Module
```
{: .output}

So using `module unload` "un-loads" a module along with its dependencies.
If we wanted to unload everything at once, we could run `module purge` (unloads everything).

```
[remote]$ module purge
```
{: .bash}
```
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) StdEnv/2016.4    3) icc/.2016.4.258   5) ifort/.2016.4.258   7) imkl/11.3.4.258
  2) nixpkgs/.16.09   4) gcccore/.5.4.0    6) intel/2016.4        8) openmpi/2.1.1
```
{: .output}

Note that `module purge` is informative. It lets us know that all but a default set of packages have
been unloaded (and how to actually unload these if we truly so desired).

## Software versioning

So far, we've learned how to load and unload software packages. This is very useful. However, we
have not yet addressed the issue of software versioning. At some point or other, you will run into
issues where only one particular version of some software will be suitable. Perhaps a key bugfix
only happened in a certain version, or version X broke compatibility with a file format you use. In
either of these example cases, it helps to be very specific about what software is loaded.

Let's examine the output of `module avail` more closely.

```
[remote]$ module avail
```
{: .bash}
```
----------------------------------------------------------- Core Modules -----------------------------------------------------------
   StdEnv/2016.4 (S,L)     imkl/11.3.4.258 (L,math,D:11)      mcr/R2014b         (t)          python/3.5.2     (t,D:3:3.5)
   bioperl/1.7.1 (bio)     imkl/2017.1.132 (math,2017)        mcr/R2015a         (t)          qt/4.8.7         (t)
   eclipse/4.6.0 (t)       impute2/2.3.2   (bio)              mcr/R2015b         (t)          qt/5.6.1         (t,D)
   eigen/3.3.2   (math)    intel/2016.4    (L,t,D:16:2016)    mcr/R2016a         (t)          signalp/4.1f     (bio)
   fastqc/0.11.5 (bio)     intel/2017.1    (t,17:2017)        mcr/R2016b         (t,D)        spark/2.1.0      (t)
   g2clib/1.6.0            jasper/1.900.1  (vis)              minimac2/2014.9.15 (bio)        spark/2.1.1      (t,D)
   g2lib/1.4.0             java/1.8.0_121  (L,t)              perl/5.22.2        (t)          tbb/2017.2.132   (t)
   gatk/3.7      (bio)     mach/1.0.18     (bio)              pgi/17.3           (t)          tmhmm/2.0c       (bio)
   gcc/4.8.5     (t)       mcr/R2013a      (t)                picard/2.1.1       (bio)        trimmomatic/0.36 (bio)
   gcc/5.4.0     (t,D)     mcr/R2014a      (t)                python/2.7.13      (t,2:2.7)
```
{: .output}

Let's take a closer look at the `gcc` module. GCC is an extremely widely used C/C++/Fortran
compiler. Tons of software is dependent on the GCC version, and might not compile or run if the
wrong version is loaded. In this case, there are two different versions: `gcc/4.8.5` and
`gcc/5.4.0`. How do we load each copy and which copy is the default?

In this case, `gcc/5.4.0` has a `(D)` next to it. This indicates that it is the default - if we type
`module load gcc`, this is the copy that will be loaded.

```
[remote]$ module load gcc
[remote]$ gcc --version
```
{: .bash}
```
Lmod is automatically replacing "intel/2016.4" with "gcc/5.4.0".


Due to MODULEPATH changes, the following have been reloaded:
  1) openmpi/2.1.1

gcc (GCC) 5.4.0
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
{: .output}

Note that three things happened: the default copy of GCC was loaded (version 5.4.0), the Intel
compilers (which conflict with GCC) were unloaded, and software that is dependent on compiler
(OpenMPI) was reloaded. The `module` system turned what might be a super-complex operation into a
single command.

So how do we load the non-default copy of a software package? In this case, the only change we need
to make is be more specific about the module we are loading. There are two GCC modules: `gcc/5.4.0`
and `gcc/4.8.5`. To load a non-default module, the only change we need to make to our `module load`
command is to leave in the version number after the `/`.

```
[remote]$ module load gcc/4.8.5
[remote]$ gcc --version
```
{: .bash}
```
Inactive Modules:
  1) openmpi

The following have been reloaded with a version change:
  1) gcc/5.4.0 => gcc/4.8.5

gcc (GCC) 4.8.5
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
{: .output}

We now have successfully switched from GCC 5.4.0 to GCC 4.8.5. It is also important to note that
there was no compatible OpenMPI module available for GCC 4.8.5. Because of this, the `module`
program has "inactivated" the module. All this means for us is that if we re-load GCC 5.4.0,
`module` will remember OpenMPI used to be loaded and load that module as well.

```
[remote]$ module load gcc/5.4.0
```
{: .bash}
```
Activating Modules:
  1) openmpi/2.1.1

The following have been reloaded with a version change:
  1) gcc/4.8.5 => gcc/5.4.0
```
{: .output}

> ## Using software modules in scripts
>
> Create a job that is able to run `python3 --version`. Remember, no software is loaded by default!
> Running a job is just like logging on to the system (you should not assume a module loaded on the
> login node is loaded on a worker node).
{: .challenge}

> ## Loading a module by default
> 
> Adding a set of `module load` commands to all of your scripts and having to manually load modules
> every time you log on can be tiresome. Fortunately, there is a way of specifying a set of "default
> modules" that always get loaded, regardless of whether or not you're logged on or running a job.
>
> Every user has two hidden files in their home directory: `.bashrc` and `.bash_profile` (you can
> see these files with `ls -la ~`). These scripts are run every time you log on or run a job. Adding
> a `module load` command to one of these shell scripts means that that module will always be
> loaded. Modify either your `.bashrc` or `.bash_profile` scripts to load a commonly used module
> like Python. Does your `python3 --version` job from before still need `module load` to run?
{: .challenge}

## Installing software of our own

Most HPC clusters have a pretty large set of preinstalled software. Nonetheless, it's unlikely that
all of the software we'll need will be available. Sooner or later, we'll need to install some
software of our own.

Though software installation differs from package to package, the general process is the same:
download the software, read the installation instructions (important!), install dependencies,
compile, then start using our software.

As an example we will install the bioinformatics toolkit `seqtk`. We'll first need to obtain the
source code from GitHub using `git`.

```
[remote]$ git clone https://github.com/lh3/seqtk.git
```
{: .bash}
```
Cloning into 'seqtk'...
remote: Counting objects: 316, done.
remote: Total 316 (delta 0), reused 0 (delta 0), pack-reused 316
Receiving objects: 100% (316/316), 141.52 KiB | 0 bytes/s, done.
Resolving deltas: 100% (181/181), done.
```
{: .output}

Now, using the instructions in the README.md file, all we need to do to complete the install is to
`cd` into the seqtk folder and run the command `make`.

```
[remote]$ cd seqtk
[remote]$ make
```
{: .bash}
```
gcc -g -Wall -O2 -Wno-unused-function seqtk.c -o seqtk -lz -lm
seqtk.c: In function ‘stk_comp’:
seqtk.c:399:16: warning: variable ‘lc’ set but not used [-Wunused-but-set-variable]
    int la, lb, lc, na, nb, nc, cnt[11];
                ^
```
{: .output}

It's done! Now all we need to do to use the program is invoke it like any other program.

```
[remote]$ ./seqtk
```
{: .bash}
```
Usage:   seqtk <command> <arguments>
Version: 1.2-r101-dirty

Command: seq       common transformation of FASTA/Q
         comp      get the nucleotide composition of FASTA/Q
         sample    subsample sequences
         subseq    extract subsequences from FASTA/Q
         fqchk     fastq QC (base/quality summary)
         mergepe   interleave two PE FASTA/Q files
         trimfq    trim FASTQ using the Phred algorithm

         hety      regional heterozygosity
         gc        identify high- or low-GC regions
         mutfa     point mutate FASTA at specified positions
         mergefa   merge two FASTA/Q files
         famask    apply a X-coded FASTA to a source FASTA
         dropse    drop unpaired from interleaved PE FASTA/Q
         rename    rename sequence names
         randbase  choose a random base from hets
         cutN      cut sequence at long N
         listhet   extract the position of each het
```
{: .output}

We've successfully installed our first piece of software!
