"""After becoming famous, the CodeBots decided to move into a new building together.
Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted!
Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return
the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example:
For
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
the output should be matrixElementsSum(matrix) = 9.

example 1: There are several haunted rooms, so we'll disregard them as well as any rooms beneath them.
Thus, the answer is 1 + 5 + 1 + 2 = 9. (PICTURE PROVIDED AT:WWW.CODESIGNAL.COM)

For
matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]
the output should be matrixElementsSum(matrix) = 9.

example 2:
Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it).
Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9. (PICTURE PROVIDED AT:WWW.CODESIGNAL.COM)"""
def matrixElementsSum(matrix):
    # Step 1: We begin by defining the number of rows and columns inside our given matrix.
    # You can conceive the number of rows as the number of nested arrays inside the main array and
    # the number of columns as the number of elements in the first nested array.
    # Feel free to convince yourself that this is the case by referring to the examples of matrices shown above.
    rows = len(matrix)
    cols = len(matrix[0])
    # Step 2: Furthermore, create a new variable called "summ" (from summation) and set it equal to zero.
    # It will be used in the following for-loop.
    summ = 0
    # Step 3: Here we have an unusual for-inside-a-for loop (compared to the one that we usually observe when dealing with matrices).
    # As we are interested in the position of elements in columns (elements BELOW 0s), the outside for-loop works across all columns
    # whilst the nested for-loop works across all rows.
    for j in range(cols):
      for i in range(rows):
    # Step 4: If, while counting, the loop meets an element whose value is zero, the counting stops.
    # Otherwise, it continues counting, each time adding the value of the i-th / j-th element to the "summ" variable, defined in step 2.
        if matrix[i][j] == 0:
            break
        summ += matrix[i][j]
    # Step 5: Therefore, we end up with the total sum of non-zero elements whose position in a column is not
    # below an element of value zero.
    return summ
