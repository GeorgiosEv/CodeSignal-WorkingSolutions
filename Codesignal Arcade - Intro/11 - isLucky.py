"""Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky
if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.

Example
- For n = 1230, the output should be isLucky(n) = true;
- For n = 239017, the output should be isLucky(n) = false."""
def isLucky(n):
    # Step 1: We begin by creating an empty array, called "digits_of_n",
    # where we will store the digits of the given number n, as individual elements.
    digits_of_n = []
    # Step 2: We also create a new variable, called "summ" (from summation), and set its value to zero.
    # It will be useful in one of the later steps.
    summ = 0
    # Step 3: I have personally seen this while-loop trick being used to split numbers into their individual digits.
    # As it will take quite a long text to explain this comprehensively, I'd suggest you use the print() function in each
    # step to see what how each of these steps works. The important thing to mention is the "appending" step where each
    # digit, where each digit is stored as an elememnt in "digits_of_n" array.
    while n > 0:
        rem = n % 10
        digits_of_n.append(rem)
        n = int(n / 10)
    # Step 4: Furthermore, we implement a for-loop that goes over all elements inside the "digits_of_n" array, one by one.
    # If the element's index is up to the middle of the length of the array, we add the element's numeric value to "summ".
    # Otherwise, we subtract it. NOTE THAT for arrays of even length, you can find the "middle" by dividing the length by 2
    # (i.e. for arrays of length 4, the 2nd element is the "middle), whilst for array of odd length, the "middle" is the
    # element having equal numbers of elements on both its sides.
    for i in range(len(digits_of_n)):
        if i < len(digits_of_n)/2:
            summ += digits_of_n[i]
        else:
            summ -= digits_of_n[i]
    # Step 5: Finally, we check if the summation is zero or not. If the sum is zero, then the ticket number is lucky,
    # according to the definition of the exercise.
    if summ == 0:
        return True
    return False
