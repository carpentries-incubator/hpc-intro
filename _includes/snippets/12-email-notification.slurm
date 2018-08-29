> ## Setting up email notifications
> 
> Jobs on an HPC system might run for days or even weeks.
> We probably have better things to do than constantly check on the status of our job
> with `squeue`.
> Looking at the [online documentation for `sbatch`](https://slurm.schedmd.com/sbatch.html)
> (you can also google "sbatch slurm"),
> can you set up our test job to send you an email when it finishes?
> 
> Hint: you will need to use the `--mail-user` and `--mail-type` options.
{: .challenge}