def sortByHeight(a):
    j = 0
    a_sort = sorted([i for i in a if i != -1])
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i] = a_sort[j]
            j += 1
    return a