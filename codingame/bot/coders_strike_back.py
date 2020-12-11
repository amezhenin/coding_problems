import sys
import math
import collections
import numpy as np
from numpy import linalg as LA

"""
TODO:
    * attach enemy ahead in race, not closest one
"""


def log(msg):
    print(msg, file=sys.stderr, flush=True)


Bot = collections.namedtuple("Bot", "x y vx vy angle cp_id cp_x cp_y")

COMPENSATION = 2
CP_RADIUS = 600
BOT_RADIUS = 400
MAX_THRUST = 100


def unit_vector(vector):
    return vector / LA.norm(vector)


def deg_to_vector(d):
    return unit_vector(np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))]))


def is_same_direction(bot, speed, checkpoint):
    if LA.norm(speed) == 0 or LA.norm(checkpoint - bot) == 0:
        return 1.0

    l = LA.norm(unit_vector(checkpoint - bot) + unit_vector(speed))
    # if l > math.sqrt(2):
    #     return 1.0
    # penalty = math.sqrt(2) - l
    return l > math.sqrt(2)


class Game:
    def __init__(self):
        self.round = 0
        self.enemies = []
        self.laps = int(input())  # FIXME: start using this to determine last checkpoint
        cp_count = int(input())
        self.checkpoints = []
        for i in range(cp_count):
            x, y = map(int, input().split())
            self.checkpoints.append((x, y))
        log(f"{len(self.checkpoints)} checkpoints: {self.checkpoints}")


    def read_bot(self):
        x, y, vx, vy, angle, cp_id = map(int, input().split())
        bot = Bot(x, y, vx, vy, angle, cp_id, self.checkpoints[cp_id][0], self.checkpoints[cp_id][1])
        return bot


    def adjust_cp_coord(self, bot):
        # log(f"Bot: {bot}")
        if bot.vx != 0:
            t = (bot.cp_x - bot.x) / bot.vx
        elif bot.vy != 0:
            t = (bot.cp_y - bot.y) / bot.vy
        else:
            # log(f"Zero speed")
            return bot.cp_x, bot.cp_y

        px = (t * bot.vx) + bot.x
        py = (t * bot.vy) + bot.y

        # minimum distance to checkpoint center
        dist = LA.norm(np.array([bot.cp_x - px, bot.cp_y - py]))
        # log(f"Min CP dist: {dist} in {t} rounds")
        if dist < CP_RADIUS:
            if t < 3:
                next_cp_id = (bot.cp_id + 1) % len(self.checkpoints)
                log(f"Switching to CP {next_cp_id}")
                next_cp = self.checkpoints[next_cp_id]
                return next_cp[0], next_cp[1]
            return px, py


        nx = bot.cp_x - int(bot.vx * COMPENSATION)
        ny = bot.cp_y - int(bot.vy * COMPENSATION)
        return nx, ny


    def move_to_checkpoint(self, bot):

        dist = math.hypot(abs(bot.x - bot.cp_x), abs(bot.y - bot.cp_y))

        same_dir = is_same_direction(
            np.array([bot.x, bot.y]),
            # np.array([bot.vx, bot.vy]),
            deg_to_vector(bot.angle),
            np.array([bot.cp_x, bot.cp_y])
        )
        if self.round == 1:
            thrust = "BOOST"
        elif not same_dir:
            thrust = 0
        elif dist < 2000:
            thrust = 30
        elif dist < 1000:
            thrust = 20
        # elif next_checkpoint_dist < 500 and math.hypot(abs(x - opponent_x), abs(y - opponent_y)) < 850:
        #     thrust = "SHIELD"
        else:
            thrust = 100

        if self.shield_needed(bot):
            thrust = "SHIELD"

        nx, ny = self.adjust_cp_coord(bot)

        print("%s %s %s CP:%s" % (int(nx), int(ny), thrust, thrust))


    def shield_needed(self, bot):
        min_dist = BOT_RADIUS * 100
        for en in self.enemies:
            d = math.hypot(abs(bot.x + bot.vx - en.x - en.vx), abs(bot.y + bot.vy - en.y - en.vy))
            min_dist = min(min_dist, d)
        log(f"Min enemy dist {min_dist}")
        return min_dist <= (BOT_RADIUS + MAX_THRUST) * 2


    def attack(self, bot):
        en1, en2 = self.enemies
        # d1 = math.hypot(abs(bot.x - en1.x), abs(bot.y - en1.y))
        # d2 = math.hypot(abs(bot.x - en2.x), abs(bot.y - en2.y))
        # enemy, dist = en1, d1
        # if d1 > d2:
        #     enemy, dist = en2, d2
        enemy = en1 if en1.cp_id >= en2.cp_id else en2
        dist = math.hypot(abs(bot.x - enemy.x), abs(bot.y - enemy.y))

        nx = enemy.x - int(enemy.vx * COMPENSATION)
        ny = enemy.y - int(enemy.vy * COMPENSATION)
        thrust = 100
        if self.shield_needed(bot):
            thrust = "SHIELD"
        print("%s %s %s AT:%s" % (nx, ny, thrust, thrust))


    def next_round(self):
        self.round += 1

        bot1 = self.read_bot()
        bot2 = self.read_bot()

        en1 = self.read_bot()
        en2 = self.read_bot()
        self.enemies = [en1, en2]

        self.move_to_checkpoint(bot1)
        #self.move_to_checkpoint(bot2)
        self.attack(bot2)




if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()

