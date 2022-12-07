

path = []
directories = {}




def addSize(directory, rPath, s):
    print(f"{directory} , {rPath}, {s}")
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
        print(line)
        foundYa = line.split(" ")
        if foundYa[1]  == "cd":
            print(f"Found path {foundYa[2]}, currentpath: {path}")
            if foundYa[2] == "..":
                path = path[:-1]
            else:
                path.append(foundYa[2])
        elif foundYa[0].isdigit():
            print(f"It is a digit! {foundYa[0]}")
            directories = addSize(directories, path, int(foundYa[0]))



total = 0
def getSize(directory):
    total = 0
    for key in directory.keys():
        if key != "size":
            total += getSize(directory[key])
        else:
            if directory[key]<100000:
                total += directory[key]
    return total

print("===============")
print(directories)
print(getSize(directories))


