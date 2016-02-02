def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or # across the top
    (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or         # across the middle
    (board['low-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or         # across the bottom
    (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or         # down the left side
    (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or         # down the middle
    (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or         # down the right side
    (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or         # diagonal
    (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))           # diagonal
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board)   #calling on function printBoard to print the tictactoe board
        print('Turn for ' + turn + '. Move on which space?')    #asking player X or O to pick a space
        move = input()      #ask player to input move
        board[move] = turn
        if( checkWinner(board, 'X') ):      #calls upon function checkWinner to see if player X is in winning position
            print('X wins!')        #lets the players know that X wins and end program
            break
        elif ( checkWinner(board, 'O') ):       #if X doesnt win, checks to see if O is the winner 
            print('O wins!')        #prints O is the winner and end program
            break
    
        if turn == 'X':     #player X goes first then player O          
            turn = 'O'
        else:
            turn = 'X'      #if player O goes first then player X is second
        
    printBoard(board)       
    
