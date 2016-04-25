---
title: "Formatting"
teaching: 10
exercises: 0
questions:
- "How are Software Carpentry lessons formatted?"
objectives:
- "Explain the header of each episode."
- "Explain the overall structure of each episode."
- "Explain why blockquotes are used to format parts of episodes."
- "Explain the use of code blocks in episodes."
keypoints:
- "Lesson episodes are stored in _episodes/dd-subject.md."
- "Each episode's title must include a title, time estimates, motivating questions, lesson objectives, and key points."
- "Episodes should not use sub-headings or HTML layout."
- "Code blocks can be have the source, regular output, or error class."
- "Special sections are formatted as blockquotes that open with a level-2 header and close with a class identifier."
- "Special sections may be callouts or challenges; other styles are used by the template itself."
---
A lesson consists of one or more episodes,
each of which has:

*   a [YAML][yaml] header containing required values
*   some teachable content
*   some exercises

## Locations and Names

Episode files are stored in `_episodes` so that [Jekyll][jekyll] will create a [collection][jekyll-collection] for them.
Episodes are named `dd-subject.md`,
where `dd` is a two-digit sequence number (with a leading 0)
and `subject` is a one- or two-word identifier.
For example,
the episodes of this example lesson are
`_episodes/01-tooling.md`
`_episodes/02-formatting.md`,
and `_episodes/03-organization.md`.
These become `/01-tooling/`, `/02-formatting/`, and `/03-organization/` respectively in the published site
(the episode file `dd-subject.md` is turned into `dd-subject/index.html`).
When referring to other episodes, use:

{% raw %}
    [link text]({{ site.root }}/dd-subject/)
{% endraw %}

i.e., use the episode's directory path below the site root.
This will ensure that the link is valid both when previewing during desktop development
and when the site is published on GitHub.

## Episode Header

Each episode's [YAML][yaml] header must contain:

*   the episode's title
*   time estimates for teaching and exercises
*   motivating questions
*   lesson objectives
*   a summary of key points

These values are stored in the header so that [Jekyll][jekyll] will read them
and make them accessible in other pages as `site.episodes.the_episode.key`,
where `the_episode` is the particular episode
and `key` is the key in the [YAML][yaml] header.
This lets us do things like
list each episode's key questions in the syllabus on the lesson home page.

> ## Raw Text
>
> Markdown in YAML values in the header is *not* rendered when the value is used elsewhere.
{: .callout}

## Episode Structure

The episode layout template in `_layouts/episode.html` automatically creates
an introductory block that summarizes the lesson's teaching time,
exercise time,
key questions,
and objectives.
It also automatically creates a closing block that lists its key points.
In between,
authors should use only:

*   paragraphs
*   images
*   tables
*   ordered and unordered lists
*   code samples (described below).
*   special blockquotes (described below)

Authors should *not* use:

*   sub-headings
*   HTML layout (e.g., `div` elements).

## Formatting Code

Inline code fragments are formatted using back-quotes.
Longer code blocks are formatted by opening and closing the block with `~~~` (three tildes),
with a class specifier after the block:

    ~~~
    for thing in collection:
        do_something
    ~~~
    {: .source}

which is rendered as:

~~~
for thing in collection:
    do_something
~~~
{: .source}

The class specified at the bottom using an opening curly brace and colon,
the class identifier with a leading dot,
and a closing curly brace.
The [template]({{ site.template_repo }}) provides three styles for code blocks:

*   `.error`: error messages.
*   `.output`: program output.
*   `.source`: program source.

> ## Why No Syntax Highlighting?
>
> We do not use syntax highlighting for code blocks
> because some learners' systems won't do it,
> or will do it differently than what they see on screen.
{: .callout}

## Special Blockquotes

We use blockquotes to group headings and text
rather than wrapping them in `div` elements.
in order to avoid confusing [Jekyll][jekyll]'s parser
(which sometimes has trouble with Markdown inside HTML).
Each special blockquote must started with a level-2 header,
but may contain anything after that.
For example,
a callout is formatted like this:

~~~
> ## Callout Title
>
> text
> text
> text
>
> ~~~
> code
> ~~~
{: .callout}
~~~

(Note the empty lines within the blockquote after the title and before the code block.)
This is rendered as:

> ## Callout Title
>
> text
> text
> text
>
> ~~~
> code
> ~~~
{: .callout}

The [lesson template]({{ site.template_repo }}) defines styles
for the following special blockquotes:

*   `.callout`: an aside or other comment.
*   `.challenge`: an exercise.
*   `.getready`: preparatory material.
*   `.keypoints`: key points of an episode.
*   `.objectives`: episode objectives.
*   `.prereq`: lesson prerequisites.
*   `.testimonial`: a laudatory quote from a user.

Most authors will only use `.callout` and `.challenge`,
as the others are automatically generated by the template.

[jekyll]: http://jekyllrb.com/
[jekyll-collection]: https://jekyllrb.com/docs/collections/
[yaml]: http://yaml.org/
