import random
from markovSentence import genMarkovParagraph
from markovSentence import getRandWord 

def genChapter(introList, introCount, sourceList, sourceCount):
	intro = genMarkovParagraph(introList[random.randint(0,len(introList)-1)],"",introCount)

	introWord = getRandWord(intro)

	chapter = intro + "\n\n"

	for x in range(0,sourceCount):
		paralen = random.randint(1,10)
		para = genMarkovParagraph(sourceList[random.randint(0,len(sourceList)-1)],introWord,paralen)

		chapter = chapter + para + "\n"

	return chapter

print genChapter(["data/texts/KingJamesBible.txt"],1,
	["data/texts/sleepyhollow.txt","data/texts/Lovecraft.DunwichHorror.txt","data/texts/mobydick.txt"],1)


print genChapter(["data/texts/KingJamesBible.txt"],1,
	["data/texts/sherlock.txt","data/texts/fellowshipOfTheRing.txt"],1)
