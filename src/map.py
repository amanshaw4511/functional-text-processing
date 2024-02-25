#!/usr/bin/python3
import sys
from common import get_lines_of_type

fn = sys.argv[1]
type = ""

if len(sys.argv) == 3:
    type = get_lines_of_type(sys.argv[3])

lines = map(str.strip, sys.stdin)
if type:
    lines = map(type, lines)

for _i, _ in enumerate(lines):
    print(eval(fn))
