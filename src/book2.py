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

introList = [getTextlist("data/texts/KingJamesBible.txt"),
	getTextlist("data/texts/sonnets.txt")]

sourceList = [getTextlist("data/texts/cthulu.txt"),
	getTextlist("data/texts/lovecraft.txt"),
	getTextlist("data/texts/metamorphosis.txt")]


outFile = open('output/book2.txt','w')

chCount = 13

for ch in range(1,chCount):
	print "Chapter " + str(ch) + "...\n"

	intro = genChapter(introList, 1,"")

	outFile.write("Chapter " + str(ch) + "\n")
	outFile.write(intro)
	outFile.write("\n\n")
	introWord = getRandWord(intro)
	outFile.write(genFirstPersonChapter(sourceList,random.randint(2,5)))
	outFile.write("\n\n")
	outFile.write(genChapter(sourceList,random.randint(5,10),introWord))
	outFile.write("\n\n")
	outFile.write(genFirstPersonChapter(sourceList,random.randint(2,5)))
	outFile.write("\n\n***\n\n")

f.close()