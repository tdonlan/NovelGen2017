#get a list of proper nouns from a text
from markovSentence import genMarkovParagraph
from textblob import TextBlob
import random
import re

def readTextAndFilter(filename):
	f = open(filename,"r")
	text = f.read()
	text = re.sub('[^A-Za-z0-9]+', ' ', text)
	return str(text)

def filterNouns(nounlist):
	nounlist = filter(lambda x:nounlist.count(x) > 3,nounlist)
	nounlist2 = sorted(nounlist, key=lambda x:nounlist.count(x))
	unique = []
	[unique.append(item) for item in nounlist2 if item not in unique]

	return unique

def getTextlist(filename):
	f = open(filename,"r")
	return f.read().split()

def getProperNouns(text):
	f = open("data/google-10000-english-no-swears.txt","r")
	commonlist = []
	for line in f:
		commonlist.append(line.strip())

	textlist = text.split()
	pnouns = [x for x in textlist if x.istitle() and x.lower() not in commonlist]
	return pnouns

def getProperNouns2(text):
	blob = TextBlob(text)

	taglist = blob.tags

	taglist2 = []

	for tag in taglist:
		if ('NNP' in tag[1]):
			taglist2.append(tag[0])
			print tag[0] + " - " + tag[1]
	return taglist2

def genTitle(nounlist):
	title = "The " + nounlist[random.randint(0,len(nounlist)-1)] + " of " + nounlist[random.randint(0,len(nounlist)-1)]
	return title.replace(",", "").replace(".","")

def getProperNounListSorted(filename):
	text = readTextAndFilter(filename)
	nounlist = getProperNouns(text)
	return filterNouns(nounlist)
