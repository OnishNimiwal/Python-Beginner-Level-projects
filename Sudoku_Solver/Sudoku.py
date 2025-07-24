def find_next_empty(puzzle):
    # -1 represent that the space in the puzzle is empty
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None


def is_valid(guess,puzzle,row,col):
    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    col_vals=[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # now find out where the 3*3 matrix starts and then check the 
    # 3 values for the row and the col
    row_start=(row//3)*3
    col_start=(col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+1):
            if puzzle[r][c]==guess:
                return False
            
    return True


def solve_sudoku(puzzle):
    row,col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1,10):
        if is_valid(guess,puzzle,row,col):
            puzzle[row][col]=guess
            if solve_sudoku(puzzle):
                return True
        
        # If the given guess is not correct bactrack remove the guess and call again the function for the next guess
        puzzle[row][col]=-1
    return False
  
def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # horizontal separator every 3 rows

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # vertical separator every 3 columns

            val = board[i][j]
            print(val if val != -1 else ".", end=" ")
        print()  # newline after each row


if __name__=='__main__':
    example_board=[
    [5, 3, -1,   -1, 7, -1,   -1, -1, -1],
    [6, -1, -1,   1, 9, 5,   -1, -1, -1],
    [-1, 9, 8,   -1, -1, -1,   -1, 6, -1],

    [8, -1, -1,   -1, 6, -1,   -1, -1, 3],
    [4, -1, -1,   8, -1, 3,   -1, -1, 1],
    [7, -1, -1,   -1, 2, -1,   -1, -1, 6],

    [-1, 6, -1,   -1, -1, -1,   2, 8, -1],
    [-1, -1, -1,   4, 1, 9,   -1, -1, 5],
    [-1, -1, -1,   -1, 8, -1,   -1, 7, 9]
    ]
    

if solve_sudoku(example_board):
    print("✅ Solved Sudoku:\n")
    print_sudoku(example_board)
else:
    print("❌ No solution exists.")