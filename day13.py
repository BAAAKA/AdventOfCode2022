remRam = []

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for i in range(len(f)):
        if i%3==0:
            rem = eval(f[i])
            ram = eval(f[i+1])
            remRam.append([rem, ram])
            print([rem, ram])

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

        print(f"Compare {rem} vs {ram}")
        print(f"Compare {rem_i} vs {ram_i}")

        if type(rem_i) == list or type(ram_i) == list:
            #print("Oh, something is a list or both are lists, time to lists")
            if type(rem_i) == list and type(ram_i) == list:
                naroehoedoe = compare(rem_i, ram_i)
            elif type(rem_i) == list:
                naroehoedoe = compare(rem_i, [ram_i])
            else:
                naroehoedoe = compare([rem_i], ram_i)
        elif rem_i == ram_i:
            print("Equal")
            naroehoedoe = 'equal'
        elif rem_i > ram_i:
            print("Rem is bigger")
            naroehoedoe = "rem"
        else:
            print("Ram is bigger")
            naroehoedoe = "ram"

        if naroehoedoe == 'equal':
            pass
        else:
            return naroehoedoe

    return 'equal'

print("###############################")
kindred = 0


for i in range(len(remRam)):
    print(f"== {i+1} ==")
    a = remRam[i]
    returnValue = compare(*a)
    if returnValue == 'rem':
        print(">>> Wrong")
    else:
        print(">>> Right")
        kindred += i+1

#a = [[[0], [[[], 8, 2, 10], [[], [7, 8, 9, 4]]], [2, [[7, 10, 4, 0], 1, 10], 10]], [[[[0, 5, 3, 8], 4], [5], [[0, 2, 2, 8, 0], 8, 7, [4, 8, 10]], 1]]]
#print(compare(*a))

print(kindred)

# 3505 too low

# Ram -> Right -> Right Order
# Rem -> left -> Wrong Order
