#given a large text, extract the basic structure (titles, chapter beaks, paragraphs, etc)

f = open("data/Lovecraft.DunwichHorror.txt","r")

#read full text into list
textlist = f.read().split("\n")

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
