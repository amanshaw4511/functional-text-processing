#!/usr/bin/python3
import sys

fn = sys.argv[1]
init = sys.argv[2]

lines = map(str.strip, sys.stdin)


_a = eval(init)
for _i, _ in enumerate(lines):
    _a = eval(fn)

print(_a)
