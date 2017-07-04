---
title: "Using a cluster: Accessing software"
teaching: 0
exercises: 0
questions:
- "What is the module system and how does it work?"
objectives:
- "Understand how to load and use a software package."
keypoints:
- "Load software with `module load softwareName`"
- "Unload software with `module purge`"
- "You can edit your `.bashrc` file to automatically load a software package."
---

On a high-performance computing system, no software is loaded by default.
If we want to use a software package, we will need to "load" it ourselves.

Before we start using individual software packages, however, 
we should understand the reasoning behind this approach.
The two biggest factors are software incompatibilities and versioning.

Software incompatibility is a major headache for programmers.
Sometimes the presence (or absence) 
of a software package will break others that depend on it.
Two of the most famous examples are Python 2 and 3 and C compiler versions.
Python 3 famously provides a `python` command 
that conflicts with that provided by Python 2. 
Software compiled against a newer version of the C libraries 
and then used when they are not present will result in a nasty
`'GLIBCXX_3.4.20' not found` error, for instance. 

Software versioning is another common issue.
A team might depend on a certain package version for their research project - 
if the software version was to change (for instance, if a package was updated),
it might affect their results.
Having access to multiple software versions allow a set of researchers to take 
software version out of the equation if results are weird.

## Environment modules (Lmod)

Environment modules are the solution to these problems.
A module is a self-contained software package - 
it contains all of the files required to run a software packace 
and loads required dependencies.

To see available software modules, use `module avail`

```
module avail
```
{: .bash}
```
----------------------------- MPI-dependent avx2 modules -------------------------------
   abinit/8.2.2     (chem)      lammps/20170331                    plumed/2.3.0        (chem)
   abyss/1.9.0      (bio)       mrbayes/3.2.6            (bio)     pnetcdf/1.8.1       (io)
   boost-mpi/1.60.0 (t)         ncl/6.4.0                          quantumespresso/6.0 (chem)
   cdo/1.7.2        (geo)       ncview/2.1.7             (vis)     ray/2.3.1           (bio)


[snip]

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

## `$PATH` and loading software

To load a software module, use `module load`.
In this example we will use Python 3.

Intially, Python 3 is not loaded. 

```
which python3
```
{: .bash}
```
/usr/bin/which: no python3 in (/opt/software/slurm/16.05.9/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/avx2/Compiler/intel2016.4/openmpi/2.1.1/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/imkl/11.3.4.258/mkl/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/imkl/11.3.4.258/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/ifort/2016.4.258/compilers_and_libraries_2016.4.258/linux/bin/intel64:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/gcc-5.4.0/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/icc/2016.4.258/compilers_and_libraries_2016.4.258/linux/bin/intel64:/opt/software/bin:/opt/puppetlabs/puppet/bin:/opt/software/slurm/current/bin:/opt/software/slurm/bin:/cvmfs/soft.computecanada.ca/easybuild/bin:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/bin:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/sbin:/cvmfs/soft.computecanada.ca/custom/bin:/opt/software/slurm/current/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/yourUsername/.local/bin:/home/yourUsername/bin)
```
{: .output}

We can load the `python3` command with `module load`.

```
module load python/3.5.2
which python3
```
{: .bash}
```
/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/python-3.5.2/bin/python3
```
{: .output}

So what just happened?

To understand the output, first we need to understand the nature of the 
`$PATH` environment variable.
`$PATH` is a special ennvironment variable that controls where a UNIX system looks for software.
Specifically `$PATH` is a list of directories (separated by `:`)
that the OS searches through for a command before giving up and telling us it can't find it.
As with all environment variables we can print it out using `echo`.

```
echo $PATH
```
{: .bash}
```
/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/python-3.5.2/bin:/opt/software/slurm/16.05.9/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/avx2/Compiler/intel2016.4/openmpi/2.1.1/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/imkl/11.3.4.258/mkl/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/imkl/11.3.4.258/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/ifort/2016.4.258/compilers_and_libraries_2016.4.258/linux/bin/intel64:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/gcc-5.4.0/bin:/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/icc/2016.4.258/compilers_and_libraries_2016.4.258/linux/bin/intel64:/opt/software/bin:/opt/puppetlabs/puppet/bin:/opt/software/slurm/current/bin:/opt/software/slurm/bin:/cvmfs/soft.computecanada.ca/easybuild/bin:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/bin:/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/sbin:/cvmfs/soft.computecanada.ca/custom/bin:/opt/software/slurm/current/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/yourUsername/.local/bin:/home/yourUsername/bin
```
{: .output}

You'll notice a similarity to the output of the `which` command. 
In this case, there's only one difference:
the `/cvmfs/soft.computecanada.ca/nix/var/nix/profiles/python-3.5.2/bin` directory at the beginning.
When we ran `module load python/3.5.2`, 
it added this directory to the beginning of our `$PATH`.
Let's examine what's there:

```
ls /cvmfs/soft.computecanada.ca/nix/var/nix/profiles/python-3.5.2/bin
```
{: .bash}
```
2to3		  idle3    pip3.5    python3	       python3.5m-config  virtualenv
2to3-3.5	  idle3.5  pydoc3    python3.5	       python3-config	  wheel
easy_install	  pip	   pydoc3.5  python3.5-config  pyvenv
easy_install-3.5  pip3	   python    python3.5m        pyvenv-3.5
```
{: .output}



