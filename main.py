# ( . ) = Dirt
# ( - ) = Visited point
# ( @ ) = The vacuum cleaner
# ( # ) = Wall

import random
import numpy as np
import time

# Create a 10x10 matrix world
world = []
for i in range(12):
    row = []
    for j in range(12):
        # Add walls to the edges of the world
        if i == 0 or i == 11 or j == 0 or j == 11:
            row.append('#')
        else:
            row.append(' ')
    world.append(row)

# Define the amount of wals within the environment
num_wals = random.randint(1,30)
# Place wals randomly in the world
for i in range(num_wals):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    while world[x][y] != ' ':
        x = random.randint(1, 10)
        y = random.randint(1, 10)
    world[x][y] = '#'

# Define the amount of dirt within the environment
num_dirt = random.randint(1,70)
# Place dirt randomly in the world
for i in range(num_dirt):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    while world[x][y] != ' ':
        x = random.randint(1, 10)
        y = random.randint(1, 10)
    if( world[x-1][y] != '#' and  world[x+1][y] != '#'):
         world[x][y] = '.'

# Print the world
for row in world:
    print(' '.join(row))
print("number of dirt is:",num_dirt)
print("number of walls is:",num_wals)

array = np.array(world)

x = 1
y = 1
counter = 0
arraylastStep = []
while '.' in array :

    time.sleep(1)
    print('-----   Restart   -----   Values X :' + str(x) + " - Y:" + str(y) + ' - Counter:'+str(counter+1))

    if (12 != y + 1 and ( array[y + 1][x] == '.')):
        counter = counter + 1
        array[y][x] = '-'
        array[y + 1][x] = '@'
        y = y + 1
        arraylastStep.append([y, x])

    elif ( 0 != y-1 and ( array[y - 1][x] == '.')):
        counter = counter + 1
        array[y][x] = '-'
        array[y - 1][x] = '@'
        y = y - 1
        arraylastStep.append([y, x])

    elif ( 12 != x+1 and (array[y][x+1] == '.')):
        counter = counter + 1
        array[y][x] = '-'
        array[y][x+1] = '@'
        x = x + 1
        arraylastStep.append([y, x])

    elif ( 0 != x-1 and (array[y][x-1] == '.')):
        counter = counter + 1
        array[y][x] = '-'
        array[y][x-1] ='@'
        x = x - 1
        arraylastStep.append([y, x])

    elif(  12 != y+1 and (array[y + 1][x] == ' ')):
        counter = counter+1
        array[y][x] = '-'
        array[y + 1][x] = '@'
        y=y+1
        arraylastStep.append([y,x])

    elif ( 0 != y-1 and (array[y - 1][x] == ' ')):
        counter = counter + 1
        array[y][x] = '-'
        array[y - 1][x] = '@'
        y = y - 1
        arraylastStep.append([y, x])

    elif ( 12 != x+1 and (array[y][x + 1] == ' ')):
        counter = counter + 1
        array[y][x] = '-'
        array[y][x+1] = '@'
        x = x + 1
        arraylastStep.append([y, x])

    elif ( 0 != x-1 and (array[y][x - 1] == ' ')):
        counter = counter + 1
        array[y][x] = '-'
        array[y][x-1] ='@'
        x = x - 1
        arraylastStep.append([y, x])

    else:
        counter = counter + 1
        array[y][x] = '-'
        print('x = ' + str(arraylastStep[-1][1]) + '\n''y = ' + str(arraylastStep[-1][0]))
        array[arraylastStep[-1][0], arraylastStep[-1][1]] = '@'
        y = arraylastStep[-1][0]
        x = arraylastStep[-1][1]
        arraylastStep.pop(-1)

    print(str(array[0]) + '\n' + str(array[1]) + '\n' + str(array[2]) + '\n' + str(array[3]) + '\n' + str(array[4])+ '\n' + str(array[5])+ '\n' + str(array[6])+ '\n' + str(array[7])+ '\n' + str(array[8])+ '\n' + str(array[9])+ '\n' + str(array[10]) + '\n' + str(array[11]))
print('*** End ***')