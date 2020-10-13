def centuryFromYear(year):
   cen = int(year/100)
   while year >= 1:
        if year % 100 == 0:
            return year / 100
        else:
            return cen + 1