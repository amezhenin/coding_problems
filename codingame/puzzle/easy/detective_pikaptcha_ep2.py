"""
https://www.codingame.com/training/easy/detective-pikaptcha-ep2

Input:
5 3
>000#
#0#00
00#0#
L

Output:
1322#
#2#31
12#1#
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def next_side(cur_heading, prior):
    idx = prior.find(cur_heading)
    idx = (idx + 1) % len(prior)
    return prior[idx]

width, height = [int(i) for i in input().split()]

x, y, z = 0, 0, ">"

lines = ["#" * (width + 2)]
steps = [[0] * (width + 1)] * (height+1)
for i in range(height):
    line = input()
    for c in ">v<^":
        idx = line.find(c)
        if idx >= 0:
            x = idx
            y = i
            z = c
            # steps[y][x] = 1
            line.replace(c, '0')
    line = f"#{line}#"
    lines.append(line)

lines.append("#" * (width + 2))
side = input()

# priority for L side
if side == "L":
    prior = ">v<^"
else:
    prior = ">^<v"

orig_x, orig_y = x, y

while steps[orig_y][orig_x] != 1:
    if z == ">":
        next_x, next_y = y, x + 1
    elif z == "<":
        next_x, next_y = y, x - 1
    elif z == "^":
        next_x, next_y = y + 1, x
    else:
        next_x, next_y = y - 1, x

    if lines[next_y][next_x] == "0":
        # step there
        steps[next_y][next_x] += 1
        x, y = next_x, next_y
    else:
        # turn
        z = next_side(z, prior)



for i in range(height):
    for j in range(width):
        if lines[i+1][j+1] == "#":
            print("#", end="")
        else:
            print(str(steps[i+1][j+1]), end="")
    print("")
