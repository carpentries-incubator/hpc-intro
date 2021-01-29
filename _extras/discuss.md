---
title: "Taking Your Next Steps"
teaching: 10
exercises: 60
questions:
- "How can I get started on using HPC?"
- "Where can I get help to start using HPC?"
objectives:
- "Get help to get your work up and running on an HPC system"
- "Understand where you can get help from in the future"
keypoints:
- "Understand the next steps for you in using HPC."
- "Understand how you can access help and support to use HPC."
---

Now you know enough about HPC to explore how to use it for your work or to understand
what its potential benefits are you. You may also have ideas around where the 
barriers and difficulties may lie and have further questions on how you can 
start using and/or trying HPC in your area.

This session is designed to give you the opportunity to explore these questions and
issues. The instructors and helpers on the course will be on hand to answer your
questions and discuss next steps with you.

> ## Potential discussions
>
> Things you could discuss with the instructors and helpers could include:
>
> - Your computational workflow and where advanced computing could help
> - How to get access to facilities for your work
> - How to get help and support to get your work running using advanced computing.
>   For example, software development, further training, access to local expertise
{: .callout}

## Options for this session

There are a number of different options for practical work during this session. The
challenges below include: exploring your own work; an extended example using a parallel
HPC application; an extended example using high throughput computing on multiple
serial analyses. If you have something else you want to use the session for (e.g. to
discuss things with the instructors/helpers as described above) then please feel free
to do this. The idea of the session is to help you bootstrap your use of advanced computing
and this will differ from individual to individual!

> ## Exploring your work using HPC
>
> If you have a practical example of something from your area of work that you would like
> help with getting up and running on an HPC system or exploring the performance of
> on an HPC system, this is great! Please feel free to discuss this with us and ask
> questions (both technical and non-technical).
{: .challenge}

> ## Exploring the performance of GROMACS
>
> [GROMACS](http://www.gromacs.org) is a world-leading biomolecular modelling package
> that is heavily used on HPC systems around the world. Choosing the best resources
> for GROMACS calculations is non-trivial as it depends on may factors, including:
>
> - The underlying hardware of the HPC system being used
> - The actual system being modelled by the GROMACS package
> - The balance of processes to threads used for the parallel calculation
>
> In this exercise, you should try and decide on a good choice of resources and settings
> on {{ site.remote.name }} for a typical biomolecular system. This will involve:
>
> - Downloading the input file for GROMACS from 
>   [{{ site.url }}{{site.baseurl }}/files/ion-channel.tpr](
>   {{ site.url }}{{site.baseurl }}/files/ion-channel.tpr)
> - Writing a job submission script to run GROMACS on {{ site.remote.name }} using the system
>   documentation
> - Varying the number of nodes (from 1 to 32 nodes is a good starting point) used for the GROMACS
>   job
>   and benchmarking the performance (in ns/day)
> - Using the results from this study to propose a good resource choice for this GROMACS calculation
>
> If you want to explore further than this initial task then there are a number of 
> different interesting ways to do this. For example:
> 
> - Vary the number of threads used per process
> - Reduce the number of cores used per node
> - Allow the calculation to use Symmetric Mutithreading (SMT) if enabled
>
> Please ask for more information on these options from a helper!
{: .challenge}

> ## Running many serial BLAST+ analyses in parallel
>
> [BLAST+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)
> finds regions of similarity between biological sequences. The program compares nucleotide or
> protein sequences to sequence databases and calculates the statistical significance.
>
> In this exercise, you should use what you have learnt so far to set up a way to run multiple
> serial BLAST+ analyses in parallel. There are many different ways to do this that can be used
> on their own or in combination. Some ideas include:
>
> - Using {{ site.sched.name }} job arrays to run multiple copies across different nodes
> - Using a bash loop within a node
> - Using GNU parallel within a node
>
> We have prepared an example dataset that has 100 sequences to analyse (actually this is 10
> sequences repeated 10 times). This set is based on the 
> [BLAST GNU Parallel example](
> https://github.com/LangilleLab/microbiome_helper/wiki/Quick-Introduction-to-GNU-Parallel)
>
> This exercise involves:
>
> - Downloading and expanding the dataset to the HPC system from:
>   [{{ site.url }}{{site.baseurl }}/files/parallel_example.tar.gz](
>   {{ site.url }}{{site.baseurl }}/files/parallel_example.tar.gz)
> - Writing a job submission script to run a single analysis using the `blast` module and the
>   following command:
>
>   ```
>   blastp -db pdb_blast_db_example/pdb_seqres.txt -query test_seq_0.fas
>   -evalue 0.0001 -word_size 7  -max_target_seqs 10 -num_threads 1 \
>   -out output_seq_0.blast -outfmt "6 std stitle staxids sscinames"
>   ```
>   {: .bash}
>
>   where the `\` character tells `bash` that the command continues on the next line. Note that
>   there will be no output from this alignment if it works correctly).
> - Choosing a method to run multiple copies of the analysis to complete all 100 analysis tasks in a
>   parallel way (not all 100 have to be run simultaneously).
>
> You can explore further by investigating different ways to parallelize this problem and/or
> combining multiple parallel strategies.
>
> You could also investigate the variation in performance as you run multiple copies on a node.
> At what point does the hardware become overloaded?
{: .challenge}
