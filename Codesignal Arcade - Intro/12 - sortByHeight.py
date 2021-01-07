"""Some people are standing in a row in a park. There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
People can be very tall!

Example:
- For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]."""
def sortByHeight(a):
    # Step 1: We begin by creating a counter, starting from 0, that will be used in the subsequent for-loop.
    j = 0
    # Step 2: We also create a new array, called "a_sort", where we sort (in ascending order) all elements of the given array "a"
    # that are not "trees" (i.e. do not have a value of -1).
    a_sort = sorted([i for i in a if i != -1])
    # Step 3: By implementing a for-loop, we investigate all elements of the given array "a" (NOT a_sort!) and check:
    # if the element i in array "a" is equal to -1, the for-loop continues. Otherwise, the element i in array "a" should be
    # the same as element j in array "a_sort" (starting from 0 index, as defined in step 1).
    # You can think of it as working through elements of array "a", disregarding the "trees" (-1s) and sorting the rest
    # of the elements in ascending order (as in a_sort).
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i] = a_sort[j]
            j += 1
    # Step 4: The final step is the return of the modified array "a".
    return a
