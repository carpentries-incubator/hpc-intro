# Intro to HPC

[![Build Status](https://travis-ci.org/hpc-carpentry/hpc-intro.svg?branch=gh-pages)](https://travis-ci.org/hpc-carpentry/hpc-intro)

This lesson is focused on teaching the basics of high-performance computing (HPC). The curriculum
is still in the "alpha" stage. If you would like to contribute, please see the [Lesson
Outline][lesson-outline]. Thanks!

## Quick Instructions

1. Edit [_config.yml](_config.yml) to modify the configuration options for the HPC system you
   will be using in the section titled `Workshop specific values`. These options set such things
   as the address of the host to login to, definitions of the command prompt, scheduler names.
   The default is the setup for the Graham Compute Canada cluster hosted at the University
   of Waterloo which uses the SLURM scheduler. Other examples can be found in the
   [_includes/snippets_library/](_includes/snippets_library/) directory.

2. Create the required host-specific code snippets in subdirectories in
   [_includes/snippets_library](_includes/snippets_library). These snippets provide inputs and outputs that 
   are host-specific and that are included automatically when the lesson website is built.
   1. Code snippets are in files named `snippet_name.snip` and are included automatically
      when the lesson is built. For example, if the `snippet_name` was `login_output`,
      then the snippet file would be called `login_output.snip`.
   2. Code snippets are placed in subdirectories that are named according to the episode they
      appear in. For example, if the snippet is for episode 12, then it will be in a 
      subdirectory called `12`.
   3. In the episodes source, snippets are included using [Liquid](https://shopify.github.io/liquid/)
      scripting  `include` statements. For example, the first snippet in episode 12 is included using 
      `{% include /snippets/12/info.snip %}`.

   Please contribute any configurations you create for your local systems back into the HPC Intro
   snippets library.

3. Please read [the episodes of this lesson][rendered] to format your material.

4. Please keep the master copy of your lesson in your repository's `gh-pages` branch, since that is
   what is [automatically published as a website by GitHub][github-pages].

5. To preview material, please run `make serve` from the command line to launch Jekyll with the
   correct parameters, or push to your repository's `gh-pages` branch and let GitHub take care of
   the rendering.

6. Run `make lesson-check` to check that your files follow our formatting rules.

7. If you find an error or omission in this documentation, please [file an issue in this
   repository][example-issues]. If you find an error or omission in the lesson template, please
   [file an issue in the styles repository][styles-issues] instead.

## Layout

The layout of this repository is explained in [this site's episodes][rendered]. In brief:

1. The source for pages that appear as top-level items in the navigation bar are stored in the root
   directory, including the home page (`index.md`), the reference page (`reference.md`), and the
   setup instructions (`setup.md`).

2. Source files for lesson episodes are stored in `_episodes`; `_episodes/01-xyz.md` generates
   `/01-xyz/index.html`, which can be linked to using `/01-xyz/`.

3. If you are writing lessons in R Markdown, source files go in `_episodes_rmd`. You must run `make
   lesson-rmd` to turn these into Markdown in `_episodes` and commit those Markdown files to the
   repository (since GitHub won't run anything except Jekyll to format material). You must also
   commit any figures generated from your lessons, which are stored in the `fig` directory.

4. Files that appear under the "extras" menu are stored in `_extras`.

5. Figures are stored in the `fig` directory, data sets in `data`, source code in `code`, and
   miscellaneous files in `files`.
   
6. If you wish to add a new figure to a lesson, please use appropriate Liquid variables, e.g., `{{
   site.url }}/fig/...` instead of plain `/fig/...`. For example, `![Your alt text]({{ site.url
   }}/fig/image_name.png)` rather than `![Your alt text](/fig/image_name.png)`. This helps guard
   against broken links.
   
   Note that the preferred method to include scalable vector graphics (SVG files) is 
   `{% include figure.html max-width="30%" file="{{ site.url }}/fig/image_name.svg" alt="Your alt text" caption="Your figure caption" %}`

## Getting Started

1. Run `make lesson-check` at any time to check that your lesson files follow our formatting rules.
   If you come across formatting issues that the checker doesn't report, please [file an issue in
   the styles repository][styles-issues].

2. For a list of helpful commands run `make` in this directory. If you are looking for things to
   work on, please see [the list of issues for this repository][issues].

[collections]: https://jekyllrb.com/docs/collections/
[example-issues]: https://github.com/hpc-carpentry/hpc-intro/issues/
[github-pages]: https://help.github.com/articles/creating-project-pages-manually/
[issues]: https://github.com/hpc-carpentry/hpc-intro/issues
[lesson-outline]: https://hpc-carpentry.github.io/hpc-intro/lesson-outline.html
[rendered]: https://hpc-carpentry.github.io/hpc-intro/
[setup]: https://hpc-carpentry.github.io/hpc-intro/setup.html
[styles-issues]: https://github.com/carpentries/styles/issues/
