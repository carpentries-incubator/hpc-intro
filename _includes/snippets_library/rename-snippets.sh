#!/bin/bash

# This script renames snippets from the argument directory in an effort
# to make the names more meaningful, thereby simplifying the process of
# porting to a new site.

if [[ $# != 1 ]] || [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; then
    echo "Please supply a folder name containing snippets for your site. This"
    echo "script will rename those snippets based on the script activity. E.g.,"
    echo "    $0 ComputeCanada_Graham_slurm"
    exit 1
fi

if [[ $(which git) == "" ]]; then
    echo "Error: This script requires git. Please install it and try again."
    exit 1
fi

PREFIX=$1

function rename_snip {
    git mv $1 $2
}

## Episode 12: Working on a remote HPC system

#$ {{ site.sched.info }}
rename_snip  ${PREFIX}/12/info.snip     ${PREFIX}/12/queue-info.snip
#$ sinfo -n {{ site.remote.node }} -o "%n %c %m"
rename_snip  ${PREFIX}/12/explore.snip  ${PREFIX}/12/specific-node-info.snip

## Episode 13: Scheduling jobs

# {{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh
rename_snip  ${PREFIX}/13/submit_output.snip           ${PREFIX}/13/basic-job-script.snip
#$ {{ site.sched.status }} {{ site.sched.flag.user }}
rename_snip  ${PREFIX}/13/statu_output.snip            ${PREFIX}/13/basic-job-status.snip
#$ {{ site.sched.status }} {{ site.sched.flag.user }}
rename_snip  ${PREFIX}/13/statu_name_output.snip       ${PREFIX}/13/job-with-name-status.snip
## The following are several key resource requests:
rename_snip  ${PREFIX}/13/stat_options.snip            ${PREFIX}/13/option-flags-list.snip
## Print SLURM_CPUS_PER_TASK, PBS_O_WORKDIR, or similar
rename_snip  ${PREFIX}/13/env_challenge.snip           ${PREFIX}/13/print-sched-variables.snip
#$ {{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh
rename_snip  ${PREFIX}/13/long_job_cat.snip            ${PREFIX}/13/runtime-exceeded-job.snip
#$ {{ site.sched.status }} {{ site.sched.flag.user }}
rename_snip  ${PREFIX}/13/long_job_err.snip            ${PREFIX}/13/runtime-exceeded-output.snip
#$ {{ site.sched.submit.name }} {{ site.sched.submit.options }} example-job.sh
#$ {{ site.sched.status }} {{ site.sched.flag.user }}
rename_snip  ${PREFIX}/13/del_job_output1.snip         ${PREFIX}/13/terminate-job-begin.snip
#$ {{site.sched.del }} 38759
rename_snip  ${PREFIX}/13/del_job_output2.snip         ${PREFIX}/13/terminate-job-cancel.snip
#$ {{site.sched.del }} {{ site.sched.flag.user }}
rename_snip  ${PREFIX}/13/del_multiple_challenge.snip  ${PREFIX}/13/terminate-multiple-jobs.snip
## use the compute node resources interactively
rename_snip  ${PREFIX}/13/interactive_example.snip     ${PREFIX}/13/using-nodes-interactively.snip

## Episode 14: Accessing software

#$ module avail
rename_snip  ${PREFIX}/14/module_avail.snip   ${PREFIX}/14/available-modules.snip
#$ which python
rename_snip  ${PREFIX}/14/which_missing.snip  ${PREFIX}/14/missing-python.snip
#$ module load python[3]
rename_snip  ${PREFIX}/14/load_python.snip    ${PREFIX}/14/module-load-python.snip
#$ which python
rename_snip  ${PREFIX}/14/which_python.snip   ${PREFIX}/14/python-executable-dir.snip
#$ echo $PATH
rename_snip  ${PREFIX}/14/path.snip           ${PREFIX}/14/python-module-path.snip
#$ ls $(dirname $(which python))
rename_snip  ${PREFIX}/14/ls_dir.snip         ${PREFIX}/14/python-ls-dir-command.snip
rename_snip  ${PREFIX}/14/ls_dir_output.snip  ${PREFIX}/14/python-ls-dir-output.snip
## Loading & unloading software and dependencies
rename_snip  ${PREFIX}/14/depend_demo.snip    ${PREFIX}/14/software-dependencies.snip
## gcc example
rename_snip  ${PREFIX}/14/gcc_example.snip    ${PREFIX}/14/wrong-gcc-version.snip

## Episode 15: Transferring files

## Episode 16: Using resources effectively

#$ {{ site.sched.hist }}
rename_snip  ${PREFIX}/16/stat_output.snip  ${PREFIX}/16/account-history.snip
#$ top
rename_snip  ${PREFIX}/16/top_output.snip   ${PREFIX}/16/monitor-processes-top.snip
#$ free -h
rename_snip  ${PREFIX}/16/free_output.snip  ${PREFIX}/16/system-memory-free.snip

## Episode 17: Using shared resources responsibly
