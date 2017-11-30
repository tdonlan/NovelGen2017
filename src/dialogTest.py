import random
from markovSentence import genMarkovParagraph
from markovSentence import genMarkovFirstPersonParagraph
from markovSentence import getRandWord 


def getTextlist(filename):
	f = open(filename,"r")
	return f.read().split()


def genDialog(sourceList, sourceCount, introWord):
	chapter = ""

	for x in range(0,sourceCount):
		paralen = 1
		para = genMarkovParagraph(sourceList[random.randint(0,len(sourceList)-1)],introWord,paralen)
		
		chapter = chapter + para + "\n"

	return chapter

sourceList = [getTextlist("data/texts/macbeth.txt")]

outFile = open('output/dialog.txt','w')

chCount = 25

for ch in range(1,chCount):
	print "Chapter " + str(ch) + "...\n"
	outFile.write("Chapter " + str(ch) + "\n")
	outFile.write("\n\n")
	outFile.write(genDialog(sourceList, random.randint(20,50),"I"))
	outFile.write("\n\n***\n\n")

outFile.close()