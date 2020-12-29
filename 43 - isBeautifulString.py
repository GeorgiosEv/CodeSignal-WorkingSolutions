def isBeautifulString(inputString):
    counter = [inputString.count(i) for i in string.ascii_lowercase]
    return counter[::-1] == sorted(counter)