def digitDegree(n):
    degree = 0
    while 10 <= n:
        num = str(n)
        n = sum(int(i) for i in num)
        degree += 1
    return degree
