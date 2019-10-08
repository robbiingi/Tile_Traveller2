import random
n = input("Input seed: ")
random.seed(n)
YNO = ['y','n']
WAY = ['n','e','s','w']
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


def find_directions(col, row,coins, valid):
    ''' Returns valid directions as a string given the supplied location '''
    coin_total = coins
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        pull_lever = random.choice(YNO)
        valid +=1
        print("Pull a lever (y/n):",pull_lever)
        if pull_lever == PULL_LEVER:
            coin_total += 1
            print("You received 1 coin, your total is now {:}.".format(coin_total))
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        pull_lever = random.choice(YNO)
        valid +=1
        print("Pull a lever (y/n):",pull_lever)
        if pull_lever == PULL_LEVER:
            coin_total += 1
            print("You received 1 coin, your total is now {:}.".format(coin_total))
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        pull_lever = random.choice(YNO)
        valid +=1
        print("Pull a lever (y/n):",pull_lever)
        if pull_lever == PULL_LEVER:
            coin_total += 1
            print("You received 1 coin, your total is now {:}.".format(coin_total))
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        pull_lever = random.choice(YNO)
        valid +=1
        print("Pull a lever (y/n):",pull_lever)
        if pull_lever == PULL_LEVER:
            coin_total += 1
            print("You received 1 coin, your total is now {:}.".format(coin_total))
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions, coin_total, valid

def play_one_move(col, row, valid_directions,valid):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice(WAY)
    print("Direction:",direction)
    #direction = input("Direction: ")
    direction = direction.lower()
    valid +=1
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row, valid

# The main program starts here
def main():
    victory = False
    row = 1
    col = 1
    coins = 0
    vallid = 6

    valid_directions = NORTH
    print_directions(valid_directions)

    while not victory:
        victory, col, row, vallid = play_one_move(col, row, valid_directions, vallid)
        if victory:
            print("Victory!","Total coins {:}. Moves {:}. ".format(coins, vallid))
            play()
        else:
            valid_directions, coins, vallid = find_directions(col, row, coins, vallid)
            print_directions(valid_directions)

def play():
    yes = input("Play again (y/n): ")
    yes = yes.lower()
    if yes == 'y':
        main()
    else:
        quit()

main()
