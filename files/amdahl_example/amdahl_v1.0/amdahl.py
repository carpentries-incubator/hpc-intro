#!/usr/bin/env python
"""
Amdahls law illustrator (with fake work)
"""

from mpi4py import MPI
import sys
import time
import argparse


def do_work(work_time=30, parallel_proportion=0.8, comm=MPI.COMM_WORLD):
    # How many MPI ranks (cores) are we?
    size = comm.Get_size()
    # Who am I in that set of ranks?
    rank = comm.Get_rank()
    # Where am I running?
    name = MPI.Get_processor_name()

    if rank == 0:
        # use Amdahls law to calculate the expected speedup for a given workload
        amdahl_speed_up = 1.0 / (
            (1.0 - parallel_proportion) + parallel_proportion / size
        )

        # Set the sleep times (which are used to fake the amount of work)
        serial_sleep_time = float(work_time) * (1.0 - parallel_proportion)
        parallel_sleep_time = (float(work_time) * parallel_proportion) / size

        sys.stdout.write(
            "Processors will do %s seconds of 'work', which should take %s seconds "
            "on %s cores with %s parallel proportion of the workload.\n"
            % (work_time, work_time / amdahl_speed_up, size, parallel_proportion)
        )

        sys.stdout.write(
            "Hello, World! I am process %d of %d on %s and I will do all the serial "
            "'work' for %s seconds.\n" % (rank, size, name, serial_sleep_time)
        )
        time.sleep(serial_sleep_time)
    else:
        parallel_sleep_time = None

    # Tell all processes how much work they need to do using 'bcast' to broadcast
    # (this also creates an implicit barrier, blocking processes until they recieve
    # the value)
    parallel_sleep_time = comm.bcast(parallel_sleep_time, root=0)

    # This is where everyone pretends to do work (while really we are just sleeping)
    sys.stdout.write(
        "Hello, World! I am process %d of %d on %s and I will do parallel 'work' for "
        "%s seconds.\n" % (rank, size, name, parallel_sleep_time)
    )
    time.sleep(parallel_sleep_time)


# Only the root process handles the command line arguments
rank = MPI.COMM_WORLD.Get_rank()
if rank == 0:
    # Start a clock to measure total time
    start = time.time()
    # Initialize our argument parser
    parser = argparse.ArgumentParser(prog="amdahl")

    # Adding optional arguments
    parser.add_argument(
        "-p",
        "--parallel-proportion",
        nargs="?",
        const=0.8,
        type=float,
        default=0.8,
        help="Parallel proportion should be a float between 0 and 1",
    )
    parser.add_argument(
        "-w",
        "--work-seconds",
        nargs="?",
        const=30,
        type=int,
        default=30,
        help="Total seconds of workload, should be an integer greater than 0",
    )

    # Read arguments from command line
    args = parser.parse_args()

    if not args.work_seconds > 0:
        parser.print_help()
        MPI.COMM_WORLD.Abort(1)
        sys.exit(1)

    if args.parallel_proportion <= 0 or args.parallel_proportion > 1:
        parser.print_help()
        MPI.COMM_WORLD.Abort(1)
        sys.exit(1)

    do_work(work_time=args.work_seconds, parallel_proportion=args.parallel_proportion)
    end = time.time()
    sys.stdout.write(
        "Total execution time (according to rank 0): %s seconds\n" % (end - start)
    )
else:
    do_work()
