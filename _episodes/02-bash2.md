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
- "Be able to write and edit simple scripts"
keypoints:
- "`scp` (The Secure Copy Program) is a standard way to securely transfer data to remote HPC systems."
- "File ownership is an important component of a shared computing space and can be controlled with `chgrp` and `chown`."
- "Scripts are *mostly* just lists of commands from the command line in the order they are to be performed."
---

## Making files to practice with
Before we start moving files around we should have some files to move around that don't really matter beyond their value in being moved around.  If they get lost or damaged or anything else it won't really matter because they are mostly harmless (we say "mostly" because it is possible that they might add clutter or overwrite another file with the same name but we will take steps to avoid these risks).  We will create such files using the `touch` command after using `cd` to make sure that we are in the home directory.

~~~
[remote]$ cd
[remote]$ touch fileToMove
~~~
{: .bash}

~~~
[remote]$ ls
~~~
{: .bash}

~~~
...
fileToMove
...
~~~
{: .output}

We now have a file called "fileToMove" that we can move around.  If you run an `ls -l` you will note that its size is zero.  This is because it has no content.  This makes it a fairly safe file to move around because it can't really do anything.  It is also an easy file to move around because we won't need to worry about transfer times.

> ## Overloading Commands
> Running `$ man touch` will reveal that `touch` is the command meant to be used for changing the timestamps associated with files.  We're not using it to do this though and are instead using it to create a new file.  This is because when touch is run if it is passed the name for a file that doesn't exist it will create that file.  This is a useful feature but not what the command is specifically intended for and so we sometimes refer to this as "overloading" a command.  Using the concatentate file command `cat` to print the contents of a single file is another example of this.
{: .callout}

## Creating Directories

Now that we have a file to move around we need a place to move the file to.  We can create a new directory using the `mkdir` command:

~~~
[remote]$ mkdir practiceDir
[remote]$ ls
~~~
{: .bash}

~~~
...
practiceDir
...
~~~
{: .output}

We can check the content of the new directory as well:

~~~
[remote]$ ls practiceDir
~~~
{: .bash}

~~~

~~~
{: .output}

We don't have any output returned, which is to be expected because we only just created the directory and nothing has been added to it yet.

## Moving Files Around

We can move our new file into the new directory with the move command, `mv`.  The syntax of `mv` is `$ mv file_being_moved location_moving_to`.   Moving our new file "fileToMove" to our new directory "practiceDir" can be done as follows:

~~~
[remote]$ mv fileToMove practiceDir
~~~
{: .bash}

"Silence is Golden" so as long as the move was successful we will receive no output.  We can check that the file was moved successfully using `ls`:

~~~
[remote]$ ls practiceDir
~~~
{: .bash}

~~~
fileToMove
~~~
{: .output}

We can move `fileToMove` back from `practiceDir` as well:

~~~
[remote]$ mv practiceDir/fileToMove fileToMove
~~~
{: .bash}

Again, if the transfer is successful then we will receive no output but we can use `ls` to check.

~~~
[remote]$ ls
~~~
{: .bash}

~~~
fileToMove
~~~
{: .output}

~~~
[remote]$ ls practiceDir
~~~
{: .bash}

~~~

~~~
{: .output}
 
## Copying Files
 
We can also copy files, leaving the original file while a second version is created either elsewhere or in the same location.  The copy command is `cp` and its syntax is the same as for `mv`: `$ cp file_being_copied location_copying_to`.  We can create a copy of "fileToMove" inside of the "practiceDir" directory as follows:

~~~
[remote]$ cp fileToMove practiceDir
~~~
{: .bash}

"Silence is Golden" so as long as the copy was successful we will receive no output.  We can check that the file was copied successfully using `ls`:

~~~
[remote]$ ls
~~~
{: .bash}

~~~
...
fileToMove
...
~~~
{: .output}

~~~
[remote]$ ls practiceDir
~~~
{: .bash}

~~~
fileToMove
~~~
{: .output}

## Removing Files and Directories

Sooner or later it will become important to be able to remove files and directories from a system via the command line.  This is usually done with the remove command, `rm`.  The syntax of `rm` is: `$rm optional_list_of_opitons list_of_files_to_be_removed`.  To remove "fileToMove" from our current directory, which should also be the home directory, we issue the following command:

~~~
[remote]$ rm fileToMove
~~~
{: .bash}

If the file exists and there is nothing standing in the way of your ability to delete it such as a lack of authority to do so then the `rm` command will not return any output and just remove the file.  We can confirm this with the `ls` command.

We can also remove entire directories with `rm`.  Try this now with `practiceDir`:

~~~
[remote]$ rm practiceDir
~~~
{: .bash}

~~~
rm: cannot remove 'practiceDir/': Is a directory
~~~
{: .output}

This will notably fail with an error declaring that `rm` cannot remove "practiceDir" because it is a directory.  This is not actually the case. `rm` is quite capable of removing directories, we just need to pass the appropriate options.  The option we want here is `-r` with turns on recursion, allowing the removal of all the content within a directory and any directories and files within that directory and any directories and files within those directories and so on.  Let's try again with recursion flag:

~~~
[remote]$ rm -r practiceDir
~~~
{: .bash}

The directory named "practiceDir" is now gone and so is the file named "fileToMove" that was inside it.

> ## No Trash Can or Recycle Bin
> If you are used to working with graphic user interfaces such as Windows, Mac OSX, or X-Windows on Linux then you are likely used to there being a special folder that holds any files that you delete for at least a short period of time before they are gone for good.  This feature does not exist in most command line environments.  When you use `rm` to remove a file it really is removed, short of a forensic audit of the filesystem.  Be very careful!
{: .callout}


## Moving files to and from the remote system from and to your local computer

It is often necessary to move data from your local computer to the remote system and vice versa.  There are many ways to do this and we will look at two here: `scp` and `sftp`.

### `scp` from your local computer to the remote system
The most basic command line tool for moving files around is secure copy or `scp`.

`scp` behaves similarily to `ssh` but with one additional input, the name of the file to be copied.  If we were in the shell on our local computer, the file we wanted to move was in our current directory, named "globus.tgz", and Nelle wanted to move it to her home directory on cedar.computecanada.ca then the command would be
	
~~~
[local]$ scp fileToMove nelle@cedar.computecanada.ca:
~~~
{: .bash}
	
It should be expected that a password will be asked for and you should be prepared to provide it.

Once the transfer is complete you should be able to use `ssh` to login to the remote system and see your file in your home directory.

~~~
[remote]$ ls
~~~
{: .bash}

~~~
...
fileToMove
...
~~~
{: .output}

WHAT IF YOU WANTED THE FILE SOMEWHERE OTHER THAN THE HOME DIRECTORY?

> ## Remember the `:`
> Note the colon (`:`) at the end of the command.  This is a very important modifier to include.  If it isn't included then running `scp` will result in a copy of the file that was to be moved being created in the current directory with the name of the remote system.  In the case of the globus.tgz example above it would look like the following:
> 
> ~~~
> [local]$ scp globus.tgz nelle@cedar.computecanada.ca: 
> [local]$ ls
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
> [local]$ rm nelle@cedar.computecanada.ca
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

This can come out of Jeff's stuff.

echo
localhost

nano

## Making Scripts Executable / Changing Permissions

chmod

p. 195