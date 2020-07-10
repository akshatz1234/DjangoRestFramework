with open("ID.txt", "r") as fi:
    with open("Id1.txt", "a") as fo:
        f = fi.seek()
        print(fi.read())
