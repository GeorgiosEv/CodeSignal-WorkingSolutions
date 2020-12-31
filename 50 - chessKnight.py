import itertools as t
def chessKnight(cell):
    knight_dir = list(t.permutations([1,2,-1,-2],2))
    knight_dir1 = []
    valid_moves = 0
    for i in range(len(knight_dir)):
        if sum(knight_dir[i]) != 0:
            knight_dir1.append(knight_dir[i])
    for x,y in knight_dir1:
        if (97 <= ord(cell[0]) + x <= 104) and (1 <= int(cell[1]) + y <= 8):
            valid_moves += 1
    return valid_moves