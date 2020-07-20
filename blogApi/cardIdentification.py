from flask import Flask, app, request
import pytesseract
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import cv2 as cv
from nltk.tokenize import word_tokenize, RegexpTokenizer
import re
import imutils

# For image to be preprocessedif required
def preprocess(path):
    try:
        img = cv.imread(path,0)
        blurred = cv.blur(img, (3,3))
        canny = cv.Canny(blurred, 50, 200)
        pts = np.argwhere(canny>0)
        y1,x1 = pts.min(axis=0)
        y2,x2 = pts.max(axis=0)
        cropped = img[y1:y2, x1:x2]
        imS = imutils.resize(cropped, width=950)
        cv.imwrite('/home/akshatz/Downloads/e1.jpg',imS);
        image = Image.open('/home/akshatz/Downloads/IMG_20200702_210159 (2).jpg')
        enhancer = ImageEnhance.Brightness(image)
        enhanced_im = enhancer.enhance(2)
        con = ImageEnhance.Contrast(enhanced_im)
        con1 = con.enhance(1.3)
        enhancer_object = ImageEnhance.Sharpness(con1)
        out = enhancer_object.enhance(3)
        out.save("/home/akshatz/Downloads/PAN.jpg")
        #    out.show()
        i = cv.imread('/home/akshatz/Downloads/IMG_20200702_210159.jpg (2)',0)
        ret, imgf = cv.threshold(i, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
        cv.imwrite('/home/akshatz/Downloads/e1.jpg',imgf)
        output = pytesseract.image_to_string(imgf, lang='eng')
        with open("ID.txt", "a") as f:
            f.write(output)
            print(output)
        return(output)
    except:
        return None

# Function to detect ID card
def AADHARproc(out):
    num = re.search("([0-9]{4}\ [0-9]{4}\ [0-9]{4})", out)
    if num is None:
        num = re.search("([A-Z]{5}[0-9]{4}[A-Z]{1})", out)
        if num is None:
            num = re.search("([A-Z]{1}[0-9]{7})", out)
            if num is None:
                num = re.search("([A-Z]{3}[0-9]{7})", out)
                if num is None:
                    num = re.search("([A-Z]{3}[0-9]{6})")
                    if num is None:
                        num = re.search("DL-[0-9}{14}$")
                        if num is None:
                            return "None"
                        else:   
                            return num.group(1)+" Driving License"   
                    else:
                        return num.group(1)+" EMP ID"
                else:
                    return num.group(1)+" Voter ID"
            else:
                return num.group(1)+" Passport"
        else:    
            return num.group(1)+"Pan Card"
    else:
        return num.group(1)+" Aadhaar Card"

#input file name
filename = "/home/akshatz/Downloads/ID proofs/Aadhar Card/Yash.jpeg"

# Allowed files
ALLOWED_EXTENSIONS = ['png', 'jpg']

# Function to denote allowed file formats
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# main function
app = Flask(__name__)
@app.route("/card", methods=['GET', 'POST'])
def rear():
    with open ("ID.txt", "a") as f:
        if allowed_file(filename):
            img = Image.open(filename)
            img.load()
            text = pytesseract.image_to_string(img)
            print(text)
            f.write(text+"\n")
            if text == None:
                text = AADHARproc(preprocess(filename))
                f.write(text+"\n")
                return text 
            return "NO text in document"
        else:
            return "NOT Valid FILE"


if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1',port=5000, threaded = False) 