# Oisin Curran Tic Tac Tow Game ID:sba20275
import random
# setting up the board
board = [' ' for x in range(9)]

# adding to the board
def Incert(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '

# to print out the board
def printBoard(Board):
    number = 0
    while number < 9:
        v = "| " + Board[number] + " | " + Board[number + 1] + " | " + Board[number + 2] + " |"
        h = " ___ ___ ___ "
        print(h)
        print(v)
        number += 3
    print(h)

# check to see if there a winner. only for for one letter. it check all win cases
def CheckWin(board, letter):
    return (board[6] == letter and board[7] == letter and board[8] == letter) or (board[3] == letter and board[4] == letter and board[5] == letter) or (board[0] == letter and board[1] == letter and board[2] == letter) or (board[0] == letter and board[3] == letter and board[6] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[0] == letter and board[4] == letter and board[8] == letter) or (board[2] == letter and board[4] == letter and board[6] == letter)

# take in player move and check to see if it vlad and space is free.
def playerMove():
    # while the no valid in put keep going until it valid input in is place
    run = True
    while run:
        move = input(' Please provide a number between 1 to 9  ')
        try:
            move = int(move)
            move -= 1
            if move >= 0 and move <= 9:
                if spaceIsFree(move):
                    run = False
                    Incert('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range [1 to 9]!')
        except:
            print('Please type a number!')

# getting the computer the move
def computerMove():
    # finding all the free moves
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = -1
    # check to see if there any winning position for either AI or block the person from winning
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if CheckWin(boardCopy, let):
                move = i
                return move
    # if the middle free take it
    if 4 in possibleMoves:
        move = 4
        return move
    # if there no winning position and middle not free, so they go to corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move


    edgesOpen = []
    for i in possibleMoves:
        if i in [1, 3, 5, 7]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

# for selecting a postion with in a range
def selectRandom(SetOfNum):

    lenthOfSet = len(SetOfNum)
    randomNum = random.randrange(0, lenthOfSet)
    return SetOfNum[randomNum]

# check to see if there free space
def CheckIfFull(board):
    if board.count(' ') > 0:
        return False
    else:
        return True

# the main function that runs the logic in how the order of the functions need to be called and setting up the game
def main():

    print('Tic Tac Toe!')
    printBoard(board)
    # the game will continue until the board is full
    while not (CheckIfFull(board)):
        if not (CheckWin(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print(' O\'s won this time!')
            break

        if not (CheckWin(board, 'X')):
            move = computerMove()
            # to check to see if the game is over
            if move == -1:
                print('Tie Game!')
            else:
                # this where they get put AI move is inserted into the table
                Incert('O', move)
                # the array start at 0 so we need to add one to have a normal grid lay out
                ShowMove = move +1
                print(' Ai Place in O into pos: ', ShowMove, ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if CheckIfFull(board):
        print('Tie Game!')

# this runs to set up the game and keep it going
while True:
    # to reset the board for each game
    board = [' ' for x in range(9)]
    print('-----------------------------------')
    main()