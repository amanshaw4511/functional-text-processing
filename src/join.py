#!/usr/bin/python

from common import *

joinby = " "
if len(sys.argv) > 1 :
    joinby = sys.argv[1];

lines = get_lines()

print(joinby.join(lines))



