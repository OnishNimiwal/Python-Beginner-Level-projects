import math
import random


class Player:
    def __init__(self,letter):
        #choose letter x or 0
        self.letter = letter


    def get_move(self,game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        # get the spot randomly select from the avaliable spots
        square=random.choice(game.avaliable_moves())
        return square


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        # for the avaliable moves in the game 
        valid_square = False
        val= None
        while not valid_square:
            square = input(self.letter+'\'s turn. input move(0-8):')
            # we will now check the input from the user 
            # is valid or not if not raise error if yes 
            # pass that as valid square
            try:
                val=int(square)
                if val not in game.avaliable_moves():
                    raise ValueError
                valid_square=True
            except ValueError:
                print("Invalid Square. Try Again!")
        
        return val

