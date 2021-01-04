"""
https://www.codingame.com/ide/puzzle/samegame
"""
import sys


# Remove connected regions of the same color to obtain the best score.
def log(msg):
    print(msg, file=sys.stderr, flush=True)


SIZE = 15
# SIZE = 3


def dfs(x, y, c, w, count=0):
    count += 1
    w[x][y] = 1
    if x > 0 and c[x][y] == c[x-1][y] and w[x-1][y] == 0:
        count = dfs(x-1, y, c, w, count)
    if x < SIZE-1 and c[x][y] == c[x+1][y] and w[x+1][y] == 0:
        count = dfs(x+1, y, c, w, count)
    if y > 0 and c[x][y] == c[x][y-1] and w[x][y-1] == 0:
        count = dfs(x, y-1, c, w, count)
    if y < SIZE-1 and c[x][y] == c[x][y+1] and w[x][y+1] == 0:
        count = dfs(x, y+1, c, w, count)
    return count

# game loop
while True:
    c = []
    w = [([0] * SIZE) for i in range(SIZE)]
    for i in range(SIZE):
        l = list(map(int, input().split()))
        c.append(l)
    log(c)
    mw = 0
    mi, mj = -1, -1
    for i in range(SIZE):
        for j in range(SIZE):
            if c[i][j] != -1 and w[i][j] == 0:
                new_max = dfs(i, j, c, w)
                log(f"{i} {j} Count: {new_max}")
                if new_max > mw:
                    mw = new_max
                    mi, mj = i, j


    print(f"{mj} {SIZE-mi-1}")
