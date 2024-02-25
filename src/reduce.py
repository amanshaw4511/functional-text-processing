#!/usr/bin/python3
import sys

from common import input_lines_with_type

fn = sys.argv[1]
init = sys.argv[2]

lines = input_lines_with_type(3)


acc = eval(init)
for i, it in enumerate(lines):
    acc = eval(fn)

print(acc)
