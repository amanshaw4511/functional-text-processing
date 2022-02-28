#!/usr/bin/python3
import sys

fn = sys.argv[1]

lines = map(str.strip, sys.stdin)

lines = map(lambda _ : eval(fn), lines)

for line in lines :
    print(line)
