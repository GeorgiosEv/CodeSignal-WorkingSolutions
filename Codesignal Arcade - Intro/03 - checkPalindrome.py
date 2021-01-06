"""Given the string, check if it is a palindrome.

Example:
- For inputString = "aabaa", the output should be checkPalindrome(inputString) = true;
- For inputString = "abac", the output should be checkPalindrome(inputString) = false;
- For inputString = "a", the output should be checkPalindrome(inputString) = true."""
def checkPalindrome(inputString):
    # Step 1: We turn all letters in our given string into lower case.
    inp = inputString.lower()
    # Step 2: Also, we discard all space between words or letters.
    # It is important to store the result in the same variable as in step 1.
    # Think of it as only dealing with discarding the spaces.
    inp = inp.replace(" ","")
    # The first two steps help us end up with a long, uniform (in terms of letter size) string.
    # Step 3: We define a variable called "reverse" as the reversed counterpart of the input string.
    reverse = inp[::-1]
    # Step 4: The outcome will be "True" only if the original string and its reversed counterpart are the same.
    if (reverse == inp):
        return True
    else:
        return False
