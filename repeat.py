#!/usr/bin/python3
import sys

n = int(sys.argv[1])

lines = map(str.strip, sys.stdin)

lines = (field for line in lines for field in list(line))

lines = list(lines)

for _ in range(n) :
    for line in lines :
        print(line)
