---
layout: reference
permalink: /reference/
title: Knowledge Base
---

### Quick Reference or "Cheat Sheets" for Queuing System Commands

Search online for the one that fits you best, but here's some to start:

* [Slurm summary](https://slurm.schedmd.com/pdfs/summary.pdf) from SchedMD
* [Torque/PBS summary](
  https://gif.biotech.iastate.edu/torque-pbs-job-management-cheat-sheet)
  from Iowa State
* [Translating between Slurm and PBS](
  https://www.msi.umn.edu/slurm/pbs-conversion) from University of Minnesota

### Units and Language

A computer's memory and disk are measured in units called *Bytes* (one Byte is
8 bits). As today's files and memory have grown to be large given historic
standards, volumes are noted using the
[SI](https://en.wikipedia.org/wiki/International_System_of_Units) prefixes. So
1000 Bytes is a Kilobyte (kB), 1000 Kilobytes is a Megabyte (MB), 1000
Megabytes is a Gigabyte (GB), etc.

History and common language have however mixed this notation with a different
meaning. When people say "Kilobyte", they mean 1024 Bytes instead. In that
spirit, a Megabyte is 1024 Kilobytes.

To address this ambiguity, the [International System of Quantities](
https://en.wikipedia.org/wiki/International_System_of_Quantities) standardizes
the *binary* prefixes (with base of 2<sup>10</sup>=1024) by the prefixes Kibi
(ki), Mebi (Mi), Gibi (Gi), etc. For more details, see
[here](https://en.wikipedia.org/wiki/Binary_prefix).

### "No such file or directory" or "symbol 0096" Errors

`scp` and `rsync` may throw a perplexing error about files that very much do
exist. One source of these errors is copy-and-paste of command line arguments
from Web browsers, where the double-dash string `--` is rendered as an em-dash
character "&mdash;" (or en-dash "&ndash;", or horizontal bar `―`). For example,
instead of showing the transfer rate in real time, the following command fails
mysteriously.

```
{{ site.local.prompt }} rsync —progress my_precious_data.txt {{ site.remote.user }}@{{ site.remote.login }}
rsync: link_stat "/home/{{ site.local.user }}/—progress" failed:
No such file or directory (2)
rsync error: some files/attrs were not transferred (see previous errors)
(code 23) at main.c(1207) [sender=3.1.3]
```
{: .language-bash}

The correct command, different only by two characters, succeeds:

```
{{ site.local.prompt }} rsync --progress my_precious_data.txt {{ site.remote.user }}@{{ site.remote.login }}
```
{: .language-bash}

We have done our best to wrap all commands in code blocks, which prevents this
subtle conversion. If you encounter this error, please open an issue or pull
request on the lesson repository to help others avoid it.

### Transferring Files Interactively With `sftp`

`scp` is useful, but what if we don't know the exact location of what we want
to transfer? Or perhaps we're simply not sure which files we want to transfer
yet. `sftp` is an interactive way of downloading and uploading files. Let's
connect to a cluster, using `sftp` -- you'll notice it works the same way
as SSH:

```
{{ site.local.prompt }} sftp yourUsername@remote.computer.address
```
{: .language-bash}

This will start what appears to be a bash shell (though our prompt says
`sftp>`). However we only have access to a limited number of commands. We can
see which commands are available with `help`:

```
sftp> help
```
{: .language-bash}
```
Available commands:
bye                                Quit sftp
cd path                            Change remote directory to 'path'
chgrp grp path                     Change group of file 'path' to 'grp'
chmod mode path                    Change permissions of file 'path' to 'mode'
chown own path                     Change owner of file 'path' to 'own'
df [-hi] [path]                    Display statistics for current directory or
                                   filesystem containing 'path'
exit                               Quit sftp
get [-afPpRr] remote [local]       Download file
reget [-fPpRr] remote [local]      Resume download file
reput [-fPpRr] [local] remote      Resume upload file
help                               Display this help text
lcd path                           Change local directory to 'path'
lls [ls-options [path]]            Display local directory listing
lmkdir path                        Create local directory
ln [-s] oldpath newpath            Link remote file (-s for symlink)
lpwd                               Print local working directory
ls [-1afhlnrSt] [path]             Display remote directory listing

# omitted further output for clarity
```
{: .output}

Notice the presence of multiple commands that make mention of local and remote.
We are actually connected to two computers at once (with two working
directories!).

To show our remote working directory:
```
sftp> pwd
```
{: .language-bash}
```
Remote working directory: /global/home/yourUsername
```
{: .output}

To show our local working directory, we add an `l` in front of the command:

```
sftp> lpwd
```
{: .language-bash}
```
Local working directory: /home/jeff/Documents/teaching/hpc-intro
```
{: .output}

The same pattern follows for all other commands:

* `ls` shows the contents of our remote directory, while `lls` shows our local
  directory contents.
* `cd` changes the remote directory, `lcd` changes the local one.

To upload a file, we type `put some-file.txt` (tab-completion works here).

```
sftp> put config.toml
```
{: .language-bash}
```
Uploading config.toml to /global/home/yourUsername/config.toml
config.toml                                  100%  713     2.4KB/s   00:00
```
{: .output}

To download a file we type `get some-file.txt`:

```
sftp> get config.toml
```
{: .language-bash}
```
Fetching /global/home/yourUsername/config.toml to config.toml
/global/home/yourUsername/config.toml        100%  713     9.3KB/s   00:00
```
{: .output}

And we can recursively put/get files by just adding `-r`. Note that the
directory needs to be present beforehand.

```
sftp> mkdir content
sftp> put -r content/
```
{: .language-bash}
```
Uploading content/ to /global/home/yourUsername/content
Entering content/
content/scheduler.md              100%   11KB  21.4KB/s   00:00
content/index.md                  100% 1051     7.2KB/s   00:00
content/transferring-files.md     100% 6117    36.6KB/s   00:00
content/.transferring-files.md.sw 100%   24KB  28.4KB/s   00:00
content/cluster.md                100% 5542    35.0KB/s   00:00
content/modules.md                100%   17KB 158.0KB/s   00:00
content/resources.md              100% 1115    29.9KB/s   00:00
```
{: .output}

To quit, we type `exit` or `bye`.

{% include links.md %}
