def adjacentElementsProduct(inputArray):
    ArrayEnd = []
    for i in range(len(inputArray) - 1):
        ArrayEnd.append(inputArray[i]*inputArray[i+1])
    maximum = max(ArrayEnd)
    return maximum