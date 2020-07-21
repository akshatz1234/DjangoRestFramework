import pytesseract
from flask import Flask, request
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import cv2 as cv
import re
import imutils
import util_aadhar
import util_pan
import util_dl
import util_vi
import util_pass
import util_other

# Preprocess image file
def preprocess(path):
    img = cv.imread(path,0)
    blurred = cv.blur(img, (3,3))
    canny = cv.Canny(blurred, 50, 200)
    pts = np.argwhere(canny>0)
    y1,x1 = pts.min(axis=0)
    y2,x2 = pts.max(axis=0)
    cropped = img[y1:y2, x1:x2]
    imS = imutils.resize(cropped, width=950)
    cv.imwrite('/home/akshatz/Documents/project/temp1.jpg',imS);
    image = Image.open('/home/akshatz/Documents/project/temp1.jpg')
    enhancer = ImageEnhance.Brightness(image)
    enhanced_im = enhancer.enhance(1.7)
    con = ImageEnhance.Contrast(enhanced_im)
    con1 = con.enhance(1.3)
    enhancer_object = ImageEnhance.Sharpness(con1)
    out = enhancer_object.enhance(3)
    out.save("/home/akshatz/Documents/project/t2.jpg")
    i = cv.imread("/home/akshatz/Documents/project/t2.jpg",0)
    output = pytesseract.image_to_string(i, lang='eng')
    return(output)
 
# categorization
def cat(out):
    num = re.search("([0-9]{4}\ [0-9]{4}\ [0-9]{4})", out)
    if num is None:
        num = re.search("([A-Z]{5}[0-9]{4}[A-Z]{1})", out)
        if num is None:
            num = re.search("^([A-Z]{1}[0-9]{7})", out)
            if num is None:
                num = re.search("ELECTION", out)
                if num is None:
                    num = re.search("([A-Z]{2}[0-9]{2} [0-9]{10})", out)
                    if num is None:
                        word = re.search("Permanent",out)
                        if word is None:
                            return(util_other.main_ex(out))
                        else:
                            return(util_pan.main_ex(out))
                    else:
                        return(util_dl.main_ex(out))
                else:
                    return(util_vi.main_ex(out))
            else:
                return(util_pass.main_ex(out))
        else:
            return(util_pan.main_ex(out))
    else:
        return(util_aadhar.main_ex(out))
    
# input file
filename = "/home/akshatz/Downloads/ID proofs/Aadhar Card/Kushleen.jpg"

# allowed filenames
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

# Function to denote allowed file formats
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Main Function
app = Flask(__name__)
@app.route("/card", methods=['GET', 'POST'])
def rear():
    if allowed_file(filename):
        img = Image.open(filename)
        img.load()
        text = pytesseract.image_to_string(img)
        return (cat(preprocess(filename)))
        if text == None:
            text = cat(preprocess(filename))
            return text 

if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1',port=5000, threaded = False)
