#!/bin/bash

#SBATCH --partition=short_free
#SBATCH --account=comet_training
#SBATCH --job-name=word-freq_array-test1
#SBATCH --nodes=1
#SBATCH --tasks=4
#SBATCH --array=1-4
#SBATCH --cpus-per-task=1

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
