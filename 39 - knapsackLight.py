def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 > maxW and weight2 > maxW and weight1 + weight2 > maxW:
        return 0
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if value1 < value2:
        if weight2 > maxW:
            return value1
        else:
            return value2
    if value2 < value1:
        if weight1 > maxW:
            return value2
        else:
            return value1
    if value1 == value2:
        if weight1 > maxW:
            return value2
        else:
            return value1
