
def grid(row, tree, width, height, f):
    if row < 0 or row > height-1 or tree < 0 or tree > width-1:
        return -1
    else:
        return f[row][tree]

def ninjaTree(crow, ctree, width, height, f):
    up = True
    down = True
    left = True
    right = True
    ninjaTree = int(f[crow][ctree])
    #print("ninjaTree is {}".format(ninjaTree))
    for h in range(1, height):
        valUp = int(grid(row+h, tree, width, height, f))
        valDown = int(grid(row-h, tree, width, height, f))
        if valUp >= ninjaTree:
            up = False
        if valDown >= ninjaTree:
            down = False
    for w in range(1, width):
        valRight = int(grid(row, tree+w, width, height, f))
        valLeft = int(grid(row, tree-w, width, height, f))
        if valRight >= ninjaTree:
            right = False
        if valLeft >= ninjaTree:
            #print("was unseen by {}".format(valLeft))
            left = False
    if up or down or right or left:
        return False # Not a Ninja, was seen
    return True # Shadow Ninja Tree


notNinjaN = 0
with open('tempInput.txt') as f:
    f = f.read().split("\n")
    width = len(f[0])
    height = len(f)
    for row in range(height):
        for tree in range(width):
            #print("{}".format(grid(row, tree, width, height, f)), end="")
            #print("Tree is ninja {}".format(ninjaTree(row, tree, width, height, f)))
            if not ninjaTree(row, tree, width, height, f):
                notNinjaN += 1
        print("")



print(notNinjaN)