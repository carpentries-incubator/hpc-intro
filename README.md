[![Build Status](https://travis-ci.org/carpentries/lesson-example.svg?branch=gh-pages)](https://travis-ci.org/carpentries/lesson-example)

lesson-example
==============

[![Create a Slack Account with us][create_slack_svg]][slack_heroku_invite]

This repository shows how to create a lesson using
[The Carpentries lesson template][styles],
and is itself an example of the use of that template.
Please see <https://carpentries.github.io/lesson-example/>
for a rendered version of this material,
including detailed instructions on design, setup, and formatting.

## Quick Instructions

1.  Do *not* fork this repository directly on GitHub.
    Instead, please follow the instructions in [the setup instructions][setup]
    to create a repository for your lesson by importing material
    from [the styles repository][styles].

2.  Once you have created your repository,
    run `bin/lesson_initialize.py` to create standard lesson-specific files.
    You *must* edit several values in `_config.yml`
    so that GitHub Pages will render your lesson correctly.

3.  Please read [the episodes of this lesson][rendered] to format your material.

4.  Please keep the master copy of your lesson in your repository's `gh-pages` branch,
    since that is what is
    [automatically published as a website by GitHub][github-pages].

5.  To preview material,
    please run `make serve` from the command line
    to launch Jekyll with the correct parameters,
    or push to your repository's `gh-pages` branch
    and let GitHub take care of the rendering.

6.  Run `make lesson-check` to check that your files follow our formatting rules.

7.  If you find an error or omission in this documentation,
    please [file an issue in this repository][example-issues].
    If you find an error or omission in the lesson template,
    please [file an issue in the styles repository][styles-issues] instead.

## Layout

The layout of this repository is explained in [this site's episodes][rendered].
In brief:

1.  The source for pages that appear as top-level items in the navigation bar
    are stored in the root directory,
    including the home page (`index.md`),
    the reference page (`reference.md`),
    and the setup instructions (`setup.md`).

2.  Source files for lesson episodes are stored in `_episodes`;
    `_episodes/01-xyz.md` generates `/01-xyz/index.html`,
    which can be linked to using `/01-xyz/`.

3.  If you are writing lessons in R Markdown,
    source files go in `_episodes_rmd`.
    You must run `make lesson-rmd` to turn these into Markdown in `_episodes`
    and commit those Markdown files to the repository
    (since GitHub won't run anything except Jekyll to format material).
    You must also commit any figures generated from your lessons,
    which are stored in the `fig` directory.

4.  Files that appear under the "extras" menu are stored in `_extras`.

5.  Figures are stored in the `fig` directory,
    data sets in `data`,
    source code in `code`,
    and miscellaneous files in `files`.

## Getting Started

1.  Run `bin/lesson_initialize.py` to create files
    that can't be stored in the template repository
    (because they would cause repeated merge conflicts),
    then edit `_config.yml` as described in
    [the documentation][editing-config].

2.  Run `make lesson-check` at any time
    to check that your lesson files follow our formatting rules.
    If you come across formatting issues that the checker doesn't report,
    please [file an issue in the styles repository][styles-issues].

3.  For a list of helpful commands run `make` in this directory.
    If you are looking for things to work on,
    please see [the list of issues for this repository][issues].

[collections]: https://jekyllrb.com/docs/collections/
[editing-config]: https://carpentries.github.io/lesson-example/03-organization/
[example-issues]: https://github.com/carpentries/lesson-example/issues/
[github-pages]: https://help.github.com/articles/creating-project-pages-manually/
[issues]: https://github.com/carpentries/lesson-example/issues
[rendered]: https://carpentries.github.io/lesson-example/
[setup]: https://carpentries.github.io/lesson-example/setup.html
[styles-issues]: https://github.com/carpentries/styles/issues/
[styles]: https://github.com/carpentries/styles/
[create_slack_svg]: https://img.shields.io/badge/Create_Slack_Account-The_Carpentries-071159.svg
[slack_heroku_invite]: https://swc-slack-invite.herokuapp.com
