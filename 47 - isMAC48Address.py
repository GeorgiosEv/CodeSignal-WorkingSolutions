def isMAC48Address(inputString):
    str_split = inputString.split("-")
    count = 0
    if len(inputString) != 17:
        return False
    if len(str_split) != 6:
        return False
    for i in range(0,6):
        if str_split[i] == "":
            return False
        if re.search('[a-zG-Z]', str_split[i]):
            count += 1
            if count > 0:
                return False
    return True