## this is a tic tack toe game
from math import inf as infinity
from random import choice
import platform
import time
from os import system

game = 1
# list for mat is x,y, item
#GlobalPostions = [ [0,0, 0] , [1,0,0 ] ,[2,0,0 ] ,[0,1,0 ] ,[1,1,0 ] ,[2,1,0 ] ,[0,2,0 ] ,[1,2,0 ] ,[2,2,0 ] ]
GlobalPostions = {
        1: [0, 0, " 1 "], 2: [0, 1, " 2 "], 3: [0, 2, " 3 "],
        4: [1, 0, " 4 "], 5: [1, 1, " 5 "], 6: [1, 2, " 6 "],
        7: [2, 0, " 7 "], 8: [2, 1, " 8 "], 9: [2, 2, " 9 "],
    }
show = "x"
# this will display the board
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
       
         #print(GlobalPostions[number])
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
      InputX = int(input(" Please put an Pos from 1 to 9 "))
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


