#!/bin/bash -e

#SBATCH --job-name      my_job
#SBATCH --mem           300M
#SBATCH --time          00:15:00
#SBATCH --array         2

module load R/4.1.0-gimkl-2020a
Rscript array_sum.r
echo "Done!"
