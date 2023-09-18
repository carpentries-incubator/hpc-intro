#!/bin/bash -e

module load R/4.3.1-gimkl-2022a
Rscript array_sum.r
echo "Done!"