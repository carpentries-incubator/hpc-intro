#!/bin/bash

# A bash script to read in one data file and perform word frequency analysis.
# As far as possible, uses commands which are taught in Carpentries Unix Shell workshop

DATA_FILE=$1

echo "Starting word frequency analysis of $DATA_FILE"
echo "=============================================="

# execute the following commands and output a summary of time/resource taken when it finishes
# get the contents of the text file to analyse
        time cat $DATA_FILE | \
# for all fields, replace spaces with newlines, so each word is on its own line
        cut -d ' ' -f 1-  --output-delimiter=$'\n'  | \
# delete all non-letter characters, except newlines
        tr -c -d "[A-Za-z\n]"    | \
# replace uppercase chars with lowercase
        tr '[:upper:]' '[:lower:]' | \
        sort | \
# strings ensures we only consider printable text characters
        strings -n 1 | \
# count duplicate lines (by now, lines are words in printable chars only)
        uniq -c | \
# numerically sort the counted unique words
# output to a new file
        sort -n > analysed_$DATA_FILE

echo "====================================="
echo "Completed word analysis of" $DATA_FILE
