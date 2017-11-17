from markovSentence import generateRawMarkov

f = open("data/Lovecraft.DunwichHorror.txt","r")
#read full text into list
textlist = f.read().split("\n")

f2 = open("data/fellowshipOfTheRing.txt")
textlist2 = f2.read().split()

paralist = ""
for s in textlist:
	if len(s) > 1:
		paralist+="." #paragraph
	else:
		paralist+="+"


while "++" in paralist:
	paralist = paralist.replace("++","\n")

paralist = paralist.replace("+.",".")

print(paralist)


for p in paralist:
	if "." in p:
		print(generateRawMarkov(textlist2,""))
	else:
		print(p)
