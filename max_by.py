#!/usr/bin/python3
import sys
from functools import cmp_to_key

fn = sys.argv[1]

lines = map(str.strip, sys.stdin)

lines = map(float, lines)

ans = max(lines, key=cmp_to_key(lambda _x,_y: eval(fn)))

print(ans)
