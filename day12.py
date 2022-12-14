import time
height = 'Sabcdefghijklmnopqrstuvwxyz_0'

def grid(row, col, maxRow, maxCol):
    if row < 0 or row > maxRow-1 or col < 0 or col > maxCol-1:
        return '0'
    else:
        return f[row][col]

def letToNr(letter):
    if letter == "E":
        letter = 'z'
    return height.index(letter)

def posToStr(position):
    return '{},{}'.format(*position)

lastPosition = [[0,0 ]]
previousPositions = {'0,0'}

# 31-4
def canIgoThere(currentL, targetL):
    return letToNr(currentL) - letToNr(targetL) >= -1

def christmas(position, previousPositions):
    row = position[0]
    col = position[1]
    current = grid(row, col, maxRow, maxCol)
    up = grid(row-1, col, maxRow, maxCol)
    down = grid(row+1, col, maxRow, maxCol)
    left = grid(row, col-1, maxRow, maxCol)
    right = grid(row, col+1, maxRow, maxCol)

    if current == "E":
        print(f"FOUND E")
        exit()

    #print(f"{up} {down} {left} {right}")
    #print(f"{canIgoThere(current, up)} {canIgoThere(current, down)} {canIgoThere(current, left)} {canIgoThere(current, right)}")
    possibilities = []
    if canIgoThere(current, up):
        possibilities.append([row-1, col])
    if canIgoThere(current, down):
        possibilities.append([row+1, col])
    if canIgoThere(current, left):
        possibilities.append([row, col-1])
    if canIgoThere(current, right):
        possibilities.append([row, col+1])
    #print(f"all possibleilities {possibilities}")
    returnAra = []
    for pos in possibilities:
        posStr = posToStr(pos)
        if posStr not in previousPositions:
            returnAra.append(pos)
    return returnAra

def callChristmas(positions, previousPositions):
    nextPositions = []
    for position in positions:
        nextPositions += christmas(position, previousPositions)
        for nPos in nextPositions:
            previousPositions.add(posToStr(nPos))
    #print(f"nextPositions {nextPositions}")
    return nextPositions

def printMap(positions):
    for row in range(maxRow):
        #print(f[row])
        for col in range(maxCol):
            #print(f"{row}, {col}")
            if [row, col] in positions:
                #print("0", end="")
                print("\033[0;31m" + '0' + "\033[0m", end="")
            else:
                print(grid(row, col, maxRow, maxCol), end="")
        print("")

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    maxRow = len(f)
    maxCol = len(f[0])


print("###################")
for i in range(1000):
    #print(f"Santa says its day {i}")
    lastPosition = callChristmas(lastPosition, previousPositions)
    #print(f"{lastPosition} {previousPositions}")
    print("")
    time.sleep(0.1)
    printMap(lastPosition)














