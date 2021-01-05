def evenDigitsOnly(n):
    digits_of_n = []
    while n > 0:
        rem = n % 10
        digits_of_n.append(rem)
        n = int(n / 10)
    for i in range(len(digits_of_n)):
        if digits_of_n[i] % 2 != 0:
            return False
    return True