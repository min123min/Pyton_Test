from math import inf as infinity
from random import choice
import platform
import time
from os import system
GlobalPostions = {
        1: [0, 0, " 1 "], 2: [0, 1, " 2 "], 3: [0, 2, " 3 "],
        4: [1, 0, " 4 "], 5: [1, 1, " 5 "], 6: [1, 2, " 6 "],
        7: [2, 0, " 7 "], 8: [2, 1, " 8 "], 9: [2, 2, " 9 "],
    }
def Display ():
     number = 0 
    
     while number < 9 :
         
         v = "| " + str(GlobalPostions[number+1][2]) + " | "   + str(GlobalPostions[number+2][2]) + " | " + str(GlobalPostions[number+3][2])   + " |"
         h = " _____ _____ _____  "
       
        
         print(h)
         print(v)
         number += 3 
     print(h)

def   UserInput():
      InputX = int(input(" Please put a Number from 1 to 9 "))
      x=0
      while( int(x) == 0):
        if int(InputX) < 9:
                
                GlobalPostions[InputX][2] = " O "
           
                print( GlobalPostions[InputX])
                
                x = 10
        else:
            print("wrong input. Try again")


Display()
UserInput()








       