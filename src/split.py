#!/usr/bin/python3
from common import *

delimeter = if_arg_else(1, "")

lines = input_lines_with_type()

for line in lines:
    fields = line.split(delimeter) if delimeter != "" else list(line)
    for field in fields:
        print(field)
