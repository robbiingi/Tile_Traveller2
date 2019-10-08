# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
PULL_LEVER = 'y'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")


def find_directions(col, row,coins):
    ''' Returns valid directions as a string given the supplied location '''
    coin_total = coins
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        pull_lever = input("Pull a lever (y/n): ")
        if pull_lever == PULL_LEVER:
            coin_total += 1
            print("You received 1 coin, your total is now {:}.".format(coin_total))
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        pull_lever = input("Pull a lever (y/n): ")
        if pull_lever == PULL_LEVER:
            coin_total += 1
            print("You received 1 coin, your total is now {:}.".format(coin_total))
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        pull_lever = input("Pull a lever (y/n): ")
        if pull_lever == PULL_LEVER:
            coin_total += 1
            print("You received 1 coin, your total is now {:}.".format(coin_total))
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        pull_lever = input("Pull a lever (y/n): ")
        if pull_lever == PULL_LEVER:
            coin_total += 1
            print("You received 1 coin, your total is now {:}.".format(coin_total))
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions, coin_total

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

# The main program starts here
def main():
    victory = False
    row = 1
    col = 1
    coins = 0

    valid_directions = NORTH
    print_directions(valid_directions)

    while not victory:
        victory, col, row = play_one_move(col, row, valid_directions)
        if victory:
            print("Victory!","Total coins {:}.".format(coins))
            play()
        else:
            valid_directions, coins = find_directions(col, row, coins)
            print_directions(valid_directions)

def play():
    yes = input("Play again (y/n): ")
    yes = yes.lower()
    if yes == 'y':
        main()
    else:
        quit()

main()
