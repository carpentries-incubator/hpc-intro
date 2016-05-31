---
title: "Using Divs"
teaching: 5
exercises: 0
questions:
- "Should we use div instead of blockquote for challenge?"
objectives:
- "Show the differences between divs and blockquotes for challenges."
keypoints:
- "The CSS changes are surprisingly small."
---
This is a challenge formatted using a `div`,
with one solution inside the `div:

<div class="challenge" markdown="1">

## Div Challenge Title as H2

This is the text explaining the challenge.

~~~
this code
is part of
the challenge
~~~
{: .source}

> ## Solution
>
> We can put the solution(s) in blockquotes inside the `div`.
> (Or we could define yet another `div` type.)
> 
> ~~~
> code in solution
> ~~~
> {: .output}
{: .solution}

</div>

This is a challenge formatted as a `blockquote`,
with a single solution as a nested `blockquote`:

> ## Blockquote Challenge Title as H2
>
> For comparison, this is a challenge done the old way (as a blockquote).
>
> ~~~
> this code
> is part of
> the challenge
> ~~~
> {: .source}
>
> > ## Solution
> >
> > And here is the body of the solution.
> >
> > ~~~
> > code in solution
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

This is a challenge formatted as a `blockquote`,
with the solution as a peer (not nested) `blockquote`:

> ## Blockquote Challenge Title as H2
>
> And this is the challenge with the solutions outside.
>
> ~~~
> this code
> is part of
> the challenge
> ~~~
> {: .source}
{: .challenge}

> ## Solution
>
> And here is the body of the solution.
>
> ~~~
> code in solution
> ~~~
> {: .output}
{: .solution}
