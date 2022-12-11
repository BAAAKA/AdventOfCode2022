
class monkey:
    def __init__(self, name, startingItems, operation, condition, ifTrue, ifFalse):
        self.name = name
        self.startingItems = startingItems
        self.operation = operation
        self.condition = int(condition)
        self.ifTrue = int(ifTrue)
        self.ifFalse = int(ifFalse)
        self.inspectCount = 0

    def monkeOperation(self, old):
        item = eval(self.operation)
        item = item%magicNumber
        return item

    def addItem(self, item):
        self.startingItems.append(item)

    def conditionMet(self, item):
        return item%self.condition == 0

    def clearItems(self):
        self.startingItems = []

    def inspectedItem(self):
        self.inspectCount += 1

monkeys = []
with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for i, l in enumerate(f):
        if l[:6] == "Monkey":
            name = l[:-1]
            startingItems = list(map(int, f[i+1][18:].split(",")))
            operation = f[i+2][19:]
            condition = f[i+3][21:] # Divisible by
            ifTrue = f[i+4][29:] # Throw to Monkey x
            ifFalse = f[i+5][30:] # Throw to Monkey x
            monkeys.append(monkey(name, startingItems, operation, condition, ifTrue, ifFalse))

magicNumber = 1
for i2, m in enumerate(monkeys):
    print(f"== Moneky {i2} ==")
    print(m.name)
    print(m.startingItems)
    print(m.operation)
    print(m.condition)
    print(m.ifTrue)
    print(m.ifFalse)
    magicNumber *= m.condition


print(magicNumber)

print("##########################")
for round in range(10000):
    print(f"Starting round {round}")
    for monke in monkeys:
        print(f"Monkey {monke.name}:")
        for item in monke.startingItems:
            monke.inspectedItem()
            #print(f" Monkey inspects an item with a worry level of {item}")
            item = monke.monkeOperation(item)
            #print(f"  Worry level is multiplied by {monke.operation} to {item}.")
            #item = int(item/3)
            #print(f"  Monkey gets bored with item. Worry level is divided by 3 to {item}")
            if monke.conditionMet(item):
                #print(f"  Current worry level is not divisible by {monke.condition}.")
                #print(f"  Item with worry level {item} is thrown to monkey {monke.ifTrue}.")
                monkeys[monke.ifTrue].addItem(item)
            else:
                #print(f"  Current worry level is!! divisible by {monke.condition}.")
                #print(f"  Item with worry level {item} is thrown to monkey {monke.ifFalse}.")
                monkeys[monke.ifFalse].addItem(item)
        monke.clearItems()

print("##########################")
inspected = []
for monke in monkeys:
    print("{}: {}, {}".format(monke.name, monke.startingItems, monke.inspectCount))
    inspected.append(monke.inspectCount)

print(sorted(inspected))