def buildPalindrome(st):
    for i in range(len(st)):
        sub = st[i:len(st)]
        if sub[::-1] == sub:
            missing = st[0:i]
            return st + missing[::-1]
    return st