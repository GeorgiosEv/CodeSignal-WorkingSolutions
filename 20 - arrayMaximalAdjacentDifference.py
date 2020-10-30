def arrayMaximalAdjacentDifference(inputArray):
    return max((abs(inputArray[i+1]-inputArray[i]) for i in range(0,len(inputArray)-1)))