#!/usr/bin/python3
import sys

n = int(sys.argv[1])

lines = map(str.strip, sys.stdin)

for i, line in enumerate(lines):
    if i < n:
        continue
    print(line)
