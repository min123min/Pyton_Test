import math
import time
from player import HumanPlayer, SmartComputerPlayer

GlobalPostions = {
        1: [0, 0, " 1 "], 2: [0, 1, " 2 "], 3: [0, 2, " 3 "],
        4: [1, 0, " 4 "], 5: [1, 1, " 5 "], 6: [1, 2, " 6 "],
        7: [2, 0, " 7 "], 8: [2, 1, " 8 "], 9: [2, 2, " 9 "],
    }

class TicTacToe():
    def __init__(self):
        self.current_winner = None

   

    def print_board(self):
        number = 0 
    
        while number < 9 :
         
         v = "| " + str(GlobalPostions[number+1][2]) + " | "   + str(GlobalPostions[number+2][2]) + " | " + str(GlobalPostions[number+3][2])   + " |"
         h = " _____ _____ _____  "
       
        
         print(h)
         print(v)
         number += 3 
         print(h)

   

    def make_move(self, square, letter):
        pos = square + 1
        if GlobalPostions[pos][2].isnumeric == True:
            GlobalPostions[pos][2] = " X "
            if self.winner(square, letter) == True:
                 self.current_winner = letter   #  work needed 
            return True
        return False

    def winner(self, square, letter):

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


    def empty_squares(self):
        i = 1
        while  i< 10:
            if GlobalPostions[i][2].isnumeric == True:
                return True
        i += 1 
        return False

    def num_empty_squares(self):
        i = 1
        count = 0 
        while  i< 10:
            if GlobalPostions[i][2].isnumeric == True:
                count += 1
        i += 1 
 
        return count

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player):

 

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

    
            print(letter + ' makes a move to square {}'.format(square))
            game.print_board()
            print('')

            if game.current_winner:
               
                print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)


    print('It\'s a tie!')



if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player)