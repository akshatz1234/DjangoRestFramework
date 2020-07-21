import commonUtility
        
def main_ex(output):
    tokenized_text = word_tokenize(output)
    classified_text = st.tag(tokenized_text)
    # print(classified_text)
    data = {}
    data['name'] = nameex(classified_text)
    data['dob'] = dateex(output)
    data['age'] = age(data['dob'])
    data['docType'] = "PAN_card"
    data['gender'] = ""
    data['bloodGroup'] = ""
    data['address'] = ""
    return jsonify(data)