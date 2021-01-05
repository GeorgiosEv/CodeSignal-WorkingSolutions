from itertools import groupby
def lineEncoding(s):
    s2 = ""
    for k,g in groupby(s):
        l = len(list(g))
        if l == 1:
            s2 += k
        else:
            s2 += str(l) + k
    return s2