
nilou = 0
with open('tempInput.txt') as f:
    f = f.read().strip().split("\n")
    for i in range(int(len(f)/3)):
        b = "".join(set(f[i*3])) + "".join(set(f[i*3+1])) + "".join(set(f[i*3+2]))
        for item in set(b):
            if b.count(item) == 3:
                if item.isupper(): nilou+=ord(item)-38
                else: nilou+=ord(item)-96
                break


print(nilou)