def chessBoardCellColor(cell1, cell2):
    cell1_elm = ord(cell1[0])+int(cell1[1])
    cell2_elm = ord(cell2[0])+int(cell2[1])
    return (cell1_elm + cell2_elm)%2 == 0