import re

def nextGeneration(position, remainRounds, valveDict):
    nextPos = []
    print(f"start {position}")

    posName = position[0]
    tif = position[1]
    history = position[2]
    print(f"Im {posName} and can go to {valveDict[posName]}")

    tempTif = remainRounds*valveDict[posName][0]
    nextPos.append([posName, tempTif, []])
    print(nextPos)


    # print(f"A {valveDict[posName][1]}")
    history.append(posName)
    for p in valveDict[posName][1]:
        if not p in history:
            nextPos.append([p, tif, history])

    return nextPos


def printAllPositions(allPos):
    print("++=======")
    for pos in allPos:
        print(pos)

def main():
    valveDict = {}
    allPos = [ ["AA", 0, []] ] # Pos, tif, places since last opening
    remainRounds = 2
    nextallPos = []
    with open('tempInput.txt') as f:
        f = f.read().split("\n")
        for i, l in enumerate(f):
            pat = 'Valve (.{2}) has flow rate=([\d]*); tunnels? leads? to valves? ([a-zA-Z,\s]*)$'
            l = re.findall(pat, l)[0]
            name = l[0]
            flowrate = int(l[1])
            paths = [x.strip() for x in l[2].split(',')]
            valveDict[name] = (flowrate, paths)

    for valve in valveDict.keys():
        print(f"{valve} = {valveDict[valve]}")

    for i in range(2):
        for position in allPos:
            print(position)
            nextallPos += nextGeneration(position, remainRounds, valveDict)
        printAllPositions(nextallPos)
        allPos = nextallPos



if __name__ == "__main__":
    main()




