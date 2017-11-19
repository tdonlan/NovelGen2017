from textblob import TextBlob

text = '''
The birch canoe slid on the smooth planks.
'''

blob = TextBlob(text)

taglist = blob.tags

taglist2 = []

for tag in taglist:
	if ('NN' in tag[1]  or  'VB' in tag[1]):
		taglist2.append(tag[0])
		print tag[0] + " - " + tag[1]

print taglist2

print(blob.noun_phrases)