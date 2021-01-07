"""Several people are standing in a row and need to be divided into two teams. The first person goes into team 1,
the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers,
where the first element is the total weight of team 1, and the second element is the total weight
of team 2 after the division is complete.

Example:
- For a = [50, 60, 60, 45, 70], the output should be alternatingSums(a) = [180, 105]."""
def alternatingSums(a):
    # Step 1: We begin by creating an array, called "alt_sum", that includes only two elements of value 0.
    alt_sum = [0, 0]
    # Step 2: Moreover, we define the variable "length", which is the numerical value of the length of input array a.
    length = len(a)
    # Step 3: Starting from the first element of input array "a" and working all the way through its length,
    # we check whether the element's index is even or odd. If the element i is even, we add its value to the
    # first element of the "alt_sum" array, whilst if it is odd we add it to the second element.
    for i in range(0, length):
        if i % 2 == 0:
            alt_sum[0] += a[i]
        else:
            alt_sum[1] += a[i]
    # Step 4: To conclude, we return the alt_sum array.
    return alt_sum
