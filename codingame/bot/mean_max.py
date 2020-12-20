"""
https://www.codingame.com/multiplayer/bot-programming/mean-max
"""
import sys
import numpy as np
from numpy import linalg as LA


def log(msg):
    print(msg, file=sys.stderr, flush=True)


class Wreck:
    def __init__(self, unit_id, radius, x, y, vx, vy, extra):
        self.id = unit_id
        self.r = radius
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])
        self.e = extra  # water in the wreck

class Tanker:
    def __init__(self, unit_id, mass, radius, x, y, vx, vy, extra, extra_2):
        self.id = unit_id
        self.m = mass
        self.r = radius
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])
        self.e = extra  # water in the tanker
        self.ee = extra_2  # max capacity of the tanker

class Reaper:
    def __init__(self, unit_id, mass, radius, x, y, vx, vy,):
        self.id = unit_id
        self.m = mass
        self.r = radius
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])

class Destroyer:
    def __init__(self, unit_id, mass, radius, x, y, vx, vy,):
        self.id = unit_id
        self.m = mass
        self.r = radius
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])


class Player:
    def __init__(self):
        self.score = 0
        self.rage = 0
        self.reaper = None
        self.destroyer = None


class Game:
    def __init__(self):
        self.round = 0
        self.me = Player()
        self.enemies = [Player(), Player()]
        self.wrecks = []
        self.tankers = []


    def next_round(self):
        self.round += 1
        self.update_state()

        print(self.move_reaper())
        print(self.move_destroyer())
        print(f"WAIT")


    def update_state(self):
        self.wrecks = []
        self.tankers = []

        self.me.score = int(input())
        self.enemies[0].score = int(input())
        self.enemies[1].score = int(input())

        self.me.rage = int(input())
        self.enemies[0].rage = int(input())
        self.enemies[1].rage = int(input())

        unit_count = int(input())
        for i in range(unit_count):
            inputs = input().split()
            # log(inputs)
            """
              unit_id    unit_type    player    mass    radius      x      y    vx    vy    extra    extra_2
            ---------  -----------  --------  ------  --------  -----  -----  ----  ----  -------  ---------
                    0            0         0     0.5       400  -1258   2210   303  -232       -1         -1
                    1            1         0     1.5       400   -276   2291     0     0       -1         -1
                    2            0         1     0.5       400  -2398  -4576  -112  -267       -1         -1
                    3            1         1     1.5       400  -1584  -5217   170    68       -1         -1
                    4            0         2     0.5       400   4883    177   193  -299       -1         -1
                    5            1         2     1.5       400   5456   1129  -192   162       -1         -1
                    6            3        -1     4         850   1802   1843  -180   -74        3          9
                    7            3        -1     3.5       850  -2647    604   240  -117        2          9
                    8            3        -1     4         850    690  -2473    26   193        3          9
                    9            3        -1     3         850   3440   1219  -159  -120        1          9
                   10            3        -1     3         850  -2881   2294   177  -113        1          9
                   11            3        -1     3         850   -660  -3591   -24   197        1          9
                   13            3        -1     3         650  -1806   3350   108   -47        1          5
                   17            3        -1     3         600    189   5737    -9  -257        1          4
                   18            3        -1     3         600   4876  -3036  -218   136        1          4
                   15            4        -1    -1         650   5030    867     0     0        1         -1
                   16            4        -1    -1         650  -1761  -4790     0     0        1         -1
            """
            unit_id = int(inputs[0])
            unit_type = int(inputs[1])  # 0 (Reaper), 1 (Destroyer), 3 (Tanker), 4 (Wreck)
            player = int(inputs[2])
            mass = float(inputs[3])
            radius = int(inputs[4])
            x = int(inputs[5])
            y = int(inputs[6])
            vx = int(inputs[7])
            vy = int(inputs[8])
            extra = int(inputs[9])
            extra_2 = int(inputs[10])

            if player == -1 and unit_type == 4:
                # we parse wrecks
                assert mass == -1 and extra_2 == -1
                w = Wreck(unit_id, radius, x, y, vx, vy, extra)
                self.wrecks.append(w)
            elif player == -1 and unit_type == 3:
                # we parse tanker
                t = Tanker(unit_id, mass, radius, x, y, vx, vy, extra, extra_2)
                self.tankers.append(t)
            else:
                # we parse player unit
                assert player in (0, 1, 2) and unit_type in (0, 1) and extra == -1 and extra_2 == -1
                if player == 0:
                    plr = self.me
                else:
                    plr = self.enemies[player-1]
                if unit_type == 0:
                    # we parse Reaper
                    reaper = Reaper(unit_id, mass, radius, x, y, vx, vy)
                    plr.reaper = reaper
                else:
                    # we parse Destroyer
                    destroyer = Destroyer(unit_id, mass, radius, x, y, vx, vy)
                    plr.destroyer = destroyer
                pass
        pass


    def move_reaper(self):
        bot = self.me.reaper

        if len(self.wrecks) == 0:
            # we don't have wrecks, so we follow our destroyer
            # TODO: destroyer can be moving
            d = self.me.destroyer
            return f"{d.pos[0]} {d.pos[1]} 300 DESTR"

        # we have some wrecks
        w = self.wrecks[0]
        d = LA.norm(bot.pos - w.pos)

        for i in self.wrecks:
            dd = LA.norm(bot.pos - i.pos)
            if dd < d:
                w = i
                d = dd

        throttle = 300
        if w.r > d:
            # throttle = 0
            log("Collecting water")
            return "WAIT WAIT"
        elif d < 1000:
            throttle = 100
        elif d < 2000:
            throttle = 200
        return f"{w.pos[0]} {w.pos[1]} {throttle} {throttle} {int(d)}/{w.r}"


    def move_destroyer(self):
        bot = self.me.destroyer

        tankers = self.tankers
        tankers = list(filter(lambda x: x.e > 0, tankers))
        log(f"Tankers with water {len(tankers)}/{len(self.tankers)}")
        if len(tankers) == 0:
            return "WAIT WAIT"

        # TODO: distance should take into account speed
        t = self.tankers[0]
        d = LA.norm(bot.pos - t.pos)

        for i in tankers:
            dd = LA.norm(bot.pos - i.pos)
            if dd < d:
                t = i
                d = dd
        return f"{t.pos[0]} {t.pos[1]} 300 {int(d)}"



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
