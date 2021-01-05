"""Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example:
For inputArray = [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product."""
def adjacentElementsProduct(inputArray):
    # Step 1: Initially, define an empty array where we will store the products of adjacent elements from the input array.
    ArrayEnd = []
    # Step 2: Using a for-loop, we go over all entries of the input array, calculating the products of adjacent elements
    # and appending them to the empty array from step 1.
    for i in range(len(inputArray) - 1):
        ArrayEnd.append(inputArray[i]*inputArray[i+1])
    #Step 3: We seek the largest entry in "ArrayEnd" from step 1, using the max() function.
    maximum = max(ArrayEnd)
    return maximum
