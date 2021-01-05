"""Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size.
Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the
previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of
additional statues needed.

Example:
For statues = [6, 2, 3, 8], the output should be makeArrayConsecutive2(statues) = 3.
Ratiorg needs statues of sizes 4, 5 and 7."""
def makeArrayConsecutive2(statues):
    # Step 1: We begin by creating a new array called "stat_arr", which will accommodate the sorted version of the original "statues" array.
    stat_arr = sorted(statues)
    # Step 2: Furthermore, we use the first element of the sorted array as our index (that will be used in the following steps).
    i = stat_arr[0]
    # Step 3: We create an empty list called "result" to store our (numbered) missing statues.
    result = list()
    # Step 4: We initiate a while-loop with the condition that the index from Step 2 is not equal to the last (hence largest) entry of
    # the stat_arr. You must make sure that you add the "incrementation by 1" part to make the while loop proceed to the next element.
    while  i != stat_arr[-1]:
        i += 1
    # Step 5: Here, using a simple if statement, we examine whether the i-th (integer) element is included in the stat_arr.
    # If it is not, we append it to the result list. Otherwise, the loop continues.
        if i not in stat_arr:
            result.append(i)
        else:
            continue
    # Step 6: Finally, we return the length/size of the result list, i.e. the number of our "missing" statues.
    return len(result)
