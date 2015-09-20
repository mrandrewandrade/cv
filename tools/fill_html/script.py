import re
import os.path
#empty list of words
words = []

#read file word by word
f = open('default.html')
for word in f.read().split():
    words.append(word)

#regex to find *.html
regex = re.compile('\w+\.html')
#copy over the words which match regex
okay_items = [x for x in words if regex.match(x)]
for webpage in okay_items:
	#if file does not exist	
     if not os.path.isfile(webpage):
        file = open(webpage, 'w')
        file.close()
		
print okay_items
