import pytesseract
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import cv2 as cv
from nltk.tokenize import word_tokenize
import re
import imutils


def preprocess(path):
    img = cv.imread(path,0)
    blurred = cv.blur(img, (3,3))
    canny = cv.Canny(blurred, 50, 200)
    pts = np.argwhere(canny>0)
    y1,x1 = pts.min(axis=0)
    y2,x2 = pts.max(axis=0)
    cropped = img[y1:y2, x1:x2]
    imS = imutils.resize(cropped, width=950)
    cv.imwrite('/home/akshatz/Downloads/IMG_20200702_210159.jpg',imS);
    image = Image.open('/home/akshatz/Downloads/IMG_20200702_210159.jpg (2)')
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
    cv.imwrite('/home/akshatz/Downloads/IMG_20200702_210159.jpg',imgf)
    output = pytesseract.image_to_string(imgf, lang='eng')
    with open("ID.txt", "a") as f:
        f.write(output)
        print(output)
    return(output)


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
                            return num.group(1)+"  ID"
                    else:
                        return num.group(1)+" Voter ID"
                else:
                    return num.group(1)+" Passport"
            else:    
                return num.group(1)+"Pan Card"
        else:
            return num.group(1)+" Aadhaar Card"
    else:   
        return num.group(1)+" Driving License"   

def rear():
    # print("Hello")
    # try:
    filename = '/home/akshatz/Downloads/PAN.jpg'
    #     return(AADHARproc(preprocess(file)))
    # except:
    #     return None
    text = str(((pytesseract.image_to_string(Image.open(filename))))) 
    print(text)
rear()
