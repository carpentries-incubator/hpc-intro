---
layout: lesson
root: .
---

{% include gh_variables.html %}
{% assign hours = site.hpc_start_time | divided_by: 60 %}
{% assign minutes = site.hpc_start_time | modulo: 60 %}
{% assign late_start_episode = site.episodes | where: "slug", site.hpc_start_lesson | first %}
The first half of this workshop will cover basics of command line (in an HPC environment).

The second harlf of this workshop will provide an introduction and overview to the tools available on high-performance computing systems and how to use them effectively.

If you are already comfortable with command line and wish to skip the first half you may join for the [{{late_start_episode.title}}]({{site.url}}/{{site.hpc_start_lesson}}) at {% if hours < 10 %}0{% endif %}{{ hours}}:{% if minutes < 10 %}0{% endif %}{{ minutes }}

> ## Prerequisites
>
> While we cover the bash essentials, we still recommend checking out the 
> [shell-novice](https://swcarpentry.github.io/shell-novice/) lesson for a better foundation in bash.
{: .prereq}

By the end of this workshop, students will know how to:

* Identify problems a cluster can help solve
* Use the UNIX shell (also known as terminal or command line) to operate a
  computer, connect to a cluster, and write simple shell scripts.
* Submit and manage jobs on a cluster using a scheduler, transfer files, and
* Use software through environment modules.
* Review and optimise job resource usage.

> ## Getting Started
>
> To get started, follow the directions in the "[Setup](
> {{ page.root }}/setup.html)" tab and follow any installation instructions.
{: .callout}

Note that this is the draft HPC Carpentry release. Comments and feedback are
welcome.

This is a hands on workshop, excersises will generally depend on the previous steps having been completed, so it is important to keep up!

{% include links.md %}
