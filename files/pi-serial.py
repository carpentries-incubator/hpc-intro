#!/usr/bin/env python3

"""Serial example code for estimating the value of π.

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
"""

import numpy as np
import sys
import datetime


def inside_circle(total_count):
    """Single-processor task for a group of samples.

    Generates uniform random x and y arrays of size total_count, on the
    interval [0,1), and returns the number of the resulting (x,y) pairs
    which lie inside the unit circle.
    """

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

    if len(sys.argv) > 1:
        n_samples = int(sys.argv[1])
    else:
        n_samples = 8738128 # trust me, this number is not random :-)

    # Time how long it takes to estimate π.
    start_time = datetime.datetime.now()
    counts = inside_circle(n_samples)
    my_pi = 4.0 * counts / n_samples
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
    print(summary.format(1, n_samples, memory_required, elapsed_time,
                         accuracy))
