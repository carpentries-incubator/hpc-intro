---
layout: page
title: Setup
root: .
---

There are several pieces of software you will wish to install before the
workshop. Though installation help will be provided at the workshop, we
recommend that these tools are installed (or at least downloaded) beforehand.

1. [A terminal application or command-line interface](
   #where-to-type-commands-how-to-open-a-new-shell)
2. [A Secure Shell application](#ssh-for-secure-connections)
3. [A public-private key pair](#public-private-key-pair-for-ssh)
4. [An SSH key agent](#ssh-agent-for-easier-key-handling)

> ## Bash and SSH
>
> This lesson requires a terminal application (`bash`, `zsh`, or others) with
> the ability to securely connect to a remote machine (`ssh`).
{: .prereq}

## Where to Type Commands: How to Open a New Shell

The shell is a program that enables us to send commands to the computer and
receive output. It is also referred to as the terminal or command line.

Some computers include a default Unix Shell program. The steps below describe
some methods for identifying and opening a Unix Shell program if you already
have one installed. There are also options for identifying and downloading a
Unix Shell program, a Linux/UNIX emulator, or a program to access a Unix Shell
on a server.

### Unix Shells on Windows

Computers with Windows operating systems do not automatically have a Unix Shell
program installed. In this lesson, we encourage you to use an emulator included
in Git for Windows, which gives you access to both Bash shell commands and Git.
If you have attended a Software Carpentry workshop session, it is likely you
have already received instructions on how to install Git for Windows.

Once installed, you can open a terminal by running the program Git Bash from
the Windows start menu.

#### Shell Programs for Windows

* [Git for Windows][git4win] -- *Recommended*
* [Windows Subsystem for Linux][ms-wsl] -- advanced option for Windows 10

> ## Alternatives to Git for Windows
>
> Other solutions are available for running Bash commands on Windows. There is
> now a Bash shell command-line tool available for Windows 10. Additionally,
> you can run Bash commands on a remote computer or server that already has a
> Unix Shell, from your Windows machine. This can usually be done through a
> Secure Shell (SSH) client. One such client available for free for Windows
> computers is PuTTY. See the reference below for information on installing and
> using PuTTY, using the Windows 10 command-line tool, or installing and using
> a Unix/Linux emulator.
>
> For advanced users, you may choose one of the following alternatives:
>
> * Install the [Windows Subsystem for Linux][ms-wsl]
> * Use the Windows [PowerShell][ms-shell]
> * Read up on [Using a Unix/Linux emulator][unix-emulator] (Cygwin) or Secure
>   Shell (SSH) client (PuTTY)
>
> > ## Warning
> >
> > Commands in the Windows Subsystem for Linux (WSL), PowerShell, or Cygwin
> > may differ slightly from those shown in the lesson or presented in the
> > workshop. Please ask if you encounter such a mismatch -- you're
> > probably not alone.
> {: .challenge}
{: .discussion}

### Unix Shell on macOS

On macOS, the default Unix Shell is accessible by running the Terminal program
from the `/Application/Utilities` folder in Finder.

To open Terminal, try one or both of the following:

* In Finder, select the Go menu, then select Utilities. Locate Terminal in the
  Utilities folder and open it.
* Use the Mac ‘Spotlight’ computer search function. Search for: `Terminal` and
  press <kbd>Return</kbd>.

For an introduction, see [How to Use Terminal on a Mac][mac-terminal].

### Unix Shell on Linux

On most versions of Linux, the default Unix Shell is accessible by running the
[(Gnome) Terminal](https://help.gnome.org/users/gnome-terminal/stable/) or
[(KDE) Konsole](https://konsole.kde.org/) or
[xterm](https://en.wikipedia.org/wiki/Xterm), which can be found via the
applications menu or the search bar.

### Special Cases

If none of the options above address your circumstances, try an online search
for: `Unix shell [your operating system]`.

## SSH for Secure Connections

All students should have an SSH client installed. SSH is a tool that allows us
to connect to and use a remote computer as our own.

### SSH for Windows

Git for Windows comes with SSH preinstalled: you do not have to do anything.

> ## GUI Support for Windows
>
> If you know that the software you will be running on the cluster requires a
> graphical user interface (a GUI window needs to open for the application to
> run properly), please install [MobaXterm](https://mobaxterm.mobatek.net) Home
> Edition.
{: .discussion}

### SSH for macOS

macOS comes with SSH pre-installed: you do not have to do anything.

> ## GUI Support for macOS
>
> If you know that the software you will be running requires a graphical user
> interface, please install [XQuartz](https://www.xquartz.org).
{: .discussion}

### SSH for Linux

Linux comes with SSH and X window support preinstalled: you do not have to do
anything.

## Public-Private Key Pair for SSH

SSH keys are an alternative method for authentication to obtain access to
remote computing systems. They can also be used for authentication when
transferring files or for accessing version control systems. In this section
you will create a pair of SSH keys:

* a private key which you keep on your own computer, and
* a public key which is placed on the remote HPC system that you will access.

### SSH Keys on Linux, Mac, MobaXterm, and Windows Subsystem for Linux

Once you have opened a terminal, check for existing SSH keys and filenames
since existing SSH keys are overwritten.

```
{{ site.local.prompt }} ls ~/.ssh/
```
{: .language-bash}

Ensure `id_ed25519` does not exist; else, use a different name.

Generate a new public-private key pair using the following command, which will
produce a stronger key than the `ssh-keygen` default. When prompted, enter a
strong password that you will remember. Cryptography is only as good as the
weakest link, and this will be used to connect to a powerful, precious,
computational resource.

```
{{ site.local.prompt }} ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519
```
{: .language-bash}

* `-o` (no default): use the OpenSSH key format,
  rather than PEM.
* `-a` (default is 16): number of rounds of passphrase derivation; increase to
  slow down brute force attacks.
* `-t` (default is [rsa][wiki-rsa]): specify the "type" or cryptographic
  algorithm. [EdDSA][wiki-dsa] with a 256-bit key is faster than RSA with a
  comparable strength.
* `-f` (default is /home/user/.ssh/id_algorithm): filename to store your keys.
  If you already have SSH keys, make sure you specify a different name:
  `ssh-keygen` will overwrite the default key if you don't specify!

If ed25519 is not available and the above command fails, generate your key-pair
using the older (but strong and trusted) [RSA][wiki-rsa] cryptosystem:

```
{{ site.local.prompt }} ls ~/.ssh/
{{ site.local.prompt }} ssh-keygen -o -a 100 -t rsa -b 4096 -f ~/.ssh/id_rsa
```
{: .language-bash}

The flag `-b` sets the number of bits in the key. The default is 2048.
EdDSA uses a fixed key length, so this flag would have no effect.

Take a look in `~/.ssh` (use `ls ~/.ssh`). You should see the two new files:

* your private key (`~/.ssh/id_ed25519` or `~/.ssh/id_rsa`)
* shareable public key (`~/.ssh/id_ed25519.pub` or `~/.ssh/id_rsa.pub`)

If a key is requested by the system administrators, the *public* key is the one
to provide.

> ## Private keys are your secure digital passport
>
> A private key that is visible to anyone but you should be considered
> compromised, and must be destroyed. This includes having improper permissions
> on the directory it (or a copy) is stored in, traversing any network that is
> not secure (encrypted), attachment on unencrypted email, and even displaying
> the key (which is ASCII text) in your terminal window.
>
> Protect this key as if it unlocks your front door. In many ways, it does.
{: .caution}

For more information on SSH security and some of the flags set here, an
excellent resource is ["Secure Secure Shell"][ssh-flags].

### SSH Keys on Windows

If you are using PuTTY on Windows, download and use `puttygen` to generate the
key pair. See the PuTTY [documentation][putty-gen].

## SSH Agent for Easier Key Handling

An SSH key is only as strong as the password used to unlock it, but on the
other hand, typing out a complex password every time you connect to a machine
is tedious and gets old very fast. This is where the [SSH Agent][ssh-agent]
comes in.

Using an SSH Agent, you can type your password for the private key once, then
have the Agent remember for some number of hours or until you log off. Unless
some nefarious actor has physical access to your machine, this keeps the
password safe, and removes the tedium of entering the password multiple times.

Just remember your password, because once it expires in the Agent, you have to
type it in again.

### SSH Agents on Linux, macOS, and Windows

Open your terminal application and check if an agent is running:

```
{{ site.local.prompt }} ssh-add -l
```
{: .language-bash}

If you get an error like this one,

```
Error connecting to agent: No such file or directory
```
{: .error}

... then you need to launch the agent *as a background process*.

```
{{ site.local.prompt }} eval $(ssh-agent)
```
{: .language-bash}

Now you can add your key to the agent:

```
{{ site.local.prompt }} ssh-add -t 8h ~/.ssh/id_ed25519
```
{: .language-bash}
```
Enter passphrase for .ssh/id_ed25519: 
Identity added: .ssh/id_ed25519
Lifetime set to 86400 seconds
```
{: .output}

For the duration (8 hours), whenever you use that key, the SSH Agent will
provide the key on your behalf without you having to type a single keystroke.

### SSH Agent on PuTTY

If you are using PuTTY on Windows, download and use `pageant` as the SSH agent.
See the PuTTY [documentation][putty-gen].

<!-- links -->
[git4win]: https://gitforwindows.org/
[mac-terminal]: https://www.macworld.co.uk/feature/mac-software/how-use-terminal-on-mac-3608274/
[ms-wsl]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
[ms-shell]: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core?view=powershell-7
[mobax-gen]: https://mobaxterm.mobatek.net/documentation.html
[putty-gen]: https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html
[ssh-agent]: https://www.ssh.com/academy/ssh/agent
[ssh-flags]: https://stribika.github.io/2015/01/04/secure-secure-shell.html
[unix-emulator]: https://faculty.smu.edu/reynolds/unixtut/windows.html
[wiki-rsa]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[wiki-dsa]: https://en.wikipedia.org/wiki/EdDSA
[wsl]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
