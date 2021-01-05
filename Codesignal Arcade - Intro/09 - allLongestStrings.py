def allLongestStrings(inputArray):
    max_arr = []
    max_len = len(max(inputArray, key = len))
    for i in inputArray:
        if len(i) == max_len:
            max_arr.append(i)
    return max_arr