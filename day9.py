head = [0, 0]
tails = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tailPath = []

def goTo(head, direciton):
    if direction == "R": head[1]+=1
    elif direciton == "L": head[1]-=1
    elif direciton == "U": head[0]+=1
    elif direciton == "D": head[0]-=1
    return head

def happyTail(head, tail):
    if abs(head[1]-tail[1])<2 and abs(head[0]-tail[0])<2:
        return tail
    if head[0] > tail[0]:
        tail[0]+=1
    elif head[0] < tail[0]:
        tail[0]-=1

    if head[1] > tail[1]:
        tail[1] += 1
    elif head[1] < tail[1]:
        tail[1] -= 1
    return tail

with open('tempInput.txt') as f:
    f = f.read().split("\n")
    for step in f:
        direction, steps = step.split()
        print(f"{direction}, {steps}")
        for s in range(int(steps)):
            head = goTo(head, direction)
            tails[0] = happyTail(head, tails[0])
            for i in range(len(tails)-1):
                tails[i+1] = happyTail(tails[i], tails[i+1])
            tailPath.append(tuple(tails[8]))
            print(f"Happy Head, going to {head}, and tail does {tails}")


print(f"Happy Head is at {head} and tail {tails}")
uniqueTailPath = list(set(tailPath))
print(uniqueTailPath)
print(f"length is {len(uniqueTailPath)}")