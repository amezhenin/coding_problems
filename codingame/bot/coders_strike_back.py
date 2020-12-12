import sys
import math

import numpy as np
from numpy import linalg as LA


def log(msg):
    print(msg, file=sys.stderr, flush=True)


COMPENSATION = 3
ATTACK_COMPENSATION = 6
CP_RADIUS = 600
BOT_RADIUS = 400
MAX_THRUST = 100


def unit_vector(vector):
    return vector / LA.norm(vector)


def deg_to_vector(d):
    return unit_vector(np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))]))



class Bot:
    def __init__(self, bot_id, x, y, vx, vy, angle, cp_id, checkpoints, old_bot):
        self.id = bot_id
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])
        self.angle = deg_to_vector(angle)
        self.cp_id = cp_id
        self.cp = checkpoints[cp_id]
        self.checkpoints = checkpoints
        # this is sum of checkpoint IDs to determine who is ahead
        if old_bot is None:
            self.cp_sum = 0
        else:
            self.cp_sum = old_bot.cp_sum + (old_bot.cp_id != self.cp_id)


    def __repr__(self):
        point = self.leader_points
        return f"ID_{self.id} ({point[0]}, {point[1]})"


    def detailed(self):
        return f"{str(self)} {str(self.cp_id)} {str(self.pos)} {str(self.v)}"

    def next_checkpoint(self):
        """
        Return checkpoint AFTER next one
        """
        idx = (self.cp_id + 1) % len(self.checkpoints)
        return self.checkpoints[idx]


    def is_same_direction(self, point):
        if LA.norm(point - self.pos) == 0:
            return True

        # log(f"Bot: {self.cp} {self.pos} {self.v}")
        l = LA.norm(unit_vector(point - self.pos) + unit_vector(self.angle))
        # log(f"Bot: {self} Norm {l}")
        return l > math.sqrt(2)


    def adjust_cp_coord(self):
        # log(f"Bot: {self}")
        if LA.norm(self.v) != 0:
            t = min((self.cp - self.pos) / (self.v + 1e-20))
        else:
            # log("Zero speed")
            return self.cp, False

        pos = (t * self.v) + self.pos

        # minimum distance to checkpoint center
        dist = LA.norm(self.cp - pos)
        # log(f"Min CP dist: {dist} in {t} rounds")
        if dist < CP_RADIUS:
            if 0 < t < 3.5:
                # log("Switching to CP after next")
                next_cp = self.next_checkpoint()
                return next_cp, True
            # log("Keeping course to point inside CP")
            return pos, False

        # log("Turning and moving to CP")
        new = self.cp - self.v * COMPENSATION
        return new, False


    @property
    def leader_points(self):
        dist = LA.norm(self.cp - self.pos)
        return self.cp_sum, -int(dist)


    @staticmethod
    def sort(bot_a, bot_b):
        """
        We sort bots by their leadership in the race
        """
        # we take bot with highest CPs passed and lowest distance to next one (if equal)
        bots = [bot_a, bot_b]
        bots.sort(reverse=True, key=lambda x: x.leader_points)
        return bots



class Game:
    def __init__(self):
        self.round = 0
        self.bots = [None, None]
        self.enemies = [None, None]
        self.laps = int(input())  # FIXME: start using this to determine last checkpoint
        # log(f"Laps: {self.laps}")
        cp_count = int(input())
        self.checkpoints = []
        for i in range(cp_count):
            x, y = map(int, input().split())
            self.checkpoints.append(np.array((x, y)))
        # log(f"{len(self.checkpoints)} checkpoints: {self.checkpoints}")


    def read_bot(self, bot_id, old_bot):
        x, y, vx, vy, angle, cp_id = map(int, input().split())
        bot = Bot(bot_id, x, y, vx, vy, angle, cp_id, self.checkpoints, old_bot)
        return bot



    def move_to_checkpoint(self, bot):
        dist = LA.norm(bot.pos - bot.cp)

        if self.round == 1:
            thrust = "BOOST"
        elif not bot.is_same_direction(bot.cp):
            thrust = 0
        # elif dist < 1000:
        #     thrust = 30
        elif dist < 1500:
            thrust = 50
        # elif dist < 2000:
        #     thrust = 70
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
            d = LA.norm(bot.pos + bot.v - (en.pos + en.v))
            min_dist = min(min_dist, d)
        # log(f"Min enemy dist {min_dist}")
        return min_dist <= (BOT_RADIUS * 2 + MAX_THRUST)


    def attack(self, bot):
        """
        """
        # sort enemies by their position in the race
        enemies = Bot.sort(*self.enemies)
        log(f"Enemies: {enemies[0]} {enemies[1]}")
        enemy = enemies[0]

        # If enemy closer to next checkpoint, go to his CP after the next one.
        if LA.norm(bot.pos - enemy.cp) > LA.norm(enemy.pos - enemy.cp):
            new = enemy.next_checkpoint()
        else:
            # If you are closer to enemies CP, attack him
            new = enemy.pos + (enemy.angle * 100 + enemy.v - bot.v) * ATTACK_COMPENSATION

        # new = enemy.pos - enemy.v * COMPENSATION
        # if self.round == 1:
        #     thrust = "BOOST"
        if not bot.is_same_direction(new):
            thrust = 0
        else:
            thrust = 100
        if self.shield_needed(bot):
            thrust = "SHIELD"
        print("%s %s %s AT:%s" % (int(new[0]), int(new[1]), thrust, thrust))


    def next_round(self):
        self.round += 1

        bot1 = self.read_bot(1, self.bots[0])
        bot2 = self.read_bot(2, self.bots[1])
        self.bots = [bot1, bot2]  #Bot.sort(bot1, bot2)
        #log(f"Bots: {self.bots[0]} {self.bots[1]}")

        en1 = self.read_bot(1, self.enemies[0])
        en2 = self.read_bot(2, self.enemies[1])
        self.enemies = [en1, en2]

        # before first checkpoint we are racing, because anything can happen there
        if self.bots[0].cp_sum + self.bots[1].cp_sum == 0:
            self.move_to_checkpoint(self.bots[0])
            self.move_to_checkpoint(self.bots[1])
        else:
            # after first CP we can see who is leader
            leader, attaker = Bot.sort(*self.bots)
            log(f"Bots:    {leader} {attaker}")

            # we have to process bots in order
            if self.bots[0] is leader:
                self.move_to_checkpoint(self.bots[0])
                self.attack(self.bots[1])
            else:

                self.attack(self.bots[0])
                self.move_to_checkpoint(self.bots[1])
            pass
        pass



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()

