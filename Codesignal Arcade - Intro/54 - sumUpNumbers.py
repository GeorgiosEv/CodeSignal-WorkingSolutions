def sumUpNumbers(inputString):
    def getNumbers(str):
        nums = re.findall(r'[0-9]+', str)
        return nums
    numbers = getNumbers(inputString)
    total = 0
    for i in numbers:
        total += int(i)
    return total