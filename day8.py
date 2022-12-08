
def grid(row, tree, width, height, f):
    if row < 0 or row > height-1 or tree < 0 or tree > width-1:
        return 10
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


def gudTree(row, tree, width, height, f):
    up = 1
    down = 1
    left = 1
    right = 1
    gudHomeTree = int(f[row][tree])
    for u in range(1, height):
        valUp = int(grid(row-u, tree, width, height, f))
        if valUp == 10:
            up-=1
            break
        if valUp < gudHomeTree:
            up += 1
        else:
            break

    for d in range(1, height):
        valDown = int(grid(row+d, tree, width, height, f))
        if valDown == 10:
            down-=1
            break
        if valDown < gudHomeTree:
            down += 1
        else:
            break

    for r in range(1, width):
        valRight = int(grid(row, tree+r, width, height, f))
        if valRight == 10:
            right-=1
            break
        if valRight < gudHomeTree:
            right += 1
        else:
            break

    for l in range(1, width):
        valLeft = int(grid(row, tree-l, width, height, f))
        if valLeft == 10:
            left-=1
            break
        if valLeft < gudHomeTree:
            left += 1
        else:
            break
    val = right*left*up*down
    #print(f" - {up} {down} {left} {right} | {val}")
    return val

# notNinjaN = 0
bestTreeVal = 0
with open('tempInput.txt') as f:
    f = f.read().split("\n")
    width = len(f[0])
    height = len(f)
    for row in range(height):
        for tree in range(width):
            #print("{}".format(grid(row, tree, width, height, f)), end="")
            #print("Tree is ninja {}".format(ninjaTree(row, tree, width, height, f)))
            gudTreeValue = gudTree(row, tree, width, height, f)
            if gudTreeValue>bestTreeVal:
                bestTreeVal=gudTreeValue
            print(gudTreeValue)
        print("")

print(bestTreeVal)

