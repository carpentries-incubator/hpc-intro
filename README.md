lesson-example
==============

This repository shows how to create a lesson using
the [Software Carpentry lesson template][swc-lesson-template],
and is itself an example of the use of that template.

1.  Do *not* fork this repository directly on GitHub.
    Instead, please follow the instructions in [the setup instructions][setup]
    to create a repository for your lesson from
    [the template repository][styles].

2.  Once you have created the repository,
    please go through [the episodes][rendered] to format your lesson.

3.  Please keep the master copy of your lesson in your repository's `gh-pages` branch,
    since that is what is
    [automatically published as a website by GitHub][github-pages].
    To simplify reviewing,
    please make changes in feature branches
    and then submit pull requests against the `gh-pages` branch
    of your lesson's repository.

## Layout

The layout of this repository is explained in [this site's episodes][rendered].
In brief:

1.  The source for pages that appear as direct items in the navigation bar
    are stored in the root directory.
2.  Source files for lesson episodes are stored in `_episodes`
    so that we can make use of [Jekyll collections][collections];
    `_episodes/01-xyz.md` generates `/01-xyz/index.html`,
    which can be linked to using `/01-xyz/`.
3.  Files that appear under the "extras" menu pulldown are stored in `_extras`.
4.  Figures and other files are stored in the `files` directory,
    while data sets are stored in `data`
    and source code for examples in `code`.

## Getting Started

1.  Run `bin/lesson-initialize` to create files
    that can't be stored in the template repository
    (because they would cause repeated merge conflicts),
    then edit `_config.yml` as described in the episode on organization.

2.  For a list of helpful commands run `make` in this directory.
    If you are looking for things to work on,
    please see [the list of issues for this repository][issues].

[collections]: https://jekyllrb.com/docs/collections/
[github-pages]:(https://help.github.com/articles/creating-project-pages-manually/
[issues]: https://github.com/gvwilson/new-lesson-example/issues/
[rendered]: https://gvwilson.github.io/new-lesson-example/
[setup]: setup.md
[styles]: https://github.com/swcarpentry/styles/
