#!/usr/bin/env python3

"""
Parallel code to extract mean, min, and max of Nelle Nemo's assay results
"""

import locale as l10n
from mpi4py import MPI
import numpy as np
import os
import sys
l10n.setlocale(l10n.LC_ALL, "")

# Declare an MPI Communicator for the parallel processes to talk through
comm = MPI.COMM_WORLD

# Read the number of parallel processes tied into the comm channel
cpus = comm.Get_size()

# Find out the index ("rank") of *this* process
rank = comm.Get_rank()


def list_assay_files(path):
    """
    Walk the specified path, using one rank *only*.
    Record NENE*.txt files labeled A or B (not Z).
    Return list of file paths.
    """
    if rank != 0:
        print("Rank {} tried scanning the directory.".format(rank))
        sys.exit()

    valid_names = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.startswith("NENE") and f.endswith(("A.txt", "B.txt")):
                fullpath = os.path.join(root, f)
                valid_names.append(fullpath)

    return valid_names


def partition_files(list_of_files, number_of_parts):
    """
    Split the provided list of files into a number of roughly-equal parts
    """
    return np.array_split(list_of_files, number_of_parts)


def get_local_file_names(path):
    if rank == 0:
        # Let only one MPI process scan the directory for files.
        all_files = list_assay_files(path)
        partitions = partition_files(all_files, cpus)
    else:
        partitions = []

    # Every rank gets its own chunk of the list of assay files.
    # This function is *blocking*: no rank returns until all are able to.
    return comm.scatter(partitions, root = 0)


def extract_concentrations(goo_file):
    """
    Read file `goo_file` into NumPy array.
    Return array if it contains 300 entries.
    """
    concentrations = np.loadtxt(goo_file)
    if len(concentrations) != 300:
        return None
    return concentrations


def get_assay_results(files):
    # Every rank reads their private list of files into NumPy arrays
    concentrations = []
    for f in files:
        result = extract_concentrations(f)
        if result is not None:
            concentrations.append(result)

    print("Rank {} crunched data from {} files.".format(comm.Get_rank(), len(concentrations)))

    # Convert list of NumPy arrays into a 2-D NumPy array
    return np.array(concentrations)


# "Main" program

if __name__ == '__main__':
    """
    This program is entered as many times as there are MPI processes.

    Each process knows its index, called 'rank', and the number of
    ranks, called 'cpus', from the MPI calls at the top of the module.
    """

    # Guard against improper invocations of the program

    usage_string = "Usage:\n    mpirun -np {} {} directory_name"

    if len(sys.argv) != 2 or sys.argv[1] == "--help":
        if rank == 0:
            print(usage_string.format(cpus, sys.argv[0]))
            sys.exit()

    # Distribute assay files in the specified directory to the parallel ranks
    path = sys.argv[1]
    files = get_local_file_names(path)

    # Read local set of files into NumPy array -- ignoring partial results
    concentrations = get_assay_results(files)

    # Calculate the total number of valid assay results from local numbers
    valid_results = len(concentrations) # local
    valid_results = comm.reduce(valid_results) # global

    # For each protein, collect the mean, min, and max values from all files
    assay_avg = np.sum(concentrations, axis=0).tolist()
    assay_min = np.amin(concentrations, axis=0).tolist()
    assay_max = np.amax(concentrations, axis=0).tolist()

    for i in range(len(assay_avg)):
        assay_avg[i] = comm.reduce(assay_avg[i], op=MPI.SUM)
        assay_min[i] = comm.reduce(assay_min[i], op=MPI.MIN)
        assay_max[i] = comm.reduce(assay_max[i], op=MPI.MAX)

    # Generate the global report using Rank 0, only
    if rank == 0:
        assay_avg = np.divide(assay_avg, valid_results)
        csv_name = "{}.csv".format(path.rstrip("/")) # prevent "path/.csv", which would be a hidden file
        with open(csv_name, "w") as csv:
            print("mean,min,max", file=csv)
            for a, n, x in zip(assay_avg, assay_min, assay_max):
                print("{},{},{}".format(a, n, x), file=csv)
