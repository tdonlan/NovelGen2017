from markovSentence import generateRawMarkov
from markovSentence import generateBiDirMarkov

print(generateBiDirMarkov("data/Lovecraft.DunwichHorror.txt","hate",10))

print(generateBiDirMarkov("data/KingJamesBible.txt","love",10))