import sys
import random
import re
from random import shuffle
from properNouns import genTitle
from properNouns import getProperNouns

file1 = sys.argv[1]
chapters = open(file1,"r").read().split("***")

print len(chapters)

shuffle(chapters)

part=1
partcount = 1
partlen = len(chapters) / 5


#iterate over chapters

i=1
for v in chapters:
	if partcount ==1:
		print 'Part ' + str(part)
		print genTitle(getProperNouns(v))
		print ""
	#print i
	v = re.sub('Chapter [0-9]+','Chapter ' + str(i),v)

	print v
	i=i+1
	partcount = partcount + 1
	if (partcount > partlen):
		i =1
		part = part + 1
		partcount =1

