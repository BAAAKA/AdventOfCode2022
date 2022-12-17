import re
import time
def nextGeneration(position, remainRounds, valveDict):
    nextPos = []
    posName = position[0]
    tif = position[1]
    opened = position[2]
    history = position[3]
    #print(f"Im {posName} and can go to {valveDict[posName]}")
    print(opened)
    if len(opened) == 6:
        print("Same length, return position")
        return [position]

    for p in valveDict[posName][1]:
        if not p in history:
            nextPos.append([p, tif, opened, history+[posName]])

    if valveDict[posName][0] != 0 and posName not in opened:
        tempTif = remainRounds*valveDict[posName][0]
        nextPos.append([posName, tif+tempTif, opened + [posName], []])

    return nextPos


def printAllPositions(allPos, valveDict, generation):
    highestVal = 0
    print(f"======= Print of Generation {generation} =======")
    for key in valveDict.keys():
        print(f"{key}", end='')
        for pos in allPos:
            if key == pos[0]:
                print(f" {pos[1]}, ", end='')
                if pos[1]>highestVal:
                    highestVal = pos[1]
        print("")
    print(f"Highest Val is {highestVal}, {len(allPos)}")


def main():
    valveDict = {}
    allPos = [["AA", 0, [], []]] # Pos, tif, , places opened, places since last opening
    rounds = 30-2
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
    cutVal = 0
    for i in range(1, rounds):
        print(f"cutValue is {cutVal}, therefore {int(cutVal / 1.5)}")
        nextallPos = []
        for position in allPos:
            if position[1]+500 < int(cutVal):
                continue #Skip this one
            elif position[1]>cutVal:
                cutVal = position[1]
            nextallPos += nextGeneration(position, (rounds-i), valveDict)
        printAllPositions(nextallPos, valveDict, i)
        allPos = nextallPos

# Too High 2054

if __name__ == "__main__":
    main()




