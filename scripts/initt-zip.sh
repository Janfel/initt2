#!/bin/bash

dir="$1"
name="${dir##*/}"
ext="initt.txz"
zip="tar cJf"

cd "$dir" \
&& $zip "$name.$ext" *
