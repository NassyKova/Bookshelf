#!/bin/bash
if [ $# -eq 1 ] && [ $1 == "help" ]
then
    cat help.txt
else
    python3 bookshelf.py
fi