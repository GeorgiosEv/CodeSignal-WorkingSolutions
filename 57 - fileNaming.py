def fileNaming(names):
    if names == []:
        return []
    new_names = []
    for name in names:
        if name not in new_names:
            new_names.append(name)
        else:
            for i in range(1,1000):
                new_name = name + '(' + str(i) + ')'
                if new_name not in new_names:
                    new_names.append(new_name)
                    break
    return new_names 