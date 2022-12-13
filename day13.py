remRam = []

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for i in range(len(f)):
        if len(str(f[i]))>0:
            rem = eval(f[i])
            remRam.append(rem)
            print(f[i])

def getAraVal(ara, index):
    if len(ara)-1 >= index: # 3 <= 4
        return ara[index]
    else:
        return -1

def compare(rem, ram):
    longer = len(rem)
    if longer<len(ram):
        longer = len(ram)

    for i in range(longer):
        naroehoedoe = 0

        rem_i = getAraVal(rem, i)
        ram_i = getAraVal(ram, i)

        if rem_i == -1 and ram_i == -1:
            pass
        elif rem_i == -1:
            return "ram"
        elif ram_i == -1:
            return "rem"

        if type(rem_i) == list or type(ram_i) == list:
            print("Oh, something is a list or both are lists, time to lists")
            if type(rem_i) == list and type(ram_i) == list:
                naroehoedoe = compare(rem_i, ram_i)
            elif type(rem_i) == list:
                naroehoedoe = compare(rem_i, [ram_i])
            else:
                naroehoedoe = compare([rem_i], ram_i)
        elif rem_i == ram_i:
            naroehoedoe = 'equal'
        elif rem_i > ram_i:
            naroehoedoe = "rem"
        else:
            naroehoedoe = "ram"

        if naroehoedoe == 'equal':
            pass
        else:
            return naroehoedoe
    return 'equal'

print("###############################")


def sortingStuff(remRam):
    rowz = len(remRam)
    for i in range(1, rowz):
        if compare(remRam[i-1], remRam[i]) == 'ram':
            pass
        else:
            temp = remRam[i-1].copy()
            remRam[i - 1] = remRam[i]
            remRam[i] = temp
    return remRam


def itsBigBrainTime(remRam):
    lastremRam = "hahahHAHFSEHFEWSH"
    print("AAAAAAA")
    while lastremRam != remRam:
        lastremRam = remRam.copy()
        remRam = sortingStuff(remRam)
    print("DONE")
    return remRam

remRam = itsBigBrainTime(remRam)

keyIndex = []
for i, r in enumerate(remRam):
    print(r)
    if r in [[[2]], [[6]]]:
        keyIndex.append(i+1)

print(keyIndex)

# Ram -> Right -> Right Order -> No Switch
# Rem -> left -> Wrong Order
