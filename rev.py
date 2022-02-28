#!/usr/bin/python3
import sys

lines = map(str.strip, sys.stdin)

lines = list(lines)

for line in reversed(lines) :
    print(line)
