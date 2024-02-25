#!/usr/bin/python3
from common import input_lines_with_type

lines = input_lines_with_type()

lines = list(lines)

for line in reversed(lines):
    print(line)
