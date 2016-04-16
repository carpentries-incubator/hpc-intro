---
title: "Lesson Organization"
teaching: 10
exercises: 0
questions:
- "How are the files in a lesson organized?"
objectives:
- "Explain overall organization of lesson files."
keypoints:
- "FIXME"
---
Our lessons need artwork,
CSS style files,
and a few bits of Javascript.
We could load these from the web,
but that would make offline authoring difficult.
Instead, each lesson's repository is self-contained.

Note: files that appear as top-level items in the navigation menu are stored in the root directory.
Files that appear under the "extras" menu are stored in the `_extras` directory
(which is turned into a [Jekyll collection][jekyll-collection] for easier processing).

## Standard Files

The [lesson template]({{ site.template_repo }}) provides the following files
which should *not* be modified:

*   `CONDUCT.md`: the code of conduct.
*   `LICENSE.md`: the lesson license.
*   `Makefile`: commands for previewing the site, cleaning up junk, etc.
*   `_extras/contributing.md`: contribution guidelines.

Run `make` on its own to get a list of targets in the Makefile.

## Common Files

Most lessons will contain the following files which are *not* in the template
(to avoid repeated merge conflicts):

*   `AUTHORS`: names and email addresses of authors.
*   `CITATION`: how the lesson should be cited in publications.
*   `README.md`: brief description of the lesson displayed by GitHub.
*   `index.md`: the home page for the lesson (discussed below).
*   `reference.md`: a reference guide for the lesson (discussed below).
*   `setup.md`: setup instructions for the lesson (discussed below).
*   `_extras/discussion.md`: general discussion.
*   `_extras/guide.md`: the instructors' guide.

## Layouts and Inclusions

Page layouts are stored in `_layouts`,
while snippets of HTML included by these layouts are stored in `_includes`,
because that's what [Jekyll][jekyll] requires.

## Assets

The `assets` directory contains the CSS, Javascript, fonts, and image files
used in the generated website.

[jekyll]: http://jekyllrb.com/
[jekyll-collection]: https://jekyllrb.com/docs/collections/
