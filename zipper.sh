#!/bin/bash

src="templates"
dest="templates-bin"
ext="initt.txz"
cwd="$PWD"
zip="tar cJf"

for dir in $(ls "$src")
do
    (
    cd "$src/$dir" \
    && $zip "$dir.$ext" *
    )
done

mv "$src"/*/*."$ext" "$dest"
