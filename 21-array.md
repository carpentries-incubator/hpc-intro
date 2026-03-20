---
title: Parallelising with Job Arrays.
teaching: 15
exercises: 5
---



::::::::::::::::::::::::::::::::::::::: objectives

- Prepare a job submission script for an array job.
- Launch a job to be executed in parallel over several nodes

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What are job arrays?
- What benefit does job arrays bring?
- What type of jobs would benefit from job arrays?

::::::::::::::::::::::::::::::::::::::::::::::::::


Parallel computing is a technique used to divide big tasks into smaller ones that can be solved simultaneously. Parallelism can be accomplished in different ways and it depends on the tasks that needs doing as well as the algorithms implemented to perform these tasks.

One way of implementing parallel computing is to distribute a job across multiple processors. This is usually accomplished by using the Message Passage Interface (MPI) which is a standardised way for CPU cores to communicate with one another while working together on a task. Software has to be written specifically to utilize MPI to take advantage of this.

Another form of parallel computing is an array job. This type of job is advantages if the same software has to be run across several files. An example of this would be in bioinformatics where the same workflow has to applied to a set of files that contain data for different samples. There is no need for the different jobs to "talk" to one another while they run. The advantage only lies in the fact that the jobs can run in parallel. One could potentially run such processes manually across different computers but imagine having a hundred files and each taking two hours to complete. You can run them in series which would take two hundred hours or you can manually start them across, say, four computers which would mean it would take 25 hours. But it would take you some time to start all these jobs if you do it manually. To complicate matters things will quite often go wrong and workflow won't complete in which case you have to first notice this, correct the problem and then restart it all.

Array jobs are controlled by the Slurm scheduler. You will need only one set of scripts to which you supply a list of files. Slurm will automatically distribute the jobs across available nodes. If any of the jobs fail you can easily restart the jobs to execute only on the files that failed.

```bash
cd training directory
mkdir username
cd username
```

Download the word frequency script
```
wget https://raw.githubusercontent.com/NewcastleRSE-Training/hpc-intro/refs/heads/main/episodes/files/word-freq.sh

```

write a small file to test our script

```bash
[yourUsername@login1 ~]$ nano test-data.txt
[yourUsername@login1 ~]$ cat test-data.txt
```

```bash
This is a small file - it will be very useful for trying out our script.
Some words are repeated in this file
- we can look for repeated words
and count them (to see which words are repeated most often).
```

To test the script we will run it on the login node. Remember, never do this with resource intensive script. You could even run the script on your laptop or desktop if it uses Linux or Mac. This specific script will not work on Windows as not all the commands in the script are available on the Windows operating system.

```bash
bash word-freq.sh test-data.txt
```

To the results, type the output of the script to screen:

```bash
cat analyzed_test-data.txt
```

You should get something like this:

```
      1 a
      1 and
      1 be
      1 can
      1 count
      1 in
      1 is
      1 it
      1 look
      1 most
      1 often
      1 our
      1 out
      1 script
      1 see
      1 small
      1 some
      1 them
      1 to
      1 trying
      1 useful
      1 very
      1 we
      1 which
      1 will
      2 are
      2 file
      2 for
      2 this
      3 repeated
      3 words

```
Once we have proved that the script runs without a problem we can write a script that can be submitted to Slurm. Using `nano`, create a script called `job_single_word-freq.sh` containing the following:

```bash
#!/bin/bash

#SBATCH --partition=short_free
#SBATCH --account=comet_training
#SBATCH --job-name=word-freq_single-test1
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --cpus-per-task=1

echo "Starting word frequency script"
bash word-freq.sh test-data.txt
echo "Finished word frequency script"
```

::::instructor
The complete script can be downloaded from: https://raw.githubusercontent.com/NewcastleRSE-Training/hpc-intro-comet/refs/heads/main/episodes/files/job_single_word-freq.sh
::::




:::::::::::::::::::::::::::::::::::::::  challenge

How would you submit the script to Slurm for execution?


:::::::::::::::  solution

  
```bash
sbatch job_single_word-freq.sh
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

If you haven't done so already, download the data to be used for the script. The data consists of several books from the Gutenberg project as text files. The downloaded books should be as follows:

|Filename|Book name|
|---|---|
|data.1|The collected works of Shakespeare|
|data.2|Geoffrey Chaucers Cantebury Tales |
|data.3|Moby Dick by Herman Melville|
|data.4|Homers Odyssey|


::::instructor
Download the data using https://raw.githubusercontent.com/NewcastleRSE-Training/hpc-intro-comet/refs/heads/main/episodes/files/make-data.sh
::::

::::: challenge

How would we change the `job_single_word-freq.sh` script to use the first of the four data files in stead of `test-data.txt`?

:::: solution

```bash
#!/bin/bash

#SBATCH --partition=short_free
#SBATCH --account=comet_training
#SBATCH --job-name=wordfreq
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --cpus-per-task=1

echo "Starting word frequency script"
bash word-freq.sh data.1
echo "Finished word frequency script"
```

::::

:::::


::::: challenge

Write a batch script to call the word-freq.sh as an array job with 4 parallel jobs to process all 4 text files (job_array_word-freq.sh). To do this you will need the directive `#SBATCH --array=1-4`. When using this directive, each job will be given a job number. In this case it will be job numbers one to four. While running the script for a specific job number, that number will be available in an environment variable called `${SLURM_ARRAY_TASK_ID}`.

:::: solution

```bash



#SBATCH -pshort_free
#SBATCH --account=comet_training
#SBATCH -Jmakefreq
#SBATCH 1
#SBATCH 4
#SBATCH --array=1-4
#SBATCH 1

# Do a word frequency analysis of each of the following
# data sets simultaneously:
#
# data.1 - The collected works of Shakespeare
# data.2 - Geoffrey Chaucers Cantebury Tales 
# data.3 - Moby Dick by Herman Melville
# data.4 - Homers Odyssey
#
# We should be able to process all four data sets in the same
# time it took to process just the first.

echo "Starting word frequency script"
bash word-freq.sh data.${SLURM_ARRAY_TASK_ID}
echo "Finished word frequency script"
```

::::

:::::


:::: instructor

You can download the script from https://raw.githubusercontent.com/NewcastleRSE-Training/hpc-intro-comet/refs/heads/main/episodes/files/job_array_word-freq.sh

::::


:::::::::::::::::::::::::::::::::::::::: keypoints

- Parallel programming allows applications to take advantage of parallel hardware.
- The queuing system facilitates executing parallel tasks.
- Parallel computing allows applications to distribute the workload over several CPUs or nodes
- Parallelising over CPUs uses MPI (Message Passing Interface)
- Parallelising over nodes can be accomplished using array jobs

::::::::::::::::::::::::::::::::::::::::::::::::::
