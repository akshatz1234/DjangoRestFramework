#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:27:36 2020

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
        
def reg(output):
    """
    In: OCR output(specifically back)
    Out: Processed text
    """
    regex = re.compile('[^A-Za-z0-9\s\,]')
    spc = re.compile("\s\s+")
    rn = re.compile('(DO|SO|D0|S0)')
    c = regex.sub('',output)
    c1 = rn.sub('',c)
    c2 = spc.sub(" ", c1)
    c3 = re.sub('(,\s)+', ', ', c2)
    return(c3)

def addex(c3):
    """
    In: Proccesed text
    Out: Address
    """
    tkn_add = word_tokenize(reg(c3))
#    print(tkn_add)
    add = ""
    y = 0
    pin = re.compile('^\d{6}$')
    for i in tkn_add:
        p = pin.search(i)
        if y == 1:
            add += i + ' '
        if i == 'ADDRESS' or i == 'Add':
            y = 1
        elif p is not None:
            y = 0
    return(add)

def bloodGroup(output):
    regex = r"\bB\+|\bB-|\bA\+|\bA-|\bAB\+|\bAB-|\bO\+|\bO-"
    bg = re.search(regex, output)
    if bg is None:
        return("None")
    else:
        return(bg.group(0))

        
def main_ex(output):
    tokenized_text = word_tokenize(output)
    classified_text = st.tag(tokenized_text)
    data = {}
    data['name'] = nameex(classified_text)
    data['dob'] = dateex(output)[1]
    data['age'] = dateex(output)[0]
    data['docType'] = "Driving Licence"
    data['address'] = addex(reg(output))
    data['gender'] = ""
    data['bloodGroup'] = bloodGroup(output)
    return jsonify(data)