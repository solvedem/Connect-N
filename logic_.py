import random
from check_board import *
from input_output import *

########################################################
##  LOGIC FUNCTIONS
########################################################

#
# ------------------------------------------------------
# Searches a specific column for zeroes (empty spaces)
# True if any zeros are found, else false
# ------------------------------------------------------

def zero_search(board_,column_choice):
    return 0 in [board_[i][column_choice - 1] for i in range(len(board_)-1)]

# 
# ------------------------------------------------------
# Computer opponent, random choice between 1 and 7
# ------------------------------------------------------

def random_computer_choice(board_):
    temp = random.choice(range(1,len(board_[0])+1))
    while not zero_search(board_, temp):
        temp = random.choice(range(1,len(board_[0])+1))
    return temp

#
# ------------------------------------------------------
# Helper function to swap player number in main loop
# ------------------------------------------------------

def player_number(i):
    if i % 2 == 0:
        return 1
    return 2

#
# ------------------------------------------------------
# Moves player's piece onto board
# Returns board and position of move as list
# ------------------------------------------------------

def handle_move_(board_, column_choice, user_number):
    i =  len(board_) - 1
    column_choice -= 1
    position = 0
    while i >= 0:
        if board_[i][column_choice] == 0:
            board_[i][column_choice] = user_number
            position = [[i],[column_choice]]
            break
        i -= 1

    return [board_, position]


#
# ------------------------------------------------------
# Returns players' moves - [1..7]
# ------------------------------------------------------

def get_player_move(player_turn, game_type, board_):

    # Simulation
    if game_type == "s":
        while True:
            choice = random_computer_choice(board_)
            if not zero_search(board_,choice):
                continue
            return choice
    
    # Player vs. Computer
    # Computer Player's turn
    if game_type == "c" and player_turn == 2:
        while True:
            choice = random_computer_choice(board_)
            if not zero_search(board_, choice):
                continue
            return choice
            
    # Users Turn
    while True:
        choice = ""
        while choice < 1 or choice > len(board_[0]):
            choice = get_integer(player_turn)
        if not zero_search(board_, choice):
            continue
        return choice
    



#
# ------------------------------------------------------
# Gets user input for size of board and creates the board
# ------------------------------------------------------


def create_board(board_size):
    w, h  = board_size[0], board_size[1]
    return [[0 for x in range(w)] for y in range(h)]

def width(board_):
    return len(board_[0])

def height(board_):
    return len(board_)

def possible_moves(board_):
    return width(board_)*height(board_)


#
# ------------------------------------------------------
# Final output
# ------------------------------------------------------

def output_winner(board_, player_num, game_type, moves, show, n):
    if game_type == "s":
        if show[2]:
            output_(board_)
        else:
            return 0
    else:
        output_(board_)
    
    if not check_for_wins(board_, player_num, n):
        print "Draw"

    else:
        # Human Vs. CPU
        if game_type == "c":
            if player_num == 1:
                print "Player 1 Wins"
            else:
                print "Computer Wins"
                
        # Simulation (CPU Vs. CPU)
        if game_type == "s":
            if player_num == 1:
                print "Simulation 1 Wins"
            else:
                print "Simulation 2 Wins"

        # Multiplayer (Human Vs. Human)
        if game_type == "m":
            if player_num == 1:
                print "Player 1 Wins"
            else:
                print "Player 2 Wins"

def winner(board_, player_num, game_type, moves, n):
    if not check_for_wins(board_, player_num, n):
        return 0
    else:
        if game_type == "c":
            if player_num == 1:
                return 1
            return 2
        if game_type == "s":
            if player_num == 1:
                return 1
            return 2
        if game_type == "m":
            if player_num == 1:
                return 1
            return 2   


        
