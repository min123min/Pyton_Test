## this is a tic tack toe game
from math import inf as infinity
from random import choice
import platform
import time
from os import system

game = 1
HUMAN = -1
COMP = +1
# list for mat is x,y, item
#GlobalPostions = [ [0,0, 0] , [1,0,0 ] ,[2,0,0 ] ,[0,1,0 ] ,[1,1,0 ] ,[2,1,0 ] ,[0,2,0 ] ,[1,2,0 ] ,[2,2,0 ] ]
GlobalPostions = {
        1: [0, 0, " 1 "], 2: [0, 1, " 2 "], 3: [0, 2, " 3 "],
        4: [1, 0, " 4 "], 5: [1, 1, " 5 "], 6: [1, 2, " 6 "],
        7: [2, 0, " 7 "], 8: [2, 1, " 8 "], 9: [2, 2, " 9 "],
    }


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')



def Display ():
     number = 0 
    
     while number < 9 :
         
         v = "| " + str(GlobalPostions[number+1][2]) + " | "   + str(GlobalPostions[number+2][2]) + " | " + str(GlobalPostions[number+3][2])   + " |"
         h = " _____ _____ _____  "
       
        
         print(h)
         print(v)
         number += 3 
     print(h)




    #  for i in range(0,10):
    #     if i%3==0:
    #         print(h)
    #     else:
    #         print(v)

def   UserInput():
      InputX = int(input(" Please put a Number from 1 to 9 "))
      x=0
      while( int(x) == 0):
        if int(InputX) < 9:
                
                GlobalPostions[InputX][2] = " O "
                #GlobalPostions[int(InputX)][2] = "O"
                print( GlobalPostions[InputX])
                
                x = 10
        else:
            print("wrong input. Try again")
       




def CheckIfOver():
    clean()
    if(GlobalPostions[1][2] == GlobalPostions[2][2] == GlobalPostions[3][2]):
        print("Game Over")
        game=0
    elif(GlobalPostions[4][2] == GlobalPostions[5][2] == GlobalPostions[6][2]):
        print("Game Over")
        game=0
    elif(GlobalPostions[7][2] == GlobalPostions[8][2] == GlobalPostions[9][2]):
        print("Game Over")
        game=0
    elif(GlobalPostions[1][2] == GlobalPostions[4][2] == GlobalPostions[7][2]):
        print("Game Over")
        game=0
    elif(GlobalPostions[2][2] == GlobalPostions[5][2] == GlobalPostions[8][2]):
        print("Game Over")
        game=0
    elif(GlobalPostions[3][2] == GlobalPostions[6][2] == GlobalPostions[9][2]):
        print("Game Over")
        game=0
    elif(GlobalPostions[1][2] == GlobalPostions[5][2] == GlobalPostions[9][2]):
        print("Game Over")
        game=0
    elif(GlobalPostions[3][2] == GlobalPostions[5][2] == GlobalPostions[7][2]):
        print("Game Over")
        game=0
    else:
        print("Not Over Yet")
    

while game == 1:  ## check to see if the game is over 
    Display()
    UserInput()
    CheckIfOver()

def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []
    for x, in GlobalPostions:
        cell.append([x])
    
    return cells

def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False

def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)

