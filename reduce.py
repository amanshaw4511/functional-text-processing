#!/usr/bin/python3
import sys
from functools import reduce

fn = sys.argv[1]
init = sys.argv[2]

lines = map(str.strip, sys.stdin)

res = reduce(lambda _a, _: eval(fn) ,lines, eval(init))

print(res)
