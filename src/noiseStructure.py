#random num - sentence length.  
#0 or > 25 paragraph break
#1-10 sections / chapter
#10 - 20 chapters / part
#3-10 parts / book

import random

parts = random.randint(3,10)

print "Book 1"
for p in range(1,parts+1):
	print "Part " + str(p) + "/" + str(parts)
	chapters = random.randint(10,20)
	for c in range(1,chapters+1):
		print "Chapter " + str(c) + "/" + str(chapters)
		sections = random.randint(5,10)
		for s in range(1,sections+1):
			print "s" + str(s) 
			while True:
				plen = random.randint(1,30)
				if plen > 25:
					break
				else: 
					print ".",# "s(" + str(plen) + ")",
			print ""
			print " --- "

