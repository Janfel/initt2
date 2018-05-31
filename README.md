# Overview
initt is an utility to initialize project directories based on templates. It is a rewrite of my previous project init-templates, which is unusable at the moment. init-templates will never leave the development stage, because all development has shifted to initt.

# Disclaimer
**Never use templates from untrusted sources!** A template can execute a script with your permissions, so malware could do a lot of harm. **Please check the templates `init.sh` before use!** You can extract and inspect a templates `init.sh` like this:
```
$ tar xJf path/to/template.initt init.sh
$ nano init.sh
```

# Installation
You can install init-templates either manually or with a script.

## Prerequisites
- A Linux/Unix based operating system
- The `bash` shell
- `git`
- The `makepp` build system

### Makepp
Makepp most likely will not be installed on your system, neither will you find it in your distributions repositories. You can get it from:
- [The official website](https://makepp.sourceforge.net)
- [CPAN](https://metacpan.org/release/makepp)
- My personal [PKGBUILD]() (Arch Linux and derivatives only)

## Manual Installation
1. Clone or download this repo `makepp install`
```
$ git clone "https://github.com/Janfel/initt2.git" initt
$ cd initt
```

2. Run `makepp install` or `makepp uinstall` (Standard $PREFIX is /usr)
```
$ makepp install
```

3. If you installed locally with `makepp uinstall`, add `~/bin/` to your `$PATH`

# Usage

## initt
Use this to create a directory from a template.
```
initt language [-n project-name] [-d template-dir]
```
### Where:
- language: A language template that is installed on your system like `python` or `go`. Defaults to `empty`.
- project-name: The name of your project. If omitted, your current working directory will be initialized and its name will be used.
- template-dir: Here you can override the default template directory.

## initt-zip
Whith this tool you can create your own templates from directories. There is a very nice explanation of this process in `./example/Explanation.md` with an example directory and step-by-step instructions. Have a look.
```
initt-zip templatedir
```
### Where:
- templatedir: The directory you want to convert into a template file.
- outdir: Where to place the generated template file.
