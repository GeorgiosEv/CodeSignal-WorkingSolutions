def almostIncreasingSequence(sequence):
    n = len(sequence)
    if len(sequence) <= 2:
        return True
    c1 = 0
    c2 = 0
    for i in range(1, n-1):
        if sequence[i-1] >= sequence[i]:
            c1 += 1
        if sequence[i-1] >= sequence[i+1]:
            c2 += 1
    if sequence[n-1] <= sequence[n-2]:
        c1 += 1
    if c1 <= 1 and c2 <= 1:
        return True
    else:
        return False