```
$ cat example-job.sh
#!/bin/bash
#SBATCH -J new_name

echo 'This script is running on:'
hostname
sleep 120
$ sbatch example-job.sh
```
{: .bash}

```
[remote]$ squeue -u yourUsername
```
{: .bash}
```
   JOBID     USER ACCOUNT           NAME  ST REASON    START_TIME                TIME  TIME_LEFT NODES CPUS
   38191 yourUsername yourAccount       new_name  PD Priority  N/A                       0:00    1:00:00     1  1
```
{: .output}