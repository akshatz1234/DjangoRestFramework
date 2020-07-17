#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:09:37 2020

@author: vishwa
"""

from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
import re
from itertools import groupby
from flask import jsonify
import util_age


st = StanfordNERTagger('/home/akshatz/Documents/stanford-ner-4.0.0/classifiers/english.conll.4class.distsim.crf.ser.gz',
                       '/home/akshatz/Documents/stanford-ner-4.0.0/stanford-ner.jar',
                       encoding='utf-8')



def nameex(txt):
    """
    In: Classified text from StanfordNER
    Out: Name
    """
    for tag, chunk in groupby(txt, lambda x:x[1]):
        if tag != "O" and tag == 'PERSON':
            a=" ".join(w for w, t in chunk)
            return(a)
            break

def dateex(output):
    """
    In: Output from the OCR
    out: Date
    """
    date = re.findall("([0-9]{2}\/[0-9]{2}\/[0-9]{4}|[0-9]{2}\-[0-9]{2}\-[0-9]{4})", output)
    if not date:
        return("None","None")
    else:
        a = []
        for i in date:
            a.append(util_age.main(i))
        f = a.index(max(a))
        dob = date[f]
        return(max(a),dob)

def main_ex(output):
    tokenized_text = word_tokenize(output)
    classified_text = st.tag(tokenized_text)
#    print(classified_text)
    data = {}
    data['name'] = nameex(classified_text)
    data['dob'] = dateex(output)[1]
    data['age'] = dateex(output)[0]
    data['docType'] = "Passport"
    return jsonify(data)