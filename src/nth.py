#!/usr/bin/python3
import sys

nth = int(sys.argv[1])

lines = map(str.strip, sys.stdin)

for i, line in enumerate(lines):
    if i + 1 == nth:
        print(line)
        break
