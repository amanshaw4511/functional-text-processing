#!/usr/bin/python

from common import *

joinby = if_arg_else(1, " ")
prefix = if_arg_else(2, "")
postfix = if_arg_else(3, "")

lines = input_lines_with_type()

print(prefix + joinby.join(lines) + postfix)
