#!/bin/bash

# run translator on all input lines
output=""
while read line; do 
    #echo "go run ../translator.go $line"
    output+=$(go run ../translator.go $line)
    output+=" "
done <test.in

# get expecetd output from test.out
expected=""
while read line; do
    expected+=$line
    expected+=" "
done <test.out

echo "translated: $output"
echo "expected:   $expected"

# compare output vs expected
[ "$output" == "$expected" ] && echo "Outputs match"
