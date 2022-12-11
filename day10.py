freqX = 1
ongoing = 0
cycle = 1
line = 0
with open('tempInput.txt') as f:
    f = f.read().split("\n")
    f.append("END")

    while True:
        if (cycle-1) % 40 == 0:
            cycle = 1
            print("")

        if abs(cycle - freqX - 1) < 2:
            print("#", end = '')
        else:
            print(".", end = '')
        #print(f"we have cycle {cycle}, value {freqX} ", end= "")

        if ongoing == 0:
            signal = f[line].split(" ")
            line += 1
            if signal[0] == "noop":
                ongoing = 0
            elif signal[0] == "addx":
                ongoing = int(signal[1])
            elif signal[0] == "END":
                break
        else:
            freqX += ongoing
            ongoing = 0
            signal = 0
        #print(f"Signal going to {signal}")
        cycle+=1
print(freqX)
