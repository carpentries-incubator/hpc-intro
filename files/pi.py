#!/usr/bin/env python3

"""Parallel example code for estimating the value of pi.

We can estimate the value of pi by a stochastic algorithm.  Consider
a circle of radius 1, inside a square that bounds it, with vertices
at (1,1), (1,-1), (-1,-1), and (-1,1).  The area of the circle is
just pi, whereas the area of the square is 4.  So, the fraction of
the area of the square which is covered by the circle is pi/4.

A point selected at random uniformly from the square thus has a
probability pi/4 of being within the circle.

We can estimate pi by examining a large number of randomly-selected
points from the square, and seeing what fraction of them lie
within the circle.  If this fraction is f, then our estimate for
pi is pi ~ 4*f.  

This task lends itself naturally to parallelization -- the task
of selecting a sample point and deciding whether or not it's inside
the circle is independent of all the other samples, so they can
be done simultaneously.  We only need to aggregate the data at the
end to compute our fraction f and our estimate for pi.
"""
import sys
from mpi4py import MPI
import numpy as np

np.random.seed(2017)

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def inside_circle(total_count):
    """Single-processor task for a group of samples.

    Generates uniform random x and y arrays of size total_count, on
    the interval (-1,1), and returns the number of the resulting
    (x,y) pairs which lie inside the unit circle.
    """
    hname = MPI.Get_processor_name()
    print("Rank %d generating %d samples on host %s." % 
            (rank, total_count, hname))
    
    x = np.float32(np.random.uniform(size=total_count))
    y = np.float32(np.random.uniform(size=total_count))

    radii = np.sqrt(x*x + y*y)

    count = len(radii[np.where(radii<=1.0)])

    return count


if __name__=='__main__':
    """Main MPI executable.

    This conditional is entered as many times as there are MPI processes.

    Each process knows its index, called 'rank', and the number
    of ranks, called 'size', from the MPI calls at the top 
    of the module.

    Rank 0 divides the data arrays among the ranks (including itself), 
    then each rank independently runs the 'inside_circle' function
    with its share of the samples.  The disparate results are then
    aggregated via the 'gather' operation, and then the estimate
    for pi is computed.

    An estimate of the required memory is also computed.
    """
    
    n_samples = 100000
    if len(sys.argv) > 1:
        n_samples = int(sys.argv[1])

    if rank == 0:
        print("Generating %d samples." % n_samples)
        # Rank zero builds two arrays with one entry for each
        # rank, one for the number of samples they should run,
        # and one for them to store their count info.
        partitions = [ int(n_samples/size) for item in range(size)]
        counts = [ int(0) ] *size
    else:
        partitions = None
        counts = None

    # All ranks participate in the "scatter" operation,
    # which assigns the rank-local scalar variables to
    # their appropriate array components.  partition_item
    # is the number of samples this rank should generate,
    # and count_item is the place to put the number of
    # counts we see.
    partition_item = comm.scatter(partitions, root=0)
    count_item = comm.scatter(counts, root=0)

    # Each rank locally populates its count_item variable.
    count_item = inside_circle(partition_item)

    # All ranks participate in the "gather" operation, which
    # sums the rank's count_items into the total "counts".
    counts = comm.gather(count_item, root=0)
    if rank == 0:
        # Only rank zero writes the result, although it's known to all.
        my_pi = 4.0 * sum(counts) / n_samples
        sizeof = np.dtype(np.float32).itemsize
        print("[     mpi version] required memory %.3f MB" % (n_samples*sizeof*3/(1024*1024)))
        print("[using %3i cores ] pi is %f from %i samples" % (size,my_pi,n_samples))
