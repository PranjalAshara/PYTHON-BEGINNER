from termcolor import colored

X = 'X'
O = 'O'

board =[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

# To determine the color of the cell
# Red if X
# Green of O
def cell(mark):
    color = 'red' if mark == X else 'green'
    return colored(mark,color)

# This method is created to print the board
def print_board(board):
    line = '---+---+---'
    print(line)
    for row in board:
        print(f' {cell(row[0])} | {cell(row[1])} | {cell(row[2])}')
        print(line)

# This method helps us to determine the winner
# The first loop checks if all 3 items inside any inner list are identical and not empty 
# The second loop chains indices [0][col] == [1][col] == [2][col] across rows using a loop tracker.
# We manually check the diagonals
def check_winner(board):

    #check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    
    #check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True
    
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ' or\
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True      
    
    return False

# In order to determine whether the board is full or not
# If any cell is empty in any row then it will return false
# otherwise true
def full_board(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# It is used for Exception Handling
# It avoid crashes in case the user inputs text instead of integer
# Intentionally triggers ValueError in case the input is <0 or >2
def get_position(prompt):
    while True:
        try:
            position = int(input(prompt))
            if position<0 or position>2:
                raise ValueError
            return position
        except ValueError:
            print('Invalid Input')

# It gets input from the player
# Use enters the value between 0 and 2 for row and column through get_position() funciton to validate the input
def get_move(current_player):
    print(f"Player {current_player}'s turn")
    while True:
        row = get_position('Enter row(0-2): ')
        column = get_position('Enter column(0-2): ')

        if board[row][column] == ' ':
            board[row][column] = current_player
            break
        print('This spot is already taken')

def main():
    print_board(board)
    current_player = X

    while True:
        get_move(current_player)

        print_board(board)

        if check_winner(board):
            print(f'Player {current_player} wins!')
            break
        
        if full_board(board):
            print(f'The board is full')
            break
        current_player= O if current_player == X else X

if __name__ == '__main__':
    main()