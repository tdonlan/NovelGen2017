from textblob import TextBlob

text = '''
When a traveler in north central Massachusetts takes the wrong fork
at the junction of the Aylesbury pike just beyond Dean's Corners he
comes upon a lonely and curious country
'''

blob = TextBlob(text)

taglist = blob.tags

print(taglist)

for tag in taglist:
	if ('NN' in tag[1]  or  'VB' in tag[1]):
		print tag[0] + " - " + tag[1]

print(blob.noun_phrases)