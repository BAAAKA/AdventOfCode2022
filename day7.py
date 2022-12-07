path = []
directories = {}

def addSize(directory, rPath, s):
    if "size" in directory.keys():
        directory['size'] += s
    else:
        directory['size'] = s
    if rPath != []:
        d = rPath[0]
        rPath = rPath[1:]
        if d not in directory.keys():
            directory[d] = {}
        directory[d] = addSize(directory[d], rPath, s)
    return directory

with open('tempInput.txt') as f:
    f = f.read().strip().split("\n")
    for line in f:
        foundYa = line.split(" ")
        if foundYa[1]  == "cd":
            if foundYa[2] == "..":
                path = path[:-1]
            else:
                path.append(foundYa[2])
        elif foundYa[0].isdigit():
            directories = addSize(directories, path, int(foundYa[0]))
# PART1
def getSize(directory):
    total = 0
    for key in directory.keys():
        if key != "size":
            total += getSize(directory[key])
        else:
            if directory[key]<100000:
                total += directory[key]
    return total

# PART2
DAZBEE = 70000000
def getBestSize(directory, DAZBEE):
    for key in directory.keys():
        if key == 'size':
            if directory[key]<DAZBEE and directory[key] > 8381165:
                DAZBEE = directory[key]
        else:
            DAZBEE = getBestSize(directory[key], DAZBEE)
    return DAZBEE

print("===============")
print(directories)
print("size over 100000 total {}".format(getSize(directories)))
print("best Size {}".format(getBestSize(directories, DAZBEE)))
