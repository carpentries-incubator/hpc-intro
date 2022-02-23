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

import pycuda.driver as cuda
from pycuda.compiler import SourceModule
import pycuda.autoinit
import sys
import datetime 
import numpy as np

def main():

    if len(sys.argv) > 1:
        NUM_BLOCK = int(sys.argv[1])
    else:
        NUM_BLOCK = 512 

    # Set number of grid block size same as thread block size 
    NUM_THREAD = NUM_BLOCK

    # Set number of samples to be the number of thread blocks 
    # by the number of threads per block
    SZ = NUM_BLOCK*NUM_THREAD

    # Time how long it takes to estimate π.
    start_time = datetime.datetime.now()

    # Initialise x and y values to be used in estimation
    x_values = np.random.uniform(size=SZ)
    x_values = x_values.astype(np.float32)
    y_values = np.random.uniform(size=SZ)
    y_values = y_values.astype(np.float32)

    # Initialise the number of counts found inside the circle to be used in estimation
    total_count = np.zeros((SZ,), dtype='int32')

    # This is the GPU kernel, defined in C and read in as a string.
    # The "__global__" keyword indicates the function is intended to be called from the
    # host and run on the GPU.
    # The variable "tid" calculates the current thread ID. Each thread performs the estimation
    # of one sample.			
    mod = SourceModule("""
    __global__ void calculatePi(float *x_values, float *y_values, int *total_count) {
            int tid = threadIdx.x + blockIdx.x * blockDim.x;
                if ((x_values[tid] * x_values[tid]) + (y_values[tid] * y_values[tid]) < 1.0f) {
                    total_count[tid] = 1;
                }
                else{
                    total_count[tid] = 0;
                }    
    }
        """)

    # "get_function" enables the GPU kernel to be called in PyCUDA 
    func = mod.get_function("calculatePi")

    # Now the GPU kernel is called with three array inputs and two further inputs determining the
    # grid block size and thread block size 
    func(cuda.In(x_values),cuda.In(y_values), cuda.InOut(total_count), grid=(NUM_BLOCK,1,1),block=(NUM_THREAD,1, 1))

    # Sum up the total number of points counted
    count = sum(total_count)

    # final calculation of pi
    my_pi = (4.0 * count) / SZ

    elapsed_time = (datetime.datetime.now() - start_time).total_seconds()

    # Memory required is dominated by the size of x, y, and radii from
    # inside_circle(), calculated in MiB
    size_of_float = np.dtype(np.float64).itemsize
    memory_required = 3 * SZ * size_of_float / (1024**2)

    # accuracy is calculated as a percent difference from a known estimate
    # of π.
    pi_specific = np.pi
    accuracy = 100*(1-my_pi/pi_specific)

    # Uncomment either summary format for verbose or terse output
    # summary = "{:d} threads, {:d} samples, {:f} MiB memory, {:f} seconds, {:f}% error"
    summary = "{:d},{:d},{:f},{:f},{:f}"
    print(summary.format(SZ, SZ, memory_required, elapsed_time, accuracy))




if __name__ == '__main__':
    main()

