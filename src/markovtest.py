import random

f = open("data/fellowshipOfTheRing.txt","r")

#read full text into list
textlist = f.read().split()
#print(textlist[0:100])

#read random word.
curword = textlist[random.randint(0,len(textlist)-1)]
for x in range(0,100):
	print curword + " ",

	#search for all instances of word in text, get next word in list
	
	nextwordlist  = []
	indices = [i for i, x in enumerate(textlist) if x == curword]
	for i in indices:
		if i < len(textlist):
			nextwordlist.append(textlist[i+1])

	#select randomly from list
	curword = nextwordlist[random.randint(0,len(nextwordlist)-1)]
