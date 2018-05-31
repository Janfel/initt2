#!/bin/bash

src="templates"
dest="templates-bin"
ext="initt.txz"
cwd="$PWD"
zip="scripts/initt-zip.sh"

for dir in $(ls "$src")
do
    $zip "$src/$dir"
done

mv "$src"/*/*."$ext" "$dest"
