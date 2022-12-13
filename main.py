with open('tempInput.txt') as f:
    f = f.read().split("\n")
    maxRow = len(f)
    maxCol = len(f[0])
    for row in range(maxRow):
        for col in range(maxCol):
            #print(f"{f[row][col]}")
            if f[row][col] == 'E':
                print(f"found E at [{row}, {col}]")
