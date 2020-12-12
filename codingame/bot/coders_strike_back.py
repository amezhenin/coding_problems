import sys
import math

import numpy as np
from numpy import linalg as LA


def log(msg):
    print(msg, file=sys.stderr, flush=True)


COMPENSATION = 2
CP_RADIUS = 600
BOT_RADIUS = 400
MAX_THRUST = 100


def unit_vector(vector):
    return vector / LA.norm(vector)


def deg_to_vector(d):
    return unit_vector(np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))]))



class Bot:
    def __init__(self, x, y, vx, vy, angle, cp_id, checkpoints):
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])
        self.angle = deg_to_vector(angle)
        self.cp_id = cp_id
        self.cp = checkpoints[cp_id]
        self.checkpoints = checkpoints


    def __repr__(self):
        return str(self.pos)


    def next_checkpoint(self):
        """
        Return checkpoint AFTER next one
        """
        idx = (self.cp_id + 1) % len(self.checkpoints)
        return self.checkpoints[idx]


    def is_same_direction(self):
        if LA.norm(self.cp - self.pos) == 0:
            return True

        # log(f"Bot: {self.cp} {self.pos} {self.v}")
        l = LA.norm(unit_vector(self.cp - self.pos) + unit_vector(self.angle))
        log(f"Bot: {self} Norm {l}")
        return l > math.sqrt(2)


    def adjust_cp_coord(self):
        # log(f"Bot: {self}")
        if LA.norm(self.v) != 0:
            t = min((self.cp - self.pos) / (self.v + 1e-20))
        else:
            # log(f"Zero speed")
            return self.cp, False

        pos = (t * self.v) + self.pos

        # minimum distance to checkpoint center
        dist = LA.norm(self.cp - pos)
        # log(f"Min CP dist: {dist} in {t} rounds")
        if dist < CP_RADIUS:
            if t < 3.5:
                # log(f"Switching to CP after next")
                next_cp = self.next_checkpoint()
                return next_cp, True
            return pos, False

        new = self.cp - self.v * COMPENSATION
        return new, False


class Game:
    def __init__(self):
        self.round = 0
        self.enemies = []
        self.laps = int(input())  # FIXME: start using this to determine last checkpoint
        cp_count = int(input())
        self.checkpoints = []
        for i in range(cp_count):
            x, y = map(int, input().split())
            self.checkpoints.append(np.array((x, y)))
        # log(f"{len(self.checkpoints)} checkpoints: {self.checkpoints}")


    def read_bot(self):
        x, y, vx, vy, angle, cp_id = map(int, input().split())
        bot = Bot(x, y, vx, vy, angle, cp_id, self.checkpoints)
        return bot



    def move_to_checkpoint(self, bot):
        dist = LA.norm(bot.pos - bot.cp)

        if self.round == 1:
            thrust = "BOOST"
        elif not bot.is_same_direction():
            thrust = 0
        elif dist < 1000:
            thrust = 30
        elif dist < 1500:
            thrust = 50
        elif dist < 2000:
            thrust = 70
        else:
            thrust = 100

        # if self.shield_needed(bot):
        #     thrust = "SHIELD"

        new, is_next_cp = bot.adjust_cp_coord()
        if is_next_cp:
            thrust = 0
        print("%s %s %s CP:%s" % (int(new[0]), int(new[1]), thrust, thrust))


    def shield_needed(self, bot):
        min_dist = BOT_RADIUS * 100
        for en in self.enemies:
            # d = math.hypot(abs(bot.x + bot.vx - en.x - en.vx), abs(bot.y + bot.vy - en.y - en.vy))
            d = LA.norm(bot.pos + bot.v - (en.pos + en.v))
            min_dist = min(min_dist, d)
        log(f"Min enemy dist {min_dist}")
        return min_dist <= (BOT_RADIUS * 2 + MAX_THRUST)


    def attack(self, bot):
        """
        New alg for attack:
            If enemy closer to next checkpoint, go to his CP after the next one.
            If you are closer to enemies CP, attack him
        """
        en1, en2 = self.enemies
        enemy = en1 if en1.cp_id >= en2.cp_id else en2

        new = enemy.pos - enemy.v * COMPENSATION
        thrust = 100
        if self.shield_needed(bot):
            thrust = "SHIELD"
        print("%s %s %s AT:%s" % (int(new[0]), int(new[1]), thrust, thrust))


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

