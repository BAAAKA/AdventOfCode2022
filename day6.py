

with open('tempInput.txt') as f:
    f = f.read().split("\n")[0]
    for i in range(14, len(f)):
        owl = f[i - 14:i]
        if len(owl) == len(set(owl)):
            print(f"it is the {owl} at {i}")
            break

