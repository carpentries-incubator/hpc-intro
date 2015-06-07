## FAQ

*   *Where can I get help?*

    Mail [admin@software-carpentry.org](mailto:admin@software-carpentry.org),
    or join our [discussion list](http://lists.software-carpentry.org/mailman/listinfo/discuss_lists.software-carpentry.org)
    and ask for help there.

*   *Where can I report problems or suggest improvements?*

    Please
    [file an issue](https://github.com/swcarpentry/lesson-template/issues?q=is%3Aopen+is%3Aissue)
    or [mail us](mailto:admin@software-carpentry.org).

*   *Why does the new lesson's repository have to be created using import? Why not fork `lesson-template` on GitHub?*

    Because any particular user can only have one fork of a repository,
    but instructors frequently need to work on several workshops at once.

*   *Why use Markdown?*

    1.  It is simpler, and easier to write, than HTML or LaTeX.
    2.  It is a lowest common denominator: anything that can be expressed in Markdown can easily be translated into richer formats.
    3.  It is used by a much wider variety of people than other text markup formats like reStructured Text (reST).

*   *Why use Pandoc?  Why not some other converter?*

    Because it supports a richer dialect of Markdown than Jekyll
    (the converter that GitHub uses by default).
    In particular, Pandoc allows us to add styles to headings
    and lets us specify languages for code blocks without having to wrap them in `div` tags.

*   *What do the [labels](https://github.com/swcarpentry/lesson-template/issues?q=is%3Aopen+is%3Aissue) mean?*

    *   `bug`: something that is wrong
    *   `build`: changes to `Makefile`, the validator, or lesson creation process
    *   `defer`: we will work on, but not now
    *   `discussion`: for conversations about specific problems and questions
    *   `documentation`: information about how to use the lesson-template
    *   `enhancement`: asks for, or adds, a new feature, new information or reword old ones
    *   `newcomer-friendly`: issue or pull request is a good starting point for someone who is relatively new to GitHub and/or this project
    *   `upstream`: issue or pull request involving upstream repository, e.g. https://github.com/swcarpentry/lesson-template
    *   `work-in-progress`: a pull request that is not yet ready for review

*   *How can we create input cells for particular languages?*

    Use

        ~~~ {.lang}
        some code
        ~~~

    where `lang` is `bash` for the Unix Shell, `r` for R, `matlab` for MATLAB,
    `python` for Python, and `sql` for SQL. For a full list, check:

    ~~~ {.bash}
    $ pandoc -v
    ~~~

## Debugging

Please add notes about problems and solutions below.

*   `pandoc: command not found`

    You probably don't have [Pandoc](http://pandoc.org/installing.html) installed.

*   `pandoc: Error running filter tools/filters/blockquote2div.py`
    due to `ImportError: No module named 'pandocfilters'`

    You probably haven't installed
    [pandocfilters](https://pypi.python.org/pypi/pandocfilters/1.2.3).

*   `pandoc: Error running filter tools/filters/blockquote2div.py
    tools/filters/blockquote2div.py not found in path`

    Git has likely checked out the files with the incorrect line endings.
    On Unix systems the recommended setting is:

    ~~~ {.bash}
    git config --global core.autocrlf input
    ~~~

    and on Windows:

    ~~~ {.bash}
    git config --global core.autocrlf true
    ~~~

    Note that after changing this setting you will need to either re-clone
    or re-checkout the files in the repository.

*   If a lesson generates Markdown from an IPython Notebook,
    then whenever a figure is moved, added, or removed,
    the auto-generated names of the image files produced by `.ipynb`-to-`.md` conversion will change.
    This confuses version control.
