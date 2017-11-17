#prints a small subset from a large list of common words

import random

def getRandomWords(wordlist):
	retval = []
	count = random.randint(2,5);
	for x in range(0,count):
		retval.append(wordlist[random.randint(0,len(wordlist)-1)])

	return retval

f = open("data/google-10000-english-no-swears.txt","r")
wordlist = []
for line in f:
    wordlist.append(line.strip())

newlist = getRandomWords(wordlist)
print newlist
