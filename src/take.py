#!/usr/bin/python3
from common import input_lines_with_type, if_arg_else_throw

n = int(if_arg_else_throw(1))

lines = input_lines_with_type()

for i, line in enumerate(lines):
    if i >= n:
        break

    print(line)
