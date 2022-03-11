#!/usr/bin/python

from common import *

joinby = sys.argv[1];

lines = get_lines()

print(joinby.join(lines))



