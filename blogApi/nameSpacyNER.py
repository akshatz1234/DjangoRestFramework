from nltk.tokenize import word_tokenize
import nltk
import re
text = open("ID.txt").read()
# text = "JATIN PRAFULBHAI ZALA"
tokenized_text = word_tokenize(text)
n = nltk.pos_tag(tokenized_text)
dictionary = dict()
print(n)
# print(dictionary)
for name, typeofText in n:
	dictionary.setdefault(name, typeofText)
	# print(dictionary)
for key, value in dictionary.items():
	with open("id.txt", "a") as f:
		if "NNP" in value:
			print(key, end=" ")
			f.write(key+" ")
		elif "CD" in value:
			f.write("\n")
			f.write("Age= "+ key + "\n")
