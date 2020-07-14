from nltk.tokenize import word_tokenize
import nltk
import re
text = open("ID.txt").read()

tokenized_text = word_tokenize(text)
n = nltk.pos_tag(tokenized_text)
# for i in range(n):
	# print(n[i])
# query = [lis[1] for lis in n]
# result = [lis[0] for lis in n]
# query =  ", ".join(map(str, query))
# print(query)
# result = ", ".join(map(str, result))
# print(query, result)
# print(type(result))
# print(result)
# print(text)
# print(n)
# if query.find('NNP'):
# 	print(result)
# print(n)
dictionary = dict()
# print(tokenized_text)
for name, typeofText in n:
	dictionary.setdefault(name, []).append(typeofText)
# print(dictionary)
# if dict_values == "NNP" or dict_values == "NNP, NNP":
# 	print(dict.keys)
for key, value in my_dict.items(): 
         if val == value: 
             return key 