---
title: "Using RMarkdown"
teaching: 10
exercises: 2
questions:
- "How to write a lesson using RMarkdown?"
objectives:
- "Explain how to use RMarkdown with the new lesson template."
- "Demonstrate how to include pieces of code, figures, and challenges."
keypoints:
- "It shouldn't be difficult"
---
This episode demonstrates all the features that can be used when writing a
lesson in RMarkdown.

This first chunk is really important, and should be included in all markdown lessons.



The rest of the lesson should be written as a normal RMarkdown file. You can
include chunk for codes, just like you'd normally do:

Normal output:


~~~
1 + 1
~~~
{: .r}



~~~
[1] 2
~~~
{: .output}

Output with error message:


~~~
x[10]
~~~
{: .r}



~~~
[1] NA
~~~
{: .output}

Output generating figures:


~~~
library(ggplot2)
~~~
{: .r}



~~~
Warning: package 'ggplot2' was built under R version 3.1.3
~~~
{: .error}



~~~
ggplot(diamonds, aes(x = carat,  y = price, color = cut)) +
    geom_point()
~~~
{: .r}

<img src="../fig/swc-rmd-plot-example-1.png" title="plot of chunk plot-example" alt="plot of chunk plot-example" style="display: block; margin: auto;" />

For the challenges and their solutions, you need to pay attention to the where
the `>` go and where to leave blank lines. Otherwise, you can include chunks in
it to include instructions and solutions.

> ## Challenge: Can you do it?
>
> What is the output of this command?
>
> 
> ~~~
> paste("This", "new", "template", "looks", "good")
> ~~~
> {: .r}
>
> > ## Solution
> >
> > 
> > ~~~
> > [1] "This new template looks good"
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
