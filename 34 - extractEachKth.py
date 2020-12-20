def extractEachKth(inputArray, k):
    inp = []
    for i in range(len(inputArray)):
        if (i+1)%k == 0:
            pass
        else:
            inp.append(inputArray[i])
    return inp