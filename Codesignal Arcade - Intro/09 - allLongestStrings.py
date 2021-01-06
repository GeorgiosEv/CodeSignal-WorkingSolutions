"""Given an array of strings, return another array containing all of its longest strings.

Example:
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"]."""
def allLongestStrings(inputArray):
    # Step 1: We begin by defining an empty array called "max_arr", where we will store the longest strings from the given array.
    max_arr = []
    # Step 2: The next step is to define the maximum string length inside our given array.
    # BE CAREFUL: Variable max_len should be defined as follows. If we break it into its components, we can see that:
    # max(inputArray, key = len) locates ONLY ONE of the strings that satisfies the maximum value in terms of the key parameter
    # provided (which, in this case, is the string's length) and the outside len() function defines the value of this maximum length.
    # You are free to test it on a random input array containing various random strings, using a Python compiler online.
    max_len = len(max(inputArray, key = len))
    # Step 3: Now, we go over all strings inside the input array checking if their individual length is equal to the
    # maximum length value defined in step 2. If it is, then we append the respective string to the "max_arr" defined above.
    for i in inputArray:
        if len(i) == max_len:
            max_arr.append(i)
    # Step 4: We conclude by returning the max_arr.
    return max_arr
