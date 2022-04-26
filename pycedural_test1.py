import sqlite3 as sl
from multiprocessing.dummy import Array
from random import randint

#--------------------------VARIABLES-----------------------------------
one = [1,2]
two = [1,2,3]
three = [2,3,4]
four = [3,4,5]
five = [4,5,6]
six = [5,6,7]
seven = [6,7,8]
eight = [7,8,9]
nine = [8,9]

global IDBpyIndex
IDBpyIndex = 0
grid = [
    [0,0,0,0,0,0,0,0,0], #1
    [0,0,0,0,0,0,0,0,0], #2
    [0,0,0,0,0,0,0,0,0], #3
    [0,0,0,0,0,0,0,0,0], #4
    [0,0,0,0,0,0,0,0,0], #5
    [0,0,0,0,0,0,0,0,0], #6
    [0,0,0,0,0,0,0,0,0], #7
    [0,0,0,0,0,0,0,0,0], #8
    [0,0,0,0,0,0,0,0,0]  #9
]

#--------------------------FUNCTIONS-----------------------------------
def waveVal(wave, xx , yy):
    strict = 0 # 0 - Not Strict ; 1 - Strict ; 2 - Very Strict
    match wave:
        case 1:
            return one[randint(0,1)]
        case 2:
            return two[randint(strict,2)]
        case 3:
            return three[randint(strict,2)]
        case 4:
            return four[randint(strict,2)]
        case 5:
            return five[randint(strict,2)]
        case 6:
            return six[randint(strict,2)]
        case 7:
            return seven[randint(strict,2)]
        case 8:
            return eight[randint(strict,2)]
        case 9:
            return nine[randint(0,1)]
        case 0:
            return randint(1,9)
            


#-------------------------PROCESSING-----------------------------------


print("----------------------------------------------------------------------------------------------")
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])

xValue = randint(0,8)
yValue = randint(0,8)
waveValue = randint(1,9)

grid[xValue][yValue] = waveValue

print("----------------------------------------------------------------------------------------------")
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print("----------------------------------------------------------------------------------------------")
row = 9
column = 9
newValue = ""
count=0

while(count <= 1000):
    for xx in range(column):
        for yy in range(row):
            if (xx == xValue) and (yy == yValue):
                if not (xx == 8):
                    grid[xx+1][yy] = waveVal(grid[xx][yy], xx, yy)
                if not (yy == 8):
                    grid[xx][yy+1] = waveVal(grid[xx][yy], xx, yy) 
                if not (xx == 0):
                    grid[xx-1][yy] = waveVal(grid[xx][yy], xx, yy)
                if not (yy == 0):
                    grid[xx][yy-1] = waveVal(grid[xx][yy], xx, yy)
            elif (grid[xx][yy] != 0):
                if (xx != 8) and grid[xx+1][yy] == 0:
                    grid[xx+1][yy] = waveVal(grid[xx][yy], xx, yy)
                if (yy != 8) and grid[xx][yy+1] == 0:
                    grid[xx][yy+1] = waveVal(grid[xx][yy], xx, yy) 
                if (xx != 0) and grid[xx-1][yy] == 0:
                    grid[xx-1][yy] = waveVal(grid[xx][yy], xx, yy)
                if (yy != 0) and grid[xx][yy-1] == 0:
                    grid[xx][yy-1] = waveVal(grid[xx][yy], xx, yy)
            else:
                grid[xx][yy] = 0

            if (grid[xx][yy] == 0):
                count = 0
            else:
                count += 1

print("----------------------------------------------------------------------------------------------")
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print("----------------------------------------------------------------------------------------------")
print("Final")