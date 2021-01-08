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
        if i == "SOUTH" and (m[l+1][c] in " $SNEWBIT" or (m[l+1][c] == "X" and breaker)):
            return i
        elif i == "EAST" and (m[l][c+1] in " $SNEWBIT" or (m[l][c+1] == "X" and breaker)):
            return i
        elif i == "NORTH" and (m[l-1][c] in " $SNEWBIT" or (m[l-1][c] == "X" and breaker)):
            return i
        elif i == "WEST" and (m[l][c-1] in " $SNEWBIT" or (m[l][c-1] == "X" and breaker)):
            return i
    assert False

lines, C = [int(i) for i in input().split()]
m = []
tp = []
tp_dict = {}
l, c = 0, 0
for i in range(lines):
    row = list(input())
    log(row)
    m.append(row)
    for j in range(len(row)):
        if row[j] == "@":
            row[j] = " "
            l, c = i, j
        elif row[j] == "T":
            tp.append((i, j))

log(f"Pos {l} {c}")
if len(tp) > 0:
    assert len(tp) == 2
    tp_dict[tp[0]] = tp[1]
    tp_dict[tp[1]] = tp[0]

breaker = False
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
    elif p == "B":
        breaker = not breaker
    elif p == "X":
        m[l][c] = " "
    elif p == "I":
        dirs = dirs[::-1]
    elif p == "T":
        l, c = tp_dict[(l, c)]

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
