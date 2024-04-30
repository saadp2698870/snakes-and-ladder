import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, value, pos):
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    pos[player] += value
    
    if pos[player] in snakes:
        print(f"Oops! Player {player+1} landed on a snake. They are now on square {snakes[pos[player]]}")
        pos[player] = snakes[pos[player]]
    elif pos[player] in ladders:
        print(f"Yay! Player {player+1} climbed a ladder. They are now on square {ladders[pos[player]]}")
        pos[player] = ladders[pos[player]]
    
    return pos[player]

def play_game():
    pos = [0, 0]
    player = 0
    
    while True:
        value = roll_dice()
        print(f"Player {player+1} rolled a {value}")
        
        if pos[player] + value > 100:
            print("Roll again, you need to land exactly on 100 to win.")
            continue
        
        pos[player] = move_player(player, value, pos)
        
        if pos[player] == 100:
            print(f"Player {player+1} wins!")
            break
        
        player = not player

play_game()