def alphabeticShift(inputString):
    return "".join(chr(ord(i)+1) if i != "z" else "a" for i in inputString)