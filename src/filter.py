#!/usr/bin/python3
import sys
from common import input_lines_with_type

fn = sys.argv[1]

lines = input_lines_with_type(2)

for i, it in enumerate(lines):
    if eval(fn):
        print(it)
