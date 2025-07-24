import math
import time
from player import HumanPlayer,RandomComputerPlayer,Genius_computer_player
class Tic_Tac_Toe:
    # Creation of the board here
    
    def __init__(self):
        self.board = self.make_board() # a board list created wich have 9 blank spaces in 1-D list
        self.current_winner = None 

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        # Logic for which group of three spaces we are choosing
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # When i = 0: self.board[0:3] → ['X', 'O', '-']
                                                                # When i = 1: self.board[3:6] → ['-', 'X', 'O']
                                                                # When i = 2: self.board[6:9] → ['-', '-', 'X']
            print('| ' + ' | '.join(row)+' |')
    
    @staticmethod
    def print_board_nums():
        # 0| 1| 2 etc tells us the box that corresponds to the sapce in the 3x3 board
        number_board=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+' |')

    def make_move(self,square,letter):
        # we will return true if the valid move  and assign the move else retun false
        if self.board[square] == ' ':
            self.board[square] = letter
            # Check if we get the winner
            if self.winner(square,letter):
                self.current_winner=letter
            return True
        return False

    def winner(self,square,letter):
        # Winner when there is consecutive three letter in any direction
        # 1st row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # 2nd column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # 3rd diagonal
        # to win in the diagonal the square must be the even no (0,2,4,6,8)
        if square %2==0:
            diagonal1=[self.board[i] for i in (0,4,8)]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2=[self.board[i] for i in (2,4,6)]
            if all([spot == letter for spot in diagonal1]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')


    def avaliable_moves (self):
        # method 1 with list one liner code
        return [i for  i, spot in enumerate(self.board)if spot==' '] # enumerate is used for creating the tuple of index, value
        # method 2 by creating the moves and than returning it
        # moves = []
        # for (i,spot) in enumerate(self.board):
                # ['x','x','0']-->[[o,'x'],[1,'x'],[2,'0']]
                # if spot==' ':
                    # moves.append(i)
        # return moves

    




def play(game,x_player,o_player,print_game=True): # print_game represents if you want to continue playing with the opponent than true if want the another opponent means like comp. vs comp. than false
    # in this function we will gona return the winner
    if print_game:
        game.print_board_nums()
    letter = 'X' # Starting letter
    #iterate till game has empty moves ( dont worry about the winners as if we got than we simply return)
    while game.empty_squares():
        if letter == 'O':
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)

        # now make move
        if game.make_move(square,letter):
            if print_game:
                print(letter +f" makes a move to square {square}")
                game.print_board()
                print(' ')
            # Check if that letter wons
            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')
                return letter

        # after making the move alternate the letter
        letter='O' if letter == 'X' else 'X'
    #Some break
    time.sleep(1)

    if print_game:
        print('It\'s a tie!!')


if __name__=='__main__':
    x_wins=0
    o_wins=0
    ties=0
    for _ in range(10):
        x_player=RandomComputerPlayer('X')
        o_player=Genius_computer_player('O')
        t=Tic_Tac_Toe()
        result=play(t,x_player,o_player,print_game=False)
        if result=='X':
            x_wins+=1
        if result=='O':
            o_wins+=1
        else:
            ties+=1
    print(f'We see after 10 iterations {x_wins} X_wins, {o_wins} O_wins and {ties} ties')

