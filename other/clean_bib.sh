#!/bin/bash
cp ../refs.bib refs.bib.old
# ./gradlew buildLatex
python clean_bib.py --texfile=../Main2.tex --input=../refs.bib --dropunused