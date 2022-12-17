import re

sensors = []
theLine = set()
beaconOnLine = set()
xymax = 4000000
def getManhattan(x,y, x2, y2):
    return abs(int(x)-int(x2)) + abs(int(y)-int(y2))

def crossWidth(crossingVal):
    return crossingVal*2+1

def animalCrossing(sensor, yLine):
    x = sensor[0]
    y = sensor[1]
    manhattan = sensor[2]
    distance = abs(y-yLine)
    crossingVal = abs(distance-manhattan)
    print(f"Crosses yline at {sensor[0]}/{yLine} with distance of {distance}, crossingVal {crossingVal} -> {crossWidth(crossingVal)}")
    getCrossCoord(x, crossWidth(crossingVal), yLine)

def getCrossCoord(x, crossWidth, yLine):
    startX = int(x-(crossWidth-1)/2)
    for i in range(crossWidth):
        coord = '({},{})'.format(startX+i, yLine)
        #print(coord)
        theLine.add(coord)

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for l in f:
        pat = 'Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)'
        l = re.search(pat, l)
        sensors.append((int(l[1]), int(l[2]), getManhattan(l[1],l[2],l[3],l[4]))) # x, y, manhattan


def amIalone(x, y, sensors):
    alone = True
    for sensor in sensors:
        distance = getManhattan(x, y, sensor[0], sensor[1])
        if distance <= sensor[2]:
            alone = False
            #print(f"IM NOT ALONE ({x}, {y})")
            break
    if alone:
        print(f"IM ALONE ({x}, {y})")

def isInField(x, y):
    return x<xymax and y<xymax and y>0 and x>0

def getBorderCor(sensor):
    x = sensor[0]
    y = sensor[1]
    manhattan = sensor[2]
    man_x = 0
    man_y = manhattan
    for i in range(manhattan*2+1): # 2*2+1 = 5 RIght Side
        #print("{}, {}".format(x+man_x, y+man_y))
        x_right = x+man_x+1
        y_right = y+man_y
        if isInField(x_right, y_right):
            amIalone(x_right, y_right, sensors)
        if y+man_y>y:
            man_x+=1
        else:
            man_x-=1
        man_y-=1

    man_x = 0
    man_y = manhattan
    for i in range(manhattan*2+1): # 2*2+1 = 5 RIght Side
        #print("{}, {}".format(x+man_x, y+man_y))
        x_left = x+man_x-1
        y_left = y+man_y
        if isInField(x_left, y_left):
            amIalone(x_left, y_left, sensors)
        if y+man_y>y:
            man_x-=1
        else:
            man_x+=1
        man_y-=1

testSensor = (2,2,2)
getBorderCor(testSensor)

for sensor in sensors:
    print(f"trying Sensor {sensor}, gonna take a bit ehe")
    getBorderCor(sensor)


#IM ALONE (3135800, 2766584)