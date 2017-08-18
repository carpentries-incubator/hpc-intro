---
title: "Measuring code speed"
menu: main
weight: 7
---

## What is the fastest way of doing things?

We already know how to measure the execution speed of a piece of code (or block of code) with `%timeit`.
`%timeit` is a magic function from IPython - 
the only catch is that it must be used from an IPython interpreter.
However, the major advantage of using `%timeit` is that you don't have to import anything, 
and you'll never accidentally choose the wrong number of iterations to time 
(and get stuck waiting forever for your timing results to come back).

To review:

`%timeit` - times a single line.

```
%timeit [1] * 10000
```
```
10000 loops, best of 3: 35.1 µs per loop
```

`%%timeit` - times an IPython cell.

```
%%timeit
last = 0
for i in range(10000):
	last += i
```
```
1000 loops, best of 3: 866 µs per loop
```

## Profiling code

Though the above technique tells you which of two pieces of code is faster, 
it does not identify which portion of code is the slowest.
Profiling code allows us to identify areas for improvement.

Python ships with a profling module called `cProfile`. 
`cProfile` lets us see exactly how long was used to run each line of code as well as all internal calls made by a function.
Slower code will have longer execution times,
and is an area of an improvement for us to focus our efforts on.

To profile a block of code, we use the `cProfile.run()` function
(the code to profile is input as a string).

```
cProfile.run(
'''
test = np.arange(10000000)
np.sin(test)
'''
)
```
```
         4 function calls in 0.519 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.468    0.468    0.519    0.519 <string>:2(<module>)
        1    0.000    0.000    0.519    0.519 {built-in method builtins.exec}
        1    0.050    0.050    0.050    0.050 {built-in method numpy.core.multiarray.arange}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

## Profiling script execution

We can also profile scripts from the command-line using the following syntax
(the `-s cumtime` sorts code by cumulative time spent in each function):

`python3 -m cProfile -s cumtime some_script.py`

However, this is not super useful, especially if the call stack is huge (it can be really tough to interpret the results!)
There is a nice visualizer called "Snakeviz" we can use to get around this.

For this demo, make sure you've got the `requests` and `snakeviz` modules installed:
```
pip install --user requests snakeviz
```

Now create a script that looks like the following (called "iss.py"?):

```
import requests

r = requests.get('http://api.open-notify.org/iss-now.json')
server_response = r.json()
iss_location = server_response['iss_position']

print('The International Space Station is currently at {}, {}'.
        format(iss_location['latitude'], iss_location['longitude']))
```

We can create a profile of our program with the following commands:

```
python3 -m cProfile -o iss.profile iss.py
snakeviz iss.profile
```

You now have a way to visualize our code execution.
Looking at the code profile, the vast majority of time was actually spent importing the requests module, 
with a small amount of time spent performing the HTTP request (`requests.get()`).

## [Next section](../performance/)

