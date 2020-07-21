import commonUtility
 
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
    data['docType'] = "Aadhar_Card"
    data['gender'] = genex(tokenized_text)
    data['bloodGroup'] = ""
    data['address'] = ""
    return jsonify(data)