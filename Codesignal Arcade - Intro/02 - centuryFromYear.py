"""Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - 
from the year 101 up to and including the year 200, etc.

Example:
- For year = 1905, the output should be centuryFromYear(year) = 20;
- For year = 1700, the output should be centuryFromYear(year) = 17. """
def centuryFromYear(year):
    # We begin by getting the INTEGER quotient of the division of the year given by 100.
    # This will give us the first two digits, which would be the century.
    cen = int(year/100)
    # However, we should keep in mind that we refer to years between e.g. 1701 - 1800
    # as the "18th century". Hence, we implement a while loop, where the condition is
    # that the year is a positive integer (which is always true). If the remainder of the
    # division of the year by 100 is 0, then the two first digits of the division represent
    # the century. Otherwise, if the remainder is non-zero, the century is found by adding 1
    # to the result of the division (i.e. "cen").
    while year >= 1:
        if year % 100 == 0:
            return year / 100
        else:
            return cen + 1
