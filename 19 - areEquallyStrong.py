def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    personal_max = max(yourLeft, yourRight)
    friend_max = max(friendsLeft, friendsRight)
    sum1 = yourLeft + yourRight
    sum2 = friendsLeft + friendsRight
    if sum1 == sum2 and personal_max == friend_max:
        return True
    return False