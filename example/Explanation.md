# How to make your own template

## The Directory
You can place anything you want copied in the root directory or in subdirectories. This is helpful for copying **Makefiles** and **`.gitignore`** files. Do not create empty directories or files here, use `file.txt` and `dir.txt` instead. You can create files with names like **{{myname}}** and rename them using `init.sh`.

## dir.txt
In this file you can list empty directories that you want to be created. You can also list a subdirectory of a nonexistent directory, to get both created. This is helpful for creating directories like `bin` and `doc`. Using **{{myname}}** and renaming in `init.sh` also works.

## file.txt
Here you can list any files you want to be created, but you can not specify their contents; they remain empty. You can use this to create files like `README.md` and `License`. You can not implicitly create directories here, but you can use those created by `dir.txt`.

## init.s<span></span>h
This file will be executed as a script after `dir.txt` and `file.txt`. Please add a *shebang* like `#!/usr/bin/env bash` as the first line, specifying the interpreter to be used. The variable `$1` will always correspond to your projects name, so you can use this to rename **{{myname}}** directories dynamically. In this script you can do whatever you want, so it is at the same time the most flexible and the most dangerous part of this program. Please think of this before doing things like `rm -rf` or using templates from untrusted sources.

## Zipping up
The by far easiest way to create a template from your directory is to use the `initt-zip` script distributed with this program. Simply type:
```
$ initt-zip path/to/mydir
```
This will create the file `path/to/mydir/mydir.initt.txz` that you can install by typing:
```
$ mv path/to/mydir.initt.txz ~/.local/share/init-templates/myname.initt.txz
```
You can now use this template like any other:
```
$ initt myname -n myprojectname
```

## Have Fun
