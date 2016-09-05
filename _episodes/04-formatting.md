---
title: "Formatting"
teaching: 10
exercises: 0
questions:
- "How are Software and Data Carpentry lessons formatted?"
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

The diagram below shows the internal structure of a single episode file
(click on the image to see a larger version):

<a href="{{ page.root }}/fig/episode-format.png"><img src="{{ page.root }}/fig/episode-format-small.png" alt="Formatting Rules" /></a>

## Locations and Names

Episode files are stored in `_episodes`
so that [Jekyll][jekyll] will create a [collection][jekyll-collection] for them.
Episodes are named `dd-subject.md`,
where `dd` is a two-digit sequence number (with a leading 0)
and `subject` is a one- or two-word identifier.
For example,
the first three episodes of this example lesson are
`_episodes/01-design.md`,
`_episodes/02-tooling.md`
and `_episodes/03-formatting.md`.
These become `/01-design/index.html`, `/02-tooling/index.html`, and `/03-formatting/index.html`
in the published site.
When referring to other episodes, use:

{% raw %}
    [link text]({{ page.root }}/dd-subject/)
{% endraw %}

i.e., use the episode's directory path below the site root
*without* the `index.html` (which the web server fills in automatically).
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

{% raw %}
    ~~~
    for thing in collection:
        do_something
    ~~~
    {: .source}
{% endraw %}

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

~~~
.source: program source.
~~~
{: .source}

~~~
.output: program output.
~~~
{: .output}

~~~
.error: error messages.
~~~
{: .error}

The following styles are all synonyms for `.source`;
please use them where possible to indicate the type of source being displayed,
in case we decide to adopt syntax highlighting at some point:

*   `.bash`: Bash shell commands
*   `.make`: Makefiles
*   `.matlab`: MATLAB source
*   `.python`: Python source
*   `.r`: R source
*   `.sql`: SQL source

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
> {: .source}
{: .callout}
~~~
{: .source}

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
> {: .source}
{: .callout}

The [lesson template]({{ site.template_repo }}) defines styles
for the following special blockquotes:

<div class="row">
  <div class="col-md-6" markdown="1">

> ## .callout
>
> An aside or other comment.
{: .callout}

> ## `.challenge`
>
> An exercise.
{: .challenge}

> ## `.checklist`
>
> Checklists.
{: .checklist}

> ## `.discussion`
>
> Discussion questions.
{: .discussion}

> ## `.keypoints`
>
> Key points of an episode.
{: .keypoints}

  </div>
  <div class="col-md-6" markdown="1">

> ## `.objectives`
>
> Episode objectives.
{: .objectives}

> ## `.prereq`
>
> Prerequisites.
{: .prereq}

> ## `.solution`
>
> Exercise solution.
{: .solution}

> ## `.testimonial`
>
> A laudatory quote from a user.
{: .testimonial}

  </div>
</div>

Note that `.challenge` and `.discussion` have the same color but different icons.
Note also that one other class, `.quotation`,
is used to mark actual quotations
(the original purpose of the blockquote element).
This does not add any styling,
but is used to prevent the checking tools from complaining about a missing class.

Most authors will only use `.callout`, `.challenge`, and `.prereq`,
as the others are automatically generated by the template.
Note that `.prereq` is meant for describing things that learners should know before starting this lesson;
setup instructions do not have a particular style,
but are instead put on the `setup.md` page.

Note also that solutions are nested inside exercises as shown below:

~~~
> ## Challenge Title
>
> This is the body of the challenge.
>
> ~~~
> it may include some code
> ~~~
> {: .source}
>
> > ## Solution
> >
> > This is the body of the solution.
> >
> > ~~~
> > it may also include some code
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
~~~
{: .source}

The double indentation is annoying to edit,
but the alternatives we considered and discarded are worse:

1.  Use HTML `<div>` elements for the challenges.
    Most people dislike mixing HTML and Markdown,
    and experience shows that it's all too easy to confuse Jekyll's Markdown parser.

2.  Put solutions immediately after challenges rather than inside them.
    This is simpler to edit,
    but clutters up the page
    and makes it harder for tools to tell which solutions belong to which exercises.

[jekyll]: http://jekyllrb.com/
[jekyll-collection]: https://jekyllrb.com/docs/collections/
[yaml]: http://yaml.org/
