"""Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.

Example:
- For inputString = "(bar)", the output should be reverseInParentheses(inputString) = "rab";
- For inputString = "foo(bar)baz", the output should be reverseInParentheses(inputString) = "foorabbaz";
- For inputString = "foo(bar)baz(blim)", the output should be reverseInParentheses(inputString) = "foorabbazmilb";
- For inputString = "foo(bar(baz))blim", the output should be reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim"."""
def reverseInParentheses(inputString):
    # Step 1: We create a for-loop that goes over all elements of the input string. If element i is an opening bracket, then i
    # is defined as "start". In a similar manner, if element i is a closing bracket, i is defined as "end". NOTE THAT
    # if you write it as "i = start" or "i = end", an error will pop up (tested) as you would have not defined any variables
    # under those names, whilst the way that is written now you define as "start" and "end" elements that are
    # "(" and ")" respectively.
    for i in range(len(inputString)):
        if inputString[i] == "(":
            start = i
        if inputString[i] == ")":
            end = i
    # Step 2: Furthermore, we apply the function inside itself and concatenate the individual modified parts:
    # the part of the input string up to (and NOT including) the "starting" point (i.e. opening bracket) is left intact.
    # The same goes for the part of the input string one element AFTER the "ending" point (i.e. closing bracket) 
    # till the actual end of the input string. The part of the input string that is located one element after 
    # the starting point ("start"+1 included) and up to the "ending" point NOT included is reversed.
            return reverseInParentheses(inputString[:start] + inputString[start+1:end][::-1] + inputString[end+1:])
    # Step 3: To conclude, we return the modified input string.
    return inputString
