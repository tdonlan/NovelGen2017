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
def genMarkovParagraph(filename, curword, linecount):
	para = ""

	sent = generateBiDirMarkovSentence(filename,curword,random.randint(10,25))

	for x in range(0,linecount):
		para = para + " " + sent
		word = getRandWord(sent)
		sent = generateBiDirMarkovSentence(filename,word,random.randint(10,25))

	return para

def genMarkovFirstPersonParagraph(filename, linecount):
	para = ""

	curword = "I"

	sent = generateMarkovSentence(filename,curword,random.randint(10,25))

	for x in range(0,linecount):
		para = para + " " + sent
		word = getRandWord(sent)
		sent = generateBiDirMarkovSentence(filename,word,random.randint(10,25))

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
			if i < len(textlist):
				nextwordlist.append(textlist[i+1])

		#select randomly from list
		nextword = nextwordlist[random.randint(0,len(nextwordlist)-1)]

		prevwordlist  = []
		indices = [i for i, x in enumerate(textlist) if x == prevword]
		for i in indices:
			if i < len(textlist):
				prevwordlist.append(textlist[i-1])

		prevword = prevwordlist[random.randint(0,len(prevwordlist)-1)]

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
			if i < len(textlist):
				nextwordlist.append(textlist[i+1])

		#select randomly from list
		curword = nextwordlist[random.randint(0,len(nextwordlist)-1)]

	return retval

def generateMarkovSentence(filename, curword,length):
	f = open(filename,"r")

	#read full text into list
	textlist = f.read().split()

	raw = generateRawMarkov(textlist,curword,length)
	sentPattern = "[A-Z][^.!?]*[.!?]"
	sents = re.findall(sentPattern,raw)
	if len(sents) == 0:
		return raw[0].upper() + raw[1:] + "."
	else:
		return sents[0]
	
def generateBiDirMarkovSentence(filename, curword, length):
	f = open(filename,"r")

	#read full text into list
	textlist = f.read().split()

	raw = generateBiDirMarkov(textlist,curword,length)
	sentPattern = "[A-Z][^.!?]*[.!?]"
	sents = re.findall(sentPattern,raw)
	if len(sents) == 0:
		return raw[0].upper() + raw[1:] + "."
	else:
		return sents[random.randint(0,len(sents)-1)]
