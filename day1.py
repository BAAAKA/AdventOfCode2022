with open('day1.txt','r') as f:
    lines = f.readlines()

lines.append("\n")
tValue = 0
mValues = [0,0,0]

for l in lines:
    if l == "\n":
        if tValue>mValues[0]:
            mValues[0] = tValue
            mValues = sorted(mValues)
        tValue=0
        continue
    tValue += int(l.strip())
print("Total Calories {}".format(sum(mValues)))
