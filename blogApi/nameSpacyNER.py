import spacy
from spacy.matcher import Matcher


nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

fileName = "ID.txt" 

introductionFileText = open(fileName).read()
doc = nlp(introductionFileText)
for token in doc:
# if token.pos_== "PROPN":
    print(token)
    # else:
    #     pass

# print(type(token))

