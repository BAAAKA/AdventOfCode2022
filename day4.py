
z = 0
with open('tempInput.txt') as f:
    f = f.read().strip().split("\n")
    for i in range(len(f)):
        dazbee = f[i].split(",")
        s1, e1 = map(int, dazbee[0].split("-"))
        s2, e2 = map(int, dazbee[1].split("-"))
        if (s1 <=  s2 and e1 >= s2) or (s2 <= s1 and e2 >= s1): z += 1
print(z)
