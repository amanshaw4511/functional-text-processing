#!/usr/bin/python3
import sys

start = 0
step = 1
stop = 0

if len(sys.argv) == 4:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
    step = int(sys.argv[3])
elif len(sys.argv) == 3:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
elif len(sys.argv) == 2:
    stop = int(sys.argv[1])
else:
    pass

for x in range(start, stop + 1, step):
    print(x)
