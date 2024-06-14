#!/bin/bash
for filename in `find ../img -name "*.svg" -print`; do
    echo "$filename"
    ext="${filename##*.}"
    f="${filename%.*}"
    inkscape --export-area-drawing --export-type=pdf "$filename"
done