import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet

def nameex(txt):
    Sentences = nltk.sent_tokenize(txt)
    tokens = []
    for Sent in Sentences:
        tokens.append(nltk.word_tokenize(Sent)) 
    Words_List = [nltk.pos_tag(token) for token in tokens]

    nouns_list = []

    for l in WordsList:
        for word in l:
            if re.match('[NN.*]', word[1]):
                nouns_list.append(word[0])

    names = []
    for nouns in nouns_list:
        if not wordnet.synsets(Nouns):
            names.append(Nouns)
    return names