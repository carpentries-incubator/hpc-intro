#!/usr/bin/env python3
import numpy as np
import sys

def inside_circle(total_count):
    x = np.random.uniform(size=total_count)
    y = np.random.uniform(size=total_count)
    radii = np.sqrt(x*x + y*y)
    count = len(radii[np.where(radii<=1.0)])
    return count

if __name__ == '__main__':
    n_samples = int(sys.argv[1])
    counts = inside_circle(n_samples)
    my_pi = 4.0 * counts / n_samples
    print(my_pi)
