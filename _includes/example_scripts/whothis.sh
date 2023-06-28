#!/bin/bash

echo "I am task #${SLURM_PROCID} running on node '$(hostname)' with $(nproc) CPUs"