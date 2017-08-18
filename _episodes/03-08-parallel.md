---
title: "Running code in parallel"
menu: main
weight: 9
---

Python does not thread very well.
Specifically, Python has what's known as a Global Interpreter Lock (GIL).
The GIL ensures that only one thread can run at a time.
This can make multithreaded processing very difficult.
Instead, the best way to go about doing things is to use multiple independent processes to perform the computations.
This method skips the GIL,
as each individual process has it's own GIL that does not block the others.
This is typically done using the `multiprocessing` module.

Before we start, we will need the number of CPU cores in our computer.
To get the number of cores in our computer, we can use the `psutil` module.
We are using `psutil` instead of `multiprocessing` because `psutil` counts cores instead of threads.
Long story short, cores are the actual computation units, 
threads allow additional multitasking using the cores you have.
For heavy compute jobs, you are generally interested in cores.

```
import psutil
# logical=True counts threads, but we are interested in cores
psutil.cpu_count(logical=False)
```
```
8
```

Using this number, we can create a pool of worker processes withh which to parallelize our jobs:

```
from multiprocessing import Pool
pool = Pool(psutil.cpu_count(logical=False))
```

The `pool` object gives us a set of parallel workers we can
use to parallelize our calculations.
In particular, there is a map function
(with identical syntax to the `map()` function used earlier),
that runs a workflow in parallel.

Let's try `map()` out with a test function that just runs sleep.

```
import time

def sleeping(arg):
    time.sleep(0.1)

%timeit list(map(sleeping, range(24)))
%timeit pool.map(sleeping, range(24))
```
```
1 loop, best of 3: 2.4 s per loop
1 loop, best of 3: 302 ms per loop
```

That worked nicely! However what happens when we try a lambda function?

```
pool.map(lambda x: time.sleep(0.1), range(24))
```
```
---------------------------------------------------------------------------
PicklingError                             Traceback (most recent call last)
<ipython-input-10-df8237b4b421> in <module>()
----> 1 pool.map(lambda x: time.sleep(0.1), range(24))

# more errors omitted
```

The `multiprocessing` module has a major limitation:
it only accepts certain functions, and in certain situations.
For instance any class methods, lambdas, or functions defined in `__main__` wont' work.
This is due to the way Python "pickles" (read: serializes) data
and sends it to the worker processes.
"Pickling" simply can't handle a lot of different types of Python objects.

Fortunately, there is a fork of the `multiprocessing` module called `multiprocess` 
that works just fine (`pip install --user multiprocess`). 
`multiprocess` uses `dill` instead of `pickle` to serialize Python objects,
and does not suffer the same issues.
Usage is identical:

```
# shut down the old workers
pool.close()

from multiprocess import Pool
pool = Pool(8)
%timeit pool.map(lambda x: time.sleep(0.1), range(24))
pool.close()
```
```
1 loop, best of 3: 309 ms per loop
```

{{<admonition title="Chunk size" type="note">}}
The `chunksize` argument lets you process data in chunks, 
cutting down time lost to inter-process communication.
{{</admonition>}}

## [Next section](../sm-intro/)


