#!/usr/bin/env python3
import numpy as np
import sys
from mpi4py import MPI

def inside_circle(total_count):
    x = np.random.uniform(size=total_count)
    y = np.random.uniform(size=total_count)
    radii = np.sqrt(x*x + y*y)
    count = len(radii[np.where(radii<=1.0)])
    return count

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    cpus = comm.Get_size()
    rank = comm.Get_rank()
    n_samples = int(sys.argv[1])
    if rank == 0:
        partitions = [ int(n_samples / cpus) ] * cpus
        counts = [ int(0) ] * cpus
    else:
        partitions = None
        counts = None
    partition_item = comm.scatter(partitions, root=0)
    count_item = inside_circle(partition_item)
    counts = comm.gather(count_item, root=0)
    if rank == 0:
        my_pi = 4.0 * sum(counts) / sum(partitions)
        print(my_pi)
