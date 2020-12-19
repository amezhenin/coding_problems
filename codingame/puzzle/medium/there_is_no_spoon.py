"""
https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1
"""

import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
m = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    m.append(line)
log("\n".join(m))
for i in range(height):
    for j in range(width):
        if m[i][j] != "0":
            continue
        ri, rj = -1, -1
        di, dj = -1, -1
        jj = j + 1
        while jj < width:
            if m[i][jj] == "0":
                ri, rj = i, jj
                break
            jj += 1

        ii = i + 1
        while ii < height:
            if m[ii][j] == "0":
                di, dj = ii, j
                break
            ii += 1

        print(f"{j} {i} {rj} {ri} {dj} {di}")

