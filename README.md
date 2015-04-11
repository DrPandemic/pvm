# pvm
Easily manage Python versions.

# Goal
There is already many solutions like : [virtualenv](https://pypi.python.org/pypi/virtualenv) and others. But there is none really simple to use.
The inspiration comes from [nvm](https://github.com/creationix/nvm) and [rvm](https://github.com/wayneeseguin/rvm).
The initiale goal is to have a limited set of functions, but just enough to be able to quickly run application with any version of Python on your system.

# Good to know
I'm desinging it to work on my arch linux box, so there is some specific things that could only apply for arch. If you are interested to help for other distro, leave an issue.

# Usage
```pvm ls``` Show installed versions.

```pvm use [version]``` Let you choose which python version to use.

```pvm set [version]``` Let you choose which python version to set as default.

```pvm default`` Use default python version.
