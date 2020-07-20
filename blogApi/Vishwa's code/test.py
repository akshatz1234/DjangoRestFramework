import pytesseract
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import cv2 as cv
from nltk.tokenize import word_tokenize
import re
import imutils
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
from itertools import groupby

st = StanfordNERTagger('/home/akshatz/Documents/stanford-ner-4.0.0/classifiers/english.conll.4class.distsim.crf.ser.gz',
                       '/home/akshatz/Documents/stanford-ner-4.0.0/stanford-ner.jar',
                       encoding='utf-8')



def preprocess(path):
    img = cv.imread(path,0)
    blurred = cv.blur(img, (3,3))
    canny = cv.Canny(blurred, 50, 200)
    pts = np.argwhere(canny>0)
    y1,x1 = pts.min(axis=0)
    y2,x2 = pts.max(axis=0)
    cropped = img[y1:y2, x1:x2]
    imS = imutils.resize(cropped, width=950)
    cv.imwrite('/home/vishwa/card_idf/temp/temp1.jpg',imS);
    image = Image.open('/home/vishwa/card_idf/temp/temp1.jpg')
    enhancer = ImageEnhance.Brightness(image)
    enhanced_im = enhancer.enhance(1.7)
    con = ImageEnhance.Contrast(enhanced_im)
    con1 = con.enhance(1.3)
    enhancer_object = ImageEnhance.Sharpness(con1)
    out = enhancer_object.enhance(3)
    out.save("/home/vishwa/card_idf/temp/t2.jpg")
    #    out.show()
    i = cv.imread("/home/vishwa/card_idf/temp/t2.jpg",0)
    ret, imgf = cv.threshold(i, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imwrite('/home/vishwa/card_idf/temp/t12.jpg',imgf);
    output = pytesseract.image_to_string(i, lang='eng')
    print(output)
#    num = re.search("^([A-Z]{1}[0-9]{7})", output)
#    return(num.group(1))
#    tokenized_text = word_tokenize(output)
#    classified_text = st.tag(tokenized_text)
#    print(classified_text)
#ipath = '/home/vishwa/card_idf/data'
#images = os.listdir(ipath)
#for i in images:
#    filename = os.path.join(ipath, i)
#    print(i)
#    preprocess(filename)
print(preprocess("/home/vishwa/card_idf/data/d1.jpg"))





















