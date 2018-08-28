---
title: "Wildcards and pipes"
teaching: 45
exercises: 10
questions:
- "How can I run a command on multiple files at once?"
- "Is there an easy way of saving a command's output?"
objectives:
- "Redirect a command's output to a file."
- "Process a file instead of keyboard input using redirection."
- "Construct command pipelines with two or more stages."
- "Explain what usually happens if a program or pipeline isn't given any input to process."
keypoints:
- "The `*` wildcard is used as a placeholder to match any text that follows a pattern."
- "Redirect a commands output to a file with `>`."
- "Commands can be chained with `|`"
---

> ## Required files
> If you didn't get them in the last lesson, 
> make sure to download the example files used in the next few sections:
> 
> **Using wget** - `wget http://hpc-carpentry.github.io/hpc-intro/files/bash-lesson.tar.gz`
>
> **Using a web browser** - [http://hpc-carpentry.github.io/hpc-intro/files/bash-lesson.tar.gz](http://hpc-carpentry.github.io/hpc-intro/files/bash-lesson.tar.gz)
{: .testimonial}

Now that we know most of the basic UNIX commands, we are going to explore
some more advanced features. The first of these features is the wildcard `*`.
In our examples before, we've done things to files one at a time and
otherwise had to specify things explicitly. The `*` character lets us speed
things up and do things across multiple files.

Ever wanted to move, delete, or just do "something" to all files of a certain
type in a directory? `*` lets you do that, by taking the place of one or more
characters in a piece of text. So `*.txt` would be equivalent to all `.txt`
files in a directory for instance. `*` by itself means all files. Let's use
our example data to see what I mean.

```
$ ls
```
{: .bash}
```
bash-lesson.tar.gz                           SRR307024_2.fastq  SRR307028_1.fastq
dmel-all-r6.19.gtf                           SRR307025_1.fastq  SRR307028_2.fastq
dmel_unique_protein_isoforms_fb_2016_01.tsv  SRR307025_2.fastq  SRR307029_1.fastq
gene_association.fb                          SRR307026_1.fastq  SRR307029_2.fastq
SRR307023_1.fastq                            SRR307026_2.fastq  SRR307030_1.fastq
SRR307023_2.fastq                            SRR307027_1.fastq  SRR307030_2.fastq
SRR307024_1.fastq                            SRR307027_2.fastq
```
{: .output}

Now we have a whole bunch of example files in our directory. For this example
we are going to learn a new command that tells us how long a file is: `wc`.
`wc -l file` tells us the length of a file in lines.

```{.bash}
$ wc -l dmel-all-r6.19.gtf
```
```{.output}
542048 dmel-all-r6.19.gtf
```

Interesting, there are over 540000 lines in our `dmel-all-r6.19.gtf` file.
What if we wanted to run `wc -l` on every .fastq file? This is where `*`
comes in really handy!
`*.fastq` would match every file ending in `.fastq`.

```{.bash}
$ wc -l *.fastq
```
```{.output}
20000 SRR307023_1.fastq
20000 SRR307023_2.fastq
20000 SRR307024_1.fastq
20000 SRR307024_2.fastq
20000 SRR307025_1.fastq
20000 SRR307025_2.fastq
20000 SRR307026_1.fastq
20000 SRR307026_2.fastq
20000 SRR307027_1.fastq
20000 SRR307027_2.fastq
20000 SRR307028_1.fastq
20000 SRR307028_2.fastq
20000 SRR307029_1.fastq
20000 SRR307029_2.fastq
20000 SRR307030_1.fastq
20000 SRR307030_2.fastq
320000 total
```

That was easy. What if we wanted to do the same command, except on every file in the directory? A nice trick to keep in mind is that `*` by itself matches *every* file.

```
$ wc -l *
```
{: .bash}
```
    53037 bash-lesson.tar.gz
   542048 dmel-all-r6.19.gtf
    22129 dmel_unique_protein_isoforms_fb_2016_01.tsv
   106290 gene_association.fb
    20000 SRR307023_1.fastq
    20000 SRR307023_2.fastq
    20000 SRR307024_1.fastq
    20000 SRR307024_2.fastq
    20000 SRR307025_1.fastq
    20000 SRR307025_2.fastq
    20000 SRR307026_1.fastq
    20000 SRR307026_2.fastq
    20000 SRR307027_1.fastq
    20000 SRR307027_2.fastq
    20000 SRR307028_1.fastq
    20000 SRR307028_2.fastq
    20000 SRR307029_1.fastq
    20000 SRR307029_2.fastq
    20000 SRR307030_1.fastq
    20000 SRR307030_2.fastq
  1043504 total
```
{: .output}

> ## Multiple wildcards
> You can even use multiple `*`s at a time. How would you run `wc -l` on every file with "fb" in it?
{: .challenge}

> ## Using other commands
> Now let's try cleaning up our working directory a bit. Create a folder
> called "fastq" and move all of our .fastq files there in one `mv` command.
{: .challenge}

## Redirecting output

Each of the commands we've used so far does only a very small amount of work.
However, it's extremely easy to chain these small UNIX commands together to
perform otherwise complicated actions!

For our first foray into "piping", or redirecting output, we are going to use
the `>` operator to write output to a file. When using `>`, whatever is on
the left of the `>` is written to the filename you specify on the right of
the arrow. The actual syntax looks like `command > filename`.

Let's try several basic usages of `>`. `echo` simply prints back, or echoes
whatever you type after it.

```
$ echo "this is a test"
$ echo "this is a test" > test.txt
$ ls
$ cat test.txt
```
{: .bash}
```
this is a test

bash-lesson.tar.gz                           fastq
dmel-all-r6.19.gtf                           gene_association.fb
dmel_unique_protein_isoforms_fb_2016_01.tsv  test.txt

this is a test
```
{: .output}

Awesome, let's try that with a more complicated command, like `wc -l`.

```
$ wc -l * > word_counts.txt
$ cat word_counts.txt
```
{: .bash}
```
wc: fastq: Is a directory

    53037 bash-lesson.tar.gz
   542048 dmel-all-r6.19.gtf
    22129 dmel_unique_protein_isoforms_fb_2016_01.tsv
        0 fastq
   106290 gene_association.fb
        1 test.txt
   723505 total
```
{: .output}

Notice how we still got some output to the console even though we "piped" the
output to a file? Our expected output still went to the file, but how did the
error message get skipped and not go to the file?

This phenomenon is an artifact of how UNIX systems are built. There are 3
input/output streams for every UNIX program you will run: `stdin`, `stdout`,
and `stderr`.

Let's dissect these three streams of input/output in the command we just ran:
`wc -l * > word_counts.txt`

* `stdin` is the input to a program. In the command we just ran, `stdin` is
  represented by `*`, which is simply every filename in our current directory.

* `stdout` contains the actual, expected output. In this case, `>` redirected
  `stdout` to the file `word_counts.txt`.

* `stderr` typically contains error messages and other information that doesn't
  quite fit into the category of "output". If we insist on redirecting both
  `stdout` and `stderr` to the same file we would use `&>` instead of `>`.

Knowing what we know now, let's try re-running the command, and send all of
the output (including the error message) to the same `word_counts.txt` files
as before.

```
$ wc -l * &> word_counts.txt
```
{: .bash}

Notice how there was no output to the console that time. Let's check that the error message went to the file like we specified.

```
$ cat word_counts.txt
```
{: .bash}
```
    53037 bash-lesson.tar.gz
   542048 dmel-all-r6.19.gtf
    22129 dmel_unique_protein_isoforms_fb_2016_01.tsv
wc: fastq: Is a directory
        0 fastq
   106290 gene_association.fb
        1 test.txt
        7 word_counts.txt
   723512 total
```
{: .output}

Success! The `wc: fastq: Is a directory` error message was written to the file. Also, note how the file was silently overwritten by directing output to the same place as before. Sometimes this is not the behaviour we want. How do we append (add) to a file instead of overwriting it?

Appending to a file is done the same was as redirecting output. However, instead of `>`, we will use `>>`.

```
$ echo "We want to add this sentence to the end of our file" >> word_counts.txt
$ cat word_counts.txt
```
{: .bash}
```
  22129 dmel_unique_protein_isoforms_fb_2016_01.tsv
 471308 Drosophila_melanogaster.BDGP5.77.gtf
      0 fastq
1304914 fb_synonym_fb_2016_01.tsv
 106290 gene_association.fb
      1 test.txt
1904642 total
We want to add this sentence to the end of our file
```
{: .output}

## Chaining commands together

We now know how to redirect `stdout` and `stderr` to files. We can actually
take this a step further and redirect output (`stdout`) from one command to
serve as the input (`stdin`) for the next. To do this, we use the `|` (pipe)
operator.

`grep` is an extremely useful command. It finds things for us within files.
Basic usage (there are a lot of options for more clever things, see the `man`
page) uses the syntax `grep whatToFind fileToSearch`. Let's use `grep` to
find all of the entries pertaining to the `Act5C` gene in *Drosophila
melanogaster*.

```
$ grep Act5C dmel-all-r6.19.gtf
```
{: .bash}

The output is nearly unintelligible since there is so much of it. Let's send
the output of that `grep` command to `head` so we can just take a peek at the
first line. The `|` operator lets us send output from one command to the next:

```
$ grep Act5C dmel-all-r6.19.gtf | head -n 1
```
{: .bash}
```
X	FlyBase	gene	5900861	5905399	.	+	.	gene_id "FBgn0000042"; gene_symbol "Act5C";
```
{: .output}

Nice work, we sent the output of `grep` to `head`. 
Let's try counting the number of entries for Act5C with `wc -l`.
We can do the same trick to send `grep`'s output to `wc -l`:

```
$ grep Act5C dmel-all-r6.19.gtf | wc -l
```
{: .bash}
```
46
```
{: .output}

Note that this is just the same as redirecting output to a file, then reading the number of lines from that file.

> ## Writing commands using pipes
> How many files are there in the "fastq" directory we made earlier? (Use the shell to do this.)
{: .challenge}

> ## Reading from compressed files
> Let's compress one of our files using gzip.
> ```{.bash}
> $ gzip gene_association.fb
> ```
>
> `zcat` acts like `cat`, except that it can read information from `.gz` (compressed) files. 
> Using `zcat`, can you write a command to take a look at the top few lines of the 
> `gene_association.fb.gz` file (without decompressing the file itself)?
{: .challenge}
