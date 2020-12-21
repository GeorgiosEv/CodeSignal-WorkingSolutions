def longestDigitsPrefix(inputString):
    count = 0
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            count += 1
        else:
            return inputString[0:count]
    return inputString