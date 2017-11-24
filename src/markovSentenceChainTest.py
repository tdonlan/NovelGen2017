#start with a random sentence, then use a random word to generate the next part, etc
import random
from markovSentence import generateMarkovSentence
from markovSentence import generateBiDirMarkovSentence
from markovSentence import generateBiDirMarkov

def getRandWord(sentence):
	split = sentence.split()
	return split[random.randint(0,len(split)-1)]


count = random.randint(5,10)
src = "data/texts/aliceInWonderland.txt"
sent = generateBiDirMarkovSentence(src,"",random.randint(10,25))

for x in range(0,count):
	print sent
	word = getRandWord(sent)
	print word
	sent = generateBiDirMarkovSentence(src,word,random.randint(10,25))
