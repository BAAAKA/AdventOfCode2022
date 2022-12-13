remRam = []

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for i in range(len(f)):
        if i%3==0:
            rem = eval(f[i])
            ram = eval(f[i+1])
            remRam.append([rem, ram])


def compare(rem, ram):
    rem1 = rem[0]
    ram1 = ram[0]
    if type(rem) == list and type(ram)==list:
        print("Both lists")



print(remRam)
for i in range(len(remRam)):
    print(f"== {i} ==")
    print(f"compraison {remRam[i][0]} and {remRam[i][1]}")




