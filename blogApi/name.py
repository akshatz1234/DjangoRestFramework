# from nltk.tokenize import MWETokenizer

# tokenize = MWETokenizer("ID.txt")
# print(tokenize)

# -*- coding: utf-8 -*-

# from nltk.tag import StanfordNERTagger
# from nltk.tokenize import word_tokenize

# st = StanfordNERTagger('/home/akshatz/Documents/stanford-ner-4.0.0/classifiers/english.conll.4class.distsim.crf.ser.gz',
#                        '/home/akshatz/Documents/stanford-ner-4.0.0/stanford-ner.jar',
#                        encoding='utf-8')

# text = 'Vishwa, 18 years old working in XYZ company'

# tokenized_text = word_tokenize(text)
# classified_text = st.tag(tokenized_text)

# print(classified_text)
import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet

String = 'Ravana was killed in a war'

Sentences = nltk.sent_tokenize(String)
Tokens = []
for Sent in Sentences:
    Tokens.append(nltk.word_tokenize(Sent)) 
Words_List = [nltk.pos_tag(Token) for Token in Tokens]

Nouns_List = []

for List in Words_List:
    for Word in List:
        if re.match('[NN.*]', Word[1]):
             Nouns_List.append(Word[0])

Names = []
for Nouns in Nouns_List:
    if not wordnet.synsets(Nouns):
        Names.append(Nouns)

print (Names)