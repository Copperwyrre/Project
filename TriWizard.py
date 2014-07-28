import random
f = open('TestMap.txt', 'r')
maze = f.readlines()
new_maze = [line.replace('\n', '') for line in maze]
for line in new_maze:
    print(line)




