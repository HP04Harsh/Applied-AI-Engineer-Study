#!/bin/bash

for file in *.txt; do
    
    if [ -f "$file" ]; then
     
        newname="${file%.txt}.md"
        mv "$file" "$newname"
        echo "Renamed: $file -> $newname"
    fi
done
