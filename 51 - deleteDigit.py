def deleteDigit(n):
    num = str(n)
    result = list(int(''.join(num[:i]+num[1+i:])) for i in range(len(num)))
    return max(result)