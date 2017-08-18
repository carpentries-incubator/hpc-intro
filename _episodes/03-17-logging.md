---
title: "Logging"
teaching: 15
exercises: 0
questions:
- "How do I manage logs from parallel processes?"
objectives:
- "Set standardized log files for each rule type."
keypoints:
- "The `log` keyword/wildcard is a useful tool for managing logfiles."
- "Use `&&` to ensure that shell commands are only executed if previous commands were successful."
---

By default, Snakemake prints all output from stderr and stdout from rules.
This is useful, but if a failure occurs (or we otherwise need to inspect the logs)
it can be extremely difficult to determine what happened
or which rule had an issue.

The solution to this issue is to redirect the output from each rule/
set of inputs to a dedicated logfile.
We can do this using the `log` keyword.
Let's modify our `count_words` rule to be slighly more verbose and redirect
this output to a dedicated logfile.

Two things before we start:

* `&>` is a handy operator in bash that redirects both stdout and stderr to a file.
* `&>>` does the same thing as `&>`, but appends to a file instead of overwriting it.

```
# count words in one of our "books"
rule count_words:
    input: 	
        wc='wordcount.py',
        book='books/{file}.txt'
    output: 'dats/{file}.dat'
    threads: 4
    log: 'dats/{file}.log'
    shell:
        '''
        echo "Running {input.wc} with {threads} cores on {input.book}." &> {log}
        python {input.wc} {input.book} {output} &>> {log}
        '''
```
{: .python}

```
snakemake clean
snakemake -j 8
cat dats/abyss.log
```
{: .bash}
```
# snakemake output omitted
Running wordcount.py with 4 cores on books/abyss.txt.
```
{: .output}

Notice how the pipeline no longer prints to the pipeline's log, 
and instead redirects this to a logfile.

> ## Choosing a good logfile location
> 
> Though you can put a log anywhere (and name it anything),
> it is often a good practice to put the log in the same directory
> where the rule's output will be created.
> If you need to investigate the output for a rule and associated logfiles,
> this means that you only have to check one location!
{: .callout}

