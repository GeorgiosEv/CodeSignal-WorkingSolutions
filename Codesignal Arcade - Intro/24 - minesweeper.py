def minesweeper(matrix):
    row = len(matrix)
    col = len(matrix[0])
    def neighbouring_squares(i,j):
        return (sum(matrix[x][y]    for x in range(i-1,i+2) if 0 <= x < row
                                    for y in range(j-1,j+2) if 0 <= y < col
                                    if i != x or j != y))
    return [[neighbouring_squares(i,j) for j in range(col)] for i in range(row)]