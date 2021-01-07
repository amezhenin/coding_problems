"""
https://www.codingame.com/ide/puzzle/bender-episode-1

5 5
#####
#@  #
#   #
#  $#
#####
"""
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)

dirs = ["SOUTH", "EAST", "NORTH", "WEST"]
def next_dir(cur_dir):
    for i in [cur_dir] + dirs:
        if i == "SOUTH" and m[l+1][c] in " $SNEW":
            return i
        elif i == "EAST" and m[l][c+1] in " $SNEW":
            return i
        elif i == "NORTH" and m[l-1][c] in " $SNEW":
            return i
        elif i == "WEST" and m[l][c-1] in " $SNEW":
            return i
    assert False

lines, C = [int(i) for i in input().split()]
m = []
l, c = 0, 0
for i in range(lines):
    row = list(input())
    log(row)
    m.append(row)
    for j in range(len(row)):
        if row[j] == "@":
            row[j] = " "
            l, c = i, j

log(f"Pos {l} {c}")

d = "SOUTH"
steps = []
for _ in range(1000):
    p = m[l][c]
    log(f"L {l} C {c} '{p}' {d}")
    if p == "$":
        for s in steps:
            print(s)
        log("exit")
        exit(1)
    elif p == "S":
        d = "SOUTH"
    elif p == "N":
        d = "NORTH"
    elif p == "W":
        d = "WEST"
    elif p == "E":
        d = "EAST"

    d = next_dir(d)
    steps.append(d)
    if d == "SOUTH":
        l = l + 1
    elif d == "EAST":
        c = c + 1
    elif d == "NORTH":
        l = l - 1
    else:  # d == "WEST"
        c = c - 1
    pass



print("LOOP")
