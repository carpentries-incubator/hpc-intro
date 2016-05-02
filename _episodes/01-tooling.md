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
- "Lessons are stored in Git repositories on GitHub."
- "Lessons are written in Markdown."
- "Jekyll translates the files in the gh-pages branch into HTML for viewing."
- "The site's configuration is stored in _config.yml."
- "Each page's configuration is stored at the top of that page."
- "Groups of files are stored in collection directories whose names begin with an underscore."
---
This episode describes tools we use to manage lessons,
which simplify many tasks but make other things more complicated.

## Repositores on GitHub

All of our lessons are stored in Git repositories on GitHub.
Git uses the term *clone* to mean "a copy of a repository",
while GitHub uses the term *fork* to mean "a copy of a GitHub-hosted repo that is also hosted on GitHub"
and the term *clone* to mean "a copy of a GitHub-hosted repo that's located on someone else's machine".
In both cases,
the duplicate has a reference that points to the original repo.

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
Websites can be static HTML pages,
which are published as-is,
or can use [Jekyll][jekyll] as described below.
If the repository's URL is `https://github.com/USERNAME/REPOSITORY`,
the website is `https://USERNAME.github.io/REPOSITORY`.

> ## Why Doesn't My Site Appear?
>
> If the root directory of a repository contains a file called `.nojekyll`,
> GitHub will *not* generate a website for that repository's `gh-pages` branch.
{: .callout}

## Markdown

We write lessons in Markdown because it's simple to learn
and isn't tied to any specific language.
(The ReStructured Text format popular in the Python world,
for example,
is a complete unknown to R programmers.)
If authors want to write lessons in something else,
such as [R Markdown][r-markdown],
they must generate HTML or Markdown that [Jekyll][jekyll] can process
and commit that to the repository.
The [next episode]({{ site.root }}/02-formatting/) describes the Markdown we use.

> ## Teaching Tools
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

The header must be formatted as [YAML][yaml],
and may contain Booleans, numbers, character strings, lists, and dictionaries of name/value pairs.
Values from the header are referred to in the page as `page.variable`.

> ## Back in the Day...
>
> The previous version of our template did not rely on Jekyll,
> but instead required authors to build HTML on their desktops
> and commit that to the lesson repository's `gh-pages` branch.
> This allowed us to use whatever mix of tools we wanted for creating HTML (e.g., [Pandoc][pandoc]),
> but complicated the common case for the sake of uncommon cases,
> and didn't model the workflow we want learners to use.
{: .callout}

## Configuration

[Jekyll][jekyll] also reads values from a configuration file called `_config.yml`,
which are referred to in pages as `site.variable`.
The [lesson template]({{ site.template_repo }}) does *not* include `_config.yml`,
since each lesson will change some of its value,
which would result in merge collisions each time the lesson was updated from the template.
Instead,
the [template]({{ site.template_repo }}) contains `_templates/_config_template.yml`;
authors should copy this file to create `_config.yml`
and then edit values in the top half.

The [template]({{ site.template_repo }}) also contains `_config_dev.yml`,
which overrides some settings for use during desktop development.
The Makefile that comes with the [template]({{ site.template_repo }})
adds these values to those in `_config.yml` when running a local server
(see [below](#previewing)).

## Collections

If several Markdown files are stored in a directory whose name begins with an underscore,
[Jekyll][jekyll] creates a [collection][jekyll-collection] for them.
We rely on this for both lesson episodes (stored in `_episodes`)
and extra files (stored in `_extras`).
For example,
putting the extra files in `_extras` allows us to populate the "Extras" menu pulldown automatically.
To make this clear,
we store files that appear directly in the navigation bar
(rather than under a pulldown menu)
in the root directory of the lesson.

## Previewing

[Jekyll][jekyll] can be used in two ways:
to compile source files into HTML pages in the `_site` directory,
or to do that and also run a small web server at <http://127.0.0.1:4000/>
so that the pages can be previewed.
We strongly recommend using the latter,
since it ensures that inter-page links will work
and extra resources (such as glyph icons) will load properly.

The Makefile in the root directory of the project has commands for doing both:
`make site` builds files but does not run a server,
while `make serve` builds the files and runs a server.
(It also re-builds the site whenever it notices changes in the source files.)
Run `make` on its own to get a list of commands.

[github-importer]: https://import.github.com/
[jekyll]: http://jekyllrb.com/
[jekyll-collection]: https://jekyllrb.com/docs/collections/
[jupyter]: https://jupyter.org/
[pandoc]: https://pandoc.org/
[r-markdown]: http://rmarkdown.rstudio.com/
[rstudio]: https://www.rstudio.com/
[yaml]: http://yaml.org/
