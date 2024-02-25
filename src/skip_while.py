#!/usr/bin/python3
from common import input_lines_with_type, if_arg_else_throw

fn = if_arg_else_throw(1)

lines = input_lines_with_type(2)

for it in lines:
    if eval(fn):
        continue
    print(it)
