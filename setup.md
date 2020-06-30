---
title: Setup
---

Our lesson template is kept in the [`carpentries/styles` repository][styles]. The `styles`
repository is carefully curated so that changes made to it are easily mergeable by downstream
lessons. The `styles` repository contains various bits that take Markdown files and render them as a
lesson web page. For more information on how to develop lessons and maintain them, see our
[lesson-example][lesson-example]. It will walk you through the basics of lesson design and how to
use GitHub, Markdown and Jekyll for lesson development. Follow the instructions below to make your
own empty lesson in your own GitHub account. Once you've done that you can just write Markdown code
and have lesson web pages just like the [lesson-example][lesson-example] and all of our other
lessons, but with your lesson content.

## Requirements

* A GitHub account
* A working [Python 3.4+](https://www.python.org) environment to run the lesson initialization
  script
* (Optional) A local install of [Jekyll](https://jekyllrb.com/) (version 3.2 or higher) which will
  require the Ruby language to be installed.

## Creating a New Lesson

We will assume that your user ID is `timtomch` and the name of your
new lesson is `data-cleanup`.

1.  We'll use the [GitHub's importer][importer] to make a copy of this repo in your own GitHub
    account. (Note: This is like a GitHub Fork, but not connected to the upstream changes)

2.  Put the URL of **[the styles repository][styles]**, that is
    **https://github.com/carpentries/styles** in the "Your old repository’s clone URL" box.
    Do not use the URL of this repository,
    as that will bring in a lot of example files you don't actually want.

3.  Select the owner for your new repository.
    In our example this is `timtomch`,
    but it may instead be an organization you belong to.

4.  Choose a name for your lesson repository.
    In our example, this is `data-cleanup`.

5.  Make sure the repository is public.

6.  At this point, you should have a page like this:

    ![]({{ page.root }}/fig/using-github-import.png)

    You can now click "Begin Import".
    When the process is done,
    you can click "Continue to repository" to visit your newly-created repository.

    Through the Github interface you can begin to edit and

7.  If you want to work on the lesson from your local machine, you can
    now clone your newly-created repository to your computer:

    ~~~
    $ git clone -b gh-pages https://github.com/timtomch/data-cleanup.git
    ~~~
    {: .language-bash}

    Note that the URL for your lesson will have your username and chosen repository name.

8.  Go into that directory using:

    ~~~
    $ cd data-cleanup
    ~~~
    {: .language-bash}

    Note that the name of your directory should be what you named your lesson
    on the example this is `data-cleanup`.

9. To be able to pull upstream style changes, you should manually add the
     styles repository as a remote called `template`:

    ~~~
    $ git remote add template https://github.com/carpentries/styles.git
    ~~~
    {: .language-bash}

    This will allow you to pull in changes made to the template,
    such as improvements to our CSS style files.
    (Note that the user name above is `carpentries`, *not* `timtomch`,
    since you are adding the master copy of the template as a remote.)

10. Configure the `template` remote to not download tags:

    ~~~
    $ git config --local remote.template.tagOpt --no-tags
    ~~~
    {: .language-bash}

10. Make sure you are using the `gh-pages` branch of the lesson template:

    ~~~
    $ git checkout gh-pages
    ~~~
    {: .language-bash}

	This will ensure that you are using the most "stable" version of the
	template repository. Since it's being actively maintained by the
	Software Carpentry community, you could end up using a development branch
	that contains experimental (and potentially not working) features without
	necessarily realising it. Switching to the `gh-branch` ensures you are
	using the "stable" version of the template.

11. Run `bin/lesson_initialize.py` to create all of the boilerplate files
    that cannot be put into the styles repository
    (because they would trigger repeated merge conflicts).

12. Create and edit files as explained further in
    [the episodes of this lesson]({{ page.root }}{% link index.md %}#schedule).

13. (requires Jekyll Setup from below) Preview the HTML pages for your lesson:

    ~~~
    $ make serve
    ~~~
    {: .language-bash}

    Alternatively, you can try using Docker:

    ~~~
    $ make docker-serve
    ~~~
    {: .language-bash}

14. Commit your changes and push to the `gh-pages` branch of your
    repository:

    ~~~
    $ cd data-cleanup
    $ git add changed-file.md
    $ git commit -m "Explanatory message"
    $ git push origin gh-pages
    ~~~
    {: .language-bash}

15. [Tell us][email] where your lesson is so that we can add it to
    the appropriate index page(s).

## Notes

1.  SSH cloning (rather than the HTTPS cloning used above)
    will also work for those who have set up SSH keys with GitHub.

2.  Once a lesson has been created, please submit changes
    for review as pull requests that contain Markdown files only.

3.  Some people have had intermittent errors during the import process,
    possibly because of the network timing out.
    If you experience a problem, please re-try;
    if the problem persists,
    please [get in touch][email].


## Setup Instructions for a specific existing lesson

1.  Installation instructions for core lessons are included in
    the [workshop template's home page][workshop-repo],
    so that they are all in one place.
    The `setup.md` files of core lessons link to
    the appropriate sections of the [workshop template page][workshop-repo].

2.  Other lessons' `setup.md` include full installation instructions organized by OS
    (following the model of the workshop template home page).

## Jekyll Setup for Lesson Development

Though not essential, it is desirable to be able to preview changes on your own machine
before pushing them to GitHub.

In order to preview changes locally, you must install the software described below.

### Windows

For Windows, there are two main ways to setup your system to be able to render the lessons.

- Option 1 relies on the Windows Subsystem for Linux (WSL). WSL allows you to run a Linux
  environment directly from Windows.
- Option 2 relies on using Windows built-in applications.

> ## Option 1 - Using the Windows Subsystem for Linux (WSL)
>
> If your version of Windows supports it, using the WSL will make the installation of the tools
> needed easier. Instructions to install Linux distributions from Windows 10/Windows Server are
> available from the [Microsoft website](https://docs.microsoft.com/en-us/windows/wsl/about).
>
> Once you have installed a Linux distribution, you can follow the installation instructions for
> [Linux](#linux-ubuntu) listed below. If you install a distribution other than Ubuntu, you will
> need to adjust the commands that install the packages.
{: .solution}

> ## Option 2 - Using Windows built-in applications
>
> With the instructions below, you'll be able to preview websites for non-R based lessons. You'll be
> able to do so from the Git Bash terminal or from the "Command Prompt with Ruby" that comes with
> the Ruby installation. You won't be able to use the `make` commands as Make isn't available from
> the Git Bash terminal (see the optional section below for more info).
>
> 1. **Ruby**, go to <https://rubyinstaller.org/> choose Ruby+DevKit for your
>   system (typically x64), and the most recent version available. During the
>   installation process, choose to install the MSYS2 toolchain. On the last step
>   of the installation screen, make sure that "Run 'ridk install'" is checked.
>   This will bring a terminal window with 3 options, press "Enter" (for the
>   default installation). After this step completes, you'll be prompted again,
>   and press "Enter" again (for the default option). Once the installation is
>   complete, restart your system.
>
>2. Navigate to the folder that contains the lesson, and you can now use `bundle
>   exec jekyll serve` from your Git Bash terminal to preview the lessons.
>
> ### Optional (but recommended)
>
> With these instructions, you'll be able to use the `make` commands and render all lessons
> including those that use R. However, you won't be able to do so from the Git Bash terminal, but
> from the other terminals (Windows Powershell, cmd.exe, or the Command Prompt with Ruby).
>
>1. In the File Explorer, right-click on "This PC" icon, and click on
>   "Properties". Click on "Advanced System Settings", and click on the button
>   "Environment Variables". Click on the variable "Path", and then the "Edit"
>   button. Click on the "New" button and add `C:\Ruby26-x64\msys64\usr\bin` (use
>   the File Explorer to make sure this is the correct path for your Ruby and
>   MSYS2 installation). If you're working on R-based lessons and R isn't already
>   listed there, you need to add it by adding `C:\Program Files\R\R-3.x.x\bin`
>   (using the correct path and R version number for your installation).
>
>2. Open the "Command Prompt with Ruby" (if it was open before you edited the
>   Path, close it and re-open it).
{: .solution}

Regardless of the option you chose, go to the section [For Everyone](#for-everyone).

### macOS

1. First make sure you have Homebrew installed by doing

To install Homebrew, open the [Homebrew website](https://brew.sh/) and copy/paste the first command
on that page into your Terminal. It will look something like:

  ~~~
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ~~~
  {: .language-bash}

 If you're not sure whether you have brew installed, type

  ~~~
  brew help
  ~~~
  {: .language-bash}

  If you have Homebrew installed, you should see something like:

  ~~~
  Example usage:
  brew search [TEXT|/REGEX/]
  brew info [FORMULA...]
  brew install FORMULA...
  brew update
  brew upgrade [FORMULA...]
  brew uninstall FORMULA...
  brew list [FORMULA...]

Troubleshooting:
  brew config
  brew doctor
  brew install --verbose --debug FORMULA

Contributing:
  brew create [URL [--no-fetch]]
  brew edit [FORMULA...]

Further help:
  brew commands
  brew help [COMMAND]
  man brew
  https://docs.brew.sh
  ~~~
  {: .output}


2. **Ruby** -- `brew install ruby`

3. **bundler** -- `gem install bundler --user-install`

4. Go to the section [For Everyone](#for-everyone)

### Linux (Ubuntu)

1.  **[Ruby](https://www.ruby-lang.org/en/downloads/)** and other dependencies.

    You will need to have the following packages installed (some might already
    be on your system):

    ~~~
    sudo apt-get install ruby ruby-dev build-essential libxml2-dev
    ~~~
    {: .language-bash}

2. **[bundler](https://bundler.io/)**

    ~~~
    gem install bundler --user-install
    ~~~
    {: .language-bash}

    `gem` is the package management framework for Ruby. It was installed as part
    of Ruby in the step above. `bundler` is also a package manager but at the
    scale of a project instead of being system-wide. It makes it easier to
    manage dependencies.


### For Everyone

1. **The GitHub Pages Ruby Gem**

    Make sure there is a `Gemfile` at the root of your lesson repository. This
    file should only contain:

    ~~~
    source 'https://rubygems.org'
    gem 'github-pages', group: :jekyll_plugins
    ~~~

    If you don't have it, create it and the two lines above to it.

    At the root of your repository type

    ~~~
    bundle update
    ~~~
    {: .language-bash}

    If you haven't used `bundler` yet for your project, this command will
    install all the needed dependencies. Otherwise, it will update them to match
    the current versions used by GitHub Pages.

4. **Generate the lesson**

    Now you are ready to run jekyll to build your website and run a local server. To do this run:

    ~~~
    make serve
    ~~~
    {: .language-bash}

    There will be several lines of output after this. If there were errors or warnings you can use
    them to fix your lesson and run again if ti it failed. If it was successful the last few lines
    will include `Server address: http://127.0.0.1:4000` and `Server running... press ctrl-c to
    stop`. You can see your rendered site by pointing your browser to the address shown.

### For R-based lessons

You will need a recent version of R (>= 3.5.0). Installation instructions are available from the [CRAN website](https://cran.r-project.org).

We use the [knitr][cran-knitr], and [remotes](https://cran.r-project.org/package=remotes) to format
lessons written in R Markdown and figure out needed packages to execute the code in the lesson. You
will need to install the `remotes` package to build R lessons (and this example lesson), the other
packages will be installed automatically during the rendering of the lesson. You can install this
package by opening an R terminal and typing:

~~~
install.packages('remotes', repos = 'https://cran.rstudio.com')
~~~
{: .language-r}

### Troubleshooting

1. Check your version of Ruby:

   ~~~
   ruby -v
   ~~~
   {: .language-bash}

   You need Ruby 2.1.0 or later (currently GitHub pages uses Ruby 2.5.8). If you
   have an older version of Ruby, if possible upgrade your operating system to a
   more recent version. If it's not possible, consider using [rbenv](https://github.com/rbenv/rbenv).

    ~~~
    rbenv install 2.5.8
    ~~~
    {: .language-bash}

    And then instructing `rbenv` to use it in your lesson development process by
    executing the following command from your lesson directory:

    ~~~
    rbenv local 2.5.8
    ~~~
    {: .language-bash}

2.  **[RubyGems][rubygems]**
    is a tool which manages Ruby packages. It should have been installed along with Ruby and you can
    test your installation by running

    ~~~
    gem --version
    ~~~
    {: .language-bash}

3. If you want to run `bin/lesson_check.py` (which is invoked by `make lesson-check`)
you will need the [PyYAML][pyyaml] module for Python 3.


{% include links.md %}
