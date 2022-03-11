#!/usr/bin/python3
import sys

lines = map(str.strip, sys.stdin)

lines = (field for line in lines for field in list(line))

for line in lines :
    print(line)
