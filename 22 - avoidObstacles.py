def avoidObstacles(inputArray):
    for i in range(2, max(inputArray)+2):
        if i not in inputArray and all(j%i != 0 for j in inputArray):
            return i