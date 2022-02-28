#!/usr/bin/python3
import sys

delimeter = sys.argv[1]

lines = map(str.strip, sys.stdin)

lines = (field for line in lines for field in line.split(delimeter))

for line in lines :
    print(line)
