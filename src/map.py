#!/usr/bin/python3
import sys
from common import input_lines_with_type, if_arg_else_throw

fn = if_arg_else_throw(2)

lines = input_lines_with_type(2)

for i, it in enumerate(lines):
    print(eval(fn))
