def validTime(time):
    time_split = time.split(":")
    if 00 <= int(time_split[0]) <= 23 and 00 <= int(time_split[1]) <= 59:
        return True
    return False