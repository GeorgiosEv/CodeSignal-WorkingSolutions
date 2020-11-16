def boxBlur(image):
    def pixels(matrix, i, j):
        summ = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                summ += matrix[x][y]
                mean = summ // 9
        return mean

    output = []
    row = len(image)
    col = len(image[0])
    for i in range(1, row - 1):
        arr = []
        for j in range(1, col - 1):
            arr.append(pixels(image, i, j))
        output.append(arr)
    return output