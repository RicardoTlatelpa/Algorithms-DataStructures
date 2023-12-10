'''
5.17 The soduku checker problem
Check whether a 9x9 2D array representing a partially completed
sodoku is valid. Specifically, check that no row, column, or 
3x3 2D subarray contains duplicates. A 0-value in the 2D array
indicates that entry is blank; every other entry is in
[1,9].
'''

def sodoku_checker(board):
    def validate_cell(row,col,val):
        # check if there are duplicates in the row and col
        for i in range(9):
            if i != row:
                r = board[i][col]
                if r == val:
                    return False
            if i != col:
                c = board[row][i]
                if c == val:
                    return False
        s_r = row // 3 
        s_c = col // 3
        for r in range(s_r,s_r+3):
            for c in range(s_c,s_c+3):
                if r != row and c != col:
                    if board[r][c] == val:
                        return False
        return True
    for i in range(9):
        for j in range(9):
            cell_val = board[i][j]
            if cell_val != 0:
                is_valid = validate_cell(i,j,cell_val)
                if(is_valid == False):
                    return False
    return True
