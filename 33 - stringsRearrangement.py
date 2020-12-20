from itertools import permutations as p
def stringsRearrangement(inputArray):
    p_list = list(p(inputArray))
    for i in range(len(p_list)):
        count1 = 0
        for j in range(len(p_list[0])-1):
            count2 = 0
            for k in range(len(p_list[0][0])):
                if p_list[i][j][k] != p_list[i][j+1][k]:
                    count2 +=1
            if count2 == 1:
                count1 +=1
        if count1 >= (len(p_list[0])) - 1:
            return True
    return False