def alternatingSums(a):
    alt_sum = [0, 0]
    length = len(a)
    for i in range(0, length):
        if i % 2 == 0:
            alt_sum[0] += a[i]
        else:
            alt_sum[1] += a[i]
    return alt_sum