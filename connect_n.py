
from check_board import *

from logic_ import *

def main():

    instructions()

    # Play again Loop
    
    while play_():

        # Initial User Prompts and Board Settings

        n = connect_how_many()
        game_type = initial_prompt_game_type()
        board_size = get_board_size()
        board = create_board(board_size)
        sim_set = " "
        number_of_simulations = 1
        if game_type == "s":
            sim_set = simulation_settings()
            number_of_simulations = sim_set[1]
        
        # Multiple Simulation Loop
        
        simulation_count = 0
        winner_list = []
        
        while simulation_count < number_of_simulations:
            
            board = create_board(board_size)
            move_count = 0
            
            # Individual Game Loop
            
            while move_count < possible_moves(board):
                
                output_help(board, game_type, sim_set[0])
                pn = player_number(move_count)
                board = handle_move_(board, get_player_move(pn, game_type, board), pn)[0] 
                if check_for_wins(board, pn, n):
                    break

                move_count += 1

            winner_list.append(winner(board, pn, game_type, move_count, n))
            output_winner(board, pn, game_type, move_count, sim_set, n)
            simulation_count += 1

        simulation_results(game_type, winner_list)

main()
            


