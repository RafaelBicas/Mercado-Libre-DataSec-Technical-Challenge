###############INPUT################
board = [
    [1, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
###############INPUT################

EMPTY_SPACE = 0 #a representation of an empty space on the board before counting the neighbours 
MINE_SPACE = 9 #a constant value which the space identified by 1 must contain in the new string

#As specified on the exercise, the board input may have just 0s and 1s, this function will verify if it is correct. 
def check_input_values(input):
    for row in board:
        for value in row:
            if value != 1 and value != 0:
                return False
    return True

def check_neighbour_exists(board, x, y): 
    return 0 <= x < len(board) and 0 <= y < len(board[0]) #Verifying if the value being compared is in/out of scope
                
def identify_neighbour_values(board, x, y):
    
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if(check_neighbour_exists(board, i, j) and board[i][j] != MINE_SPACE):
                board[i][j] += 1
    
    return board

def identify_mines(board):
    bombs_board = []

    for x in range(0,len(board)): 
        new_row = []
        for y in range(0, len(board[x])):
            if(board[x][y] == 0):
                new_row.append(EMPTY_SPACE)
            else: #The space being verified has a bomb
                new_row.append(MINE_SPACE)
        bombs_board.append(new_row)

    return bombs_board
    

def main():
    if not check_input_values(board):
        print("Invalid board. The board should only contain 0s and 1s.")
        return
    
    new_board = identify_mines(board)

    for x in range(0,len(board)): 
        for y in range(0, len(board[x])):
            if board[x][y] == 1:
                new_board = identify_neighbour_values(new_board, x, y)
            
    for row in new_board:
        print(row)

if __name__ == '__main__':
    main()