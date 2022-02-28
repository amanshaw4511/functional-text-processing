#!/usr/bin/python3
import sys

lines = map(str.strip, sys.stdin)

lines = map(float, lines)

print(min(lines))
