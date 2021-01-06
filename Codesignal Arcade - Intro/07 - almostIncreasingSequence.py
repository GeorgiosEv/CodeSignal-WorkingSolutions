"""Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence
by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
Sequence containing only one element is also considered to be strictly increasing.

Example:
- For sequence = [1, 3, 2, 1], the output should be almostIncreasingSequence(sequence) = false.
There is no one element in this array that can be removed in order to get a strictly increasing sequence.
- For sequence = [1, 3, 2], the output should be almostIncreasingSequence(sequence) = true.
You can remove 3 from the array to get the strictly increasing sequence [1, 2].
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3]."""
def almostIncreasingSequence(sequence):
    # Step 1: We begin by assigning the length of the given sequence to the variable n.
    n = len(sequence)
    # Step 2: By definition, if the sequence contains up to 1 elements, it is considered to be strictly increasing.
    if n <= 2:
        return True
    # Step 3: We set up two counters, namely c1 and c2, so that we count how many elements should be removed.
    # NOTE THAT c1 refers ONLY to adjacent elements whilst c2 refers to elements just before and just after the i-th element.
    c1 = 0
    c2 = 0
    # Step 4: This for-loop (and its content) is a tricky part. The range of the for-loop starts from 1 and goes all the way to (n-1)th element.
    # BE CAREFUL: We set n-1 to avoid getting our index out of range in the second if statement inside the for-loop.
    for i in range(1, n-1):
    # Step 5: If the element prior to the index element i has a bigger value than i, we add 1 hit to the first counter.
        if sequence[i-1] >= sequence[i]:
            c1 += 1
    # Step 6: If the element just before the index element i has a bigger value than the element just after i,
    # we add 1 hit to the second counter.
        if sequence[i-1] >= sequence[i+1]:
            c2 += 1
    # Step 7: If the element two places to the left of the index element i has a bigger value than the element prior to i,
    # we add 1 hit to the first counter.
    if sequence[n-1] <= sequence[n-2]:
        c1 += 1
    # Step 8: If BOTH of the counters have up to 1 hit (that means 0 or 1 EACH), then the sequence is almost increasing.
    if c1 <= 1 and c2 <= 1:
        return True
    else:
        return False
