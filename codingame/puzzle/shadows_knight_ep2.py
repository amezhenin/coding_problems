"""
https://www.codingame.com/training/expert/shadows-of-the-knight-episode-2
"""

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
m[px][py] = 0

def dist(x, y, x2, y2):
    d = (x-x2)**2 + (y-y2)**2
    return d


# game loop
while True:
    bomb = input()
    # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    nx, ny = 0, 0
    max_dist = 0

    for i in range(w):
        for j in range(h):
            if m[i][j] == 1:
                d = dist(x, y, i, j)
                pd = dist(px, py, i, j)
                if (bomb == "COLDER" and d <= pd) or (bomb == "WARMER" and d >= pd) or (bomb == "SAME" and d != pd):
                    m[i][j] = 0
                else:
                    if d > max_dist:
                        max_dist = d
                        nx, ny = i, j
    px, py = x, y
    x, y = nx, ny
    m[px][py] = 0
    # log(f"Ones {ones}")
    print(f"{x} {y}")



"""
# SOLUTION with linear algebra. unfinished
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
def cmp(a, b):
    if a > b: return 1
    if a < b: return -1
    return 0

def dist(x, y, x2, y2):
    d = (x-x2)**2 + (y-y2)**2
    return d

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x1, y1 = [int(i) for i in input().split()]

m = np.ones(shape=(w, h))
m[x1][y1] = 0

# first time no direction
_ = input()
x2 = w - x1 - 1
y2 = h - y1 - 1
print(f"{x2} {y2}")

# game loop
while True:
    bomb = input()
    assert x1 - x2 != 0 or y1 - y2 != 0, "Same jump" 
    
    if x1 - x2 == 0:
        # log("dX == 0")
        if bomb == "COLDER":
            f = lambda _x, _y: cmp(_y, (y1 + y2) / 2) == -cmp(y2, (y1 + y2) / 2)
        elif bomb == "WARMER":
            f = lambda _x, _y: cmp(_y, (y1 + y2) / 2) == cmp(y2, (y1 + y2) / 2)
        else:
            f = lambda _x, _y: _y == (y1 + y2) / 2
    elif y1 - y2 == 0:
        # log("dY == 0")
        if bomb == "COLDER":
            f = lambda _x, _y: cmp(_x, (x1 + x2) / 2) == -cmp(x2, (x1 + x2) / 2)
        elif bomb == "WARMER":
            f = lambda _x, _y: cmp(_x, (x1 + x2) / 2) == cmp(x2, (x1 + x2) / 2)
        else:
            f = lambda _x, _y: _x == (x1 + x2) / 2
    else:
        # log("dX != 0 and dY != 0")
        b = (y1 + y2) / 2 + 2 * ((x1 - x2) / (y1 - y2))
        left = lambda _x, _y: _y + _x * ((x1-x2) / (y1-y2))
        log(f"B: {b} LEFT2: {cmp(left(x2, y2), b)}")
        if bomb == "COLDER":
            f = lambda _x, _y: cmp(left(_x, _y), b) == -cmp(left(x2, y2), b)
        elif bomb == "WARMER":
            f = lambda _x, _y: cmp(left(_x, _y), b) == cmp(left(x2, y2), b)
        else:
            f = lambda _x, _y: left(_x, _y) == b

    max_dist = 0
    nx, ny = x2, y2
    ones = 0
    for i in range(w):
        for j in range(h):
            if m[i][j] == 0:
                continue

            if f(i, j) is False:
                m[i][j] = 0
            else:
                ones += 1
                next_dist = dist(i, j, x2, y2)
                if next_dist > max_dist:
                    max_dist = next_dist
                    nx, ny = i, j
    x1, y1 = x2, y2
    x2, y2 = nx, ny
    m[x1][y1] = 0
    log(f"Ones {ones}")
    print(f"{x2} {y2}")

"""