#!/usr/bin/python3
import sys

start = sys.argv[1]
step = sys.argv[2]
stop = sys.argv[3]

_init = eval(start)
_ = _init
while (eval(stop)):
    print(_)
    _ = eval(step)
