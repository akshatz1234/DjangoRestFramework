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

def preprocess(path):
    img = cv.imread(path,0)
    blurred = cv.blur(img, (3,3))
    canny = cv.Canny(blurred, 50, 200)
    pts = np.argwhere(canny>0)
    y1,x1 = pts.min(axis=0)
    y2,x2 = pts.max(axis=0)
    cropped = img[y1:y2, x1:x2]
    imS = imutils.resize(cropped, width=950)
    cv.imwrite('/home/akshatz/Documents/project/temp1.jpg',imS)
    image = Image.open('/home/vishwa/card_idf/data/temp1.jpg')
    enhancer = ImageEnhance.Brightness(image)
    enhanced_im = enhancer.enhance(1.7)
    con = ImageEnhance.Contrast(enhanced_im)
    con1 = con.enhance(1.3)
    enhancer_object = ImageEnhance.Sharpness(con1)
    out = enhancer_object.enhance(3)
    out.save("/home/vishwa/card_idf/data/t2.jpg")
    #    out.show()
    i = cv.imread("/home/vishwa/card_idf/data/t2.jpg",0)
#    ret, imgf = cv.threshold(i, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
#    cv.imwrite('/home/vishwa/card_idf/data/t12.jpg',imgf);
    output = pytesseract.image_to_string(i, lang='eng')
    print(output)
    return(output)
 

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
                                    return("None")
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
    
app = Flask(__name__)
@app.route("/card", methods=['GET', 'POST'])
def rear():
	f = request.files['photo']
	f.save('')
	print("file saved")
	return(cat(preprocess('')))


if __name__ == "__main__":
    app.debug = True
    app.run(host = '192.168.0.111',port=2020, threaded = False)
