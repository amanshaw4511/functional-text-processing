#!/usr/bin/python3
import sys

fn = sys.argv[1]

lines = map(str.strip, sys.stdin)

for _i, _ in enumerate(lines) :
    if eval(fn):
        print(_)
