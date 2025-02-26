#FEB 25, DAY 1


""" 
    Today I will show you guys important hints for drawBoard() as well as some hints for 
    dropPiece()
"""

BOARD = [ 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],        
    ]


print(BOARD)
#^ This looks stupid

"""
    Natural inclination is to do a for loop 
"""
 
 
"""
for row in BOARD:
    print(row)
    
    
""" 
#This is not quite right either


""" 
    print() technically does two things 
    
    1) It prints the thing in the parentheses to the terminal 
    2) It returns the new line 
"""

print(1)
print()
print(2)

"""
    So really what the print statement does is 
    
    prints message \n into the terminal
    
    
    \n is an example of an escape sequence, they are special characters that you can put in strings that
    changes the output
    
    \n - new line 
    
    message\n 
    
    
    we can change what goes at the end of a print statement, rather than \n
    
    print(<message>)
""" 

""" 
    print() actually has two parameters that we care about
    
    print(<message>,end = "" )
    
    end = is how we change what is put at the end of our message
    
    by default end = \n
    
    but we can change it to something else
"""

print("X", end ="|") #its now no longer X | \n its just X |
print()

for char in BOARD[0]:
   pass
    
""" 
    What you should do for draw board is a nested for loop
    
    The theme in lab 6 is nested for loops in general, pretty much every single function except switch player
    is going to end up being nested for loops
"""

for row in BOARD: 
    #TODO implement drawboard
    for char in row:
         print(char, end = "|")
    
    
#Thats drawboard() 

"""
    Switchplayer can be done in two lines 
    If you look in my completed def main()
    
    switchplayer returns either X or O depending on
    what current player is
    
    so we dont need to keep track of player 1 and player 2
    
    we only need to keep track of the current player and flip it
    when their turn is over 
"""

"""
    Tic Tac Toe allows players to put X's or O's in any xy coordinate pair on the board. This is not 
    how connect 4 
    
    The question is, how do we implement dropPiece() in such a way that it accounts for gravity 
    
    dropPiece(board,player,column) #three parameters
    
    Board[row][column]
    
    what you need to do for dropPiece() is you need to go down the column
    
    Board[0][column]
    Board[1][column]
    Board[2][column]
    Board[...][column]
    
    so you go down the column up until three cases happen
    
        1) Board[0][column] < this has to be equal to a 0 
            Reason: If it wasn't the column would be full, so you need to make them choose again 
        2) Board[last][column] < check if this is equal to 0, if it is, replace with current player
        3) Board[curr][column] = not 0, then you need to replace board[curr-1][column]
"""

BOARD = [ 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             ["X",0,0,0,0,0,0],        
    ]

"""
    Board[curr-1][column] is the piece ABOVE the last tile that is full 
    
    x = 0 
    while board[x][column] = 0 
        if it works, incerement x by 1
    as soon as the while loop exits
    replace board[x-1][column]
    
    This is naive because it doesn't check 1 and 2
    
    one more thing about drop piece:
        it should return true if the piece dropped successfully
        return false if it doesnt drop 
        
        so you should have a second while loop inside def main INSIDE your first while loop to correspond
        to whether or not drop piece is successful.
"""

#Today just finish drawBoard() and switchPlayer()


#FEB 26, DAY 2
"""
Today you should be working on dropPiece() and start working on checkWinner() if you finish dropPiece() today. 

In tictactoe all you have to give is a (row,column) pair and then the piece gets placed at that coordinate. Connect 4 is different because
all you're doing is choosing a column and then the piece drops to the first available slot in that column 

 dropPiece(board,player,column)
 
 board - game board
 player - curren t player
 column - is the column the player chooses in main() - a number
 
 board[][column]
 
 what you need to do:
    - check to see if board[0][column] == 0
        if it is, you continue the function
        if its not, return False
 
 
    - create a variable x = 0
    - while loop over x < 6 
        - if board[x][column] == 0 
            - increment x
        - else:
            - break
    - after the while loop you should have an (x,column) pair that will be the piece that is exactly one MORE than the first available slot
    - board[x-1][column] = player
    - return true
    

"""


""" 
Check Winner: 

Connect 4 is just a tictactoe game over a 6x7 board. You want 4 in a row but on a larger board

             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],  
             
What you need to do is do nested forloops that give x,y pairs over all of the pieces on the board

             [X,X,X,X,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],  
             
For horizontal victories, you need to check

currentpos, currentpos + 1, currentpos + 2, currentpos + 3 in the x direction

             [X,0,0,0,0,0,0],
             [X,0,0,0,0,0,0],
             [X,0,0,0,0,0,0],
             [X,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],  

left diagonal is +x +y

right diagonal is different

             [0,0,0,X,0,0,0],
             [0,0,X,0,0,0,0],
             [0,X,0,0,0,0,0],
             [X,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],  
             
right diagonal is +x -y


             [0,0,0,0,X,X,X], X <= error here
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],  
             
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [X,0,0,0,0,0,0],
             [X,0,0,0,0,0,0],
             [X,0,0,0,0,0,0],  
              X <= error
              
             [0,0,X,0,0,0,0],
             [0,X,0,0,0,0,0],
             [X,0,0,0,0,0,0],
   error => X[0,0,0,0,X,0,0],
             [0,0,0,0,0,X,0],
             [0,0,0,0,0,0,X],  
                            X <= error         
             
        range(len(board))
        range(len(board)-3)
        range(len(board[0]-3))
        range(3,len(board[0]))              
        range(3,len(board))
        
        you need to change the range for almost ALL of your for loops, for diagonals, BOTH for loops will have different ranges  
"""




