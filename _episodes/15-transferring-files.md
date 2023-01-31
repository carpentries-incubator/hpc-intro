---
title: "Transferring files with remote computers"
teaching: 15
exercises: 15
questions:
- "How do I transfer files to (and from) the cluster?"
objectives:
- "Transfer files to and from a computing cluster."
keypoints:
- "`wget` and `curl -O` download a file from the internet."
- "`scp` and `rsync` transfer files to and from your computer."
- "You can use an SFTP client like FileZilla to transfer files through a GUI."
---

Performing work on a remote computer is not very useful if we cannot get files
to or from the cluster. There are several options for transferring data between
computing resources using CLI and GUI utilities, a few of which we will cover.

## Download Lesson Files From the Internet

One of the most straightforward ways to download files is to use either `curl`
or `wget`. One of these is usually installed in most Linux shells, on Mac OS
terminal and in GitBash. Any file that can be downloaded in your web browser
through a direct link can be downloaded using `curl` or `wget`. This is a
quick way to download datasets or source code. The syntax for these commands is

* `curl -O https://some/link/to/a/file [-o new_name]`
* `wget https://some/link/to/a/file [-O new_name]`

Try it out by downloading some material we'll use later on, from a terminal on
your local machine, using the URL of the current codebase:
<https://github.com/hpc-carpentry/amdahl/tarball/main>

> ## Download the "Tarball"
>
> The word "tarball" in the above URL refers to a compressed archive format
> commonly used on Linux, which is the operating system the majority of HPC
> cluster machines run.
> A tarball is a lot like a `.zip` file.
> The actual file extension is `.tar.gz`, which reflects the two-stage process
> used to create the file:
> the files or folders are merged into a single file using `tar`, which is then
> compressed using `gzip`, so the file extension is "tar-dot-g-z."
> That's a mouthful, so people often say "the _xyz_ tarball" instead.
>
> You may also see the extension `.tgz`, which is just an abbreviation of
> `.tar.gz`.
>
> By default, `curl` and `wget` download files to the same name as the URL.
> In this case, that would be "main," which is not very clear.
> Use one of the above commands to save the tarball to "amdahl.tar.gz" instead.
>
> > ## Curl & Wget Commands
> >
> > ```
> > {{ site.local.prompt }} curl -O https://github.com/hpc-carpentry/amdahl/tarball/main -o amdahl.tar.gz
> > # or
> > {{ site.local.prompt }} wget https://github.com/hpc-carpentry/amdahl/tarball/main -O amdahl.tar.gz
> > ```
> > {: .language-bash}
> {: .solution}
{: .challenge}

After downloading the file, use `ls` to see it in your working directory:

```
{{ site.local.prompt }} ls
```
{: .language-bash}

## Archiving Files

One of the biggest challenges we often face when transferring data between
remote HPC systems is that of large numbers of files. There is an overhead to
transferring each individual file and when we are transferring large numbers of
files these overheads combine to slow down our transfers to a large degree.

The solution to this problem is to _archive_ multiple files into smaller
numbers of larger files before we transfer the data to improve our transfer
efficiency. Sometimes we will combine archiving with _compression_ to reduce
the amount of data we have to transfer and so speed up the transfer.

The most common archiving command you will use on a (Linux) HPC cluster is
`tar`. `tar` can be used to combine files into a single archive file and,
optionally, compress it.

Let's start with the file we downloaded from the lesson site, `amdahl.tar.gz`.
The "gz" part stands for _gzip_, which is a compression library.
This kind of file can usually be interpreted by reading its name:
it appears somebody took a folder named "hpc-carpentry-amdahl-46c9b4b,"
wrapped up all its contents in a single file with `tar`,
then compressed that archive with `gzip` to save space.
Let's check using `tar` with the `-t` flag, which prints the "**t**able of
contents" without unpacking the file, specified by `-f <filename>`,
on the remote computer.
Note that you can concatenate the two flags, instead of writing `-t -f` separately.

```
{{ site.local.prompt }} tar -tf amdahl.tar.gz
hpc-carpentry-amdahl-46c9b4b/
hpc-carpentry-amdahl-46c9b4b/.github/
hpc-carpentry-amdahl-46c9b4b/.github/workflows/
hpc-carpentry-amdahl-46c9b4b/.github/workflows/python-publish.yml
hpc-carpentry-amdahl-46c9b4b/.gitignore
hpc-carpentry-amdahl-46c9b4b/LICENSE
hpc-carpentry-amdahl-46c9b4b/README.md
hpc-carpentry-amdahl-46c9b4b/amdahl/
hpc-carpentry-amdahl-46c9b4b/amdahl/__init__.py
hpc-carpentry-amdahl-46c9b4b/amdahl/__main__.py
hpc-carpentry-amdahl-46c9b4b/amdahl/amdahl.py
hpc-carpentry-amdahl-46c9b4b/requirements.txt
hpc-carpentry-amdahl-46c9b4b/setup.py
```
{: .language-bash}

This shows a folder which contains a few files. Let's see about that
compression, using `du` for "**d**isk **u**sage".

```
{{ site.local.prompt }} du -sh amdahl.tar.gz
8.0K     amdahl.tar.gz
```
{: .language-bash}

> ## Files Occupy at Least One "Block"
>
> If the filesystem block size is larger than 3.4 KB, you'll see a larger
> number: files cannot be smaller than one block.
> You can use the `--apparent-size` flag to see the exact size, although the
> unoccupied space in that filesystem block can't be used for anything else.
{: .callout}

Now let's unpack the archive. We'll run `tar` with a few common flags:

* `-x` to e**x**tract the archive
* `-v` for **v**erbose output
* `-z` for g**z**ip compression
* `-f «tarball»` for the file to be unpacked

The folder inside has an unfortunate name, so we'll change that as well using

* `-C «folder»` to **c**hange directories before extracting
  (note that the new directory must exist!)
* `--strip-components=«n»` to remove $n$ levels of depth from the extracted
  file hierarchy

> ## Extract the Archive
>
> Using the flags above, unpack the source code tarball into a new
> directory named "amdahl" using `tar`.
>
> ```
> {{ site.local.prompt }} mkdir amdahl
> {{ site.local.prompt }} tar -xvzf amdahl.tar.gz -C amdahl --strip-components=1
> ```
> {: .language-bash}
>
> ```
> hpc-carpentry-amdahl-46c9b4b/
> hpc-carpentry-amdahl-46c9b4b/.github/
> hpc-carpentry-amdahl-46c9b4b/.github/workflows/
> hpc-carpentry-amdahl-46c9b4b/.github/workflows/python-publish.yml
> hpc-carpentry-amdahl-46c9b4b/.gitignore
> hpc-carpentry-amdahl-46c9b4b/LICENSE
> hpc-carpentry-amdahl-46c9b4b/README.md
> hpc-carpentry-amdahl-46c9b4b/amdahl/
> hpc-carpentry-amdahl-46c9b4b/amdahl/__init__.py
> hpc-carpentry-amdahl-46c9b4b/amdahl/__main__.py
> hpc-carpentry-amdahl-46c9b4b/amdahl/amdahl.py
> hpc-carpentry-amdahl-46c9b4b/requirements.txt
> hpc-carpentry-amdahl-46c9b4b/setup.py
> ```
> {: .output}
>
> Note that we did not need to type out `-x -v -z -f`, thanks to flag
> concatenation, though the command works identically either way --
> so long as the concatenated list ends with `f`, because the next string
> must specify the name of the file to extract.
>
> We couldn't concatenate `-C` because the next string must name the directory.
>
> Long options (`--strip-components`) also can't be concatenated.
>
> Since order doesn't generally matter, an equivalent command would be
> ```
> {{ site.local.prompt }} tar -xvzC amdahl -f amdahl.tar.gz --strip-components=1
> ```
> {: .language-bash}
{: .discussion}

Check the size of the extracted directory, and compare to the compressed
file size:

```
{{ site.local.prompt }} du -sh amdahl
48K    amdahl
```
{: .language-bash}

Text files (including Python source code) compress nicely:
the "tarball" is one-sixth the total size of the raw data!

If you want to reverse the process -- compressing raw data instead of
extracting it -- set a `c` flag instead of `x`, set the archive filename,
then provide a directory to compress:

```
{{ site.local.prompt }} tar -cvzf compressed_code.tar.gz amdahl
```
{: .language-bash}
```
amdahl/
amdahl/.github/
amdahl/.github/workflows/
amdahl/.github/workflows/python-publish.yml
amdahl/.gitignore
amdahl/LICENSE
amdahl/README.md
amdahl/amdahl/
amdahl/amdahl/__init__.py
amdahl/amdahl/__main__.py
amdahl/amdahl/amdahl.py
amdahl/requirements.txt
amdahl/setup.py
```
{: .output}

If you give `amdahl.tar.gz` as the filename in the above command, `tar` will
update the existing tarball with any changes you made to the files, instead of
recompressing everything.

> ## Working with Windows
>
> When you transfer text files from a Windows system to a Unix system (Mac,
> Linux, BSD, Solaris, etc.) this can cause problems. Windows encodes its files
> slightly different than Unix, and adds an extra character to every line.
>
> On a Unix system, every line in a file ends with a `\n` (newline). On
> Windows, every line in a file ends with a `\r\n` (carriage return + newline).
> This causes problems sometimes.
>
> Though most modern programming languages and software handles this correctly,
> in some rare instances, you may run into an issue. The solution is to convert
> a file from Windows to Unix encoding with the `dos2unix` command.
>
> You can identify if a file has Windows line endings with `cat -A filename`. A
> file with Windows line endings will have `^M$` at the end of every line. A
> file with Unix line endings will have `$` at the end of a line.
>
> To convert the file, just run `dos2unix filename`. (Conversely, to convert
> back to Windows format, you can run `unix2dos filename`.)
{: .callout}

## Transferring Single Files and Folders With `scp`

To copy a single file to or from the cluster, we can use `scp` ("secure copy").
The syntax can be a little complex for new users, but we'll break it down.
The `scp` command is a relative of the `ssh` command we used to
access the system, and can use the same public-key authentication
mechanism.

To _upload to_ another computer:

```
{{ site.local.prompt }} scp local_file {{ site.remote.user }}@{{ site.remote.login }}:remote_path
```
{: .language-bash}

Note that everything after the `:` is relative to our home directory on the
remote computer. We can leave it at that if we don't have a more specific
destination in mind.

Upload the lesson material to your remote home directory like so:

```
{{ site.local.prompt }} scp amdahl.tar.gz {{ site.remote.user }}@{{ site.remote.login }}:
```
{: .language-bash}

> ## Why Not Download on {{ site.remote.name }} Directly?
>
> Most computer clusters are protected from the open internet by a _firewall_.
> For enhanced security, some are configured to allow traffic _inbound_, but
> not _outbound_.
> This means that an authenticated user can send a file to a cluster machine,
> but a cluster machine cannot retrieve files from a user's machine or the
> open Internet.
>
> Try downloading the file directly. Note that it may well fail, and that's
> OK!
>
> > ## Commands
> >
> > ```
> > {{ site.local.prompt }} ssh {{ site.remote.user }}@{{ site.remote.login }}
> > {{ site.remote.prompt }} curl -O https://github.com/hpc-carpentry/amdahl/tarball/main -o amdahl.tar.gz
> > # or
> > {{ site.remote.prompt }} wget https://github.com/hpc-carpentry/amdahl/tarball/main -O amdahl.tar.gz
> > ```
> > {: .language-bash}
> {: .solution}
>
> Did it work? If not, what does the terminal output tell you about what
> happened?
{: .discussion}

## Transferring a Directory

To transfer an entire directory, we add the `-r` flag for "**r**ecursive": copy
the item specified, and every item below it, and every item below those... 
until it reaches the bottom of the directory tree rooted at the folder name you
provided.

```
{{ site.local.prompt }} scp -r amdahl {{ site.remote.user }}@{{ site.remote.login }}:~/
```
{: .language-bash}

> ## Caution
>
> For a large directory -- either in size or number of files --
> copying with `-r` can take a long time to complete.
{: .callout}

## What's in a `/`?

When using `scp`, you may have noticed that a `:` _always_ follows the remote
computer name; sometimes a `/` follows that, and sometimes not, and sometimes
there's a final `/`. On Linux computers, `/` is the ___root___ directory, the
location where the entire filesystem (and others attached to it) is anchored. A
path starting with a `/` is called _absolute_, since there can be nothing above
the root `/`. A path that does not start with `/` is called _relative_, since
it is not anchored to the root.

If you want to upload a file to a location inside your home directory --
which is often the case -- then you don't need a leading `/`. After the
`:`, start writing the sequence of folders that lead to the final storage
location for the file or, as mentioned above, provide nothing if your home
directory _is_ the destination.

A trailing slash on the target directory is optional, and has no effect for
`scp -r`, but is important in other commands, like `rsync`.

> ## A Note on `rsync`
>
> As you gain experience with transferring files, you may find the `scp`
> command limiting. The [rsync] utility provides
> advanced features for file transfer and is typically faster compared to both
> `scp` and `sftp` (see below). It is especially useful for transferring large
> and/or many files and creating synced backup folders.
>
> The syntax is similar to `scp`. To transfer _to_ another computer with
> commonly used options:
>
> ```
> {{ site.local.prompt }} rsync -avP amdahl.tar.gz {{ site.remote.user }}@{{ site.remote.login }}:
> ```
> {: .language-bash}
>
> The options are:
>
> * `-a` (**a**rchive) to preserve file timestamps, permissions, and folders,
>    among other things; implies recursion
> * `-v` (**v**erbose) to get verbose output to help monitor the transfer
> * `-P` (partial/progress) to preserve partially transferred files in case
>   of an interruption and also displays the progress of the transfer.
>
> To recursively copy a directory, we can use the same options:
>
> ```
> {{ site.local.prompt }} rsync -avP hpc-carpentry-amdahl-46c9b4b {{ site.remote.user }}@{{ site.remote.login }}:~/
> ```
> {: .language-bash}
>
> As written, this will place the local directory and its contents under your
> home directory on the remote system. If the trailing slash is omitted on
> the destination, a new directory corresponding to the transferred directory
> will not be created, and the contents of the source
> directory will be copied directly into the destination directory.
>
> To download a file, we simply change the source and destination:
>
> ```
> {{ site.local.prompt }} rsync -avP {{ site.remote.user }}@{{ site.remote.login }}:hpc-carpentry-amdahl-46c9b4b ./
> ```
> {: .language-bash}
{: .callout}

File transfers using both `scp` and `rsync` use SSH to encrypt data sent through
the network. So, if you can connect via SSH, you will be able to transfer
files. By default, SSH uses network port 22. If a custom SSH port is in use,
you will have to specify it using the appropriate flag, often `-p`, `-P`, or
`--port`. Check `--help` or the `man` page if you're unsure.

> ## Change the Rsync Port
>
> Say we have to connect `rsync` through port 768 instead of 22. How would we
> modify this command?
>
> ```
> {{ site.local.prompt }} rsync amdahl.tar.gz {{ site.remote.user }}@{{ site.remote.login }}:
> ```
> {: .language-bash}
>
> > ## Solution
> >
> > ```
> > {{ site.local.prompt }} man rsync
> > {{ site.local.prompt }} rsync --help | grep port
> >      --port=PORT             specify double-colon alternate port number
> > See http://rsync.samba.org/ for updates, bug reports, and answers
> > {{ site.local.prompt }} rsync --port=768 amdahl.tar.gz {{ site.remote.user }}@{{ site.remote.login }}:
> > ```
> > {: .language-bash}
> (Note that this command will fail, as the correct port in this case is the
> default: 22.)
> {: .solution}
{: .challenge}

## Transferring Files Interactively with FileZilla

FileZilla is a cross-platform client for downloading and uploading files to and
from a remote computer. It is absolutely fool-proof and always works quite
well. It uses the `sftp` protocol. You can read more about using the `sftp`
protocol in the command line in the
[lesson discussion]({{ site.baseurl }}{% link _extras/discuss.md %}).

Download and install the FileZilla client from <https://filezilla-project.org>.
After installing and opening the program, you should end up with a window with
a file browser of your local system on the left hand side of the screen. When
you connect to the cluster, your cluster files will appear on the right hand
side.

To connect to the cluster, we'll just need to enter our credentials at the top
of the screen:

* Host: `sftp://{{ site.remote.login }}`
* User: Your cluster username
* Password: Your cluster password
* Port: (leave blank to use the default port)

Hit "Quickconnect" to connect. You should see your remote files appear on the
right hand side of the screen. You can drag-and-drop files between the left
(local) and right (remote) sides of the screen to transfer files.

Finally, if you need to move large files (typically larger than a gigabyte)
from one remote computer to another remote computer, SSH in to the computer
hosting the files and use `scp` or `rsync` to transfer over to the other. This
will be more efficient than using FileZilla (or related applications) that
would copy from the source to your local machine, then to the destination
machine.

{% include links.md %}

[rsync]: https://rsync.samba.org/
