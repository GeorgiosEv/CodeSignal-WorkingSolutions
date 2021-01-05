def checkPalindrome(inputString):
    inp = inputString.lower()
    inp = inp.replace(" ","")
    reverse = inp[::-1]
    if (reverse == inp):
        return True
    else:
        return False