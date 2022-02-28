#!/usr/bin/python3
import sys
import os

command = sys.argv[1]

lines = map(str.strip, sys.stdin)

for _i, _ in enumerate(lines) :
    os.system(command.replace("_",_))
