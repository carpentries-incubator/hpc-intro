# Site Structure and Maintenance

This site depends strongly on GitHub infrastructure, and a number of
operational decisions have been made during the development process
that may not be obvious to a casual or new contributor.

These are described below.

## Communications

### GitHub

#### Carpentries-Incubator Project

HPC-Intro is currently on [GitHub][hpc-intro]. You need a GitHub
account to contribute. In addition, in order to get write access to
the repository ("repo"), you will need to become a member of the HPC
Intro Maintainers team, which lives inside the "carpentries-incubator"
[project][incubator-base].

See also the instructions for [contributing](CONTRIBUTING.md).

#### HPC-Carpentry Project

There is also an HPC Carpentry [GitHub project][project-github], which
has other HPC-related lessons repos in its scope, and separate teams
of maintainers and administrators.

In particular, there is a "coordination" [repo][coord-repo], which is
a good scope for issues and concerns for the HPC carpentry community
at large, rather than any particular lesson.

There is also a [repo][mainsite-repo] for the main website covering
all HPC-Carpentry activities. This is intended to be the "front door"
of the HPC Carpentry community.

### Slack:

The main Carpentries Slack channel is reachable at
[swcarpentry.slack.com][swc-slack]. To become a member, you can
trigger in invitation from [here][slack-invite].

You can go directly to the HPC Carpentry sub-channel at
[#hpc-carpentry][hpc-slack]. These are the things to bookmark — once
you go there, the Slack engine redirects you to particular views, so
cutting/pasting URLs out of the browser's location bar is likely to be
disappointing.

Members of existing swcarpentry Slack channels can find the channel by
typing "hpc-carpentry" into the Slack search box.


### E-mail:

The top-level site is on The Carpentries' [Topicbox][topicbox]. There
are two HPC-specific lists, "discuss-hpc" and "maintainers-hpc". These
mailing lists are public: you may join any that catch your interest.
The system does not use passwords; log-ins are via a verification code
sent to your e-mail.


## Site Operation

### DOIs for Releases 

There is a web-hook that calls out to [Zenodo][zenodo] to create a
Digital Object Identifier (DOI) whenever a release is generated on the
GitHub repo. The Zenodo account is owned by Peter Steinbach (@psteinb).


### Continuous Integration

The high-level lesson structure is described reasonably well in the
[README](README.md) file, but there are some subtleties that can arise
at build-time.

You can locally preview some of the tests by providing arguments to
the `make` command that you run in the top-level directory. In
particular, `make lesson-check-all` checks a number of important
things, like the existence of files with appropriate metadata. The
actual checks are executed by the Python script in
`bin/lesson_check.py`, which can be examined for important clues.

You can control what sorts of checks a file will be subject to by
selecting a `checker` type in the list of regular-expression matches
assigned to `CHECKERS` near the bottom of `bin/lesson_check.py`.

<!-- Reference -->

[hpc-intro]: https://github.com/carpentries-incubator/hpc-intro
[incubator-base]: https://github.com/carpentries-incubator
[project-github]: https://github.com/hpc-carpentry
[coord-repo]: https://github.com/hpc-carpentry/coordination
[mainsite-repo]: https://github.com/hpc-carpentry/hpc-carpentry.org
[swc-slack]: https://swcarpentry.slack.com
[hpc-slack]: https://swcarpentry.slack.com/#hpc-carpentry
[slack-invite]: https://swc-slack-invite.herokuapp.com
[topicbox]: https://carpentries.topicbox.com
[zenodo]: https://zenodo.org/
