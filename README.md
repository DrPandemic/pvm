# Python Version Manager
Easily manage Python versions.

# Goal
There is already many solutions like : [virtualenv](https://pypi.python.org/pypi/virtualenv) and others. But there is none really simple to use.
The inspiration comes from [nvm](https://github.com/creationix/nvm) and [rvm](https://github.com/wayneeseguin/rvm).
The initiale goal is to have a limited set of functions, but just enough to be able to quickly run application with any version of Python.

# Good to know
I'm desinging it to work on my arch linux box, so there is some specific things that could only apply for arch. If you are interested to help for other distro, leave an issue.

# Usage
```pvm ls``` Show installed versions.

```pvm use [version]``` Set the default python version for this user. Will be lost on reboot.

```pvm set [version]``` Set the default python version on your system. Need to be run as root.
Since is run with another user, you could need to call ```pvm default``` after to use that version.

```pvm default``` Use default python version.

# Installation
First you need to clone the repo. You can do it anywhere, but I did it in : ```/usr/share/pvm```. Keep this in mind for the next instructions.
You need to symlink the application : ```sudo ln -s /usr/share/pvm/pvm /usr/bin/pvm```.
Finally, add this to your .bashrc, .zshrc or "the other ones" : ```source /usr/share/pvm/init-pvm.sh```.