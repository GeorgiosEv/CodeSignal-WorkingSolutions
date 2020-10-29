def areSimilar(a, b):
    check_a = []
    check_b = []
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            check_a.append(a[i])
            check_b.append(b[i])
    if count == 0:
        return True
    elif count == 2:
        return set(check_a) == set(check_b)
    else:
        return False