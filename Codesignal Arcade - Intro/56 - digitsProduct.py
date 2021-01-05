def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    for i in range(0, 4000):
        p = 1
        for j in str(i):
            p *= int(j)
        if p == product:
            return i
    return -1