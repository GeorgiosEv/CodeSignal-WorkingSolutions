def messageFromBinaryCode(code):
    phrase = ""
    bits = [int(code[i*8:i*8+8],2) for i in range(len(code)//8)]
    for j in range(len(bits)):
        phrase += chr(bits[j])
    return phrase