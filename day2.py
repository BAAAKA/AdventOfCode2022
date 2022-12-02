ayaka = {"A":{"X":4,"Y":8,"Z":3,}, "B":{"X":1,"Y":5,"Z":9,}, "C":{"X":7,"Y":2,"Z":6,}} # Q 1
momiji = {"A":{"X":3,"Y":4,"Z":8,}, "B":{"X":1,"Y":5,"Z":9,}, "C":{"X":2,"Y":6,"Z":7,}} # Q 2

with open('day2.txt') as f:
    score = sum([momiji[l[0]][l[-1]] for l in f.read().strip().split("\n")])

print(score)

