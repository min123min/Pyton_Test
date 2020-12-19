from math import inf as infinity
from random import choice
import platform
import time
from os import system
Player = 0
AI = 0
GlobalPostions = {
        1: [0, 0, " 1 "], 2: [0, 1, " 2 "], 3: [0, 2, " 3 "],
        4: [1, 0, " 4 "], 5: [1, 1, " 5 "], 6: [1, 2, " 6 "],
        7: [2, 0, " 7 "], 8: [2, 1, " 8 "], 9: [2, 2, " 9 "],
    }
def   UserInput():
    if CheckIfOver()==False:
        if empty_squares() == True:
            InputX = int(input(" Please put a Number from 1 to 9 "))
            x=0
            while( int(x) == 0):
                if int(InputX) < 9:
                        
                        GlobalPostions[InputX][2] = " O "
                
                        print( GlobalPostions[InputX])
                        
                        x = 10
                else:
                    print("wrong input. Try again")
        else:
            print("no free moves")

    else:
        print("Game Over")
def empty_squares():
        i = 1
        while  i< 10:
            num = int(GlobalPostions[i][2])
            if (num == int) == True :
                return True
        i += 1 
        return True

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
    if(GlobalPostions[1][2] == GlobalPostions[2][2] == GlobalPostions[3][2]):
        print("Game Over")
        return True
    elif(GlobalPostions[4][2] == GlobalPostions[5][2] == GlobalPostions[6][2]):
        print("Game Over")
        return True
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
Display()
UserInput()