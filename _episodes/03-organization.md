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

Each lesson is made up of *episodes*, which are focused on a particular topic and
include time for both teaching and exercises.
The episodes of this lesson explain the tools we use to create lessons
and the formatting rules those lessons must follow.

> ## Why "Episodes"?
>
> We call the parts of lessons "episodes" because
> every other term (like "topic") already has multiple meanings,
> and because it encourages us to think of breaking up our lessons
> into chunks that are about as long as a typical movie scene,
> which is better for learning than long blocks without interruption.
{: .callout}

Our lessons need artwork,
CSS style files,
and a few bits of Javascript.
We could load these from the web,
but that would make offline authoring difficult.
Instead, each lesson's repository is self-contained.

The diagram below shows how source files and directories are laid out,
and how they are mapped to destination files and directories:

![Source and Destination Files]({{ page.root }}/fig/file-mapping.svg)

> ## Collections
>
> As described [earlier]({{ page.root }}/02-tooling/#collections),
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

# Standard Files

When the lesson repository is first created,
the initial author should create a `README.md` file containing
a one-line explanation of the lesson's purpose.

The [lesson template]({{ site.template_repo }}) provides the following files
which should *not* be modified:

*   `CONDUCT.md`: the code of conduct.
*   `LICENSE.md`: the lesson license.
*   `Makefile`: commands for previewing the site, cleaning up junk, etc.

## Starter Files

The `bin/lesson_initialize.py` script creates files that need to be customized for each lesson:

`CONTRIBUTING.md`
:   Contribution guidelines.
    The `issues` and `repo` links at the bottom of the file must be changed
    to match the URLs of the lesson:
    look for uses of `FIXME`.

`_config.yml`
:   The [Jekyll][jekyll] configuration file.
    This must be edited so that its links and other settings are correct for this lesson.
    *   `carpentry` should be either "dc" (for Data Carpentry), "lc" (for Library Carpentry), or "swc" (for Software Carpentry).
    *   `title` is the title of your lesson,
        e.g.,
        "Defence Against the Dark Arts".
    *   `email` is the contact email address for the lesson.

`CITATION`
:   A plain text file explaining how to cite this lesson.

`AUTHORS`
:   A plain text file listing the names of the lesson's authors.

`index.md`
:   The home page for the lesson.
    1.  It must use the `lesson` layout.
    2.  It must *not* have a `title` field in its [YAML][yaml] header.
    3.  It must open with a few paragraphs of explanatory text.
    4.  That introduction must be followed by a single `.prereq` blockquote
        detailing the lesson's prerequisites.
        (Setup instructions appear separately.)
    5.  That must be followed by inclusion of `syllabus.html`,
        which generates the syllabus for the lesson
        from the metadata in its episodes.

`reference.md`
:   A reference guide for the lesson.
    The template will automatically generate a summary of the episodes' key points.
    1.  It must use the `reference` layout.
    2.  Its title must be `"Reference"`.
    3.  Its permalink must be `/reference/`.
    4.  It should include a glossary, laid out as a description list.
    5.  It may include other material as appropriate.

`setup.md`
:   Detailed setup instructions for the lesson.
    Note that we usually divide setup instructions by platform,
    e.g.,
    include level-2 headings for Windows, macOS, and Linux
    with instructions for each.
    The [workshop template]({{ site.workshop_repo }})
    links to the setup instructions for core lessons.
    1.  It must use the `page` layout.
    2.  Its title must be `"Setup"`.
    3.  Its permalink must be `/setup/`.
    4.  It should include whatever setup instructions are required.

`_extras/about.md`
:   General notes about this lesson.
    This page includes brief descriptions of The Carpentries,
    and is a good place to put institutional acknowledgments.

`_extras/discussion.md`
:   General discussion of the lesson contents for learners who wish to know more:
    This page normally includes links to further reading
    and/or brief discussion of more advanced topics.
    1.  It must use the `page` layout.
    2.  Its title must be `"Discussion"`.
    3.  Its permalink must be `/discuss/`.
    4.  It may include whatever content the author thinks appropriate.

`_extra/figures.md` and `_includes/all_figures.html`
:   Does nothing but include `_includes/all_figures.html`,
    which is (re)generated by `make lesson-figures`.
    This page displays all the images referenced by all of the episodes,
    in order,
    so that instructors can scroll through them while teaching.

`_extras/guide.md`
:   The instructors' guide for the lesson.
    This page records tips and warnings from people who have taught the lesson.
    1.  It must use the `page` layout.
    2.  Its title must be `"Instructors' Guide"`.
    3.  Its permalink must be `/guide/`.
    4.  It may include whatever content the author thinks appropriate.

## Figures

All figures related with the lesson **must** be placed inside the directory `fig` at the root of the project.

{% include links.md %}
