#!/usr/bin/env bash

mv cmd/{{name}} "cmd/$1"
mv internal/app/{{name}} "internal/app/$1"

echo "NAME := $1" | cat - Makefile.stub > Makefile

rm Makefile.stub
