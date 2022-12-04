
with open('tempInput.txt') as f:
    f = f.read().strip().split("\n")

    for i in range(len(f)):
        temp = f[i].split(",")
        x1 = temp[0].split("-")
        x2 = temp[1].split("-")
        print(f"{x1} and {x2}")
