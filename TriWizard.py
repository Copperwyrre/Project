import random
import time

def location(symbol):
    """Determines symbol at a location in the maze"""
    row_coor = 0
    for row in maze:
        if symbol in row:
            return [row_coor, row.find(symbol)]
        else:
            row_coor += 1

def determine(coor, maze):
    """Identifies maze coordinates"""
    x, y = coor
    if x < 0 or y < 0:
        return 'W'
    else:
        return maze[x][y]

def area(coor, maze):
    """Determines features of the area"""
    x, y = coor
    features = {'N': determine([x-1, y], maze),
                'S': determine([x+1, y], maze),
                'E': determine([x, y+1], maze),
                'W': determine([x, y-1], maze),}
    return features

def view(features):
    """Informs the player of area features"""
    return 'There is a {} to the north,\nThere is a {} to the south,\nThere is a {} to the east,\nThere is a {} to the west.\n'.format(symbols[features['N']],
                      symbols[features['S']],
                      symbols[features['E']],
                      symbols[features['W']])

def moveoption(features):
    """displays valid moves available"""
    passable = ('P', 'F', 'M', 'B', 'D', 'R')
    valid = []
    for direction in features:
        if features[direction] in passable:
            valid.append(direction)
    return valid

def playersmove(features):
    choice = None
    while choice is None:
        playermove = raw_input("Enter 'N', 'S', 'E' or 'W': ")
        if playermove.upper() in moveoption(features):
            choice = playermove.upper()
        elif playermove.upper() in ('N', 'E', 'S', 'W'):
            if features[playermove.upper()] == 'W':
                print("You walked into the wall")
            else:
                print("Your path is blocked! Choose another way.")
        else:
            print("Invalid choice!")
    return playermove

def proceed(direction, character):
    """moves player in given direction"""
    x, y = character
    move = {'N': [x-1, y],
             'S': [x+1, y], 
             'E': [x, y+1], 
             'W': [x, y-1]}
    return move[direction.upper()]



## Main

symbols = {'S': 'Start',
           'P': 'Path',
           'M': "Magic Encounter",
           'D': 'Door',
           'B': 'Monster',
           'W': 'Wall',
           'F': 'The TriWizard Cup Gleams',
           'R': 'Riddle'}

attributes = {'run_away': 50, 'bypass': 10, 'base_attepmts': 2,
              'cunning_attempts_modifier': 0, 'intell_attempts_modifier': 0, 'physical': 20}

encounters = {'M': 'stuff', 'D': 'stuff', 'B': 'stuff', 'R': 'stuff'}

f = open('TestMap.txt', 'r')
maze = f.readlines()
del f
new_maze = [line.replace('\n', '') for line in maze]

Player = raw_input ('Enter Player name: ')

attrib = raw_input("Pick your strongest attribute:\n(C)unning,(I)telligence,(S)trength,(A)gility?\n: ")
if attrib.upper() == "A":
    attributes['chosen'] = 'Agility'
    attributes['run_away'] = 100
    attributes['bypass'] = 50
if attrib.upper() == "S":
    attributes['chosen'] = 'Strength'
    attributes['physical'] = 60
if attrib.upper() == "I":
    attributes['chosen'] = 'Intelligence'
    attributes['intell_attempts_modifier'] = 2
if attrib.upper() == "C":
    attributes['chosen'] = 'Cunning'
    attributes['cunning_attempts_modifier'] = 1
print('Welcome to the TriWizard Maze {}\nYou will have to use all of your {} to make it to the TriWizard Cup:\n'.format(Player, attributes['chosen']))
character = location('S')

start = time.time()
while determine(character, maze) != 'F':
    features = area(character, maze)
    print (view(features))
    direction = playersmove(features)
    character = proceed(direction, character)
stop = time.time()
print ('You have reached the TriWizard Cup!')

    
    
    




    
    






##def encounter ():
##    """ """
##    
##    if encount 

##random.random()
##0.5641741230021968
##if random.random() <= .1:
##	print("Made it!")
##
##	
##if random.random() <= (physical / 100.0):
##	print("Strong made it.")

	
