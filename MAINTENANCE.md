# Site Structure and Maintnence

This site depends strongly on github infrastructure, and 
a number of operational decisions have been made during the
development process that may not be obvious to a casual
or new contributor.

These are described below.

## Communications

### Github:

#### Carpentries-Incubator Project

HPC-Intro is currently on [GitHub][hpc-intro].  You need a github
account to contribute.  In addition, in order to get write access to
the repo, you will need to become a member of the HPC Intro
Maintainers team, which lives inside the "carpentries-incubator"
[project][incubator-base].

See also the instructions for [contributing](CONTRIBUTING.md).

#### HPC-Carpentry Project

There is also an HPC Carpentry [Github project][project-github], which
has other HPC-related lessons repos in its scope, and separate teams
of maintainers and administrators.

In particular, there is a "coordination" [repo][coord-repo], which is
a good scope for issues and concerns for the HPC carpentry community
at large, rather than any particular lesson.

There is also a [repo][mainsite-repo] for the main website covering
all HPC-Carpentry activities. This is intended to be the "front door"
of the HPC Carpentry community.

### Slack:

The main Carpentries slack channel is reachable at
[swcarpentry.slack.com][swc-slack]. You can go directly to the HPC
Carpentry sub-channel at [#hpc-carpentry][hpc-slack]. These are the
things to bookmark -- once you go there, the Slack engine redirects
you to particular views, so cutting/pasting URLs out of the browser's
location bar is likely to be disappointing.

Members of existing swcarpentry slack channels can find the channel by
typing "hpc-carpentry" into the slack search box.

To become a member, you can trigger in invitation from [here][slack-invite].

### E-mail:

The top-level site is on [Topicbox][topicbox]. There are two
HPC-specific lists, "discuss-hpc" and "maintainers-hpc". The system
does not use passwords, log-ins are via a verification code sent to
your e-mail. I don't recall how to join the lists, my recollection is
that anyone can participate in "discuss-hpc", but "maintainers-hpc" is
by invitation?


## Site Operation

### DOIs for Releases 

There is a web-hook that calls out to [Zenodo][zenodo] to create
a Digital Object Identifier (DOI) whenever an actual release
is generated on the site.  The Zenodo account is owned by 
Peter Steinbach.




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
