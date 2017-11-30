from textblob import TextBlob
from markovSentence import generateMarkovSentence

def getTextlist(filename):
	f = open(filename,"r")
	return f.read().split()

text = str(generateMarkovSentence(getTextlist("data/texts/macbeth.txt"),"",25))
print text

blob = TextBlob(text)

taglist = blob.tags

taglist2 = []

for tag in taglist:
	if ('NNP' in tag[1]):
		taglist2.append(tag[0])
		print tag[0] + " - " + tag[1]

print taglist2