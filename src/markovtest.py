from markovSentence import generateMarkovSentence
from markovSentence import generateBiDirMarkovSentence
from markovSentence import genMarkovParagraph
from markovSentence import getRandWord 

intro = genMarkovParagraph("data/texts/KingJamesBible.txt","",1)
print intro
introwords = []
introwords.append(getRandWord(intro))

print introwords

print "\n\n"

print genMarkovParagraph("data/texts/sleepyhollow.txt",introwords[0],5)
