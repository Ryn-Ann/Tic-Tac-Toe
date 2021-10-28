import random
from IPython.display import clear_output

# Create and display the board
def display_board(board):
    
    clear_output()    
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("--|---|--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--|---|--")
    print(board[1] + " | " + board[2] + " | " + board[3])

# Get player input
def player_input():
    
    marker = ''    
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, choose X or O: ").upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Get the board, the marker ('X' or 'O') and the position to put the marker
def place_marker(board, marker, position):
    
    board[position] = marker

# Check tic tac toe
def win_game(board, mark):
    return (
    (board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
            
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side 
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle            
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
        
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal \
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal /

# Random "coin flip" to check which player move first
def first_move():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

# Check if any space on board are available
def check_space(board, position):
        
    return board[position] == ' '

# Check if the board is filld with markers
def check_board_full(board):
    for i in range(1,10):
        if check_space(board, i):
            return False
    return True

# Player chooses the position to place the marker
def player_move(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        position = int(input("Choose next position (1-9): "))
        
    return position

# Command to ask the player if they want to replay Tic Tac Toe
def play_again():
    
    choice = input("Do you want to continue, Y or N: ").lower()
    
    return choice == 'y'
	
"""
Run this game
"""	
print("A Tic-Tac-Toe Game")

while True:
    
    # Set The Board       
    board = [' '] * 10
    player1_mark, player2_mark = player_input()
    move = first_move()
    print(move + ' move first!')
    
    lets_play = input("Ready to play? Y or N: ").lower()
    if lets_play == 'y':
        game_start = True
    else:
        game_start = False
        
    while game_start:
        if move == "Player 1":
            
            # Display The Board
            display_board(board)
            # Choose a position
            position = player_move(board)
            # Place the marker on the position
            place_marker(board, player1_mark, position)
            
            # Check if Player 1 wins
            if win_game(board, player1_mark):
                display_board(board)
                print("CONGRATS PLAYER 1 you won!")
                game_start = False
            else:
                if check_board_full(board):
                    display_board(board)
                    print("Game - a draw")
                    game_start = False
                else:
                    move = 'Player 2'
                    
        else:
            # Display The Board
            display_board(board)
            # Choose a position
            position = player_move(board)
            # Place the marker on the position
            place_marker(board, player2_mark, position)
            
            # Check if Player 1 wins
            if win_game(board, player2_mark):
                display_board(board)
                print("CONGRATS PLAYER 2 you won!")
                game_start = False
            else:
                if check_board_full(board):
                    display_board(board)
                    print("Game - a draw")
                    game_start = False
                else:
                    move = 'Player 1'
                    
    if not play_again():
        break