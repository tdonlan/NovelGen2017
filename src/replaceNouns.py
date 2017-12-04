#replace the common proper nouns in one file with those from another file
import sys
from properNouns import getProperNounListSorted 

file1 = sys.argv[1]
file2 = "output/book2.txt"

file1text = open(file1,"r").read()

file1nouns = list(reversed(getProperNounListSorted(file1)))
#print file1nouns

file2nouns = list(reversed(getProperNounListSorted(file2)))

#print file2nouns

#iterate through list1 and replace in the text with the corresponding entry from list2.  if none is found, dont replace

for i,val in enumerate(file1nouns):
	if len(file2nouns) > i:
		#print val + "->" + file2nouns[i]
		file1text = file1text.replace(val,file2nouns[i])

print file1text