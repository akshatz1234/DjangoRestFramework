#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:09:57 2020

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
            print(a)
            return(a)
            break

def dateex(output):
    """
    In: Output from the OCR
    out: Date
    """
    date = re.search("([0-9]{2}\/[0-9]{2}\/[0-9]{4}|[0-9]{2}\-[0-9]{2}\-[0-9]{4})", output)
    if date is None:
        year = re.search("(19..|20..)", output)
        if year is None:
            return "None"
        else:
            return(year.group(1))
    else:
        return(date.group(1))
        
def age(dob):
    if dob == "None":
        return "None"
    else:
        return(util_age.main(dob))
    
def genex(tokenized_text):
    """
    In: OCR output Tokenized
    out: Gender
    """
    for i in tokenized_text:
        male = re.search("(^MA.E$|^Ma.e$)", i)
        female = re.search("(^FEMA.E$|^Fema.e$)", i)
        if male is not None:
            return "Male"
        if female is not None:
            return "Female"
        
def main_ex(output):
    tokenized_text = word_tokenize(output)
    classified_text = st.tag(tokenized_text)
    data = {}
    data['name'] = nameex(classified_text)
    data['dob'] = dateex(output)
    data['age'] = age(data['dob'])
    data["gender"] = genex(tokenized_text)
    data['docType'] = "Voter ID"
    data['bloodGroup'] = ""
    data['address'] = ""    
    return jsonify(data)