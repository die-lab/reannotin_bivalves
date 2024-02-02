#!/bin/bash

# Check if file is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Check if file exists
if [ ! -f "$1" ]; then
    echo "File not found: $1"
    exit 1
fi

# Read the file line by line
while IFS= read -r line1 && IFS= read -r line2 && IFS= read -r line3; do
    echo -e "$line1\t$line2\t$line3"
done < "$1"
