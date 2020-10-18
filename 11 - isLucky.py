def isLucky(n):
    digits_of_n = []
    sum = 0
    while n > 0:
        rem = n % 10
        digits_of_n.append(rem)
        n = int(n / 10)
    for i in range(len(digits_of_n)):
        if i < len(digits_of_n)/2:
            sum += digits_of_n[i]
        else:
            sum -= digits_of_n[i]
    if sum == 0:
        return True
    return False