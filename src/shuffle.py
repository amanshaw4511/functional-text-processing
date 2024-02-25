#!/usr/bin/python3
from random import shuffle
from common import input_lines_with_type

lines = input_lines_with_type()

lines = list(lines)

shuffle(lines)

for it in lines:
    print(it)
