def arrayReplace(inputArray, elemToReplace, substitutionElem):
    new = []
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            new.append(substitutionElem)
        else:
            new.append(inputArray[i])
    return new