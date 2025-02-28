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
    
    If you try to access data outside of the list indices, python is not going to let you.
    
    So the algorithm for check winner is basically the same thing as tic tac toe (except its a 4x4 square)
    
    But the problem is, the board is a 6x7 grid. So the question is, how do we check 4x4 winners on a 6x7 grid?
    The answer to this is to do nested forloops. So every condition can by checked with a 
    
    for x in _
        for y in _ 
        
    structure
    
    There's one problem though, if you remember from tic tac toe where we checked
    
    board[x][y] board[x+1][y] and board[x+2][y], we're gonna have a compilation error if we do a for loop
    over the whole board and check those same indices 
    
    
    so you're gonna go out of bounds if you check board[5+dx][y]
    
    and same for board[x][6+dy] 
    
    So the thing about range is you can specify the endpoint to be length-some number
    
             [x,x,x,x,0,0,0],
             [0,x,x,x,x,0,0],
             [0,0,x,x,x,x,0],
             [0,0,0,x,x,x,x],
             [0,0,0,0,x,x,x]x, <- compilation error 
             [0,0,0,0,0,0,0],       
             
             

    so all you need to do is rather than check the whole row, you only need to do a for loop up until the 4th
    element

    Vertical victories
    
     [x,0,0,0,0,0,0],
     [x,x,0,0,0,0,0],
     [x,x,x,0,0,0,0],
     [x,x,x,x,0,0,0],
     [0,x,x,x,0,0,0],
     [0,0,x,x,0,0,0],
            x 
            ^ compilation error  
            
            
    So really the problem with check winner is what to the range() function, and if you think about
    what indices will screw you over, you just stop at the length minus the part that kills you
"""

print(BOARD[8][5])

#FEB 26, DAY 2

""" 
    We should be just about done the lab now - final touches 
"""

#FEB 28, DAY 4 (Last day of Lab 6)

""" 
            (0,0)
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0], 
             
            board[0][0], board[0][1], board[0][2], board[0][3]
            
            board[row][column] 
            
            row: nothing
            column: + 
            
            (0,0)
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0], 

             board[0][0], board[1][0], board[2][0], board[3][0]
            
            board[row][column] 
            
            row: +
            column: nothing 
            
            (0,0)
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0], 
            
        board[0][0], board[1][1], board[2][2], board[3][3]
        
        board[row][column] 
        
        row: +
        column: +
        
        
                   (0,3)
             [0,0,0,X,0,0,0],
             [0,0,X,0,0,0,0],
             [0,X,0,0,0,0,0],
             [X,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0], 
             
             (0,3)
             (1,2)
             (2,1)
             (3,0)
             
         board[row][column]  
         
         row: +
         column: -  
            
"""