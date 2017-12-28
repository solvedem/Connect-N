
########################################################
##  INITIAL OUTPUT AND PROMPTS
########################################################

def instructions():
    print " ----- CONNECT FOUR ----- "
    print """
            This Connect Four program has 3 game types:
                    Multiplayer = Human Vs. Human
                    Computer = Human Vs. Computer
                    Simulation = Simulation Vs. Simulation

            Users will be prompted for the board size.

            The maximum board size is 50 by 50.

            The minimum board size is 4 by 4.

            The simulation game type will prompt user for
            the number of simulations and whether or not
            user will watch the simulations or simply
            see the results of the simulations.

            The maximum amount of simulations is 100.

"""
    print " -----    ------    ----- "
    print


def initial_prompt_game_type():
    game_type = ""
    while game_type != "m" and game_type != "c" and game_type != "s":
        game_type = raw_input("Multiplayer(m), CPU?(c), or Simulation(s): ")
    return game_type

def play_():
    play = ""
    while play != "p" and play != "q":
        play = raw_input("(p)lay or (q)uit: ")
    return play == "p"

def simulation_settings():
    sim_type = ""
    while sim_type != "y" and sim_type != "n":
        sim_type = raw_input("Watch Simulation Process? y or n: ")

    show = ""
    while show != "y" and show != "n":
        show = raw_input("Watch Finished Simulations? y or n: ")

    simulation_amount = ""
    while simulation_amount < 0 or simulation_amount > 100:
        print "Enter number of simulations: "
        simulation_amount = get_int()
    
    return [sim_type == "y", simulation_amount, show == "y"]

def get_board_size():
    width = ""
    height = ""
    print "----- Enter board dimensions -----"
    while width > 50 or  width <= 3:
        width = ""
        while width != type(int):
            width = raw_input("Width: ")
            try:
                width = int(width)
                break
            except:
                continue

    while height > 50 or  height <= 3:
        height = ""
        while height != type(int):
            height = raw_input("Height: ")
            try:
                height = int(height)
                break
            except:
                continue
    return [width,height]


########################################################
##  OUTPUT HELPER FUNCTIONS
########################################################

def output_(board_):
    print "----- ----- ----- ----- -----"
    for row in board_:
        print row
    print

def output_help(board_,game_type, ss):
    if game_type == "s":
        if ss and ss != " ":
            output_(board_)
    else:
        output_(board_)

def simulation_results(game_type, winner_list):
    if game_type == "s":
        print
        print " ----- Simulation Results ----- "
        if winner_list.count(1) != 1:
            print "Player 1 won ", winner_list.count(1), " times"
        else:
            print "Player 1 won ", winner_list.count(1), " time"

        if winner_list.count(2) != 1:    
            print "Player 2 won ", winner_list.count(2), " times"
        else:
            print "Player 2 won ", winner_list.count(2), " time"
        if winner_list.count(2) != 1:
            print winner_list.count(0), " draws"
        else:
            print winner_list.count(0), " draw"
            

########################################################
##  INPUT HELPER FUNCTIONS
########################################################
            
# With Prompt
def get_integer(player_num):
    choice = ""
    while type(choice) != int:
        prompt = "Player " + str(player_num) + ", Enter a choice: "
        try:
            choice = input(prompt)
        except:
            choice = get_integer(player_num)

    return choice

# No Prompt
def get_int():
    choice = ""
    while type(choice) != int:
        try:
            choice = input()
        except:
            choice = get_int()

    return choice

def connect_how_many():
    print "Connect - how many?: ",
    many = get_int()
    while many < 0 and many > 50:
        many = get_int()
    return many

