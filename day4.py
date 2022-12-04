
with open('tempInput.txt') as f:
    f = f.read().strip().split("\n")

    for i in range(len(f)):
        temp = f[i].split(",")

    print(f)