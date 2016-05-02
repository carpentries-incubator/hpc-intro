---
title: "Lesson Organization"
teaching: 10
exercises: 0
questions:
- "How are the files in a lesson organized?"
objectives:
- "Explain overall organization of lesson files."
keypoints:
- "Auxiliary files are stored in the _layouts, _includes, and assets directories."
- "The code of conduct, license, Makefile, and contribution guidelines should not be modified."
- "The README, authors' list, and citation instructions must be updated for each lesson."
- "The home page, reference guide, setup instructions, discussion page, and instructors' guide must be updated for each lesson."
- "The Makefile stores commonly-used commands."
---
Our lessons need artwork,
CSS style files,
and a few bits of Javascript.
We could load these from the web,
but that would make offline authoring difficult.
Instead, each lesson's repository is self-contained.

![Source and Destination Files]({{ site.root }}/fig/file-mapping.svg)

> ## Collections
>
> As described [earlier]({{ site.root }}/01-tooling/#collections),
> files that appear as top-level items in the navigation menu are stored in the root directory.
> Files that appear under the "extras" menu are stored in the `_extras` directory,
> while lesson episodes are stored in the `_episodes` directory.
{: .callout}

## Helper Files

As is standard with [Jekyll][jekyll] sites,
page layouts are stored in `_layouts`
and snippets of HTML included by these layouts are stored in `_includes`.
Each of these files includes a comment explaining its purpose.

Authors do not have to specify that episodes use the `episode.html` layout,
since that is set by the configuration file.
Pages that authors create should have the `page` layout unless specified otherwise below.

The `assets` directory contains the CSS, Javascript, fonts, and image files
used in the generated website.
Authors should not modify these.

## Standard Files

The [lesson template]({{ site.template_repo }}) provides the following files
which should *not* be modified:

*   `CONDUCT.md`: the code of conduct.
*   `LICENSE.md`: the lesson license.
*   `Makefile`: commands for previewing the site, cleaning up junk, etc.

## Template Files

The `_templates` directory contains files that need to be customized for each lesson:

*   `CONTRIBUTING.md`: contribution guidelines.
    This file should be copied into the root directory,
    and the `issues` and `repo` links at the bottom of the file must be changed
    to match the URLs of the lesson.
*   `_config.yml`: [Jekyll][jekyll] configuration file.
    As explained [earlier]({{ site.root }}/01-tooling/#configuration),
    `_templates/_config.yml` must be copied into the root directory
    and edited so that its links and other settings are correct for this lesson.

## Common Files

Most lessons will contain the files listed below.
These are *not* included in the template in order to avoid repeated merge conflicts.

### `README.md`

A brief description of the lesson that is displayed by GitHub.
This file does *not* include a [YAML][yaml] header,
and is *not* included in the generated website.

### `AUTHORS`

The names and email addresses of authors, one per line.
This file provides a more convenient way to view contributors than walking the Git history.

### `CITATION`

This explains how the lesson should be cited in publications.

### `index.md`

The home page for the lesson.

1.  It must use the `index` layout.
2.  It must *not* have a `title` field in its [YAML][yaml] header.
3.  It must open with a few paragraphs of explanatory text.
4.  That introduction must be followed by a single `.prereq` blockquote
    detailing the lesson's prerequisites.
    (Setup instructions appear separately.)
5.  That must be followed by inclusion of `syllabus.html`,
    which generates the syllabus for the lesson
    from the metadata in its episodes.

### `reference.md`

A reference guide for the lesson.

1.  It must use the `reference` layout.
2.  Its title must be `"Reference"`.
3.  Its permalink must be `/reference/`.
4.  It should include a glossary, laid out as a description list.
5.  It may include other material as appropriate.

The template will automatically generate a summary of the episodes' key points.

### `setup.md`

Detailed setup instructions for the lesson.

1.  It must use the `page` layout.
2.  Its title must be `"Setup"`.
3.  Its permalink must be `/setup/`.
4.  It should include whatever setup instructions are required.

Note that we usually divide setup instructions by platform,
e.g.,
include level-2 headings for Windows, Mac OS X, and Linux
with instructions for each.
The [workshop template]({{ site.workshop_repo }})
links to the setup instructions for core lessons.

### `_extras/discussion.md`

General discussion of the lesson contents for learners who wish to know more:

1.  It must use the `page` layout.
2.  Its title must be `"Discussion"`.
3.  Its permalink must be `/discuss/`.
4.  It may include whatever content the author thinks appropriate.

This page normally includes links to further reading
and/or brief discussion of more advanced topics.

### `_extras/guide.md`

The instructors' guide for the lesson.

1.  It must use the `page` layout.
2.  Its title must be `"Instructors' Guide"`.
3.  Its permalink must be `/guide/`.
4.  It may include whatever content the author thinks appropriate.

This page records tips and warnings from people who have taught the lesson.

## Makefile Targets

Commonly-used commands are stored in `Makefile`.
Run `make` on its own to get a list of commands.

[jekyll]: http://jekyllrb.com/
[jekyll-collection]: https://jekyllrb.com/docs/collections/
