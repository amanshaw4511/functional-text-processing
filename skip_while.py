#!/usr/bin/python3
import sys

fn = sys.argv[1]

lines = map(str.strip, sys.stdin)

for _ in lines:
    if eval(fn) :
        continue
    print(_)
