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

class Genius_computer_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.avaliable_moves())==9:
            square = random.choice(game.avaliable_moves())
        else:
            # get the place where to move based on the min_max algo go study it
            square=self.minimax(game,self.letter)['position']
        return square
    
    def minimax(self,state,letter):#state means at that time the state of the game
        max_player=self.letter
        other_player= 'O' if letter == 'X' else 'X'
         # base case return when we have a winner 
        if state.current_winner==other_player:
            # Keep track of the score and position 
            return {'position':None,
                    'score':1*(state.num_empty_squares()+1) if other_player==max_player else -1 *(state.num_empty_squares()+1)}
        elif not state.empty_squares():# No empty squares
            return {'position':None,'score':0}
        
        if letter == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.avaliable_moves():
            state.make_move(possible_move, letter)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if letter == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best