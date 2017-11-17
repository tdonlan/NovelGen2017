from __future__ import division
import random
from textblob import TextBlob

#genererate a single sentence with markov (include a word)?

def generateRawMarkovOld(filename,curword):
	retval = ""

	f = open(filename,"r")

	#read full text into list
	textlist = f.read().split()

	if curword == "":
		curword = textlist[random.randint(0,len(textlist)-1)]
	for x in range(0,200):
		retval += curword + " "
		
		nextwordlist  = []
		indices = [i for i, x in enumerate(textlist) if x == curword]
		for i in indices:
			if i < len(textlist):
				nextwordlist.append(textlist[i+1])

		#select randomly from list
		curword = nextwordlist[random.randint(0,len(nextwordlist)-1)]

	return retval

def generateRawMarkov(textlist, curword):
	retval = ""

	if curword == "":
		curword = textlist[random.randint(0,len(textlist)-1)]
	for x in range(0,200):
		retval += curword + " "

		if curword.endswith("."):
			break
		
		nextwordlist  = []
		indices = [i for i, x in enumerate(textlist) if x == curword]
		for i in indices:
			if i < len(textlist):
				nextwordlist.append(textlist[i+1])

		#select randomly from list
		curword = nextwordlist[random.randint(0,len(nextwordlist)-1)]

	return retval
##-------

def getMarkovSentenceOld(filename,curword,targetlen):
	raw =generateRawMarkovOld(filename,"")

	blob = TextBlob(unicode(raw,'utf-8'))

	sents = blob.sentences

	#get a sentence that is 25% of a given length
	sents = filter(lambda a: a != ".",sents)

	""""
	slens = map(lambda a: abs(len(a)-targetlen) / targetlen,sents)
	print(slens)

	sents = filter(lambda a: (abs(len(a)-targetlen) / targetlen) < 2 and (abs(len(a)-targetlen) / targetlen) > .75, sents)

	slens = map(lambda a: abs(len(a)-targetlen) / targetlen,sents)
	print(slens)

	print(sents)
	"""
	
	s = sents[random.randint(0,len(sents)-1)]
	return s

#print(getMarkovSentence("data/Lovecraft.DunwichHorror.txt","",5))