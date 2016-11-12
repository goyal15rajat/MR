#!usr/bin/env/python

import sys

for line in sys.stdin:
	line=line.strip()
	word=line.split("\n")
	word = word.strip(".")
	word = word.strip("'")
#add strip if u want to stop other english stop characters
	print '%s\t%s' % (word,1)
