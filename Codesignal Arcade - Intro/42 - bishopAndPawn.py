def bishopAndPawn(bishop, pawn):
    if ord(bishop[0]) == ord(pawn[0]):
        return False
    else:
        bishop_elm = ord(bishop[0])+int(bishop[1])
        pawn_elm = ord(pawn[0])+int(pawn[1])
        return (bishop_elm + pawn_elm)%2 == 0