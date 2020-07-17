# HPC Carpentriy Snippets Library

This directory contains snippets of code and output that are specific
to a particular site. For example, when the lesson shows the status
of the cluster and its nodes, it is preferable to show *your* cluster
and *your* nodes. If you replace the contents of the relevant snippet,
the website gets built with your cluster details, instead of generic
values (or, more precisely, values taken from ComputeCanada).

The snippets have been named so that the lessons use them in roughly
alphabetical order, while still reflecting something of the contents
of each file. So, if you're reading (or teaching) a lesson and notice
something amiss about half-way through, look to the files about
half-way through the directory. If it's the first or last snippet,
you're in particularly good luck.

This alphabetical ordering was not always the case. To reduce the
headache of keeping forks, branches, and derivative works up-to-date,
we have included a utility to rename snippets from the older scheme.
To use it, run the following command, rebuild and test your site, and
commit the changes.

```bash
$ ./rename-snippets.sh <your_snippet_directory>
```

If the naming seems counter-intuitive, please feel free to make
changes locally, and file an issue of submit a pull request to fix it
upstream. None of this is set in stone, and improvements are always
welcome.


