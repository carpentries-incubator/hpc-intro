---
layout: page
title: Setup
permalink: /setup/
---
## Setup Instructions for Actual Lessons

1. Installation instructions for core lessons are included in the [workshop template's home page][template],
   so that they are all in one place.
   The `setup.md` files of core lessons link to
    the appropriate sections of the [workshop template page][{{ site.workshop_repo }}].

2. Other lessons' `setup.md` include full installation instructions organized by OS
   (following the model of the workshop template home page).

## Setting Up for Lesson Development

If you want to set up Jekyll
so that you can preview changes on your own machine before pushing them to GitHub,
you must install the software described below.
(Note: Julian Thilo has written instructions for [installing Jekyll on Windows](http://jekyll-windows.juthilo.com/).)

1.  **Ruby**.
    This is included with Linux and Mac OS X;
    the simplest option on Windows is to use [RubyInstaller](http://rubyinstaller.org/).
    You can test your installation by running `ruby --version`.
    For more information,
    see [the Ruby installation guidelines](https://www.ruby-lang.org/en/downloads/).

2.  **[RubyGems](https://rubygems.org/pages/download)**
    (the package manager for Ruby).
    You can test your installation by running `gem --version`.

3.  **[Jekyll](https://jekyllrb.com/)**.
    You can install this by running `gem install jekyll`.

If you want to run `bin/lesson-check` (which is invoked by `make lesson-check`)
you will need Jekyll (so that you have its Markdown parser, which is called Kramdown)
and the [PyYAML](https://pypi.python.org/pypi/PyYAML) module for Python 3.
