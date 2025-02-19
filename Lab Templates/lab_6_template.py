"""
Name:
Section:
Description: Template for Lab 6
"""

"""
Scenario: We are to build a connect 4 game that runs in the terminal
"""

def drawBoard(board):
    """
    This function draws the board in  a nice, clean manner into the terminal.
        PARAMETERS:
        board: 2D List corresponding to connect 4 Board
        
        Return Type:
        NONE
    """
 

def switchPlayer(player):
    """
    Switches player from X to O or O to X
    
        PARAMETERS:
        Player (STR): Corresponds to the current player
        
        Return Type:
        Player (STR): Switched Player
    """

    
def dropPiece(board,player,column):
    """ 
    Drops piece in specified column
    
        PARAMETERS:
        board (2D List): Game board
        player (STR): current player
        column (int): column to drop piece in
        
        Return Type:
        NONE
    """

    
    
def checkWinner(board,player):
    """
    Checks Board for winner
    
        PARAMETERS:
        board(2d list): Game board
        player(STR): Current player being checked for victory
        
        Return Type:
        (BOOL): True if win False if not win 
    """
    #Check Horizontal Win

    
    #Check Vertical Win


    #Check Left Diagonal win
 
    
    #Check Right Diagonal Win

    

def main():
    ROWS = 6
    COLUMNS = 7
    BOARD = [ 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],        
    ]

    CURRENT_PLAYER = "X"
        
    
    
    
if __name__ == "__main__":
    main()