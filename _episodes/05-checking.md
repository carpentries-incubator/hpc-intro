---
title: "Checking and Previewing"
teaching: 5
exercises: 0
questions:
- "How can lesson formatting be checked?"
- "How can lessons be previewed?"
objectives:
- "Run the lesson checking script and interpret its output correctly."
- "Preview a lesson locally."
keypoints:
- "Lessons are checked by running `make lesson-check`."
- "The checker uses the same Markdown parser as Jekyll."
- "Lessons can be previewed by running `make serve`."
---

The lesson template comes with several utilities to simplify lesson development and maintenance.

## Checking

The template includes a Python program to check
whether lesson files conform to our template.
You can run this using `make lesson-check`,
which in turn invokes `bin/markdown_ast.rb` to parse Markdown files
and `bin/lesson_check.py` to check their structure.
The former is written in Ruby,
and uses Jekyll's own Markdown parser (called Kramdown)
so that we are guaranteed to be checking the same dialect of Markdown that Jekyll uses on GitHub.
The latter is written in Python 3,
and executes all of the checks.

The template also includes `bin/repo_check.py`,
which can be invoked by running `make repo-check`.
This program looks in `_config.yml` to find the repository's URL,
then checks that the repository has the right labels set up for issues and pull requests.
Other checks will be added as time goes by.

## Previewing

[Jekyll][jekyll] can be used in two ways:
to compile source files into HTML pages in the `_site` directory,
or to do that and also run a small web server at <http://0.0.0.0:4000/>
so that the pages can be previewed.
We recommend using the latter,
since it gives a more accurate impression of what your lesson will actually look like.

The Makefile in the root directory of the project contains commands for building the site.
`make site` builds files but does not run a server,
while `make serve` builds the files and runs a server.
(It also re-builds the site whenever it notices changes in the source files.)
Run `make` on its own to get a full list of commands.

In order to use Jekyll and/or the checking script,
you may need to install it and some other software.
The [setup instructions]({{ page.root }}/setup/) explain what you need and how to get it.

## Displaying Figures

The command `make lesson-figures` uses the script `bin/make_figures.py`
to regenerate `includes/all_figures.html`,
which links to every figure used in the episodes (in order).
Instructors can scroll through this page to display figures while teaching.

[jekyll]: http://jekyllrb.com/
