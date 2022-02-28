#!/usr/bin/python3
import sys

lines = map(str.strip, sys.stdin)

lines = set(lines)

for line in lines :
    print(line)
