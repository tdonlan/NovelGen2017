#get a list of proper nouns from a text
from markovSentence import genMarkovParagraph

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



text = genMarkovParagraph(getTextlist("data/texts/KingJamesBible.txt"),"",5)
print text
print getProperNouns(str(text))
