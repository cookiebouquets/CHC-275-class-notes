""" 
    The last new thing we are going to cover before Lab 6 are 2D Lists and how to manipulate them
"""

""" 
    Lab 6 is going to mancala. So if you know what the layout of mancala is, we need to have
    2dlists to be able to accurately make the board
    
   List Review:
   
   mylist = [] <= how to make a generic empty list
   
   same thing as a variable, the name doesnt really matter
   
   board = [] 
   
   How do we get something from a list? 
   
   
"""

mylist = [1,2,3]

""" 
    Lists have the values and the indices (index). The index is the position of the value at that list
"""

mylist = [1,2,3]
         #0,1,2
         
""" 
    Lists have their indices and their values. 
    
    What are the possible indices for a list?
    
    indices are 0 to length(list) - 1
    
    other things with lists:
    
    How do we add something to a list?  
    
    .append(value)
"""

mylist.append(4)

""" 
    What are the values of mylist and what are the indices? 
    
    Values = 1,2,3,4,"Hello"
    Indices = 0,1,2,3,4
    
    Lists can have mixed datatypes. In other programming languages, lists can only have one data type
    
    so for example in java, you can have a list of integers, strings, etc. 
    
    But in python you can havea list of multiple datatypes
"""

mylist.append("Hello")
print(mylist)


""" 
    You have to be careful with manipulating values because lists can have multiple datatypes 
    
    range() 

        -parameter: The list or object that has a length (a number)
        -return type: list of numbers from 0-the parameter 
        
    What is returned if I do 
    
    range(len(mylist))
"""

print(range(len(mylist)))

""" 
    len() 
    
        -parameter <- takes in a list
        -returns <- length of the list
        
        
    So that's all of the basic stuff about lists, how about 2D lists?
"""

"""
    Real world examples of 2dlists:
        - Spreadsheets 
        - Any table
        - Schedules
        - Directions
        - Game boards (chess boards, mancala boards, etc. )
        
        
    manipulating 2d lists is a skill we want to learn because 2d lists show up naturally everywhere
    
    
"""

""" 
    How do we make 2d lists?
"""

mylist = [[1,0,3,0]] #< This is how you make a 2d-list 

""" 
    Double square brackets makes a 2d list
    
    How do we manipulate these lists? 
    
    mylist is going to the outerlist 
    
    and mylist[0] is going to be the first row 
    
    
    000000
    000000
    000000
"""

mylist.append([0,0,0,0])
print(mylist)

print(mylist[0])
print(mylist[1])


#The first set of square brackets is going to end up being the rows
#The second set of square brackets is going to be the columns 


print(mylist[0][2])


#If you remember form lab 5 when we worked with nested dictionaries, the syntax
#is exactly the same as 2dlists 

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

print(board)
print("Printing Board")
for row in board:
    print(row)
    
""" 
    For loops work exactly the same as you think they do 
    
    So what using range(len)
    
    So what I would personally do, to not get confused on which is the row
    and which is column
"""

columns = len(board[0])
rows = len(board)
#^ Setting Columns and Rows to the amount of rows and columns


print(columns)
print(rows)

for x in range(rows):
    print(board[x])
    
"""
    So what i'm alluding to now is the idea of doing nested for loops to go over every single index 
    of the 2d list 
"""

#for x in range(rows):
    #for y in range(columns):
        #print(f"({x},{y})")
        
        
""" 
     ^ To manipulate 2d-lists you should use nested for-loops a lot of the time 
"""

player_1 = "X"
player_2 = "O"

"""
    So the question is, how do we check for winners in tic tac toe? 
"""

def check_winner(board,player):
    """ 
        Params:
            - Board: 2d list
            - Player: current player (X or O)
    """
    
    #Check rows first
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            print(f"{player} wins with a row victory")
            
    

board = [[0,0,0],[0,0,0],["X","X","X"]]

check_winner(board,"X")

""" 
    Row victories make sense because we can just pull out individual rows from our 2d list
    But column victories dont make nearly as much sense 
    
    board = [
        [0,0,0],
        [0,0,0],
        ["X","X","X"]
        ]
        
    Columns are not as easy because they go over every list in our 2dlist 
"""


def check_winner(board,player):
    """ 
        Params:
            - Board: 2d list
            - Player: current player (X or O)
    """
    
    columns = len(board[0])
    rows = len(board)
    
    #Check rows first
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            print(f"{player} wins with a row victory")
            
    for y in range(columns):
            if board[0][y] == player and board[1][y] == player and board[2][y] == player:
                print(f"{player} wins with a column victory")
        
            
    """ 
        [000]
        [000]
        [000] 
    """
    
board = [
         ["X",0,0],
         ["X",0,0],
         ["X",0,0]
         ]

check_winner(board,"X")

""" 
    Diagonal victories are also kinda weird 
    
    [0,0,0]
    [0,0,0]
    [0,0,0]
"""

def check_winner(board,player):
    """ 
        Params:
            - Board: 2d list
            - Player: current player (X or O)
    """
    
    columns = len(board[0])
    rows = len(board)
    
    #Check rows victory
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            print(f"{player} wins with a row victory")
         
    #Check Column Victory        
    for y in range(columns):
            if board[0][y] == player and board[1][y] == player and board[2][y] == player:
                print(f"{player} wins with a column victory")
                
    #Check Diagonal Victory
    
    #first diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(f"{player}wins with a diagonal victory" )
    
    
    #second diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(f"{player} wins with a diagonal victory" )
        

board = [
         [0,0,"X"],
         [0,"X",0],
         ["X",0,0]
         ]


check_winner(board,"X")