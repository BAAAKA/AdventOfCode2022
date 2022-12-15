
walls = []
wallsAll = []
field = []
def getCoordinates(walls):
    topLeft = [1000, 1000]
    bottomRight = [0, 0]
    walls.append([(500,0)])
    for ara in walls:
        for rock in ara:
            if rock[0] < topLeft[0]:
                topLeft[0] = rock[0]
            if rock[1] < topLeft[1]:
                topLeft[1] = rock[1]
            if rock[0] > bottomRight[0]:
                bottomRight[0] = rock[0]
            if rock[1] > bottomRight[1]:
                bottomRight[1] = rock[1]
    return topLeft, bottomRight

def startEndpoint(p1, p2, index):
    if p1[index] > p2[index]:
        end = p1
        start = p2
    else:
        end = p2
        start = p1
    return start, end

def getWallzBetween(start, end, index, otherIndex):
    wallz = []
    increases = start[index]
    staysTheSsame = start[otherIndex]
    lengthh = end[index]-start[index]+1
    if index == 1:
        for i in range(lengthh):
            wallz.append((staysTheSsame, increases+i))
    else:
        for i in range(lengthh):
            wallz.append((increases+i, staysTheSsame))
    return wallz

def getAllWallz(p1, p2):
    if p1[0] == p2[0]: # Vertical
        start, end = startEndpoint(p1, p2, 1)
        wallz = getWallzBetween(start, end, 1, 0)
    elif p1[1] == p2[1]: # Horizontal
        start, end = startEndpoint(p1, p2, 0)
        wallz = getWallzBetween(start, end, 0, 1)
    return wallz

def getAraInputWallz(ara):
    allWallz = []
    for i in range(len(ara)-1):
        allWallz += getAllWallz(ara[i], ara[i + 1])
    return allWallz

def grid(coordinates, rocks, sands):
    if coordinates in rocks:
        return "rock"
    elif coordinates[1] == 163:
        return 'rock'
    elif coordinates in sands:
        return 'sand'
    else:
        return 'empty'


def printMap(walls, sands, topLeft, bottomRight):
    width = bottomRight[0]-topLeft[0]+120
    height = bottomRight[1]-topLeft[1]+8
    moveRight = 60
    moveUp = -5
    print(f"topLeft is {topLeft}, bottomright is {bottomRight}")
    print(f"width is {width}, height is {height}")
    for row in range(height):
        for col in range(width):

            finalCol = col+topLeft[0]-moveRight
            finalRow = row+topLeft[1]+moveUp
            if (finalCol, finalRow) in walls or finalRow == 163:
                print("#", end='')
            elif (finalCol, finalRow)  == (500, 0):
                print("+", end='')
            elif (finalCol, finalRow) in sands:
                print("o", end='')
            else:
                print(".", end = '')

        print("")


def dropSand(rocks, sands, dropFrom):
    history = []
    co = dropFrom
    for i in range(300):
        history.append(co)
        if grid((co[0], co[1]+1), rocks, sands) == "empty":
            co = (co[0], co[1] + 1)
        elif grid((co[0] - 1, co[1] + 1), rocks, sands) == "empty":
            co = (co[0] - 1, co[1] + 1)
        elif grid((co[0] + 1, co[1] + 1), rocks, sands) == "empty":
            co = (co[0] + 1, co[1] + 1)
        else:
            #print(f"Ended up at {co}")
            return co
    print("Took Too long!")
    return history


with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for l in f:
        if l != '':
            walls.append(l.split(" -> "))

for i in range(len(walls)):
    for i2 in range(len(walls[i])):
        walls[i][i2] = tuple(map(int, walls[i][i2].split(',')))


topLeft, bottomRight = getCoordinates(walls)


print(walls)
sands = []
rocks = []
for wall in walls:
    rocks += getAraInputWallz(wall)

printMap(rocks, sands, topLeft, bottomRight)
#print(rocks)
print(grid((503,4), rocks, sands))
print("=================")

for i in range(100000):

    finalDestination = dropSand(rocks, sands, (500,0))
    if i%500==0:
        print(f"Working on it..., ended up at {finalDestination}")
    if finalDestination == (500,0):
        print(f"it took {i+1} sandblocks")
        print(finalDestination)
        printMap(rocks, sands, topLeft, bottomRight)
        break
    sands.append(finalDestination)
    if i%1500==0:
        printMap(rocks, sands, topLeft, bottomRight)
print("=================")
print("Done")

