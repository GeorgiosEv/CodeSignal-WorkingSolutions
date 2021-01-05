def growingPlant(upSpeed, downSpeed, desiredHeight):
    day_count = 0
    height = 0
    while height <= desiredHeight:
        height = height + upSpeed
        day_count += 1
        if height < desiredHeight:
            height = height - downSpeed
        else:
            return day_count