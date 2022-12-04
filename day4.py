


z = 0
with open('tempInput.txt') as f:
    f = f.read().strip().split("\n")

    for i in range(len(f)):
        temp = f[i].split(",")
        x1 = temp[0].split("-")
        x2 = temp[1].split("-")
        print(f"{x1} and {x2}")
        if x1[0] < x2[0] and x1[1] > x2[1]:
            z+=1
        elif x2[0] < x1[0] and x2[1] > x1[1]:
            z+=1

print(z)