#!/usr/bin/env bash

count=100 #how many files to decrypt

shopt -s extglob

#find the first Riddle.zip file
file=$(find -- *.zip)
unzip "$file"
rm "$file"

while [[ $count -gt 0 ]]; do
    file=$(find -- *.zip)
    unzip "$file"
    rm "$file"
    count=$count-1
    # body
done

echo "Done unzipping"
