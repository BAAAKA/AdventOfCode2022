import re

sensors = []
yLine = 2000000
theLine = set()
beaconOnLine = set()
xymax = 20
def getManhattan(x,y, x2, y2):
    total = abs(int(x)-int(x2)) + abs(int(y)-int(y2))
    return total

def crossWidth(crossingVal):
    return crossingVal*2+1

def animalCrossing(sensor):
    x = sensor[0]
    y = sensor[1]
    manhattan = sensor[2]
    distance = abs(y-yLine)
    crossingVal = abs(distance-manhattan)
    print(f"Crosses yline at {sensor[0]}/{yLine} with distance of {distance}, crossingVal {crossingVal} -> {crossWidth(crossingVal)}")
    getCrossCoord(x, crossWidth(crossingVal))

def getCrossCoord(x, crossWidth):
    startX = int(x-(crossWidth-1)/2)
    for i in range(crossWidth):
        coord = '({},{})'.format(startX+i, yLine)
        #print(coord)
        theLine.add(coord)
    #####

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for l in f:
        pat = 'Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)'
        l = re.search(pat, l)
        sensors.append((int(l[1]), int(l[2]), getManhattan(l[1],l[2],l[3],l[4]))) # x, y, manhattan

        if int(l[4])==yLine:
            beaconOnLine.add(f"({l[3]},{l[4]})")

for sensor in sensors:
    animalCrossing(sensor)


print(theLine)
print(len(theLine))
print(f"beaconOnLine {beaconOnLine}")
print(f"final: {len(theLine)-len(beaconOnLine)}")


# 8663710 too high