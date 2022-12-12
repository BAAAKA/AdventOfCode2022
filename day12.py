

height = 'Sabcdefghijklmnopqrstuvwxyz_0'

def grid(row, col, maxRow, maxCol):
    if row < 0 or row > maxRow-1 or col < 0 or col > maxCol-1:
        return '0'
    else:
        return f[row][col]

def letToNr(letter):
    return height.index(letter)

position = [0, 0]
path = {'0,0'}

def canIgoThere(currentL, targetL):
    return letToNr(currentL) - letToNr(targetL) >= -1

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    maxRow = len(f)
    maxCol = len(f[0])

    for row in range(maxRow):
        #print(f[row])
        for col in range(maxCol):
            #print(f"{row}, {col}")
            print(grid(row, col, maxRow, maxCol), end="")
        print("")

for x in range(10):
    row = position[0]
    col = position[1]
    current = grid(row, col, maxRow, maxCol)
    up = grid(row-1, col, maxRow, maxCol)
    down = grid(row+1, col, maxRow, maxCol)
    left = grid(row, col-1, maxRow, maxCol)
    right = grid(row, col+1, maxRow, maxCol)
    print(f"{up} {down} {left} {right}")
    print(f"{canIgoThere(current, up)} {canIgoThere(current, down)} {canIgoThere(current, left)} {canIgoThere(current, right)}")























