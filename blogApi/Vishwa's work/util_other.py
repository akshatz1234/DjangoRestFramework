import commonUtility

def bloodGroup(output):
    regex = r"\bB\+|\bB-|\bA\+|\bA-|\bAB\+|\bAB-|\bO\+|\bO-"
    bg = re.search(regex, output)
    if bg is None:
        return("None")
    else:
        return(bg.group(0))

def doctype(output):
    emp = re.search("Employee|EMPLOYEE", output)
    if emp is None:
        return("None")
    else:
        return("Employee_id")
    
        
def main_ex(output):
    tokenized_text = word_tokenize(output)
    classified_text = st.tag(tokenized_text)
    # print(classified_text)
    data = {}
    data['name'] = nameex(classified_text)
    data['dob'] = dateex(output)
    data['age'] = age(data['dob'])
    data['docType'] = doctype(output)
    data['gender'] = genex(tokenized_text)
    data['bloodGroup'] = bloodGroup(output)
    data['address'] = ""
    return jsonify(data)
