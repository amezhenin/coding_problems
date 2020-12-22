"""
https://www.codingame.com/multiplayer/bot-programming/mean-max
"""
import sys
import numpy as np
from numpy import linalg as LA


def log(msg):
    print(msg, file=sys.stderr, flush=True)

ARENA = 6000
TOWN_RADIS = 3000
SKILL_RANGE = 2000
SKILL_RADIUS = 1000
SKILL_COST = 60


def dist(a, b, with_speed=True):
    if with_speed:
        LA.norm(a.pos + a.v - b.pos - b.v)

    return LA.norm(a.pos - b.pos)

class Wreck:
    def __init__(self, unit_id, radius, x, y, extra):
        self.id = unit_id
        self.r = radius
        self.pos = np.array([x, y])
        self.v = np.array([0, 0])  # need it to calculate distance with speed compensation
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


class Bot:
    def __init__(self, unit_id, mass, radius, x, y, vx, vy):
        self.id = unit_id
        self.m = mass
        self.r = radius
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])

    @property
    def speed(self):
        return int(LA.norm(self.v))


class Player:
    def __init__(self):
        self.score = 0
        self.rage = 0
        self.reaper = None
        self.destroyer = None
        self.doof = None


class Game:
    def __init__(self):
        self.round = 0
        self.me = Player()
        self.enemies = [Player(), Player()]
        self.wrecks = []
        self.tankers = []

        s = np.sqrt(2)
        points = [[ARENA, 0], [ARENA//s, -ARENA//s],
                  [0, -ARENA], [-ARENA//s, -ARENA//s],
                  [-ARENA, 0], [-ARENA//s, ARENA//s],
                  [0, ARENA], [ARENA//s, ARENA//s]]
        self.doof_points = list(map(lambda x: np.array([int(x[0]), int(x[1])]), points))
        self.next_doof_point = 0


    def next_round(self):
        self.round += 1
        self.update_state()

        print(self.move_reaper())
        print(self.move_destroyer())
        print(self.move_doof())


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
                    0            0         0     0.5       400  -2679   3862   121  -266       -1         -1
                    1            1         0     1.5       400  -1970   3041   365  -301       -1         -1
                    2            2         0     1         400    514   5083    -8    65       -1         -1
                    3            0         1     0.5       400  -1746   1115   474  -698       -1         -1
                    4            1         1     1.5       400  -1233  -2595    42   181       -1         -1
                    5            2         1     1         400  -1450   -716   407   376       -1         -1
                    6            0         2     0.5       400  -1145    122   384  -784       -1         -1
                    7            1         2     1.5       400   2634    465  -333   110       -1         -1
                    8            2         2     1         400   2961   4241   -31  -356       -1         -1
                   15            3        -1     3.5       800   -736   2524    71  -239        2          8
                   19            3        -1     3         800  -3392  -2613   191   150        1          8
                   20            3        -1     3         850  -4895  -4033   176   142        1          9
                   21            3        -1     3         800   5142  -2005  -237    92        1          8
                   24            3        -1     3         800  -1244   8139    51  -336        1          8
                   25            3        -1     3         850   7734  -2963  -318   122        1          9
                   22            4        -1    -1         800   2039    338     0     0        5         -1
                   23            4        -1    -1         800   -716  -1927     0     0        5         -1
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
                assert mass == -1 and extra_2 == -1 and vx == 0 and vy == 0
                w = Wreck(unit_id, radius, x, y, extra)
                self.wrecks.append(w)
            elif player == -1 and unit_type == 3:
                # we parse tanker
                assert extra > 0 and extra_2 > 0
                t = Tanker(unit_id, mass, radius, x, y, vx, vy, extra, extra_2)
                self.tankers.append(t)
            else:
                # we parse player unit
                assert player in (0, 1, 2) and unit_type in (0, 1, 2) and extra == -1 and extra_2 == -1
                if player == 0:
                    plr = self.me
                else:
                    plr = self.enemies[player-1]
                if unit_type == 0:
                    # we parse Reaper
                    reaper = Bot(unit_id, mass, radius, x, y, vx, vy)
                    plr.reaper = reaper
                elif unit_type == 1:
                    # we parse Destroyer
                    destroyer = Bot(unit_id, mass, radius, x, y, vx, vy)
                    plr.destroyer = destroyer
                else:
                    # we parse Doof
                    doof = Bot(unit_id, mass, radius, x, y, vx, vy)
                    plr.doof = doof
                    pass
                pass
        pass


    def can_cast_skill(self):
        return self.me.rage >= SKILL_COST


    def move_reaper(self):
        bot = self.me.reaper

        if len(self.wrecks) == 0:
            # we don't have wrecks, so we follow our destroyer
            d = self.me.destroyer
            if dist(bot, d) < 2000:
                return f"WAIT WAIT DESTR"
            p = d.pos + d.v
            return f"{p[0]} {p[1]} 300 DESTR"

        # we have some wrecks
        w = self.wrecks[0]
        d = dist(bot, w, with_speed=False)

        for i in self.wrecks:
            dd = dist(bot, i, with_speed=False)
            if dd < d:
                w = i
                d = dd

        if w.r > d:
            # breaking mechanism
            alt_d = dist(bot, w, with_speed=True)
            log(f"D {d} ALT {alt_d}")
            if w.r < alt_d:
                p = bot.pos - bot.v
                return f"{p[0]} {p[1]} 100 BREAKING V:{bot.speed}"
            log("Collecting water")
            return "WAIT WAIT"

        throttle = int(d - bot.speed)
        throttle = min(max(throttle, 0), 300)
        p = w.pos - bot.v
        return f"{p[0]} {p[1]} {throttle} T:{throttle} V:{bot.speed}"


    def move_destroyer(self):
        bot = self.me.destroyer

        tankers = self.tankers
        if len(tankers) == 0:
            return "WAIT WAIT"

        t = tankers[0]
        d = dist(bot, t)

        for i in tankers:
            dd = dist(bot, i)
            if dd < d:
                t = i
                d = dd
        return f"{t.pos[0]} {t.pos[1]} 300 {int(d)}"


    def move_doof(self):
        bot = self.me.doof
        t = self.doof_points[self.next_doof_point]
        d = LA.norm(bot.pos - t)
        if d < 2000:
            log("Next CP")
            self.next_doof_point = (self.next_doof_point + 1) % len(self.doof_points)
            t = self.doof_points[self.next_doof_point]
            d = LA.norm(bot.pos - t)

        return f"{t[0]} {t[1]} 300"



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
