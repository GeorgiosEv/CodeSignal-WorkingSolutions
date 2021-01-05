def commonCharacterCount(s1, s2):
    s1_l = list(s1)
    s2_l = list(s2)
    common = []
    for i in s1_l:
        if i in s2_l:
            common.append(i)
            s2_l.remove(i)
    return len(common)