#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
import locale

try:
    parallel_file = sys.argv[1]
except IndexError:
    print("you did not specify a parallel timing file")
    print("Usage: {} parallel_file serial_file".format(sys.argv[0]))
    sys.exit(1)
try:
    serial_file = sys.argv[2]
except IndexError:
    print("you did not specify a serial timing file")
    print("Usage: {} parallel_file serial_file".format(sys.argv[0]))
    sys.exit(1)

locale.setlocale(locale.LC_ALL, "")

data = np.genfromtxt(parallel_file, delimiter=',')
cores = data[:, 0]
n_samples = data[0, 1]
memory_required = data[:, 2]
elapsed_time = data[:, 3]
accuracy = data[:, 4]

data_serial = np.genfromtxt(serial_file, delimiter=',')
n_samples_serial = data_serial[:, 1]
baseline_row = int(np.argwhere(n_samples_serial==n_samples))
baseline_values = data_serial[baseline_row, :]

serial_time = data_serial[baseline_row, 3]
speedup = serial_time/elapsed_time
print("Serial time: {}, speedup: {}".format(serial_time, speedup))

plot_dict = { 'Elapsed time (s)': elapsed_time,
              'Speedup factor': speedup, }

for label in plot_dict:
    value = plot_dict[label]
    plt.figure()
    plt.plot(cores, value, 's')
    plt.xlabel('Number of cores')
    plt.ylabel(label)
    plt.title('MPI π calculator results ({:n} samples)'.format(int(n_samples)))
    if (label == 'Speedup factor'):
        for proportion in [0.5, 0.75, 0.9, 0.95, 0.99]:
            amdahl_cores = np.arange(cores.max())+1
            amdahl_speedup = 1.0/((1-proportion)+proportion/amdahl_cores)
            plt.plot(amdahl_cores, amdahl_speedup,
                     label='{}% parallel efficiency'.format(100*proportion))
        plt.legend()
        plt.grid()
    filename = label.replace(' ', '_')
    plt.savefig('{:s}'.format('mpi_'+filename))
