from nltk.tokenize import word_tokenize
import nltk
import re
text = open("ID.txt").read()

tokenized_text = word_tokenize(text)
n = nltk.pos_tag(tokenized_text)
# print(n)
dictionary = dict()
# print(tokenized_text)
for name, typeofText in n:
	dictionary.setdefault(name, typeofText)

for key, value in dictionary.items():
	if 'NNP' in value:
		print(key)
