---
title: "GitHub, Markdown, and Jekyll"
teaching: 10
exercises: 0
questions:
- "How are pages published?"
objectives:
- "Explain how GitHub Pages produce web sites from Git repositories."
- "Explain Jekyll's formatting rules."
keypoints:
- "FIXME"
---
## Repositores on GitHub

Git uses the term *clone* to mean "a copy of a repository".
GitHub uses the term *fork* to mean, "a copy of a GitHub-hosted
repo that is also hosted on GitHub", and the term *clone* to mean
"a copy of a GitHub-hosted repo that's located on someone else's
machine".  In both cases, the duplicate has a remote called
`origin` that points to the original repo; other remotes can be
added manually.

A user on GitHub can only have one fork of a particular repo.
This is a problem for us because an author may be involved in
writing several lessons, each of which has its own website repo.
Those website repositories ought to be forks of this one, but
since GitHub doesn't allow that, we've had to find a workaround.

## GitHub Pages

If a repository has a branch called `gh-pages` (which stands for
"GitHub pages"), then GitHub uses the HTML and Markdown files in
that branch to create a website for the repository.  If the
repository's URL is `http://github.com/darwin/finches`, the URL
for the website is `http://darwin.github.io/finches`.

## Markdown

We use Markdown for writing pages because it's simple to learn,
and isn't tied to any specific language (the ReStructured Text
format popular in the Python world, for example, is a complete
unknown to R programmers).  If authors want to use something else
to author their lessons (e.g., Jupyter Notebooks), it's up to them
to generate and commit Markdown formatted according to the rules
below.

> ## Tooling
>
> Note that we do *not* prescribe what tools instructors should use
> when actually teaching.  The Jupyter Notebook, Python IDEs like
> Spyder, and the GOCLI (Good Ol' Command Line Interpreter) are all
> equally welcome up on stage --- all we specify is the format of
> the lesson notes.
{: .callout}

## Jekyll

GitHub uses Jekyll to turn Markdown into HTML.  Jekyll looks for
a header at the top of each page formatted like this:

~~~
---
variable: value
other_variable: other_value
---
...stuff in the page...
~~~
{: .source}

and inserts the values of those variables into the page when
formatting this.  Lesson authors will usually not have to worry
about this.

Jekyll also takes values from a `_config.yml` configuration file
and inserts them into the page.  Lesson authors will also not
have to worry about this in most cases, provided they update the
`title`, `lesson_repo`, and `lesson_site` variables in `_config.yml`.

In order to display properly, our generated HTML pages need artwork,
CSS style files, and a few bits of Javascript.  We could load these
from the web, but that would make offline authoring difficult.
Instead, each lesson's repository is self-contained and has a copy of
all these third party resources, and a way of updating them (and only
them) on demand.
