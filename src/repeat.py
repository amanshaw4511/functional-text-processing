#!/usr/bin/python3
from common import *

n = int(if_arg_else(1, 1))

lines = input_lines_with_type()

lines = list(lines)
for _ in range(n):
    for line in lines:
        print(line)
