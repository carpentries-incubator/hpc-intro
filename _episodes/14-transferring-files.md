---
title: "Transferring files"
teaching: 30
exercises: 10
questions:
- "How do I upload/download files to the cluster?"
objectives:
- "Be able to tranfer files to and from a computing cluster."
keypoints:
- "`wget` downloads a file from the internet."
- "`sftp`/`scp` transfer files to and from your computer."
- "You can use an SFTP client like FileZilla to transfer files through a GUI."
---

One thing people very frequently struggle with is transferring files 
to and from a cluster.
We'll cover several methods of doing this from the command line,
then cover how to do this using the GUI program FileZilla, 
which is much more straightforwards.

## Grabbing files from the internet

To download files from the internet, 
the easiest tool to use is `wget`.
The syntax is relatively straightforwards: `wget https://some/link/to/a/file.tar.gz`
We've actually done this before to download our example files:

```
[remote]$ wget https://hpc-carpentry.github.io/hpc-intro/files/bash-lesson.tar.gz
```
{: .bash}

## Transferring single files and folders with scp

To copy a single file to or from the cluster, we can use `scp`.
The syntax can be a little complex for new users, 
but we'll break it down here:

To transfer *to* another computer:
```
[local]$ scp /path/to/local/file.txt yourUsername@remote.computer.address:/path/on/remote/computer
```
{: .bash}

To download *from* another computer:
```
[local]$ scp yourUsername@remote.computer.address:/path/on/remote/computer/file.txt /path/to/local/copy
```
{: .bash}

Note that we can simplify doing this by shortening our paths.
On the remote computer, everything after the `:` is relative to our home directory.
We can simply just add a `:` and leave it at that if we don't care where the file goes.

```
[local]$ scp local-file.txt yourUsername@remote.computer.address:
```
{: .bash}

To recursively copy a directory, we just add the `-r` (recursive) flag:

```
[local]$ scp -r some-local-folder/ yourUsername@remote.computer.address:target-directory/
```
{: .bash}

## Transferring files interactively with sftp

`scp` is useful, but what if we don't know the exact location of what we want to transfer?
Or perhaps we're simply not sure which files we want to tranfer yet.
`sftp` is an interactive way of downloading and uploading files.
Let's connect to a cluster, using `sftp`- you'll notice it works the same way as SSH:

```
sftp yourUsername@remote.computer.address
```
{: .bash}

This will start what appears to be a bash shell (though our prompt says `sftp>`).
However we only have access to a limited number of commands.
We can see which commands are available with `help`:

```
sftp> help
```
{: .bash}
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
We are actually connected to two computers at once (with two working directories!).

To show our remote working directory:
```
sftp> pwd
```
{: .bash}
```
Remote working directory: /global/home/yourUsername
```
{: .output}

To show our local working directory, we add an `l` in front of the command:

```
sftp> lpwd
```
{: .bash}
```
Local working directory: /home/jeff/Documents/teaching/hpc-intro
```
{: .output}

The same pattern follows for all other commands:

* `ls` shows the contents of our remote directory, while `lls` shows our local directory contents.
* `cd` changes the remote directory, `lcd` changes the local one.

To upload a file, we type `put some-file.txt` (tab-completion works here).

```
sftp> put config.toml
```
{: .bash}
```
Uploading config.toml to /global/home/yourUsername/config.toml
config.toml                                   100%  713     2.4KB/s   00:00 
```
{: .output}

To download a file we type `get some-file.txt`:

```
sftp> get config.toml
```
{: .bash}
```
Fetching /global/home/yourUsername/config.toml to config.toml
/global/home/yourUsername/config.toml                               100%  713     9.3KB/s   00:00 
```
{: .output}

And we can recursively put/get files by just adding `-r`.
Note that the directory needs to be present beforehand.

```
sftp> mkdir content
sftp> put -r content/
```
{: .bash}
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

## Transferring files interactively with FileZilla (sftp)

FileZilla is a cross-platform client for downloading and uploading files to and from a remote computer.
It is absolutely fool-proof and always works quite well.
In fact, it uses the exact same protocol as `sftp` under the hood.
If `sftp` works, so will FileZilla!

Download and install the FileZilla client from [https://filezilla-project.org](https://filezilla-project.org).
After installing and opening the program, 
you should end up with a window with a file browser of your local system 
on the left hand side of the screen.
When you connect to the cluster, your cluster files will appear on the right hand side.

To connect to the cluster, 
we'll just need to enter our credentials at the top of the screen:

* Host: `sftp://login.cac.queensu.ca`
* User: Your cluster username
* Password: Your cluster password
* Port: (leave blank to use the default port)

Hit "Quickconnect" to connect!
You should see your remote files appear on the right hand side of the screen.
You can drag-and-drop files between the left (local) and right (remote) sides 
of the screen to transfer files.

## Compressing files

Sometimes we will want to compress files ourselves to make file transfers easier.
The larger the file, the longer it will take to transfer. 
Moreover, we can compress a whole bunch of little files into one big file to make it easier
on us (no one likes transferring 70000 little files)!

The two compression commands we'll probably want to remember are the following:

* Compress a single file with Gzip - `gzip filename`
* Compress a lot of files/folders with Gzip - `tar -czvf archive-name.tar.gz folder1 file2 folder3 etc`

> ## Transferring files
> Using one of the above methods, try transferring files to and from the cluster.
> Which method do you like the best?
{: .challenge}

> ## Working with Windows
> When you transfer files to from a Windows system to a Unix system 
> (Mac, Linux, BSD, Solaris, etc.) this can cause problems.
> Windows encodes its files slightly different than Unix,
> and adds an extra character to every line.
> 
> On a Unix system, every line in a file ends with a `\n` (newline).
> On Windows, every line in a file ends with a `\r\n` (carriage return + newline).
> This causes problems sometimes.
> 
> Though most modern programming languages and software handles this correctly,
> in some rare instances, you may run into an issue.
> he solution is to convert a file from Windows to Unix encoding with the `dos2unix` command.
> 
> You can identify if a file has Windows line endings with `cat -A filename`.
> A file with Windows line endings will have `^M$` at the end of every line.
> A file with Unix line endings will have `$` at the end of a line.
> 
> To convert the file, just run `dos2unix filename`.
> (Conversely, to convert back to Windows format, you can run `unix2dos filename`.)
{: .callout}

> ## A note on ports
> All file tranfers using the above methods use encrypted communication over port 22.
> This is the same connection method used by SSH.
> In fact, all file transfers using these methods occur through an SSH connection.
> If you can connect via SSH over the normal port, you will be able to transfer files.
{: .callout}

