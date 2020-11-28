import math
import collections

Bot = collections.namedtuple("Bot", "x y vx vy angle cp_id cp_x cp_y")

COMPENSATION = 3


class Game:
    def __init__(self):
        self.laps = int(input())
        cp_count = int(input())
        self.checkpoints = []
        for i in range(cp_count):
            x, y = map(int, input().split())
            self.checkpoints.append((x, y))


    def read_bot(self):
        x, y, vx, vy, angle, cp_id = map(int, input().split())
        bot = Bot(x, y, vx, vy, angle, cp_id, self.checkpoints[cp_id][0], self.checkpoints[cp_id][1])
        return bot


    def move_to_checkpoint(self, bot):

        dist = math.hypot(abs(bot.x - bot.cp_x), abs(bot.y - bot.cp_y))

        # if abs(next_checkpoint_angle) > 90:
        #     thrust = 0
        if dist < 1500:
            thrust = 30
        elif dist < 1050:
            thrust = 20
        elif dist > 5000:  # and abs(next_checkpoint_angle) < 5:
            thrust = "BOOST"
        # elif next_checkpoint_dist < 500 and math.hypot(abs(x - opponent_x), abs(y - opponent_y)) < 850:
        #     thrust = "SHIELD"
        else:
            thrust = 100

        nx = bot.cp_x - int(bot.vx * COMPENSATION)
        ny = bot.cp_y - int(bot.vy * COMPENSATION)
        print("%s %s %s CP:%s" % (nx, ny, thrust, thrust))


    def attack(self, bot, en1, en2):
        d1 = math.hypot(abs(bot.x - en1.x), abs(bot.y - en1.y))
        d2 = math.hypot(abs(bot.x - en2.x), abs(bot.y - en2.y))
        enemy, dist = en1, d1
        if d1 > d2:
            enemy, dist = en2, d2
        nx = enemy.x - int(enemy.vx * COMPENSATION)
        ny = enemy.y - int(enemy.vy * COMPENSATION)
        thrust = "SHIELD" if dist < 1100 else 100
        print("%s %s %s AT:%s" % (nx, ny, thrust, thrust))


    def next_round(self):
        bot1 = self.read_bot()
        bot2 = self.read_bot()

        en1 = self.read_bot()
        en2 = self.read_bot()

        self.move_to_checkpoint(bot1)
        #self.move_to_checkpoint(bot2)
        self.attack(bot2, en1, en2)




if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
