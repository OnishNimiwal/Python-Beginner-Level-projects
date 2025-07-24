import re
import random
class Board:
    def __init__(self,dim_size,num_bombs):
        self.dim_size=dim_size
        self.num_bombs=num_bombs


        self.board=self.make_new_board()
        self.assign_values_to_boards()



        self.dug=set()#To keep the track where we have dig already

    def make_new_board(self):
        board =[[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted=0
        while bombs_planted<self.num_bombs:
            loc=random.randint(0,self.dim_size**2-1)
            row=loc//self.dim_size
            col=loc%self.dim_size

            if board[row][col]=='*':
                continue
            board[row][col]='*'
            bombs_planted+=1
        return board

    def assign_values_to_boards(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c]=='*':
                    continue
                self.board[r][c]=self.get_neighbouring_bombs(r,c)

    def get_neighbouring_bombs(self,row,col):
        #let's iterate through each place in the board and if find the bomb than we will assign value +1 for that particualr neighbouring
        # loc[r-1][c-1]
        # loc[r-1][c]
        # loc[r-1][c+1]
        # loc[r][c-1]
        # loc[r][c+1]
        # loc[r+1][c-1]
        # loc[r+1][c]
        # loc[r+1][c+1]
        num_neighbouring_bomb=0
        for r in range(max(0,row-1),min(self.dim_size-1,(row+1))+1):
            for c in range(max(0,col-1),min(self.dim_size-1,(col+1))+1):
                if r==row and c==col:
                    continue#  no need to check for that col on which we are present
                if self.board[r][c]=='*':
                    num_neighbouring_bomb+=1
        return num_neighbouring_bomb
                              
    def dig(self,row,col):
        # few scenes
        # when bomb dig Game over
        # when place dig were there is noether bomb nor a no which representas the no of neigbuoring bombs
        # then dig till neighbouring we get bomb or no
        
        self.dug.add((row,col))
        if self.board[row][col]=='*':
            return False
        elif self.board[row][col]>0:
            return True
        else:
            # means we have dug out the 0 now rcursively dig all neighbouring places till the neighbour's of the neighbouring place is a bomb or a no.
            for r in range(max(0,row-1),min(self.dim_size-1,(row+1))+1):
                for c in range(max(0,col-1),min(self.dim_size-1,(col+1))+1):
                    if (r,c) in self.dug:
                        continue
                    else:
                        self.dig(r,c)
        return True

    def __str__(self):
        # for showing the board
        visible_board=[[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col]=str(self.board[row][col])

                else:
                    visible_board[row][col]=' '
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play(dim_size=10,num_bombs=10):
    #Step 1 create the board of the dim_size size and plant the bombs
    #Step 2 Ask the user where he/she want to dig
    #Step 3a: If the location is of the bomb show the game over mesg
    #Step 3b: If not the Bomb dig recursively until the each square is next to bomb
    #Step 4 Repeat the steps 2 and 3 until there are no more places to dig and show Victory
    board = Board(dim_size,num_bombs)


    while len(board.dug)<board.dim_size**2-board.num_bombs:
        print(board)
        user_input=re.split(',(\\s)*',input('Where you want to dig ,enter row and column: '))
        row,col=int(user_input[0]),int(user_input[-1])
        if row<0 or row>=board.dim_size or col<0 or col>=board.dim_size:
            print('Enter valid location,Try again')
            continue
        safe=board.dig(row,col)
        if not safe: 
            break
    if safe:
        print("You are victorius")
    else:
        print("Sry Game Over")
    # printing whole board when Game over
        board.dug=[(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__=='__main__':
    play()
