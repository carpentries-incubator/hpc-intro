---
title: "Resources and parallelism"
teaching: 30
exercises: 15
questions:
- "How do I scale a pipeline across multiple cores?"
- "How do I manage access to resources while working in parallel?"
objectives:
- "Modify your pipeline to run in parallel."
keypoints:
- "Use `threads` to indicate the number of cores used by a rule."
- "Resources are arbitrary and can be used for anything."
- "The `&&` operator is a useful tool when chaining bash commands."
---

After the excercises at the end of our last lesson, 
our Snakefile looks something like this:

```
# our zipf analysis pipeline
DATS = glob_wildcards('books/{book}.txt').book

rule all:
    input:
        'zipf_analysis.tar.gz'

# delete everything so we can re-run things
rule clean:
    shell:  
        '''
        rm -rf results dats plots
        rm -f results.txt zipf_analysis.tar.gz
        '''

# count words in one of our "books"
rule count_words:
    input: 	
        wc='wordcount.py',
        book='books/{file}.txt'
    output: 'dats/{file}.dat'
    shell: 	'python {input.wc} {input.book} {output}'

# create a plot for each book
rule make_plot:
    input:
        plotcount='plotcount.py',
        book='dats/{file}.dat'
    output: 'plots/{file}.png'
    shell:  'python {input.plotcount} {input.book} {output}'

# generate summary table
rule zipf_test:
    input:  
        zipf='zipf_test.py',
        books=expand('dats/{book}.dat', book=DATS)
    output: 'results.txt'
    shell:  'python {input.zipf} {input.books} > {output}'

# create an archive with all of our results
rule make_archive:
    input:
        expand('plots/{book}.png', book=DATS),
        expand('dats/{book}.dat', book=DATS),
        'results.txt'
    output: 'zipf_analysis.tar.gz'
    shell: 'tar -czvf {output} {input}'
```
{: .python}

At this point, we have a complete data analysis pipeline.
Very cool.
But how do we make it run as efficiently as possible?

## Running in parallel

Up to this point, Snakemake has printed out an interesting message
whenever we run our pipeline.

```
Provided cores: 1
Rules claiming more threads will be scaled down.
```
{: .output}

So far, Snakemake has been run with one core.
Let's scale up our pipeline to run in parallel.
The only change we need to make is run Snakemake with the `-j` argument.
`-j` is used to indicate number of CPU cores available, 
and on a cluster, maximum number of jobs (we'll get to that part later).

```
snakemake clean
snakemake -j 4    # 4 cores is usually a safe assumption when working on a laptop/desktop
```
{: .bash}
```
Provided cores: 4
Rules claiming more threads will be scaled down.
# more output follows
```
{: .output}

Our pipeline ran in parallel and finished roughly 4 times as quickly!
The takeaway here is that all we need to do to scale from a 
serial pipeline is run `snakemake` with the `-j` option.

> ## How many CPUs does your computer have?
>
> Now that we can have our pipeline use multiple CPUs,
> how do we know how many CPUs to provide to the `-j` option?
> Note that for all of these options, it's best to use CPU cores,
> and not CPU threads.
>
> **Linux** - You can use the `lscpu` command.
>
> **All platforms** - Python's `psutil` module can be used to fetch the number of cores in your computer.
> Using `logical=False` returns the number of true CPU cores.
> `logical=True` gives the number of CPU threads on your system.
> 
> ```
> import psutil
> psutil.cpu_count(logical=False)
> ```
> {: .python}
{: .callout}

## Managing CPUs

Each rule has a number of optional keywords aside from the usual
`input`, `output`, and `shell`/`run`.
The `threads` keyword is used to specify how many CPU cores a rule
needs while executing.
Though in reality CPU threads are not quite the same as CPU cores, 
the two terms are interchangeable when working with Snakemake.

Let's pretend that our `count_words` rule is actually very CPU-intensive.
We'll say that it needs a whopping 4 CPUs per run.
We can specify this with the `threads` keyword in our rule.
We will also modify the rule to print out the number of threads it thinks it is using.
Please note that just giving something 4 threads in Snakemake does not make it run in parallel!
In this case `wordcount.py` is actually still running with 1 core, 
we are simply using it as a demonstration of how to go about 
running something with multiple cores.

```
rule count_words:
    input: 	
        wc='wordcount.py',
        book='books/{file}.txt'
    output: 'dats/{file}.dat'
    threads: 4
    shell:
        '''
        echo "Running {input.wc} with {threads} cores."
        python {input.wc} {input.book} {output}
        '''
```
{: .python}

Now, when we run `snakemake -j 4`, the `count_words` rules are run one at a time,
so as to give each execution the resources it needs.
All of our other rules will still run in parallel.
Unless otherwise specified with `{threads}`, rules will use 1 core by default.

```
Provided cores: 4
Rules claiming more threads will be scaled down.
Job counts:
	count	jobs
	1	all
	4	count_words
	1	make_archive
	4	make_plot
	1	zipf_test
	11

rule count_words:
    input: wordcount.py, books/last.txt
    output: dats/last.dat
    jobid: 3
    wildcards: file=last
    threads: 4

Running wordcount.py with 4 cores.
Finished job 3.
1 of 11 steps (9%) done

# other output follows
```
{: .python}

What happens when we don't have 4 cores available?
What if we tell Snakemake to run with 2 cores instead?

```
snakemake -j 2
```
{: .bash}
```
Provided cores: 2
Rules claiming more threads will be scaled down.
Job counts:
	count	jobs
	1	all
	4	count_words
	1	make_archive
	4	make_plot
	1	zipf_test
	11

rule count_words:
    input: wordcount.py, books/last.txt
    output: dats/last.dat
    jobid: 6
    wildcards: file=last
    threads: 2

Running wordcount.py with 2 cores.
Finished job 6.
1 of 11 steps (9%) done

# more output below
```
{: .output}

The key bit of output is `Rules claiming more threads will be scaled down.`.
When Snakemake doesn't have enough cores to run a rule (as defined by `{threads}`),
Snakemake will run that rule with the maximum available number of cores instead.
After all, Snakemake's job is to get our workflow done.
It automatically scales our workload to match the maximum number of cores available
without us editing the Snakefile.

## Chaining multiple commands

Up until now, all of our commands have fit on one line.
To execute multiple bash commands, the only modification we need to make
is use a Python multiline string (begin and end with `'''`)

One important addition we should be aware of is the `&&` operator.
`&&` is a bash operator that runs commands as part of a chain. 
If the first command fails, the remaining steps are not run.
This is more forgiving than bash's default "hit an error and keep going" behavior.
After all, if the first command failed, it's unlikely the other steps will work.

```
# count words in one of our "books"
rule count_words:
    input: 	
        wc='wordcount.py',
        book='books/{file}.txt'
    output: 'dats/{file}.dat'
    threads: 4
    shell:
        '''
        echo "Running {input.wc} with {threads} cores on {input.book}." &&
            python {input.wc} {input.book} {output}
        '''
```
{: .python}


## Managing other types of resources

Not all compute resources are CPUs. 
Examples might include limited amounts of RAM, number of GPUs, database locks, 
or perhaps we simply don't want multiple processes writing to the same file at once.
All non-CPU resources are handled using the `resources` keyword.

For our example, let's pretend that creating a plot with `plotcount.py` 
requires dedicated access to a GPU (it doesn't),
and only one GPU is available.
How do we indicate this to Snakemake so that it knows to give dedicated access to a GPU
for rules that need it?
Let's modify the `make_plot` rule as an example:

```
# create a plot for each book
rule make_plot:
    input:
        plotcount='plotcount.py',
        book='dats/{file}.dat'
    output: 'plots/{file}.png'
    resources: gpu=1
    shell:  'python {input.plotcount} {input.book} {output}'
```
{: .python}

We can execute our pipeline using the following (using 8 cores and 1 gpu):

```
snakemake clean
snakemake -j 8 --resources gpu=1
```
{: .bash}
```
Provided cores: 8
Rules claiming more threads will be scaled down.
Provided resources: gpu=1
# other output removed for brevity
```
{: .output}

Resources are entirely arbitrary - like wildcards, they can be named anything.
Snakemake knows nothing about them aside from the fact that they have a name and a value.
In this case `gpu` indicates simply that there is a resource called `gpu` used by `make_plot`.
We provided 1 `gpu` to the workflow, and the `gpu` is considered in use as long as the rule is running.
Once the `make_plot` rule completes, the `gpu` it consumed is added back to the pool of available `gpu`s.

But what happens if we run our pipeline without specifying the number of GPUs?

```
snakemake clean
snakemake -j 8
```
{: .bash}
```
Provided cores: 8
Rules claiming more threads will be scaled down.
Unlimited resources: gpu
```
{: .output}

If you have specified that a rule needs a certain resource, 
but do not specify how many you have, 
Snakemake will assume that the resources in question are unlimited.

> ## Other uses for `resources`
> 
> Resources do not have to correspond to actual compute resources.
> Perhaps one rule is particularly I/O heavy, 
> and it's best if only a limited number of these jobs run at a time.
> Or maybe a type of rule uses a lot of network bandwidth as it downloads data.
> In all of these cases, `resources` can be used to constrain access 
> to arbitrary compute resources so that each rule can run at it's most efficient.
> Snakemake will run your rules in such a way as to maximize throughput given your
> resource constraints.

