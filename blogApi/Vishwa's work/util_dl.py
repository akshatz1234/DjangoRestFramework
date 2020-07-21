import commonUtility
        
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