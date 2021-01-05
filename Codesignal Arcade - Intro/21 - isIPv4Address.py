def isIPv4Address(inputString):
    str_split = inputString.split(".")
    count = 0
    if len(str_split) != 4:
        return False
    for i in range(0,4):
        if str_split[i] == "" or str_split[i] == "00" or str_split[i] == "01":
            return False
        if re.search('[a-zA-Z]', str_split[i]):
            count += 1
            if count > 0:
                return False
        if str_split[i].isnumeric():
            if int(str_split[i]) < 0:
                return False
            if int(str_split[i]) > 255:
                return False
    return True