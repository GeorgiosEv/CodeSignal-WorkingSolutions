def absoluteValuesSumMinimization(a):
    sums = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(a)):
            sum += abs(a[i] - a[j])
        sums.append(sum)
    return a[sums.index(min(sums))]