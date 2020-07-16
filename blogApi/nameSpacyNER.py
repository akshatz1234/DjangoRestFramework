from nltk.tokenize import word_tokenize
import nltk
text = open("ID.txt").read()
tokenized_text = word_tokenize(text)
n = nltk.pos_tag(tokenized_text)
print(n)
dictionary = dict()
for name, typeofText in n:
	dictionary.setdefault(name, typeofText)
for key, value in dictionary.items():
	# FOR PAN CARD 
	with open("id.txt", "a") as f:
		if "NNP" in value:
			print(key, end=" ")
			f.write(key+" "+"\n")
		elif "CD" in value:
			f.write("\n")
			f.write("Age= "+ key)
			f.write("\n")