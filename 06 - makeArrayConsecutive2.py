def makeArrayConsecutive2(statues):
    stat_arr = sorted(statues)
    i = stat_arr[0]
    result = list()
    while  i != stat_arr[-1]:
        i += 1
        if i not in stat_arr:
            result.append(i)
        else:
            continue
    return len(result)
