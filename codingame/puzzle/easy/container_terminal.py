"""
https://www.codingame.com/training/easy/container-terminal
"""

def alg(line):
    stacks = []
    for c in line:
        idx = None
        for i in range(len(stacks)):
            if stacks[i] >= c:
                idx = i
                break
        if idx is None:
            stacks.append(c)
        else:
            stacks[idx] = c

    return len(stacks)


n = int(input())
for i in range(n):
    line = input()
    print(alg(line))

