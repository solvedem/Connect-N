# Checks horizontally for wins
#
import numpy as np

def check_horiz(board_,player_num, n):
    board_ = board_
    max_row = len(board_)
    max_column = len(board_[0])
    
    for row in range(max_row):
        count = 0
        for col in range(max_column):
            value = board_[row][col]
            if value == player_num:
                count += 1
            if count >= n:
                return True
            if value != player_num:
                count = 0
                
    return False


# Checks vertically for wins
#
def check_vert(board_, player_num, n):
    max_row = len(board_)
    max_column = len(board_[0])
    
    for col in range(max_column):
        count = 0
        for row in range(max_row):
            value = board_[row][col]
            if value == player_num:
                count += 1
            if count >= n:
                return True
            if value != player_num:
                count = 0
    return False

# Checks diagonally for wins
#
def check_diagonals(board_m,player_num, n):
    max_row = len(board_m) # height
    max_column = len(board_m[0]) # width 
    x = int((max_row - 4) * -1)
    y = int(max_column / 2. + 1)
    if max_column == 4:
        y = 1

        
    if max_column == 5:
        y = 2
    board_ = board_m[:]
    np_board = np.array(board_)
    diagonal_list =[]

    if max_column == 4:
        diagonal_list.append(np.diagonal(np_board))
    else:
        for i in range(x,y):
            diagonal_list.append(np.diagonal(np_board,i))

    np_board_reversed = []
    for list_ in board_:
        listx = list_[:]
        listx.reverse()
        np_board_reversed.append(listx)

    if max_column == 4:
        diagonal_list.append(np.diagonal(np_board))
    else:
        for i in range(x,y):
            diagonal_list.append(np.diagonal(np_board_reversed,i))

    for j in diagonal_list:
        count = 0
        for k in j:
            if k == player_num:
                count += 1
            if count >= n:
                return True
            if k!=player_num:
                count=0
            
    return False


def check_for_wins(board_,pn, n):
    return check_horiz(board_,pn, n) or check_vert(board_,pn, n) or check_diagonals(board_,pn, n)
