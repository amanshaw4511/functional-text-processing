#!/usr/bin/python3
import sys
from common import *

fn = if_arg_else_throw(1)

lines = input_lines_with_type(2)

for it in lines:
    if eval(fn):
        print("false")
        sys.exit(1)

print("true")
