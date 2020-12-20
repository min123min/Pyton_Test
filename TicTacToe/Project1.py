from math import inf as infinity
from random import choice
import platform
import time
from os import system
Player = " O "
AI = " X "
WhoWon = ""
GlobalPostions = {
        1: [0, 0, " 1 "], 2: [0, 1, " 2 "], 3: [0, 2, " 3 "],
        4: [1, 0, " 4 "], 5: [1, 1, " 5 "], 6: [1, 2, " 6 "],
        7: [2, 0, " 7 "], 8: [2, 1, " 8 "], 9: [2, 2, " 9 "],
    }

FreePos = [1,2,3,4,5,6,7,8,9]






def RemoveFromList(Remove, ListOfNum):
    NewList = []
    num = 0
    print ("REMOVEFUNCTION")
    
    for x in ListOfNum:
        if x == Remove:
            print(" Removed pos " + str(Remove) + " from list" )
        else:
            NewList.append(x)
        num +=1

    return NewList
def   UserInput(FreePoss):
    if CheckIfOver()==False:

        if empty_squares() == True:

            InputX = int(input(" Please put a Number from 1 to 9 "))
            x=0
            while( int(x) == 0):

                if int(InputX) < 9: 
                    NewList = RemoveFromList(InputX, FreePoss)
                    GlobalPostions[InputX][2] = " O "
                    print( GlobalPostions[InputX])
                    x = 10  
                    return NewList
        else:           
            print("NO free moves") 
            
    else:
        print("Game Over")
        
    return 



def empty_squares():
        i = 1
        while  i< 10:

            num = GlobalPostions[i][2]
            if (num == " 1 ") == True :
                return True
            elif (num == " 2 ") == True :
                return True
            elif (num == " 3 ") == True :
                return True
            elif (num == " 4 ") == True :
                return True
            elif (num == " 5 ") == True :
                return True
            elif (num == " 6 ") == True :
                return True
            elif (num == " 7 ") == True :
                return True
            elif (num == " 8 ") == True :
                return True
            elif (num == " 9 ") == True :
                return True
            i += 1 
        return False

def FreeSpotSquares():
        i = 1
        NumFreeSpot = 0
        while  i< 10:

            num = GlobalPostions[i][2]
            if (num == " 1 ") == True :
                NumFreeSpot +=1
            elif (num == " 2 ") == True :
                NumFreeSpot +=1
            elif (num == " 3 ") == True :
                NumFreeSpot +=1
            elif (num == " 4 ") == True :
                NumFreeSpot +=1
            elif (num == " 5 ") == True :
                NumFreeSpot +=1
            elif (num == " 6 ") == True :
                NumFreeSpot +=1
            elif (num == " 7 ") == True :
                NumFreeSpot +=1
            elif (num == " 8 ") == True :
                NumFreeSpot +=1
            elif (num == " 9 ") == True :
                NumFreeSpot +=1
            i += 1 
        return NumFreeSpot
def FreeSpotSquares():
        i = 1
        NumFreeSpot = []
        while  i< 10:

            num = GlobalPostions[i][2]
            if (num == " 1 ") == True :
                NumFreeSpot= [1]
            elif (num == " 2 ") == True :
                NumFreeSpot= [2]
            elif (num == " 3 ") == True :
                NumFreeSpot= [3]
            elif (num == " 4 ") == True :
                NumFreeSpot= [4]
            elif (num == " 5 ") == True :
                NumFreeSpot= [5]
            elif (num == " 6 ") == True :
                NumFreeSpot= [6]
            elif (num == " 7 ") == True :
                NumFreeSpot= [7]
            elif (num == " 8 ") == True :
                NumFreeSpot= [8]
            elif (num == " 9 ") == True :
                NumFreeSpot= [9]
            i += 1 
        return NumFreeSpot


def Display ():
     number = 0 
    
     while number < 9 :
         
         v = "| " + str(GlobalPostions[number+1][2]) + " | "   + str(GlobalPostions[number+2][2]) + " | " + str(GlobalPostions[number+3][2])   + " |"
         h = " _____ _____ _____  "
       
        
         print(h)
         print(v)
         number += 3 
     print(h)


def CheckIfOver(): 
    HUMAN = " O "
    AIBOT = " X "
    if(GlobalPostions[1][2] == GlobalPostions[2][2] == GlobalPostions[3][2]):
        if(GlobalPostions[1][2] == HUMAN):
            print("Game Over")
            return AIBOT
        elif(GlobalPostions[1][2] == AIBOT):
            print("Game Over")
            return AIBOT
    elif(GlobalPostions[4][2] == GlobalPostions[5][2] == GlobalPostions[6][2]):
        if(GlobalPostions[4][2] == HUMAN):
            print("Game Over")
            return AIBOT
        elif(GlobalPostions[4][2] == AIBOT):
            print("Game Over")
            return AIBOT
    elif(GlobalPostions[7][2] == GlobalPostions[8][2] == GlobalPostions[9][2]):
        print("Game Over")
        return True
    elif(GlobalPostions[1][2] == GlobalPostions[4][2] == GlobalPostions[7][2]):
        print("Game Over")
        return True
    elif(GlobalPostions[2][2] == GlobalPostions[5][2] == GlobalPostions[8][2]):
        print("Game Over")
        return True
    elif(GlobalPostions[3][2] == GlobalPostions[6][2] == GlobalPostions[9][2]):
        print("Game Over")
        return True
    elif(GlobalPostions[1][2] == GlobalPostions[5][2] == GlobalPostions[9][2]):
        print("Game Over")
        return True
    elif(GlobalPostions[3][2] == GlobalPostions[5][2] == GlobalPostions[7][2]):
        print("Game Over")
        return True
    else:
        print("Not Over Yet")
        return False


def minimax(ListOfFreeNum, Player):
    max_player = " X "  # yourself
    other_player = 'O'
    x=0

    if state.current_winner == other_player:
        return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
        state.num_empty_squares() + 1)}
    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -math.inf}  # each score should maximize
    else:
        best = {'position': None, 'score': math.inf}  # each score should minimize
    return best
print(FreePos)
Display()
ChangeList = UserInput( FreePos)
FreePos = ChangeList
print(FreePos)
minimax(FreePos)
