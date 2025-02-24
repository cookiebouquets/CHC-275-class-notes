#FEB 20, DAY 5 

""" 
By now you should have drawBoard() and switchPlayer() done. Today you should try to get dropPiece() done.

    1. dropPiece has 3 parameters: board,player,column
    2. we only ask for the column because the piece should fall to the bottom most place in that column
    3. a player shouldnt be able to drop a piece if the column is full 
"""

BOARD = [ 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],        
    ]

""" 
    BOARD[x][y]
    BOARD[_][column]
    
    How do we check the top most piece in the column 
    
    If you don't remember, the top left piece of the grid is (0,0)
    
    BOARD[0][column]
    
    2nd question: the empty piece is what? 0
    
    all you need to do, is check if BOARD[0][column] = 0 if its not, you should tell them to try again
    
    3rd question: So if we know overall we should be checking for 0s, and we're a given a column how do we
    get all of the pieces in the column? 
    
    BOARD[_][Column]
    
    while loop over the first index. Check if the current piece is 0. When its not, you should have a 
    
    (x,column) pair and you should set
    
    board[x][column] = current player 
"""

#Feb 24, Day 6

"""
    Some important things to remember: Board is a 6 x 7 grid
"""

print(BOARD[8][5])

