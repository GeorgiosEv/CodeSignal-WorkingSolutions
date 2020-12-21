def arrayMaxConsecutiveSum(inputArray, k):
    arr = [sum(inputArray[:k])]
    for i in range(1, len(inputArray) - (k-1)):
        arr.append(arr[i-1] - inputArray[i-1] + inputArray[i + k - 1])
    sort_arr = sorted(arr)
    return sort_arr[-1]