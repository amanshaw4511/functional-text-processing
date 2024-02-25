#!/usr/bin/python3
import sys
import os

command = sys.argv[1]
place_holder = sys.argv[2] if len(sys.argv) == 3 else '_'

lines = map(str.strip, sys.stdin)

for i, it in enumerate(lines):
    os.system(command.replace(place_holder, it))
