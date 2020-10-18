def matrixElementsSum(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    summ = 0

    for j in range(cols):
      for i in range(rows):
        if matrix[i][j] == 0:
            break
        summ += matrix[i][j]
    return summ