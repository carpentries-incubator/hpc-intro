#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys

try:
    serial_file = sys.argv[1]
except IndexError:
    print("you did not specify a serial timing file")
    print("Usage: {} serial_file".format(sys.argv[0]))
    sys.exit(1)

data = np.loadtxt(serial_file, delimiter=',', skiprows=1)
cores = data[0, 0]
n_samples = data[:, 1]
memory_required = data[:, 2]
elapsed_time = data[:, 3]
accuracy = data[:, 4]

plot_dict = { 'Memory (MiB)': memory_required,
              'Elapsed time (s)': elapsed_time,
              'Percent accuracy': accuracy }

for label in plot_dict:
    value = plot_dict[label]
    plt.figure()
    plt.plot(n_samples, value, 's')
    plt.xlabel('Number of samples')
    plt.ylabel(label)
    plt.title('Serial π calculator results')
    filename = label.replace(' ', '_')
    plt.savefig('{:s}'.format('serial_'+filename))
