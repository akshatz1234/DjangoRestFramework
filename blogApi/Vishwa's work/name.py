import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet

txt = "A fatty Vishwa, Akshat is standing"
def nameex(txt):
    Sentences = nltk.sent_tokenize(txt)
    tokens = []
    for Sent in Sentences:
        tokens.append(nltk.word_tokenize(Sent)) 
    wordsList = [nltk.pos_tag(token) for token in tokens]

    nouns_list = []

    for l in wordsList:
        for word in l:
            if re.match('[NN.*]', word[1]):
                nouns_list.append(word[0])

    names = []
    for nouns in nouns_list:
        if not wordnet.synsets(nouns):
            names.append(nouns)
    print(names)
    name = " "
    name=name.join(names)
    print(name)
nameex(txt)