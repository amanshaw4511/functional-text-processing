#!/usr/bin/python3
import sys

lines = map(str.strip, sys.stdin)

count = 0
for line in lines:
    count += 1

print(count)
