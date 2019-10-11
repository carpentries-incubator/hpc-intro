---
title: "Transferring files"
teaching: 30
exercises: 10
questions:
- "How do I upload/download files to the cluster?"
objectives:
- "Be able to transfer files to and from a computing cluster."
keypoints:
- "`wget` downloads a file from the internet."
- "`scp` transfer files to and from your computer."
- "You can use an SFTP client like FileZilla to transfer files through a GUI."
---

Computing with a remote computer offers very limited use if we cannot get files to 
or from the cluster. There are several options for transferring data between computing 
resources, from command line options to GUI programs, which we will cover here.

## Download files from the internet using wget

One of the most straightforward ways to download files is to use `wget`. Any file 
that can be downloaded in your web browser with an accessible link can be downloaded 
using `wget`. This is a quick way to download datasets or source code. 

The syntax is: `wget https://some/link/to/a/file.tar.gz`. For example, download the 
lesson sample files using the following command:

```
{{ site.host_prompt }} wget {{ site.url }}{{ site.baseurl }}/bash-lesson.tar.gz
```
{: .bash}

## Transferring single files and folders with scp

To copy a single file to or from the cluster, we can use `scp`. The syntax can be a little complex
for new users, but we'll break it down here:

To transfer *to* another computer:
```
{{ site.local_prompt }} scp /path/to/local/file.txt yourUsername@remote.computer.address:/path/on/remote/computer
```
{: .bash}

To download *from* another computer:
```
{{ site.local_prompt }} scp yourUsername@remote.computer.address:/path/on/remote/computer/file.txt /path/to/local/
```
{: .bash}

Note that we can simplify doing this by shortening our paths. On the remote computer, everything
after the `:` is relative to our home directory. We can simply just add a `:` and leave it at that
if we don't care where the file goes.

```
{{ site.local_prompt }} scp local-file.txt yourUsername@remote.computer.address:
```
{: .bash}

To recursively copy a directory, we just add the `-r` (recursive) flag:

```
{{ site.local_prompt }} scp -r some-local-folder/ yourUsername@remote.computer.address:target-directory/
```
{: .bash}

## Transferring files interactively with FileZilla (sftp)

FileZilla is a cross-platform client for downloading and uploading files to and from a remote
computer. It is absolutely fool-proof and always works quite well. It uses the `sftp`
protocol. You can read more about using the `sftp` protocol in the command line [here]({{ site.baseurl }}{% link _extras/discuss.md %}).

Download and install the FileZilla client from
[https://filezilla-project.org](https://filezilla-project.org). After installing and opening the
program, you should end up with a window with a file browser of your local system on the left hand
side of the screen. When you connect to the cluster, your cluster files will appear on the right
hand side.

To connect to the cluster, we'll just need to enter our credentials at the top of the screen:

* Host: `sftp://{{ site.host_login }}`
* User: Your cluster username
* Password: Your cluster password
* Port: (leave blank to use the default port)

Hit "Quickconnect" to connect! You should see your remote files appear on the right hand side of the
screen. You can drag-and-drop files between the left (local) and right (remote) sides of the screen
to transfer files.

## Archiving files

One of the biggest challenges we often face when transferring data between remote HPC systems
is that of large numbers of files. There is an overhead to transferring each individual file 
and when we are transferring large numbers of files these overheads combine to slow down our
transfers to a large degree.

The solution to this problem is to *archive* multiple files into smaller numbers of larger files
before we transfer the data to improve our transfer efficiency. Sometimes we will combine 
archiving with *compression* to reduce the amount of data we have to transfer and so speed up
the transfer.

The most common archiving command you will use on (Linux) HPC cluster is `tar`. `tar` can be used
to combine files into a single archive file and, optionally, compress. For example, to combine
all files within a folder called `output_data` into an archive file called `output_data.tar` we
would use:

```
tar -cvf output_data.tar output_data/
```
{: .bash}

We also use the `tar` command to extract the files from the archive once we have transferred it:

```
tar -xvf output_data.tar
```
{: .bash}

This will put the data into a directory called `output_data`. Be careful, it will overwrite data there if this
directory already exists!

Sometimes you may also want to compress the archive to save space and speed up the transfer. However,
you should be aware that for large amounts of data compressing and un-compressing can take longer
than transferring the un-compressed data  so you may not want to transfer. To create a compressed
archive using `tar` we add the `-z` option and add the `.gz` extension to the file to indicate
it is compressed, e.g.:

```
tar -czvf output_data.tar.gz output_data/
```
{: .bash}

The `tar` command is used to extract the files from the archive in exactly the same way as for
uncompressed data as `tar` recognizes it is compressed and un-compresses and extracts at the 
same time:

```
tar -xvf output_data.tar.gz
```
{: .bash}

> ## Transferring files
>
> Using one of the above methods, try transferring files to and from the cluster. Which method do
> you like the best?
{: .challenge}

> ## Working with Windows
>
> When you transfer files to from a Windows system to a Unix system (Mac, Linux, BSD, Solaris, etc.)
> this can cause problems. Windows encodes its files slightly different than Unix, and adds an extra
> character to every line.
> 
> On a Unix system, every line in a file ends with a `\n` (newline). On Windows, every line in a
> file ends with a `\r\n` (carriage return + newline). This causes problems sometimes.
> 
> Though most modern programming languages and software handles this correctly, in some rare
> instances, you may run into an issue. The solution is to convert a file from Windows to Unix
> encoding with the `dos2unix` command.
> 
> You can identify if a file has Windows line endings with `cat -A filename`. A file with Windows
> line endings will have `^M$` at the end of every line. A file with Unix line endings will have `$`
> at the end of a line.
> 
> To convert the file, just run `dos2unix filename`. (Conversely, to convert back to Windows format,
> you can run `unix2dos filename`.)
{: .callout}

> ## A note on ports
>
> All file transfers using the above methods use encrypted communication over port 22. This is the
> same connection method used by SSH. In fact, all file transfers using these methods occur through
> an SSH connection. If you can connect via SSH over the normal port, you will be able to transfer
> files.
{: .callout}

{% include links.md %}
