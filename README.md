lesson-example
==============

This repository shows how to create a lesson using
the [Software Carpentry][swc] [lesson template][swc-lesson-template],
and is itself an example of the use of that template.

1.  Do *not* fork this repository directly on GitHub.
    Instead, please follow the instructions below
    to create a repository for your lesson from
    the [lesson template][swc-lesson-template].

2.  Once you have created the repository,
    please go through [the layout instructions](LAYOUT.md) to format your lesson.

3.  Please keep the master copy of your lesson in your repository's `gh-pages` branch,
    since that is what is
    [automatically published as a website by GitHub](https://help.github.com/articles/creating-project-pages-manually/).
    To simplify reviewing,
    please make changes in feature branches
    and then submit pull requests against the `gh-pages` branch of your lesson's repository.

## Creating Your Lesson's Repository

We will assume that your user ID is `gvwilson` and the name of your
lesson is `data-cleanup`.

1.  Go to [GitHub's importer][import].

2.  Click on "Check the URL".  (GitHub won't import until you've done this.)

3.  Select the owner for your new repository.
    In our example this is `gvwilson`,
    but it may instead be an organization you belong to.

4.  Choose a name for your lesson repository.
    In our example, this is `data-cleanup`.

5.  Make sure the repository is public.

6.  At this point, you should have a page like this:

    ![](img/using-github-import.png)

    You can now click "Begin Import".
    When the process is done,
    you can click "Continue to repository" to visit your newly-created repository.

7.  Clone your newly-created repository to your desktop:

    ~~~
    $ git clone -b gh-pages https://github.com/gvwilson/data-cleanup.git
    ~~~

    Note that the URL for your lesson will be different than the one above.

8.  Go into that directory using:

    ~~~
    $ cd data-cleanup
    ~~~

    Note that the name of your directory will be different,
    since your lesson probably won't be called `data-cleanup`.

9.  Manually add the lesson template repository as a remote called `template`:

    ~~~
    $ git remote add template https://github.com/swcarpentry/lesson-template.git
    ~~~

    This will allow you to pull in changes made to the template,
    such as improvements to our CSS style files.
    (Note that the user name above is `swcarpentry`, *not* `gvwilson`,
    since you are adding the master copy of the template as a remote.)

10. Create and edit files as explained in
    [Lesson Layout](LAYOUT.md),
    [Background and Design](DESIGN.md),
    and the [FAQ](FAQ.md).

11. Build the HTML pages for your lesson:

    ~~~
    $ make preview
    ~~~

    This step requires you to have installed Pandoc (described below).
    It is *not* optional: you *must* build the web pages for your
    lesson yourself and push them to GitHub, rather than relying on
    GitHub to build them for you.

12. Commit your changes *and the HTML pages in the root directory of
    your lesson repository* and push to the `gh-pages` branch of your
    repository:

    ~~~
    $ cd data-cleanup
    $ git add changed-file.md changed-file.html
    $ git commit -m "Explanatory message"
    $ git push origin gh-pages
    ~~~

13. [Tell us](#getting-and-giving-help) where your lesson is so that we can add it to
    [the Software Carpentry lessons page][swc-lessons-page].

**Note:** SSH cloning (rather than the HTTPS cloning used above)
will also work for those who have set up SSH keys with GitHub.

**Note:** Once a lesson has been created, please submit changes
for review as pull requests that contain *only the modified Markdown files*,
and *not* the re-generated HTML.  This simplifies review considerably,
since each change appears only once.  Once the change has been approved,
the lesson maintainer(s) will merge the pull request, re-generate the HTML
locally, and pus that to GitHub.

**Note:**
some people have had intermittent errors during the import process,
possibly because of the network timing out.
If you experience a problem, please re-try;
if the problem persists,
please [get in touch](#getting-and-giving-help).

## Dependencies

Because people may choose to use the IPython Notebook, R Markdown, or
some other format for parts of their lessons, and because Jekyll (the
tool GitHub uses to build HTML pages) only supports an impoverished
form of Markdown, we require lesson authors to build the HTML pages
for their lessons on their machines with Pandoc and commit those to
the `gh-pages` branch of their lesson website.  To do this:

1. [Install Pandoc](http://www.pandoc.org/installing)

2. All Python packages required for lesson creation and validation can 
   be installed using:
   
    ~~~
    $ pip install -r requirements.txt
    ~~~
        
3. To convert Markdown files into HTML pages in the root directory, go
   into the root directory of your lesson and run:

   ~~~
   $ make preview
   ~~~

   You can run `make` on its own to get a list of other things it will
   do for you.

## Why Use a Template?

We organize our lessons in a standard way so that:

1.  To give guidance to people who aren't experienced instructional
    designers.  Requiring learning objectives, challenges, and a short
    glossary tells people what they ought to create.

2.  It's easy to find things in lessons written by different people.

3.  People using lessons written by different people can easily given
    them the same look and feel.

4.  Contributors know where to put things when they are extending or
    modifying lessons.

5.  Content can be checked mechanically.

## Why Is This Example and Documentation Separate from the Template?

We want it to be easy for authors to merge changes
made to the [lesson template][swc-lesson-template]
into their lesson.
If the lesson template contained all of the documentation in this example,
then every time a merge was done,
authors would have to re-delete those files,
undo merges into their lesson's `README.md`,
etc.
We hope that putting the core files in a repository of their own
will avoid this problem.

(Note that from Fall 2014 to Spring 2015 we tried using two branches in a single repository,
one for the core files and one for the example.
Many contributors [found it confusing](https://github.com/swcarpentry/lesson-template/issues/118);
we hope that separate repositories will be easier to keep straight.)

## Lesson Structure

Instead of putting the whole lesson in one page, authors should create
one short page per topic.  Each topic should take 10-15 minutes to
cover, and that coverage to include:

1.  Explain the topic's objectives.

2.  Perform the material.  (We expect instructors to code live, *not*
    to put lesson notes or slides on the screen.)

3.  Do one or more challenges depending on time.

Along with the lesson materials themselves, each lesson must contain:

*   *Introductory slides* to give learners a sense of where the next
    two or three hours are going to take them.

*   A *reference guide* that learners can use during the lesson and take
    away afterward.  This must include a glossary of terms, not only to
    help learners, but also to help lesson authors summarize what the
    lesson actually covers.

*   A *discussion page* that mentions more advanced ideas and tells
    learners where to go next.

*   An *instructor's guide* that presents the lesson's legend (or back
    story), summarizes our experiences with the lesson, and discusses
    solutions to the challenge exercises.  We ask everyone who teaches
    for us to review and update the instructor's guide for each lesson
    they taught after each workshop.

    Note that the this means the solutions to the lesson's challenge
    exercises will be up on the web.  We have chosen to do this
    because we believe in openness, and because there's no point
    trying to hide something that's in a publicly-readable repository.

Authors may retain copyright on their lessons, but we ask that all
lessons be published under the Creative Commons - Attribution (CC-BY)
license, or put in the public domain (CC-0), to permit remixing.

## For More Information

Please see the following for more information on:

*   [lay out your lesson](LAYOUT.md)
*   [background and design](DESIGN.md)
*   [FAQ](FAQ.md)

## Getting and Giving Help

If you find bugs in our instructions,
or would like to suggest improvements,
please [file an issue in this repository](https://github.com/swcarpentry/lesson-example/issues);
if you find bugs in the template files themselves,
please [file an issue in the `lesson-template` repository](https://github.com/swcarpentry/lesson-template/issues).
You can also [mail us](mailto:admin@software-carpentry.org) with questions or problems.

Please also [mail us](mailto:admin@software-carpentry.org)
whenever you create a new lesson and would like to advertise it on our web site.

## Maintainers

*   Andy Boughton (@abought)
*   Rémi Emonet (@twitwi)
*   Raniere Silva (@r-gaia-cs)

[swc]: http://software-carpentry.org
[swc-lesson-template]: https://github.com/swcarpentry/lesson-template
[swc-lessons-page]: http://software-carpentry.org/lessons.html
[import]: http://import.github.com/new?import_url=https://github.com/swcarpentry/lesson-template
