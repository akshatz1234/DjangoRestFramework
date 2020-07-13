import spacy

from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

fileName = "ID.txt" 
introductionFileText = open(fileName).read()
introductionFileDoc = nlp(introductionFileText)
print([token.text for token in introductionFileDoc])
