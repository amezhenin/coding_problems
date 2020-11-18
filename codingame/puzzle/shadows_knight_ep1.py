"""
https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1
"""
import sys
from collections import namedtuple


Grid = namedtuple('Grid', ['left', 'top', 'right', 'bottom'])


def log(msg):
    print(msg, file=sys.stderr, flush=True)


if __name__ == "__main__":
    w, h = [int(i) for i in input().split()]
    n = int(input())  # maximum number of turns before game over.
    x, y = map(int, input().split())
    grid = Grid(0, 0, w-1, h-1)
    log(str(grid))

    for _ in range(n):
        bomb_dir = input()
        log("Dir: %s" % bomb_dir)

        if bomb_dir == "U":
            grid = Grid(x, grid.top, x, y-1)
        elif bomb_dir == "UR":
            grid = Grid(x+1, grid.top, grid.right, y-1)
        elif bomb_dir == "R":
            grid = Grid(x+1, y, grid.right, y)
        elif bomb_dir == "DR":
            grid = Grid(x+1, y+1, grid.right, grid.bottom)
        elif bomb_dir == "D":
            grid = Grid(x, y+1, x, grid.bottom)
        elif bomb_dir == "DL":
            grid = Grid(grid.left, y+1, x-1, grid.bottom)
        elif bomb_dir == "L":
            grid = Grid(grid.left, y, x-1, y)
        elif bomb_dir == "UL":
            grid = Grid(grid.left, grid.top, x-1, y-1)
        else:
            log("Direction: " + bomb_dir)

        log(str(grid))
        x = (grid.left + grid.right) // 2
        y = (grid.top + grid.bottom) // 2

        print("%s %s" % (x, y))
    pass

