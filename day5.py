import re

alula = [[], [], [], [], [], [], [], [], []]
print(alula)
with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for i, l in enumerate(f):
        if l.strip() != "" and l[0] == "m":
            ehe = re.search("move (\d*) from (\d*) to (\d*)", l)
            n = int(ehe.group(1))
            mFrom = int(ehe.group(2)) - 1
            mTo = int(ehe.group(3)) - 1
            moveAra = alula[mFrom][:n]
            alula[mFrom] = alula[mFrom][n:]
            alula[mTo] = moveAra + alula[mTo]
        else:
            for i2 in range(len(l)):
                if l[i2] == "[":
                    inde = int(i2 / 4)
                    alula[inde].append(l[i2 + 1])

for v in alula:
    print(v)
