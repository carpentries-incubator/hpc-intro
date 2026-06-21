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
