#!/usr/bin/python3
import sys
from random import shuffle

lines = map(str.strip, sys.stdin)

lines = list(lines)

shuffle(lines)

for it in lines:
    print(_)
