# Oisin Curran TicTacToe Game

Board = [" " for x in range (9)]

def Insert(Letter, Pos):
    Board[pos-1] = Letter

def SpaceFree(Pos):
    return Board[Pos] == " "

def  PrintBoard(Board):
    number = 0

    while number < 9 :

        v = "| " + Board[number] + " | "   + Board[number+1] + " | " + Board[number+2]   + " |"
        h = " ___ ___ ___ "
        print(h)
        print(v)
        number += 3 
    print(h)

def CheckWinner(board, letter):
    return (board[6] == letter and board[7] == letter and board[8] == letter) or (board[3] == letter and board[4] == letter and board[5] == letter) or(board[0] == letter and board[1] == letter and board[2] == letter) or(board[0] == letter and board[3] == letter and board[6] == letter) or(board[1] == letter and board[4] == letter and board[7] == letter) or(board[2] == letter and board[5] == letter and board[8] == letter) or(board[0] == letter and board[4] == letter and board[8] == letter) or(board[2] == letter and board[4] == letter and board[6] == letter)

def PlayerMove():
  pass  
def Main():
    print("Enjoy Tic Tac Toe")
    PrintBoard(Board)

Main()