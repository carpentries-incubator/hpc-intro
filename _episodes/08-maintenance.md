---
title: "Maintenance"
teaching: 5
exercises: 0
questions:
- "What do lesson maintainers do?"
objectives:
- "Explain the rights and responsibilities of lesson maintainers."
keypoints:
- "Each lesson has one or two maintainers who act as editors."
- "Maintainers are responsible for ensuring that issues and change requests are addressed."
- "Maintainers have final say over lesson content."
- "We use a standard set of labels to classify issues and pull requests."
---

This episode describes the processes used to maintain our lessons.

## Maintainers

Each Carpentry lesson has multiple Maintainers,
who are responsible for making sure issues and change requests are looked at,
and who have final say over what is included in the lesson.
They are *not* responsible for writing lesson content or deciding what lessons ought to exist:
the former comes from the community,
and the latter from the Carpentry Executive Council and Curricular Advisory Committees.

The process for selecting and onboarding a new Maintainer is:

*   Opportunity for new Maintainers is announced via blog post, mailing list, and Twitter with link to application form.
*   Applications accumulate.
*   Applications are reviewed (e.g. by existing Maintainers for that lesson).
*   The new Maintainer(s) are informed, and other applicants are thanked via email.
*   To onboard the new Maintainer(s):
    *   Ask new Maintainer(s) to add themselves to the [Maintainers' email list](http://lists.software-carpentry.org/listinfo/maintainers).
    *   Invite new Maintainer(s) to join [Maintainer Onboarding Google Group](https://groups.google.com/a/carpentries.org/forum/#!forum/maintainer-onboarding). 
    *   Invite new Maintainer(s) to join [Maintainer meetings](http://pad.software-carpentry.org/maintainers).
    *   New cohort of Maintainer(s) complete [Maintainer Onboarding](https://carpentries.github.io/maintainer-onboarding/).
    *   Request write access for new Maintainer(s) to the appropriate repos from the Carpentry Executive Director.

## Release Process and Schedule

We have decided to use a **6-month release cycle** for releases, which
will be named by the year and month they happen, e.g., `2016.05`.

1.  Each lesson lives in the `gh-pages` branch of its own repository.
2.  When a release has to be made,
    the *lesson Maintainer(s)* create a branch named after the release,
    e.g., `2016.05`.
3.  A *Release Maintainer* generates HTML pages for that release and adds them to the branch.
4.  If there isn't already a directory for that release in the `swc-release` repository,
    the Release Maintainer creates one
    and adds an `index.html` page to it.
5.  The Release Maintainer adds a submodule to the release directory of `swc-release`
    that points to the newly-created release branch of the lesson.

## Issue Labels in Repositories

Our repositories use the following labels (and colors) for issues and pull requests:

*   `bug` (#bd2c00): errors to be fixed.
*   `discussion` (#fc8dc1): discussion threads.
*   `enhancement` (#9cd6dc): new features.
*   `help-wanted` (#f4fd9c): requests for assistance.
*   `instructor-training` (#6e5494): pull requests submitted as part of instructor training.
*   `newcomer-friendly` (#eec275): suitable for people who are still learning the ropes.
*   `question` (#808040): often turn into discussion threads.
*   `template-and-tools` (#2b3990): issues related to the templates and tools
    rather than the lessons themselves.
*   `work-in-progress` (#7ae78): someone is still working on this.

{% include links.md %}
