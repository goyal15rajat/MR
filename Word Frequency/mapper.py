#!usr/bin/env/python

import sys
import re
from nltk.corpus import stopwords



for line in sys.stdin:
	s=set(stopwords.words('english'))
	line=line.strip()
	if line == '':
		continue
	else:
		x=line.split()

		for word in x:
			word = word.strip(".")
			word = word.strip(",")
			word = word.strip(";")
			word = word.strip(":")
			word = word.strip('"')
			if word in s:
				continue
			else:	
				print '%s %s' % (word,1)
