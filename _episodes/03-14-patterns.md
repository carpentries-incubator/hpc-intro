---
title: "Pattern Rules"
teaching: 15
exercises: 0
questions:
- "How can I define rules to operate on similar files?"
objectives:
- "Write Snakemake pattern rules."
keypoints:
- "Use any named wildcard (`{some_name}`) as a placeholder in targets and dependencies."
---

Our Snakefile still has a ton of repeated content. The rules for each `.dat`
file all do the same thing for the part. We can
replace these rules with a single [pattern
rule]({{ page.root }}/reference/#pattern-rule) which can be used to build any
`.dat` file from a `.txt` file in `books/`:

~~~
rule count_words:
    input: 	
        wc='wordcount.py',
        book='books/{file}.txt'
    output: '{file}.dat'
    shell: 	'python {input.wc} {input.book} {output}'
~~~
{: .python}

`{file}` is another arbitrary [wildcard]({{ page.root }}/reference/#wildcard),
that we can use as a placeholder for any generic book to analyze.
Note that we don't have to use `{file}` as the name of our wildcard - 
it can be anything we want!

This rule can be interpreted as:
"In order to build a file named `[something].dat` (the target)
find a file named `books/[that same something].txt` (the dependency)
and run `wordcount.py [the dependency] [the target]`."

~~~
snakemake clean
# use the -p option to show that it is running things correctly!
snakemake -p dats   
~~~
{: .bash}

We should see the same output as before.
Note that we can still use snakemake to build individual `.dat` targets as before,
and that our new rule will work no matter what stem is being matched.

```
snakemake -p sierra.dat
```
{: .bash}

which gives the output below:

```
Provided cores: 1
Rules claiming more threads will be scaled down.
Job counts:
	count	jobs
	1	count_words
	1

rule count_words:
    input: wordcount.py, books/sierra.txt
    output: sierra.dat
    jobid: 0
    wildcards: file=sierra

python wordcount.py books/sierra.txt sierra.dat
Finished job 0.
1 of 1 steps (100%) done
```
{: .output}

> ## Using wildcards
>
> Our arbitrary wildcards like `{file}` can only be used in 
> `input:` and `output:` fields. It cannot be used in actions. 
{: .callout}

Our Makefile is now much shorter and cleaner:

~~~
# generate summary table
rule zipf_test:
    input:  'zipf_test.py', 'abyss.dat', 'last.dat', 'isles.dat'
    output: 'results.txt'
    shell:  'python {input[0]} {input[1]} {input[2]} {input[3]} > {output}'

rule dats:
     input:
         'isles.dat', 'abyss.dat', 'last.dat'

# delete everything so we can re-run things
rule clean:
    shell:  'rm -f *.dat results.txt'

# count words in one of our "books"
rule count_words:
    input: 	
        wc='wordcount.py',
        book='books/{file}.txt'
    output: '{file}.dat'
    shell: 	'python {input.wc} {input.book} {output}'
~~~
{: .python}
