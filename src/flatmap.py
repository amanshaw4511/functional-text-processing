#!/usr/bin/python3
import sys

fn = sys.argv[1]

lines = map(str.strip, sys.stdin)

for it in lines:
    for each in eval(fn):
        print(each)
