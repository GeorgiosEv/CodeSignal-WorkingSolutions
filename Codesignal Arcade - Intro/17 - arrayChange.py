def arrayChange(inputArray):
    first = inputArray[0]
    count = 0
    for i in inputArray[1:]:
        if i <= first:
            count += first - i + 1
            first = first + 1
        else:
            first = i
    return count