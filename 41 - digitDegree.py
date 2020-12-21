def digitDegree(n):
    degree = 0
    while 10 <= n:
        n = sum(int(i) for i in str(n))
        degree += 1
    return degree