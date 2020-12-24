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

SKILL_REAPER = 1
SKILL_DESTR = 1
SKILL_DOOF = 1

MANY_WRECKS = 7



def dist(a, b, with_speed=True):
    if with_speed:
        return LA.norm(a.pos + a.v - b.pos - b.v)

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
        self.unit_type = "tanker"


class Reaper:
    def __init__(self, unit_id, mass, radius, x, y, vx, vy, old=None):
        self.id = unit_id
        self.m = mass
        self.r = radius
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])
        self.unit_type = "reaper"
        # self.old = old
        self.target_id = None
        if old:
            self.target_id = old.target_id


    @property
    def speed(self):
        return int(LA.norm(self.v))


class Bot:
    def __init__(self, unit_id, mass, radius, x, y, vx, vy, unit_type):
        self.id = unit_id
        self.m = mass
        self.r = radius
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])
        self.unit_type = unit_type

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
        self.tars = []
        self.oils = []
        self.other_bots = []


    def next_round(self):
        self.round += 1
        self.update_state()

        for sf, mf in [(self.skill_reaper, self.move_reaper),
                       (self.skill_destroyer_alt, self.move_destroyer),
                       (self.skill_doof, self.move_doof)]:
            skill = sf()
            if skill:
                print(skill)
                self.me.rage -= SKILL_COST
            else:
                print(mf())
        pass


    def update_state(self):
        self.wrecks = []
        self.tankers = []
        self.tars = []
        self.oils = []
        self.other_bots = []


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
            ['138', '5', '-1', '-1', '1000', '4312', '3477', '0', '0', '1', '-1']
            
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
            unit_type = int(inputs[1])  # 0 (Reaper), 1 (Destroyer), 3 (Tanker), 4 (Wreck), 5 (Tar), 6 (Oil)
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
            elif unit_type in (0, 1, 2):
                # we parse player unit
                assert player in (0, 1, 2) and extra == -1 and extra_2 == -1
                if player == 0:
                    plr = self.me
                else:
                    plr = self.enemies[player-1]
                if unit_type == 0:
                    # we parse Reaper
                    reaper = Reaper(unit_id, mass, radius, x, y, vx, vy, plr.reaper)
                    plr.reaper = reaper
                elif unit_type == 1:
                    # we parse Destroyer
                    destroyer = Bot(unit_id, mass, radius, x, y, vx, vy, "destroyer")
                    plr.destroyer = destroyer
                else:
                    # we parse Doof
                    doof = Bot(unit_id, mass, radius, x, y, vx, vy, "doof")
                    plr.doof = doof
            elif unit_type == 5:
                # we are parsing TAR, treat it as a bot for now for simplicity
                self.tars.append(Bot(unit_id, mass, radius, x, y, vx, vy, ""))

            elif unit_type == 6:
                # we are parsing OIL, treat it as a bot for now for simplicity
                self.oils.append(Bot(unit_id, mass, radius, x, y, vx, vy, ""))

            else:
                log(inputs)
                assert False

        en1, en2 = self.enemies
        self.other_bots = self.tankers + [en1.reaper, en1.destroyer, en1.doof, en2.reaper, en2.destroyer, en2.doof]


    def can_cast_skill(self):
        return self.me.rage >= SKILL_COST


    def wreak_occupied(self, wreck):
        cnt = 0
        for i in self.other_bots:
            if dist(wreck, i) < max(wreck.r, i.r):
                cnt += 1 + (i.unit_type == "reaper")
        return cnt > 1


    def move_reaper(self):
        bot = self.me.reaper
        wrecks = []

        # chasing old wreck, disabled for now
        # if bot.target_id:
        #     wrecks = list(filter(lambda x: x.id == bot.target_id, self.wrecks))
        #     log(f"Target {bot.target_id}  Found {len(wrecks)}")

        # looking for a new one
        if len(wrecks) == 0:
            # old target is gone
            bot.target_id = None

            for w in self.wrecks:
                if not self.wreak_occupied(w):
                    wrecks.append(w)

        if len(wrecks) == 0:
            # we don't have wrecks, so we follow our destroyer
            d = self.me.destroyer
            if dist(bot, d) < 1500:
                return f"WAIT WAIT DESTR"
            p = d.pos + d.v
            return f"{p[0]} {p[1]} 300 DESTR"

        # we have some wrecks around us
        w = min(wrecks, key=lambda x: dist(bot, x))
        # w = max(wrecks, key=lambda x: x.e)

        # updating target wreck
        bot.target_id = w.id

        if w.r > dist(bot, w, with_speed=False):
            # breaking mechanism
            p = bot.pos - bot.v
            throttle = min(max(bot.speed, 0), 300)
            return f"{p[0]} {p[1]} {throttle} BRK V:{bot.speed}"
            # return "WAIT WAIT"

        throttle = int(dist(bot, w))
        throttle = min(max(throttle, 0), 300)
        p = w.pos - bot.v
        return f"{p[0]} {p[1]} {throttle} T:{throttle} V:{bot.speed}"


    def skill_reaper(self):
        if not self.can_cast_skill() or SKILL_REAPER == 0:
            return None

        bot = self.me.reaper
        ds = [self.enemies[0].destroyer, self.enemies[1].destroyer]
        tankers = []
        for t in self.tankers:
            for tar in self.tars:
                if dist(t, tar) <= SKILL_RADIUS:
                    continue
            if dist(bot, t) <= SKILL_RANGE and dist(t, self.me.destroyer) > 3000:
                tankers.append(t)

        log(f"Reaper castable tanker: {len(tankers)}")
        for t in tankers:
            if dist(t, ds[0]) < 1000 or dist(t, ds[1]) < 1000:
                pos = t.pos + t.v
                return f"SKILL {pos[0]} {pos[1]} TAR {pos[0]} {pos[1]}"
        return None


    def move_destroyer(self):
        if len(self.wrecks) >= MANY_WRECKS:
            r = self.me.reaper
            return f"{r.pos[0]} {r.pos[1]} 300"

        bot = self.me.destroyer

        tankers = []
        for t in self.tankers:
            if dist(bot, t) < 3000:
                tankers.append(t)

        if len(tankers) == 0:
            tankers = self.tankers

        if len(tankers) == 0:
            return self.attack_reaper()

        # t = max(tankers, key=lambda x: x.e)
        t = min(tankers, key=lambda x: dist(bot, x))
        pos = t.pos + t.v
        # d = dist(bot, t)

        return f"{pos[0]} {pos[1]} 300"


    def skill_destroyer(self):
        if not self.can_cast_skill() or SKILL_DESTR == 0:
            return None

        bot = self.me.destroyer
        rprs = [self.enemies[0].reaper, self.enemies[1].reaper]
        wrecks = []
        for w in self.wrecks:
            if dist(bot, w) <= SKILL_RANGE:
                wrecks.append(w)
        log(f"Destr castable wrecks: {len(wrecks)}")
        for w in wrecks:
            if dist(w, rprs[0]) < w.r or dist(w, rprs[1]) < w.r:
                return f"SKILL {w.pos[0]} {w.pos[1]} BOOM {w.pos[0]} {w.pos[1]}"
        return None


    def skill_destroyer_alt(self):
        if not self.can_cast_skill() or SKILL_DESTR == 0:
            return None

        destr = self.me.destroyer
        reaper = self.me.reaper
        if dist(destr, reaper) < SKILL_RANGE:
            for i in self.other_bots:
                if dist(reaper, i) < SKILL_RADIUS:
                    pos = reaper.pos + reaper.v
                    return f"SKILL {pos[0]} {pos[1]} BOOM {pos[0]} {pos[1]}"
        return None

    def move_doof(self):
        return self.attack_reaper()


    def skill_doof(self):
        if not self.can_cast_skill() or SKILL_DOOF == 0:
            return None

        bot = self.me.doof
        rprs = [self.enemies[0].reaper, self.enemies[1].reaper]
        wrecks = []
        for w in self.wrecks:
            if dist(bot, w) <= SKILL_RANGE:
                wrecks.append(w)
        log(f"Doof castable wrecks: {len(wrecks)}")
        for w in wrecks:
            if dist(w, rprs[0]) < w.r or dist(w, rprs[1]) < w.r:
                return f"SKILL {w.pos[0]} {w.pos[1]} OIL {w.pos[0]} {w.pos[1]}"
        return None


    def attack_reaper(self):
        en = max(self.enemies, key=lambda x: x.score)
        bot = en.reaper
        pos = bot.pos + bot.v

        return f"{pos[0]} {pos[1]} 300 ATK"



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
