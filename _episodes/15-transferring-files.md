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
[remote]$ wget https://hpc-carpentry.github.io/hpc-intro/files/bash-lesson.tar.gz
```
{: .bash}


##  Compressing files

Let's look at the file we just downloaded:

```
[remote]$ ls
bash-lesson.tar.gz
```
{: .bash}

You may recognize that this is a compressed file, or an *archive*, by the file extension `tar.gz`. 
Sometimes it is convenient to compress files to make file transfers easier. 
The larger the file, the longer it will take to transfer. Moreover, we can compress a whole bunch of little files
into one big file to make it easier on us (no one likes transferring 70000 little files)!

Let's extract this file with the `tar` command:

```
[remote]$ tar -xf bash-lesson.tar.gz
```
{: .bash}

```
[remote]$ ls
bash-lesson.tar.gz                           SRR307023_1.fastq  SRR307025_1.fastq  SRR307027_1.fastq  SRR307029_1.fastq
dmel-all-r6.19.gtf                           SRR307023_2.fastq  SRR307025_2.fastq  SRR307027_2.fastq  SRR307029_2.fastq
dmel_unique_protein_isoforms_fb_2016_01.tsv  SRR307024_1.fastq  SRR307026_1.fastq  SRR307028_1.fastq  SRR307030_1.fastq
gene_association.fb                          SRR307024_2.fastq  SRR307026_2.fastq  SRR307028_2.fastq  SRR307030_2.fastq
``` 
{: .output}

To compress files, we can use the `tar` command again, but this time with the `-c` 
flag to indicate we want to compress files. The syntax for compressing files is 
`tar -czf archive-name.tar.gz file1 file2 ...`. Let's make another archive that contains
only the `fasta` files:

```
[remote]$ tar -czf bash-lesson_fastq.tar.gz *.fastq
```
{: .bash}

```
[remote]$ ls
bash-lesson_fastq.tar.gz                     SRR307023_1.fastq  SRR307025_2.fastq  SRR307028_1.fastq  SRR307030_2.fastq
bash-lesson.tar.gz                           SRR307023_2.fastq  SRR307026_1.fastq  SRR307028_2.fastq
dmel-all-r6.19.gtf                           SRR307024_1.fastq  SRR307026_2.fastq  SRR307029_1.fastq
dmel_unique_protein_isoforms_fb_2016_01.tsv  SRR307024_2.fastq  SRR307027_1.fastq  SRR307029_2.fastq
gene_association.fb                          SRR307025_1.fastq  SRR307027_2.fastq  SRR307030_1.fastq
```
{: .output}

## Transferring single files and folders with scp

To copy a single file to or from the cluster, we can use `scp`. The syntax can be a little complex
for new users, but we'll break it down here:

To transfer *to* another computer:
```
[local]$ scp /path/to/local/file.txt yourUsername@remote.computer.address:/path/on/remote/computer
```
{: .bash}

To download *from* another computer:
```
[local]$ scp yourUsername@remote.computer.address:/path/on/remote/computer/file.txt /path/to/local/
```
{: .bash}

Note that we can simplify doing this by shortening our paths. On the remote computer, everything
after the `:` is relative to our home directory. We can simply just add a `:` and leave it at that
if we don't care where the file goes.

```
[local]$ scp local-file.txt yourUsername@remote.computer.address:
```
{: .bash}

To recursively copy a directory, we just add the `-r` (recursive) flag:

```
[local]$ scp -r some-local-folder/ yourUsername@remote.computer.address:target-directory/
```
{: .bash}

> ## A note on rsync
>
> As you gain experience with transferring files, you may find the `scp` command limiting. The
> [rsync](https://rsync.samba.org/) utility provides advanced features for file transfer and is
> typically faster compared to both `scp` and `sftp` (see below). It is especially useful for
> transferring large and/or many files and creating synced backup folders.
>
> The syntax is similar to `scp`. To transfer *to* another computer with commonly used options:
> ```
> [local]$ rsync -avzP /path/to/local/file.txt yourUsername@remote.computer.address:/path/on/remote/computer
> ```
> {: .bash}
>
> The `a` (archive) option preserves file timestamps and permissions among other things; the `v` (verbose)
> option gives verbose output to help monitor the transfer; the `z` (compression) option compresses
> the file during transit to reduce size and transfer time; and the `P` (partial/progress) option
> preserves partially transferred files in case of an interruption and also displays the progress
> of the transfer.
>
> To recursively copy a directory, we can use the same options:
> ```
> [local]$ rsync -avzP /path/to/local/dir yourUsername@remote.computer.address:/path/on/remote/computer
> ```
> {: .bash}
> 
> The `a` (archive) option implies recursion.
{: .callout}

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

* Host: `sftp://{{ site.login_host }}`
* User: Your cluster username
* Password: Your cluster password
* Port: (leave blank to use the default port)

Hit "Quickconnect" to connect! You should see your remote files appear on the right hand side of the
screen. You can drag-and-drop files between the left (local) and right (remote) sides of the screen
to transfer files.

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

> ## Transferring files
>
> Using one of the above methods, try transferring files to and from the cluster. Which method do
> you like the best?
{: .challenge}

{% include links.md %}
