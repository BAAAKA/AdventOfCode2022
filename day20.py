
def getNumbers():
    numbers = []
    with open('tempInput.txt') as f:
        f = f.read().split("\n")
        for nr in f:
            numbers.append((int(nr), False))

    return numbers

def moveStuff(index, numbers):
    val = numbers[index]
    goal = (val[0] + index)
    #print(f"{val} index {goal}")
    numbers.pop(index)
    goal = goal%4999
    if goal == 0:
        numbers.append((val[0], True))
    else:
        numbers.insert(goal, (val[0], True))
    return numbers

# -3 auf i1  bei i6 (7) = i4
# 4 auf i5 = 3
def getIndex(numbers):
    length = len(numbers)
    for i in range(length):
        if numbers[i][1]:
            continue
        return i

def final(numbers):
    print("")
    for nr in numbers:
        print(nr[0], end='|')
    print("")
    print(f"nr1 {1144%5000} {numbers[1144%5000]}") # 5000 #145 #-286
    print(f"nr2 {2144%5000} {numbers[2144%5000]}")
    print(f"nr3 {3144%5000} {numbers[3144%5000]}")

def main():
    numbers = getNumbers()
    print(numbers)
    print(f"length {len(numbers)}")
    for i in range(len(numbers)):
        index = getIndex(numbers)
        numbers = moveStuff(index, numbers)
        #final(numbers)
    final(numbers)


if __name__ == "__main__":
    main()
