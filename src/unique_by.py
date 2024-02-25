#!/usr/bin/python3
import sys

fn = sys.argv[1]

lines = map(str.strip, sys.stdin)

lines = list(lines)

lines2 = {}
for _i, _ in enumerate(lines):
    key = eval(fn)
    if key not in lines2:
        lines2[key] = _i

for key, index in lines2.items():
    print(lines[index])
