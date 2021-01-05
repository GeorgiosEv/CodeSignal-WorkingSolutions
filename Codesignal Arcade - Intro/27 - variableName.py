def variableName(name):
    str_name = [i for i in str(name)]
    non_acc_chars = [" ", ">", "<", ":", "-", "|", ".", ",", "!", "[", "]", "'", "/", "@", "#", "&", "%", "?", "*"]
    if str_name[0] in str([0,1,2,3,4,5,6,7,8,9]):
        return False
    for j in range(len(str_name)):
        if str_name[j] in non_acc_chars:
            return False
    return True