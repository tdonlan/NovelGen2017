import random
from markovSentence import genMarkovParagraph
from markovSentence import genMarkovFirstPersonParagraph
from markovSentence import getRandWord 

#raw texts -
#religious / quotes - KingJamesBible.txt, Macbeth
#narrative - fellowship, alice, sherlock, sleepyhollow
#descriptive / horror - frakenstein, lovecraft, metamorphosis, mobydick.

#pattern - each chapter - build a mystical quote from bible/shakepeare.  extract the key word.
#use keyword to generate an assortment of narrative/descriptive sentences from random sources.

def getTextlist(filename):
	f = open(filename,"r")
	return f.read().split()

def genChapter(sourceList, sourceCount, introWord):
	chapter = ""

	for x in range(0,sourceCount):
		paralen = random.randint(1,10)
		para = genMarkovParagraph(sourceList[random.randint(0,len(sourceList)-1)],introWord,paralen)

		chapter = chapter + para + "\n"

	return chapter

def genFirstPersonChapter(sourceList, sourceCount):
	chapter = ""

	for x in range(0,sourceCount):
		paralen = random.randint(1,10)
		para = genMarkovFirstPersonParagraph(sourceList[random.randint(0,len(sourceList)-1)],paralen)

		chapter = chapter + para + "\n"

	return chapter

introList = [getTextlist("data/texts/KingJamesBible.txt"),
	getTextlist("data/texts/macbeth.txt")]
firstPersonList = [getTextlist("data/texts/sherlock.txt"),
	getTextlist("data/texts/lovecraft.txt"),
	getTextlist("data/texts/Frankenstein.txt")]
list2 = [getTextlist("data/texts/mobydick.txt"),
	getTextlist("data/texts/fellowshipOfTheRing.txt")]

outFile = open('output/book1.txt','w')

chCount = 10

for ch in range(1,chCount):
	print "Chapter " + str(ch) + "...\n"

	intro = genChapter(introList, 1,"")

	outFile.write("Chapter " + str(ch) + "\n")
	outFile.write(intro)
	outFile.write("\n\n")
	introWord = getRandWord(intro)
	outFile.write(genFirstPersonChapter(firstPersonList,random.randint(2,5)))
	outFile.write("\n\n")
	outFile.write(genChapter(list2,random.randint(5,10),introWord))
	outFile.write("\n\n")
	outFile.write(genFirstPersonChapter(firstPersonList,random.randint(5,10)))
	outFile.write("\n\n")
	outFile.write(genChapter(list2,random.randint(10,20),introWord))
	outFile.write("\n\n")
	outFile.write(genFirstPersonChapter(firstPersonList,random.randint(2,5)))
	outFile.write("\n\n***\n\n")

f.close()