#Tic Tac Toe game in python

board = [' ' for x in range(9)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(Board):
    number = 0
    while number < 9 :

        v = "| " + Board[number] + " | "   + Board[number+1] + " | " + Board[number+2]   + " |"
        h = " ___ ___ ___ "
        print(h)
        print(v)
        number += 3 
    print(h)
    
def isWinner(bo, le):
    return (bo[6] == le and bo[7] == le and bo[8] == le) or (bo[3] == le and bo[4] == le and bo[5] == le) or(bo[0] == le and bo[1] == le and bo[2] == le) or(bo[0] == le and bo[3] == le and bo[6] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[0] == le and bo[4] == le and bo[8] == le) or(bo[2] == le and bo[4] == le and bo[6] == le)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        
        try:
            move = int(move)
            move -= 1
            if move >= 0 and move <= 9:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [0,2,5,8]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 4 in possibleMoves:
        move = 4
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [1,3,5,7]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break