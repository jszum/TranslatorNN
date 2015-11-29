#!/usr/bin/python

import sys
from subprocess import call


lines = sys.argv[1]

for i in range(1,9):

	args1 = "sources30px/set%s/" % i
	args2 =	lines 
	args3 = "noised/line%s/set%s/" % (lines, i)
 	call(["./liner.py", args1, args2, args3])


