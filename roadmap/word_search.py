"""
Given an M x N grid of characters `board` and a string 
`word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be 
used more than once.

Note: In other words, there are 4 valid movements
available: up, down, left, right.
And there are no self loops, or repeating steps that 
lead to the same coordinates(cell)

Something trivial to think about is the case where there
are consecutive duplicate characters in the word we are
searching for.

There are two options to prevent this situation from happening:
1. Use a set data structure to keep track of coordinates that 
have been traversed
2. Similar to the islands problem, every successful find, we can
replace the character that allowed us to move forward with a diff-
-erent character.

In order to solve this problem:
A grid must be traversed, meaning it's rows and columns
must be registered, and the grids bounds must be respected


"""
def find_word(board,word,i,j,char):
    if char == len(word):
        return True
    if (i >= 0 and i < len(board)) and (j >= 0 and j < len(board[i])):
        if board[i][j] == word[char]:

            return find_word(board, word, i + 1, j, char + 1) or find_word(board,word, i -1,j, char + 1) or find_word(board,word,i, j + 1, char + 1) or find_word(board,word, i, j -1, char + 1)
        else:
            return False
    


    
        


def exist(board,word):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == word[0]:
                a = find_word(board,word, row, col, 0)
                if a == True:
                    return True
    return False
