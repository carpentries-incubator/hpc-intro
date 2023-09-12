#!/bin/bash -e

#SBATCH --job-name      my_job
#SBATCH --mem           300M
#SBATCH --time          00:15:00
#SBATCH --array         2

module load R/4.3.1-gimkl-2022a
Rscript array_sum.r
echo "Done!"
