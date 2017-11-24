#start with a random sentence, then use a random word to generate the next part, etc
import random
from markovSentence import generateMarkovSentence
from markovSentence import generateBiDirMarkovSentence
from markovSentence import generateBiDirMarkov

def getRandWord(sentence):
	split = sentence.split()
	common = ["the","of","and","to","a","in","for","is","on","that","by","this","with","i","you","it","not","or","be","are","as"]
	filtered = [x for x in split if x.lower() not in common]
	return filtered[random.randint(0,len(filtered)-1)]

count = random.randint(5,10)
src = "data/texts/aliceInWonderland.txt"
sent = generateBiDirMarkovSentence(src,"",random.randint(10,25))

for x in range(0,count):
	print sent
	word = getRandWord(sent)
	sent = generateBiDirMarkovSentence(src,word,random.randint(10,25))
