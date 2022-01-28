'''
TIC TAC TOE - William Neves Version

font of resource: https://www.techwithtim.net/tutorials/python-programming/tic-tac-toe-tutorial/

Version 1.0

'''
import time

version = "1.0.0b"

board = [' ' for x in range(10)]

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('')

def boardIsFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def insertXO(xo, pos): # Put the X or O on the position
    board[pos] = xo

def spaceIsFree(pos): # Return True if the space is "free"
    return board[pos] == " " 

def isWinner(bo, xo):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == xo and bo[8] == xo and bo[9] == xo) or # across the top
            (bo[4] == xo and bo[5] == xo and bo[6] == xo) or # across the middle
            (bo[1] == xo and bo[2] == xo and bo[3] == xo) or # across the bottom
            (bo[7] == xo and bo[4] == xo and bo[1] == xo) or # down the left side
            (bo[8] == xo and bo[5] == xo and bo[2] == xo) or # down the middle
            (bo[9] == xo and bo[6] == xo and bo[3] == xo) or # down the right side
            (bo[7] == xo and bo[5] == xo and bo[3] == xo) or # diagonal
            (bo[9] == xo and bo[5] == xo and bo[1] == xo))   # diagonal

def playerXMove():
    play = True

    while play:
        move = input("Player X - Enter the number: ")
        try:
            move = int(move)
            if move > 0 and move <10:
                if spaceIsFree(move):
                    play = False
                    insertXO("X", move)
                else:
                    print("space occupied")
            else:
                print("number out of range")
        except:
            print("Type a number between 1-9")

def playerOMove():
    play = True

    while play:
        move = input("Player O - Enter the number: ")
        try:
            move = int(move)
            if move > 0 and move <10:
                if spaceIsFree(move):
                    play = False
                    insertXO("O", move)
                else:
                    print("space occupied")
            else:
                print("number out of range")
        except:
            print("Type a number between 1-9")

def main():
    print("****************************************************")
    print(f"Welcome to Tic-Tac-Toe - Version {version}\n")
    time.sleep(.4)
    print('''To play the game, the player needs to enter a number
in the console. The position numbers is like:\n
 7 | 8 | 9
-----------
 4 | 5 | 6
-----------
 1 | 2 |3\n''')
    print("****************************************************\n")
    print(f"Let's play!!!\n")
    time.sleep(.4)
    printBoard(board)


    while not (boardIsFull(board)):
        if not isWinner(board, "O"):
            playerXMove()
            print("")
            printBoard(board)
            time.sleep(.3)
        
        else:
            print("O win this time...")
            break

        if boardIsFull(board) == True: # Check if board is full before next player time
            break
        else:
            pass

        if not isWinner(board, "X"):
            playerOMove()
            print("")
            printBoard(board)
            time.sleep(.3)
        
        else:
            print("X win this time...")
            break
            

    if boardIsFull(board):
        print("Tie Game")

main()

while True:
    time.sleep(.4)
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        time.sleep(.3)
        print('-----------------------------------')
        main()
    else:
        break