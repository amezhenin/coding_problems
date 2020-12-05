"""
https://www.codingame.com/ide/puzzle/the-labyrinth


# -- wall
T -- current position
C -- control room
. -- empty
? -- unexplored, we init to 9999 because we will initiate it if it is reachable


10 30 23
3 6
??????????????????????????????
????.....?????????????????????
????#####?????????????????????
????..T..?????????????????????
????.....?????????????????????
????#####?????????????????????
??????????????????????????????
??????????????????????????????
??????????????????????????????
??????????????????????????????

FIXME: we ignore countdown during exploration process, but it worked anyways
FIXME: there is a bug with exploration, which I couldn't find
"""
from collections import deque
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


K = 10000
# K = 9
DIRECTION = ((-1, 0, "DOWN"), (1, 0, "UP"), (0, -1, "RIGHT"), (0, 1, "LEFT"))


class Game:
    def __init__(self, char_map=None):
        self.char_map = char_map
        self.dist_map = None
        self.explore = None
        self.ctrl_row = None
        self.ctrl_col = None
        self.kirk_row = None
        self.kirk_col = None
        self.start_row = None
        self.start_col = None
        self.rows = None
        self.cols = None
        self.countdown = None
        self.alarm_activate = False


    def loop(self):
        self.rows, self.cols, self.countdown = map(int, input().split())
        log(f"{self.rows} {self.cols} {self.countdown}")
        self.rows += 2
        self.cols += 2
        while True:
            # we will add walls around arena
            self.kirk_row, self.kirk_col = map(int, input().split())
            self.kirk_row += 1
            self.kirk_col += 1
            log(f"Kirk: {self.kirk_col} {self.kirk_row}")

            self.char_map = ["#" + input() + "#" for i in range(self.rows-2)]
            self.char_map = ["#" * self.cols] + self.char_map + ["#" * self.cols]

            # for i in self.char_map: log(i)
            self.a_star()
            # for i in self.dist_map: log(i)

            if self.kirk_row == self.ctrl_row and self.kirk_col == self.ctrl_col:
                self.alarm_activate = True

            if self.alarm_activate:
                log("Alarm")
                self.move(self.start_row, self.start_col)
            # we see control room and we know how to reach it
            elif self.ctrl_row is not None and self.dist_map[self.ctrl_row][self.ctrl_col] < K:
                log("Move to control")
                self.move(self.ctrl_row, self.ctrl_col)
            else:
                log("Explore")
                r, c = self.next_explore()
                self.move(r, c)


    def a_star(self):

        self.rows = len(self.char_map)
        self.cols = len(self.char_map[0])
        self.dist_map = []
        for i in range(self.rows):
            dist_row = []
            for j in range(self.cols):
                dist_row.append(K if self.char_map[i][j] != "#" else -K)
                if self.char_map[i][j] == "C":
                    self.ctrl_row, self.ctrl_col = i, j
                if self.char_map[i][j] == "T":
                    self.start_row, self.start_col = i, j
            self.dist_map.append(dist_row)

        self.explore = []
        # we always should have Kirk on the map and start from there
        q = deque([(self.kirk_row, self.kirk_col)])
        self.dist_map[self.kirk_row][self.kirk_col] = 0

        while len(q) > 0:
            r, c = q.popleft()

            for v, w, _ in DIRECTION:
                x = self.char_map[r+v][c+w]
                if x != "#" and self.dist_map[r+v][c+w] > self.dist_map[r][c] + 1:
                    self.dist_map[r + v][c + w] = self.dist_map[r][c] + 1
                    if x != "?":
                        q.append((r + v, c + w))
                    else:
                        self.explore.append((self.dist_map[r + v][c + w], r + v, c + w))
        # sort by distance to unexplored area
        pass


    def move(self, r, c):
        log(f"Moving from {self.kirk_row} {self.kirk_col} to {r} {c}")
        last_dir = None
        while r != self.kirk_row or c != self.kirk_col:
            for v, w, d in DIRECTION:
                if self.dist_map[r + v][c + w] + 1 == self.dist_map[r][c]:
                    r += v
                    c += w
                    last_dir = d
                pass
        print(last_dir)


    def next_explore(self):
        self.explore.sort()
        res = self.explore[0]
        # if we saw a control room we should be moving towards her first
        # FIXME: there should be counter map for this greedy algorithm, but not in tests
        if self.ctrl_row:
            dist = K
            for i in self.explore:
                new_dist = abs(self.ctrl_row-res[1]) + abs(self.ctrl_col-res[2])
                if dist > new_dist:
                    dist = new_dist
                    res = i
        return res[1], res[2]


if __name__ == "__main__":
    game = Game()
    game.loop()
    pass
