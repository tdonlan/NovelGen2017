#generate a random character
import random

def loadList(filename):
    f = open(filename,"r")
    wordlist = []
    for line in f:
        #wordlist.append(line.strip())
        wordlist.append(line.strip().replace('"','').replace(',',''))
    return wordlist

def getFromList(min,max,list):
    count = random.randint(min,max)
    retval = ""
    for x in range(0,count):
        retval += list[random.randint(0,len(list)-1)] + " "
    return retval


fNameList = loadList("data/firstnames.txt")
lNameList = loadList("data/lastnames.txt")
descList = loadList("data/descriptions.txt")
moodsList = loadList("data/moods.txt")
occupationsList = loadList("data/occupations.txt")
prefixList = loadList("data/Prefix.txt")
suffixList = loadList("data/Suffix.txt")

name = getFromList(0,1,prefixList) + " " + getFromList(1,2,fNameList) + " " + getFromList(1,2,lNameList) +  " " + getFromList(0,2,suffixList)
print name
print getFromList(1,2,occupationsList)
print getFromList(1,3,descList)
print getFromList(1,4,moodsList)