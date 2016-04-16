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
This episode describes tools we use to manage lessons,
which simplify many tasks but make other things more complicated.

## Repositores on GitHub

All of our lessons are stored in Git repositories on GitHub.
Git uses the term *clone* to mean "a copy of a repository",
while GitHub uses the term *fork* to mean "a copy of a GitHub-hosted repo that is also hosted on GitHub"
and the term *clone* to mean "a copy of a GitHub-hosted repo that's located on someone else's machine".
In both cases,
the duplicate has a remote called `origin` that points to the original repo;
other remotes can be added manually.

A user on GitHub can only have one fork of a particular repo.
This is a problem for us because an author may be involved in writing several lessons,
each of which has its own website repo.
Those website repositories ought to be forks of the [template repository]({{ site.template_repo }}),
but since GitHub doesn't allow that,
we use [GitHub Importer][github-importer] when creating new lessons.
After the lesson has been created,
we manually add the [template repository]({{ site.template_repo }}) as a remote called `template`
to update the lesson when the template changes.

## GitHub Pages

If a repository has a branch called `gh-pages` (short for "GitHub Pages"),
GitHub publishes its content to create a website for the repository.
If the repository's URL is `https://github.com/USERNAME/REPOSITORY`,
the website is `https://USERNAME.github.io/REPOSITORY`.

Websites can be static HTML pages,
which are published as-is,
or can use the [Jekyll][jekyll] templating system described below.

## Markdown

We use Markdown for lesson content because it's simple to learn
and isn't tied to any specific language
(the ReStructured Text format popular in the Python world,
for example,
is a complete unknown to R programmers).
If authors want to use something else to author their lessons,
such as [R Markdown][r-markdown],
they must generate Markdown that [Jekyll][jekyll] can process,
or static HTML,
and commit that to the repository.

> ## Tooling
>
> We do *not* prescribe what tools instructors should use when actually teaching:
> the [Jupyter Notebook][jupyter],
> [RStudio][rstudio],
> and the good ol' command line are equally welcome up on stage.
> All we specify is the format of the lesson notes.
{: .callout}

## Jekyll

GitHub uses [Jekyll][jekyll] to turn Markdown into HTML.
By default,
it looks for text files that begin with a header formatted like this:

~~~
---
variable: value
other_variable: other_value
---
...stuff in the page...
~~~
{: .source}

and inserts the values of those variables into the page when formatting this.
The three dashes that start the header *must* be the first three characters in the file:
even a single space before them will make [Jekyll][jekyll] ignore the file.

Jekyll requires the header to be formatted as [YAML][yaml],
which provides Booleans, numbers, character strings, lists, and dictionaries of name/value pairs.
Values from the header are referred to in the page as `page.variable`.

## Configuration

[Jekyll][jekyll] also reads values from a configuration file called `_config.yml`,
which are referred to in the page as `site.variable`.
The [lesson template]({{ site.template_repo }}) does *not* include `_config.yml`,
since each lesson will change some of its value,
which would result in merge collisions each time the lesson was updated from the template.
Instead,
the [template]({{ site.template_repo }}) contains `_config_template.yml`;
authors should copy this file to create `_config.yml`
and then edit values in the top half.

The [template]({{ site.template_repo }}) also contains `_config_dev.yml`,
which overrides some settings for use during desktop development.
The Makefile that comes with the [template]({{ site.template_repo }})
adds these values to those in `_config.yml` when running a local server.

## Collections

If several Markdown files are stored in a directory whose name begins with an underscore,
[Jekyll][jekyll] creates a [collection][jeyll-collection] for them.
We rely on this for both lesson episodes (stored in `_episodes`)
and extra files (stored in `_extras`).

[github-importer]: https://import.github.com/
[jekyll]: http://jekyllrb.com/
[jekyll-collection]: https://jekyllrb.com/docs/collections/
[jupyter]: https://jupyter.org/
[r-markdown]: http://rmarkdown.rstudio.com/
[rstudio]: https://www.rstudio.com/
[yaml]: http://yaml.org/
