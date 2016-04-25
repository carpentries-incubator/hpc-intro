lesson-example
==============

Documentation on the lesson template formatted according to the template's own rules.

## Layout

The layout of this repository is explained in [these episodes][rendered].

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

Copy `_config_template.yml` to create `_config.yml` and then edit the
settings in the top half.

For a list of helpful commands run `make` in this directory.

[collections]: https://jekyllrb.com/docs/collections/
[dc-lessons]: http://datacarpentry.org/lessons/
[issues]: https://github.com/gvwilson/new-lesson-example/issues/
[rendered]: https://gvwilson.github.io/new-lesson-example/
