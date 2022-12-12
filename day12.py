

height = ['abcdefghijklmnopqrstuvwxyz']

def grid(row, col, maxRow, maxCol):
    if row < 0 or row > maxRow-1 or col < 0 or col > maxCol-1:
        return 30
    else:
        return f[row][col]

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    maxRow = len(f)
    maxCol = len(f[0])

    for row in range(maxRow):
        #print(f[row])
        for col in range(maxCol):
            #print(f"{row}, {col}")
            print(f[row][col], end="")
        print("")