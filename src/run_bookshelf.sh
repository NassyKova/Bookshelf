#!/bin/bash
echo -n "Print help to read help file or hit enter to open the app: "
read VAR
    if [$1 == help]
    then
        content = cat help_file.txt
    else
        python3 bookshelf.py