import random
def monty_hall_game (switch_doors):
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range (3))

    doors_revealed = [i for i in range (3)  if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)

    if switch_doors:
        final_choice = [ i for i in range (3) if i != initial_choice and i != door_revealed] [0]
    else :
        final_choice = initial_choice   

    return doors [final_choice] == 'car'


def simulate_game(num_games) :
    win_no_switch= sum ([monty_hall_game(False) for _ in range (num_games)])
    win_switch = sum ([monty_hall_game(True) for _ in range (num_games)])

    return win_no_switch / num_games , win_switch / num_games

simulate_game(100)