def palindromeRearranging(inputString):
    odd_count = 0
    char_set = set(inputString)
    for i in char_set:
        char_count = inputString.count(i)
        if char_count % 2 != 0:
            odd_count += 1
    if odd_count <= 1:
        return True
    return False