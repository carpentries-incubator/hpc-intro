#!/usr/bin/env python3

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

    NUM_THREAD = NUM_BLOCK
    SZ = NUM_BLOCK*NUM_THREAD

    # Time how long it takes to estimate π.
    start_time = datetime.datetime.now()

    x_values = np.random.uniform(size=SZ)
    x_values = x_values.astype(np.float32)
    y_values = np.random.uniform(size=SZ)
    y_values = y_values.astype(np.float32)
    total_count = np.zeros((SZ,), dtype='int32')

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

    func = mod.get_function("calculatePi")

    func(cuda.In(x_values),cuda.In(y_values), cuda.InOut(total_count), grid=(NUM_BLOCK,1,1),block=(NUM_THREAD,1, 1))

    count = sum(total_count)

    # final calculation
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

