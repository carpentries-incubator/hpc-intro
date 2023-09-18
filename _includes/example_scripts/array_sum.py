#!/usr/bin/env python3

from multiprocessing import Pool
import numpy as np
import os


def do_par(z):
    p_complete = z * 100 / size_x
    if p_complete % 1 == 0:
        print("{0:.0f}% done...".format(p_complete))
    return sum(rng.random(size_y))


num_cpus = int(os.getenv("SLURM_CPUS_PER_TASK", "1"))
size_x = 60000  # This on makes memorier
size_y = 20000  # This one to make longer

# Time = (size_x/n) * size_y + c
# Mem  = (size_x * n) * c1 + size_y * c2

print("Using {0} cpus to sum [ {1:e} x {2:e} ] matrix.".format(num_cpus, size_x, size_y))

rng = np.random.default_rng(seed=int(os.getenv('SLURM_ARRAY_TASK_ID', "0")))

with Pool(processes=num_cpus) as pool:

    results = pool.map(do_par, range(size_x))

print("Sum is '{0:f}'.".format(sum(results)))