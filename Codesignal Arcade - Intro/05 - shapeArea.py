def shapeArea(n):
    if n == 0:
        return None
    elif n == 1:
        return 1
    elif n > 1:
        result = (n ** 2) + ((n - 1) ** 2)
        return result