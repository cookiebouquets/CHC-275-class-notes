""" 
    The last new thing we are going to cover before Lab 6 are 2D Lists and how to manipulate them
"""

"""
    Lab 6: connect 4 thats gonna be assigned tomorrow as long as i finish before then (which i will)
    
    First thing: Review on lists
    
    Recall: Lists are an ordered collection of variables

    How do we make a list?
    
"""

mylist = []

"""
    square brackets, put things in there if you want.
    
    Lists carry certain pieces of information with them:
        - length of list
        - range of indices
        - the data itself 
        
    length using len(name of list)
    
    indices: 0-len(list)-1
    
"""

mylist = [6,3,0]
         #0,1,2
         
print(mylist[0])

"""
    We pull things out of the list using the square brackets operator
    
    additionally, how do we add things to the list? 
    
    .append(data)
"""

mylist.append(4)
print(mylist)

""" 
    Lists can be of mixed data type 
    
    In other programming languages, specifically like Java, c++ <= these are strongly typed
    where you delcare the data type beforehand 
    
    but for python, we can store anything we want. 
"""

mylist.append("Hello")

print(mylist)

"""
    We can access data using square brackets, we can add things using .append, the last natural operation
    we care about are looping statements
"""

for item in mylist:
    print(item)
    
"""
    So to get the index specifically we had to use the range() function

    range() -> returns a list of all of the integers between 0 and the length of the list
"""

for x in range(len(mylist)):
    print(x)
    
    
""" 
    So how exactly are we going to augment our lists? We learned dictionaries last lab which 
    involved key-value pairs, but what if we did lists of lists? 
    
    Thought question: a 2d-list is basically just a table or grid
        -tic tac toe (game boards)
        - mancala 
        - spreadsheets 

    being able to confidently manipualate 2d lists gives us effectively the power to make any 2d game 
    we want, or do any sort of spreadsheet analysis 
"""


"""
    how do we initialize a 2dlist?
    
"""

board = [[]] #this is an empty 2d list

print(board)

""" 
    Weird quirks about 2dlists
    
    In other languages, 2dlists have a fixed size for rows
"""

board = [[1,2,3],[4,5,6,7]]

for row in board:
    print(row)

"""
    python does nothing in order to make the list a fixed size <= you have to be very careful
    with appends, len() removing things, etc. Anything that manipulates the lengths of lists traditionally
    
    you have to be careful with. 
    
    2nd quirk. 
    board = [
    [0000],
    [0000],
    [0000]
    ]
    
    going across rows is incredibly easy, but going across columns is considerably difficult 
    
    How do we get stuff out of a 2dlist?
    
    mylist[row][column]
"""

board = [
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]
]

print(board[1][1])

""" 
    Square brackets give stuff from lists like usual.
    
    So for rows: looping works exactly the same 
"""

for row in board:
    print(row)
    
for row in board:
    print(row[1])
    
""" 
    Columns are not nearly as obvious 
    
    board = [
    [0000],
    [0000],
    [0000]
    ]
    
    So the easiest way in my opinion (and best practice usually) is to pull out all of indices overall
"""

for x in range(len(board)):
    for y in range(len(board[0])):
    #2D lists start from the top left. 
        print(f"({x},{y})")
        
"""
    The real example we want to look at in this class. 
"""

player1 = "X"
player2= "O"
board = [[0,0,0],
         [0,0,0],
         [0,0,0]
         ]

"""
    How do you win in tictactoe? Three in a row in columns, rows, or diagonally
"""

def check_winner(board,player):
    #return type: none (we're going to print the winner)
    #player is either X or O
    #Row victories
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            print(f"player {player} won with a row victory")
        
    
board = [
         [0,0,0],
         [0,0,0],
         ["X","X","X"]
         ]

check_winner(board,player1)
    
def check_winner(board,player):
    #return type: none (we're going to print the winner)
    #player is either X or O
    
    #Row victories
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            
            print(f"player {player} won with a row victory")
            
            
    #Column Victories
    for x in range(len(board)):
       if board[0][x] == player and board[1][x] == player and board[2][x] == player:
           print(f"Player {player} won with a column victory")
           


board = [
         ["X",0,0],
         ["X",0,0],
         ["X",0,0]
         ]       


check_winner(board,player1)


    
def check_winner(board,player):
    #return type: none (we're going to print the winner)
    #player is either X or O
    
    #Row victories
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            
            print(f"player {player} won with a row victory")
            
            
    #Column Victories
    for x in range(len(board)):
       if board[0][x] == player and board[1][x] == player and board[2][x] == player:
           print(f"Player {player} won with a column victory")
           
    #left diagonal       
    if board[0][0] == player and board[1][1] == player and board [2][2] == player:
        print(f"Player {player} won with a diagonal victory" )
        
    #right diagonal
    if board[0][2] == player and board[1][1] == player and board [2][0] == player:
        print(f"Player {player} won with a diagonal victory" )

board = [
         ["X",0,0],
         [0,"X",0],
         [0,0,"X"]
         ]       

check_winner(board,player1)

"""
    Lab released tomorrow
"""