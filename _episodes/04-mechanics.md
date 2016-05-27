---
title: "Mechanics"
teaching: 5
exercises: 0
questions:
- "What do lesson maintainers do?"
objectives:
- "FIXME"
keypoints:
- "FIXME"
---
This episode describes the processes used to maintain our lessons.

## Maintainers

Each Software or Data Carpentry lesson has one or two maintainers,
who are responsible for making sure issues and change requests are looked at,
and who have final say over what is included in the lesson.
Together,
they also decide on changes to the lesson templates,
release procedure,
and other mechanical aspects of lesson production.
They are *not* responsible for writing lesson content or deciding what lessons ought to exist:
the former comes from the community,
and the latter from the Executive Directors and Steering Committees of Software and Data Carpentry.

The process for selecting and onboarding a new maintainer is:

*   Outgoing maintainer emails the discussion list to announce the opportunity
    *    Application information includes name, github username, statement of intent.
    *    Deadline for applications, projected timeline for selection.
    *    Name/email of contact for application process (typically outgoing maintainer).
*   Applications accumulate over a week or two.
*   Outgoing maintainer and their co-maintainer review applications and choose new maintainer. 
*   The new maintainer is informed, and other applicants are thanked via email. 
*   To onboard the new maintainer:
    *    Add new maintainer to the maintainers' list.
    *    Email the maintainers to announce the change. 
    *    Request push/merge access for new maintainer from the Software Carpentry executive director.  
    *    Write a blog post introducing new maintainer.  
    *    Optional: call between outgoing/incoming maintainer to discuss state of the repository, transition strategy, etc. 

## Release Process and Schedule

We have decided to use a **6-month release cycle** for releases, which
will be named by the year and month they happen, e.g., `2016.05`.

1. Each lesson lives in the `gh-pages` branch of its own repository.
2. When a release has to be made,
    the *lesson maintainer* (or maintainers) create a branch named after the release, e.g., `2016.05`.
3. A *release maintainer* generates HTML pages for that release and add them to the branch.
4. If there isn't already a directory for that release in the `swc-release` repository,
   the release maintainer creates one
   and adds an `index.html` page to it.
5. The release maintainer adds a submodule to the release directory of `swc-release`
   that points to the newly-created release branch of the lesson.
