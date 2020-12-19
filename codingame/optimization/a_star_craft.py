"""
https://www.codingame.com/ide/puzzle/a-star-craft
"""

m = []

for i in range(10):
    line = input()
    m.append(line)
robot_count = int(input())
for i in range(robot_count):
    inputs = input().split()
    x = int(inputs[0])
    y = int(inputs[1])
    direction = inputs[2]

res = []

for i in range(10):
    for j in range(19):
        u = m[i - 1][j]
        d = m[(i + 1) % 10][j]
        l = m[i][j - 1]
        r = m[i][(j + 1) % 19]
        x = m[i][j]

        if x != ".":
            continue

        if u + r + d == "###":
            res.append(f"{j} {i} L")
            continue
        if r + d + l == "###":
            res.append(f"{j} {i} U")
            continue
        if d + l + u == "###":
            res.append(f"{j} {i} R")
            continue
        if l + u + r == "###":
            res.append(f"{j} {i} D")
            continue

        if u + r + d == ".##":
            res.append(f"{j} {i} L")
            continue
        if r + d + l == ".##":
            res.append(f"{j} {i} U")
            continue
        if d + l + u == ".##":
            res.append(f"{j} {i} R")
            continue
        if l + u + r == ".##":
            res.append(f"{j} {i} D")
            continue



print(" ".join(res))
