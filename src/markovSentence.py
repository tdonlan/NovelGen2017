from __future__ import division
import random
import re
from textblob import TextBlob

def getRandWord(sentence):
	split = sentence.split()
	common = ["the","of","and","to","a","in","for","is","on","that","by","this","with","i","you","it","not","or","be","are","as"]
	filtered = [x for x in split if x.lower() not in common]
	return filtered[random.randint(0,len(filtered)-1)]

#generate a chained markov paragraph of length.  
def genMarkovParagraph(textlist, curword, linecount):
	para = ""

	sent = generateBiDirMarkovSentence(textlist,curword,random.randint(10,25))

	for x in range(0,linecount):
		para = para + " " + sent
		word = getRandWord(sent)
		sent = generateBiDirMarkovSentence(textlist,word,random.randint(10,25))

	return para

def genMarkovFirstPersonParagraph(textlist, linecount):
	para = ""

	curword = "I"

	sent = generateMarkovSentence(textlist,curword,random.randint(10,25))

	for x in range(0,linecount):
		para = para + " " + sent
		word = getRandWord(sent)
		sent = generateBiDirMarkovSentence(textlist,word,random.randint(10,25))

	return para

#generate bi-directional markov, starting at curword.  goes both directions until a . is encountered.
def generateBiDirMarkov(textlist, curword,length):

	if curword == "" or curword not in textlist:
		curword = textlist[random.randint(0,len(textlist)-1)]

	retval = curword
	nextword = curword
	prevword = curword

	for x in range(0,length*2):
		
		nextwordlist  = []
		indices = [i for i, x in enumerate(textlist) if x == nextword]
		for i in indices:
			if i < len(textlist)-1:
				nextwordlist.append(textlist[i+1])

		#select randomly from list
		if (len(nextwordlist) > 1):
			nextword = nextwordlist[random.randint(0,len(nextwordlist)-1)]
		else:
			nextword = textlist[random.randint(0,len(textlist)-1)]

		prevwordlist  = []
		indices = [i for i, x in enumerate(textlist) if x == prevword]
		for i in indices:
			if i < len(textlist)-1:
				prevwordlist.append(textlist[i-1])

		if (len(prevwordlist) > 1):
			prevword = prevwordlist[random.randint(0,len(prevwordlist)-1)]
		else:
			prevword = textlist[random.randint(0,len(textlist)-1)]

		retval = prevword + " " + retval + " " + nextword

	#do some processing on this?
	return retval

def generateRawMarkov(textlist, curword, length):
	retval = ""

	if curword == "" or curword not in textlist:
		curword = textlist[random.randint(0,len(textlist)-1)]
	for x in range(0,length):
		retval += curword + " "
	
		nextwordlist  = []
		indices = [i for i, x in enumerate(textlist) if x == curword]
		for i in indices:
			if i < len(textlist)-1:
				nextwordlist.append(textlist[i+1])

		#select randomly from list
		if (len(nextwordlist) > 1):
			curword = nextwordlist[random.randint(0,len(nextwordlist)-1)]
		else:
			curword = textlist[random.randint(0,len(textlist)-1)]

	return retval

def generateMarkovSentence(textlist, curword,length):
	raw = generateRawMarkov(textlist,curword,length)
	sentPattern = "[A-Z][^.!?]*[.!?]"
	sents = re.findall(sentPattern,raw)
	if len(sents) == 0:
		return raw[0].upper() + raw[1:] + "."
	else:
		return sents[0]
	
def generateBiDirMarkovSentence(textlist, curword, length):
	raw = generateBiDirMarkov(textlist,curword,length)
	sentPattern = "[A-Z][^.!?]*[.!?]"
	sents = re.findall(sentPattern,raw)
	if len(sents) == 0:
		return raw[0].upper() + raw[1:] + "."
	else:
		return sents[random.randint(0,len(sents)-1)]