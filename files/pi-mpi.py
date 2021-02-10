#!/usr/bin/env python3

"""Parallel example code for estimating the value of π.

We can estimate the value of π by a stochastic algorithm. Consider a
circle of radius 1, inside a square that bounds it, with vertices at
(1,1), (1,-1), (-1,-1), and (-1,1). The area of the circle is just π,
whereas the area of the square is 4. So, the fraction of the area of the
square which is covered by the circle is π/4.

A point selected at random uniformly from the square thus has a
probability π/4 of being within the circle.

We can estimate π by examining a large number of randomly-selected
points from the square, and seeing what fraction of them lie within the
circle. If this fraction is f, then our estimate for π is π ≈ 4f.

Thanks to symmetry, we can compute points in one quadrant, rather
than within the entire unit square, and arrive at identical results.

This task lends itself naturally to parallelization -- the task of
selecting a sample point and deciding whether or not it's inside the
circle is independent of all the other samples, so they can be done
simultaneously. We only need to aggregate the data at the end to compute
our fraction f and our estimate for π.
"""

import numpy as np
import sys
import datetime
from mpi4py import MPI


def inside_circle(total_count):
    """Single-processor task for a group of samples.

    Generates uniform random x and y arrays of size total_count, on the
    interval [0,1), and returns the number of the resulting (x,y) pairs
    which lie inside the unit circle.
    """

    host_name = MPI.Get_processor_name()
    print("Rank {} generating {:n} samples on host {}.".format(
            rank, total_count, host_name))
    x = np.float64(np.random.uniform(size=total_count))
    y = np.float64(np.random.uniform(size=total_count))

    radii = np.sqrt(x*x + y*y)

    count = len(radii[np.where(radii<=1.0)])

    return count


if __name__ == '__main__':
    """Main executable.

    This function runs the 'inside_circle' function with a defined number
    of samples. The results are then used to estimate π.

    An estimate of the required memory, elapsed calculation time, and
    accuracy of calculating π are also computed.
    """

    # Declare an MPI Communicator for the parallel processes to talk through
    comm = MPI.COMM_WORLD

    # Read the number of parallel processes tied into the comm channel
    cpus = comm.Get_size()

    # Find out the index ("rank") of *this* process
    rank = comm.Get_rank()

    if len(sys.argv) > 1:
        n_samples = int(sys.argv[1])
    else:
        n_samples = 8738128 # trust me, this number is not random :-)

    if rank == 0:
        # Time how long it takes to estimate π.
        start_time = datetime.datetime.now()
        print("Generating {:n} samples.".format(n_samples))
        # Rank zero builds two arrays with one entry for each rank:
        # one for the number of samples they should run, and
        # one to store the count info each rank returns.
        partitions = [ int(n_samples / cpus) ] * cpus
        counts = [ int(0) ] * cpus
    else:
        partitions = None
        counts = None

    # All ranks participate in the "scatter" operation, which assigns
    # the local scalar values to their appropriate array components.
    # partition_item is the number of samples this rank should generate,
    # and count_item is the place to put the number of counts we see.
    partition_item = comm.scatter(partitions, root=0)
    count_item = comm.scatter(counts, root=0)

    # Each rank locally populates its count_item variable.
    count_item = inside_circle(partition_item)

    # All ranks participate in the "gather" operation, which sums the
    # rank's count_items into the total "counts".
    counts = comm.gather(count_item, root=0)

    if rank == 0:
        # Only rank zero writes the result, although it's known to all.
        my_pi = 4.0 * sum(counts) / n_samples
        elapsed_time = (datetime.datetime.now() - start_time).total_seconds()

        # Memory required is dominated by the size of x, y, and radii from
        # inside_circle(), calculated in MiB
        size_of_float = np.dtype(np.float64).itemsize
        memory_required = 3 * n_samples * size_of_float / (1024**2)

        # accuracy is calculated as a percent difference from a known estimate
        # of π.
        pi_specific = np.pi
        accuracy = 100*(1-my_pi/pi_specific)

        # Uncomment either summary format for verbose or terse output
        # summary = "{:d} core(s), {:d} samples, {:f} MiB memory, {:f} seconds, {:f}% error"
        summary = "{:d},{:d},{:f},{:f},{:f}"
        print(summary.format(cpus, n_samples, memory_required, elapsed_time,
                            accuracy))
