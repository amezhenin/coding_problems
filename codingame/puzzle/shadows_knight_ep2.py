"""
https://www.codingame.com/training/expert/shadows-of-the-knight-episode-2
"""
import math
import numpy as np

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)
#
# DEBUG = False
#
# def debug_input():
#     __i = orig_input()
#     print(">"+__i, file=sys.stderr, flush=True)
#     return __i
# if DEBUG:
#     orig_input = input
#     input = debug_input


# with open("input.txt") as fd:
#     __inp = fd.readlines()
#     __inp = map(str, __inp)
# def input():
#     return next(__inp)[:-1]



# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
px, py = [int(i) for i in input().split()]

m = np.ones(shape=(w, h))

# first time no direction
_ = input()
x = w - px - 1
y = h - py - 1
print(f"{x} {y}")


def dist(x, y, x2, y2):
    d = (x-x2)**2 + (y-y2)**2
    return d


# game loop
while True:
    bomb = input()
    # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    tx, ty, tc, lx, ly = 0, 0, 0, 0, 0
    marked = 0
    for i in range(w):
        for j in range(h):
            if m[i][j] == 1:
                d = dist(x, y, i, j)
                pd = dist(px, py, i, j)
                if (bomb == "COLDER" and d <= pd) or (bomb == "WARMER" and d >= pd) or (bomb == "SAME" and d != pd):
                    m[i][j] = 0
                    marked = 1
                else:
                    lx, ly = i, j
                    tx += i
                    ty += j
                    tc += 1
    log(f"T: {tc} {tx} {ty}")
    px, py = x, y
    x = round(tx / tc)
    y = round(ty / tc)
    if marked == 0 or (px == x and py == y):
        x, y = lx, ly
    print(f"{x} {y}")
