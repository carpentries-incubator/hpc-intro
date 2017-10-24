---
title: "UNIX fundamentals: File Control"
teaching: 0
exercises: 0
questions:
- "How do I move files on and off the remote system?"
- "How do I control who has access to my files?"
- "How do I write and run a simple script?"
objectives:
- "Be able to move files to and from the remote system."
- "Be able to read and change file permissions."
- "Be able to write and edit simple scripts
keypoints:
- "`scp` (The Secure Copy Program) is a standard way to securely transfer data to remote HPC systems."
- "File ownership is an important component of a shared computing space and can be controlled with `chgrp` and `chown`."
- "Scripts are *mostly* just lists of commands from the command line in the order they are to be performed."
---

## Moving Files Around

`mv` and `cp`

These will be an important setup for `scp` since the syntax is basically the same before adding the server components.


## Moving files to and from the remote system from and to your local computer

It is often necessary to move data from your local computer to the remote system and vice versa.  There are many ways to do this and we will look at two here: `scp` and `sftp`.

Before we start moving files around it would be good to have some files to move around that don't really matter beyond their value in being moved around.  If they get lost or damaged or anything else it won't really matter because they are mostly harmless (we say "mostly" because it is possible that they might add clutter or overwrite another file with the same name but we can take steps to avoid these risks).

### `scp`from your local computer to the remote system
The most basic command line tool for moving files around is secure copy or `scp`.

`scp` behaves similarily to `ssh` but with one additional input, the name of the file to be copied.  If we were in the shell on our local computer, the file we wanted to move was in our current directory, named "globus.tgz", and Nelle wanted to move it to her home directory on cedar.computecanada.ca then the command would be

	$ scp globus.tgz nelle@cedar.computecanada.ca:
	
It should be expected that a password will be asked for and you should be prepared to provide it.

Once the transfer is complete you should be able to use `ssh` to login to the remote system and see your file in your home directory.

WHAT IF YOU WANTED THE FILE SOMEWHERE OTHER THAN THE HOME DIRECTORY?

> ## Remember the `:`
> Note the colon (`:`) at the end of the command.  This is a very important modifier to include.  If it isn't included then running `scp` will result in a copy of the file that was to be moved being created in the current directory with the name of the remote system.  In the case of the globus.tgz example above it would look like the following:
> 
> ~~~
> $ scp globus.tgz nelle@cedar.computecanada.ca: 
> $ ls
> ~~~
> {: .bash}
> 
> ~~~
> globus.tgz
> nelle@cedar.computecanada.ca
> ~~~
> {: .output}
> 
> If this does happen then the extra file can be removed with `rm`.
> 
> ~~~
> $ rm nelle@cedar.computecanada.ca
> ~~~
> {: .bash}
{: .callout}

NEED AN EXERCISE.  OPEN A SECOND TERMINAL WINDOW ON LOCAL SYSTEM AND USE `scp` TO PUSH A FILE TO THE REMOTE SYSTEM

### `scp	` from the remote system to your Local computer

Moving files from the remote system to the local system will also be necessary.  This is also done from the local system so instead of pushing content we'll be pulling it.  This is achieved by changing the order of the inputs passed to the `scp` command and specifying the exact location of the file that we want from the remote system.

scp simpson@cedar.computecanada.ca:junk junk

> ## Copying entire directories
> 
> HIGHLIGHT the `-r` flag here.
> 
{: .callout}

## Transferring files interactively with sftp

`scp` is useful, but what if we don't know the exact location of what we want to transfer?
Or perhaps we're simply not sure which files we want to tranfer yet.
`sftp` is an interactive way of downloading and uploading files.
To connect to a cluster, we use the command `sftp yourUsername@remote.computer.address`.
This will start what appears to be a bash shell (though our prompt says `sftp>`).
However we only have access to a limited number of commands.

We can see which commands are available with `help`:
```
help
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

# omitted further output for brevity
```
{: .output}

Notice the presence of multiple commands that make mention of local and remote.
We are actually connected to two computers at once (with two working directories!).

To show our remote working directory:
```
pwd
```
{: .bash}
```
Remote working directory: /global/home/yourUsername
```
{: .output}

To show our local working directory, we add an `l` in front of the command:

```
lpwd
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
put config.toml
```
{: .bash}
```
Uploading config.toml to /global/home/yourUsername/config.toml
config.toml                                   100%  713     2.4KB/s   00:00 
```
{: .output}

To download a file we type `get some-file.txt`:

```
get config.toml
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
mkdir content
put -r content/
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

## Grabbing files from the internet

To download files from the internet, 
the absolute best tool is `wget`.
The syntax is relatively straightforwards: `wget https://some/link/to/a/file.tar.gz`

> ## Downloading the Drosophila genome
> The *Drosophila melanogaster* reference genome is located at the following website:
> [http://metazoa.ensembl.org/Drosophila_melanogaster/Info/Index](http://metazoa.ensembl.org/Drosophila_melanogaster/Info/Index).
> Download it to the cluster with `wget`.
>
> Some additional details:
>
> * You want to go get the genome through the "Download DNA Sequence" link
> * We are interested in the `Drosophila_melanogaster.BDGP6.dna.toplevel.fa.gz` file.
{: .challenge}

> ## Working with compressed files
> 
> The file we just downloaded is gzipped (has the `.gz` 
> extension).
>You can uncompress it with `gunzip filename.gz`.
>
>File decompression reference:
>
>* **.tar.gz** - `tar -xzvf archive-name.tar.gz`
>* **.tar.bz2** - `tar -xjvf archive-name.tar.bz2`
>* **.zip** - `unzip archive-name.zip`
>* **.rar** - `unrar archive-name.rar`
>* **.7z** - `7z x archive-name.7z`
>
>However, sometimes we will want to compress files 
>ourselves to make file transfers easier.
>The larger the file, the longer it will take to 
>transfer. 
>Moreover, we can compress a whole bunch of little 
>files into one big file to make it easier
>on us (no one likes transferring 70000) little files!
>
>The two compression commands we'll probably want to 
>remember are the following:
>
>* Compress a single file with Gzip - `gzip filename`
>* Compress a lot of files/folders with Gzip - `tar -czvf archive-name.tar.gz folder1 file2 folder3 etc`
> 
{: .callout}




## Controlling File Ownership

List with `ls -l`

Change ownership with `chown`

## Groups

## Changing Group Association

chgrp

## Scripting

nano

## Making Scripts Executable / Changing Permissions

chmod

p. 195