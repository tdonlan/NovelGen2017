import random
from markovSentence import genMarkovParagraph
from markovSentence import genMarkovFirstPersonParagraph
from markovSentence import getRandWord 


def getTextlist(filename):
	f = open(filename,"r")
	return f.read().split()

def genChapter(sourceList, sourceCount, introWord):
	chapter = ""

	for x in range(0,sourceCount):
		paralen = random.randint(1,5)
		para = genMarkovParagraph(sourceList[random.randint(0,len(sourceList)-1)],introWord,paralen)

		chapter = chapter + para + "\n"

	return chapter

def genFirstPersonChapter(sourceList, sourceCount):
	chapter = ""

	for x in range(0,sourceCount):
		paralen = random.randint(1,5)
		para = genMarkovFirstPersonParagraph(sourceList[random.randint(0,len(sourceList)-1)],paralen)

		chapter = chapter + para + "\n"

	return chapter

introList = [getTextlist("data/texts/sonnets.txt")]

sourceList = [getTextlist("data/texts/aliceInWonderland.txt"),
	getTextlist("data/texts/sleepyhollow.txt")]


outFile = open('output/book3.txt','w')

chCount = 20

for ch in range(1,chCount):
	print "Chapter " + str(ch) + "...\n"

	intro = genChapter(introList, 6,"")

	outFile.write("Chapter " + str(ch) + "\n")
	outFile.write(intro)
	outFile.write("\n\n")
	introWord = getRandWord(intro)
	outFile.write(genChapter(sourceList,random.randint(5,10),introWord))
	outFile.write("\n\n")
	outFile.write(genChapter(sourceList,random.randint(5,10),introWord))
	outFile.write("\n\n")
	outFile.write(genChapter(sourceList,random.randint(5,10),introWord))	
	outFile.write("\n\n")
	outFile.write(genChapter(sourceList,random.randint(5,10),introWord))
	outFile.write("\n\n***\n\n")

outFile.close()