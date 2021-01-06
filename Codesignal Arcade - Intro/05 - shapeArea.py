"""Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the
(n - 1)-interesting polygon and appending 1-interesting polygons to its rim, side by side.
You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below. (PICTURE PROVIDED AT:WWW.CODESIGNAL.COM)

Example:
- For n = 2, the output should be shapeArea(n) = 5;
- For n = 3, the output should be shapeArea(n) = 13."""
def shapeArea(n):
    # Case 1: If the polygon is 0-interesting, it has an area equal to zero.
    if n == 0:
        return None
    # Case 2: If the polygon is 1-interesting, it has an area equal to one.
    elif n == 1:
        return 1
    # Case 3: If the polygon is n-interesting, it has an area equal to the sum of the square of n
    # and the square of n-1. A way that I thought of it (based on the picture provided) is the following: 
    # - n**2: Counted the number of the blue squares from the middle line upwards (INCLUDING the blue squares of the middle line).
    # - (n-1)**2: Counted the number of the blue squares from the middle line downwards (EXCLUDING the blue squares of the middle line).
    # Of course, you can easily check that the terms "upwards/downwards" could be inverted, without affecting the validity of your counting.
    elif n > 1:
        result = (n ** 2) + ((n - 1) ** 2)
        return result
