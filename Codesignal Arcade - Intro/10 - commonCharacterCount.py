"""Given two strings, find the number of common characters between them.

Example:
For s1 = "aabcc" and s2 = "adcaa", the output should be commonCharacterCount(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c"."""
def commonCharacterCount(s1, s2):
    # Step 1: We create two lists, namely s1_l and s2_l, where we store the characters of strings s1 and s2 respectively.
    s1_l = list(s1)
    s2_l = list(s2)
    # Step 2: We also create an empty list, where we are going to store all common characters.
    common = []
    # Step 3: Using a for-loop, we investigate the list of the first string, element by element.
    for i in s1_l:
    # Step 4: If the i-th element from the list of the first string is also present in the list of the second string,
    # we append it to the common array. BE CAREFUL: We must implement the s2_l.remove(i) to avoid double-counting.
    # I checked myself and I can assure you that you can substitute s1_l for s2_l and vice versa (in the for-loop,
    # the if statement and the double-counting term), without affecting the validity of your code.
        if i in s2_l:
            common.append(i)
            s2_l.remove(i)
    # Step 5: Finally, we return the length of the common list, to find the number of the common characters
    # between the two strings given.
    return len(common)
