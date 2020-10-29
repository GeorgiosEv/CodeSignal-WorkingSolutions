def addBorder(picture):
    new_pic = []
    border = ""
    pic_len = len(picture)
    for i in range(0, len(picture[0])+2):
        border += "*"
    new_pic.append(border)
    for i in range(0, pic_len):
        new_pic.append("*" + picture[i] + "*")
    new_pic.append(border)
    return new_pic