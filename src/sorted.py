#!/usr/bin/python3
import sys

lines = map(str.strip, sys.stdin)

lines = sorted(lines)

for _ in lines :
    print(_)
