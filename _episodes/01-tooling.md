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
This episode describes the tools we use to build and manage lessons.
These simplify many tasks, but make other things more complicated.

## Repositories on GitHub

Our lessons are stored in Git repositories (or "repos") on GitHub.
We use the term *fork* to mean "a copy of a GitHub-hosted repo that is also hosted on GitHub"
and the term *clone* to mean "a copy of a GitHub-hosted repo that's located on someone else's machine".
In both cases,
the duplicate has a reference that points to the original repo.

In an ideal world,
we would put all of the common files used by our lessons
(such as the CSS style files and the image files with project logos)
in a template repo.
The master copy of each lesson would be a fork of that repo,
and each author's working copy would be a fork of that master:

![Forking Repositories]({{ site.root }}/fig/forking.svg)

However, GitHub only allows a user to have one fork of any particular repo.
This creates a problem for us because an author may be involved in writing several lessons,
each with its own repo.
We therefore use [GitHub Importer][github-importer] to create new lessons.
After the lesson has been created,
we manually add the [template repository]({{ site.template_repo }}) as a remote called `template`
to update the lesson when the template changes.

![Repository Links]({{ site.root }}/fig/repository-links.svg)

## GitHub Pages

If a repository has a branch called `gh-pages` (short for "GitHub Pages"),
GitHub publishes its content to create a website for the repository.
If the repository's URL is `https://github.com/USERNAME/REPOSITORY`,
the website is `https://USERNAME.github.io/REPOSITORY`.

GitHub Pages sites can include static HTML pages,
which are published as-is,
or they can use [Jekyll][jekyll] as described below
to compile HTML and/or Markdown pages with embedded directives
to create the pages for display.

> ## Why Doesn't My Site Appear?
>
> If the root directory of a repository contains a file called `.nojekyll`,
> GitHub will *not* generate a website for that repository's `gh-pages` branch.
{: .callout}

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
It looks for text files that begin with a header formatted like this:

~~~
---
variable: value
other_variable: other_value
---
...stuff in the page...
~~~
{: .source}

and inserts the values of those variables into the page when formatting it.
The three dashes that start the header *must* be the first three characters in the file:
even a single space before them will make [Jekyll][jekyll] ignore the file.

The header's content must be formatted as [YAML][yaml],
and may contain Booleans, numbers, character strings, lists, and dictionaries of name/value pairs.
Values from the header are referred to in the page as `page.variable`.
For example,
this page:

~~~
---
name: Science
---
Today we are going to study {{page.name}}.
~~~

is translated into:

~~~
<html>
<body>
<p>Today we are going to study Science.</p>
</body>
</html>
~~~

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
the [template]({{ site.template_repo }}) contains a script called `bin/initialize`
which should be run *once* to create an initial `_config.yml` file.
The author should then edit the values in the top half of the file.

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
To clarify what will appear where,
we store files that appear directly in the navigation bar
in the root directory of the lesson.
[The last episode]({{ site.root }}/03-organization/) describes these files.

## Installing

You can preview changes by pushing to the `gh-pages` branch of your own repository,
but it's often easier to view them locally first.
To do that,
you will need to install [Jekyll][jekyll] and a few other packages used by GitHub Pages.
The easiest way to do that is:

1.  Install Ruby if you don't already have it.
2.  Install Ruby Gems (Ruby's package manager).
3.  `gem install github-pages` (which will give you Jekyll and things it depends on).

See [the Jekyll installation documentation][jekyll-install]
for full instructions.

## Previewing

[Jekyll][jekyll] can be used in two ways:
to compile source files into HTML pages in the `_site` directory,
or to do that and also run a small web server at <http://127.0.0.1:4000/>
so that the pages can be previewed.
We recommend using the latter,
since it gives a more accurate impression of what your lesson will actually look like.

The Makefile in the root directory of the project contains commands for building the site.
`make site` builds files but does not run a server,
while `make serve` builds the files and runs a server.
(It also re-builds the site whenever it notices changes in the source files.)
Run `make` on its own to get a full list of commands.

[github-importer]: https://import.github.com/
[jekyll]: http://jekyllrb.com/
[jekyll-collection]: https://jekyllrb.com/docs/collections/
[jekyll-install]: https://jekyllrb.com/docs/installation/
[jupyter]: https://jupyter.org/
[pandoc]: https://pandoc.org/
[r-markdown]: http://rmarkdown.rstudio.com/
[rstudio]: https://www.rstudio.com/
[yaml]: http://yaml.org/
