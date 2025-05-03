"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lukas Raska
email: raskalukas@seznam.cz
"""

def start_game():
    print("""\n
        Welcome to Tic Tac Toe 
        ============================================ 
        GAME RULES: 
        Each player can place one mark (or stone) 
        per turn on the 3x3 grid. The WINNER is 
        who succeeds in placing three of their 
        marks in a: 
        * horizontal, 
        * vertical or 
        * diagonal row 
        ============================================ 
        Let's start the game
        --------------------------------------------
        Example grid:
        +---+---+---+  
        | 0 | 1 | 2 |
        +---+---+---+
        | 3 | 4 | 5 |
        +---+---+---+
        | 6 | 7 | 8 |
        +---+---+---+
        """
    )

def make_empty_positions():
    """
    Function that will make 
    variables needed for the grid
    """  
    positions = [" " for _ in range(9)]
    round = 0
    return positions, round


def print_the_grid(current_positions):
    """
    Function that will print 
    the grid at the current state
    """ 
    separating_line = "+---+---+---+"   
    print(f"""
        {separating_line}
        | {current_positions[0]} | {current_positions[1]} | {current_positions[2]} |
        {separating_line}
        | {current_positions[3]} | {current_positions[4]} | {current_positions[5]} |
        {separating_line}
        | {current_positions[6]} | {current_positions[7]} | {current_positions[8]} |
        {separating_line}
        """)


def play_a_round(round):
    """
    Function for taking an input from players.
    Chooses the player based on the round.
    Checks if the input is number 
    and cheks if the input is a number that is on the 3x3 board
    """
    player = ""
    if round % 2 == 0:
        player = "o"
    else:
        player = "x"
    while True:
        print("============================================")
        play = input(f"Player {player} | Please enter your move number: ")
        print("============================================")
        #checking if the input is correct playing field
        if play.isnumeric() == False:
            print("Not a number")
        elif int(play) not in range(9):
            print("No such position")
        else:
            break
    return int(play), player
    

def check_valid_move(state,move,round, player):
    """
    Funtion that will check if there 
    is a stone already 
    and increase the number of rounds
    """
    if state[move] == " ":
        state[move] = player
        round += 1    
    else:
        print("A stone is there already")
    return state, round


def check_winner(state):
    """
    Funtion that will check if 
    one of the players 
    has won.
    """
    #deffining winning states
    winning_states = [
    # horizontal
    [state[0], state[1], state[2]],
    [state[3], state[4], state[5]],
    [state[6], state[7], state[8]],
    # vertical
    [state[0], state[3], state[6]],
    [state[1], state[4], state[7]],
    [state[2], state[5], state[8]],
    # diagonal
    [state[0], state[4], state[8]],
    [state[2], state[4], state[6]]
]
    
    #counting stones "x" or "o" in winning states
    #to find out if on of the players has won.
    for winning in winning_states:
        if winning.count("x") == 3:
            print("Congratulations, the player x WON!")
            quit()
        elif winning.count("o") == 3:
            print("Congratulations, the player o WON!")
            quit()
        else:
            continue


def run_the_game():
    """
    Function that will run the whole game.
    """
    start_game()
    state, round = make_empty_positions()
    print_the_grid(state)

    while round < 9:
        move,player = play_a_round(round)
        state, round = check_valid_move(state,move,round,player)
        print_the_grid(state)
        check_winner(state)        
    
    print("Game over. It is a draw. No player has won.")       


#running the game
run_the_game()