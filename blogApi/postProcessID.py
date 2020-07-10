import re
fi = "ID.txt"
fo = "Id1.txt"
with open(fi, "r") as fi:
    with open(fo, "a") as fo:
        str(fi.read())
        if re.search("^[a-zA-Z\. ]+$", str(fi.read())):
            print(str(fi.read()))   
            name = re.search("^[a-zA-Z\. ]+$")
            name = str(name)
            print(name)
            fo.write(name)