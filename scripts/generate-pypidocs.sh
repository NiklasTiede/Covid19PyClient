#!/bin/bash

SWITCH=0
START='<!-- PYPI-DOCS:START -->'
END='<!-- PYPI-DOCS:END -->'

echo "" > pypidocs.md
while read p; do
    if [[ $p == $START ]]; then
        SWITCH=1
    elif [[ $p == $END ]]; then
        SWITCH=0
    elif [[ $SWITCH -eq 1 && $p != $START ]]; then
        echo $p >> pypidocs.md
    fi
done <README.md

