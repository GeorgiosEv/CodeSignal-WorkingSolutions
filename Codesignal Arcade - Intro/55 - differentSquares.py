def differentSquares(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sq_arr = []
    sq_count = 0
    for i in range(rows-1):
        for j in range(cols-1):
            sq_2x2 = [ matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1] ]
            if sq_2x2 not in sq_arr:
                sq_arr.append(sq_2x2)
                sq_count += 1
    return sq_count