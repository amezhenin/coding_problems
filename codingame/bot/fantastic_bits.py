"""
https://www.codingame.com/multiplayer/bot-programming/fantastic-bits
"""
import sys
import numpy as np
from numpy import linalg as LA


def log(msg):
    print(msg, file=sys.stderr, flush=True)


LEFT_TARGET = (0, 3750)
RIGHT_TARGET = (16000, 3750)


class Wizard:
    def __init__(self, eid, x, y, vx, vy, has_ball):
        self.id = eid
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])
        self.has_ball = has_ball


    def move(self, pos, thrust=150):
        # 0 ≤ thrust ≤ 150
        return f"MOVE {pos[0]} {pos[1]} {thrust}"


    def throw(self, pos, power=500):
        # 0 ≤ power ≤ 500
        return f"THROW {pos[0]} {pos[1]} {power}"


class Ball:
    def __init__(self, eid, x, y, vx, vy):
        self.id = eid
        self.pos = np.array([x, y])
        self.v = np.array([vx, vy])


class Game:
    def __init__(self):
        # if 0 you need to score on the right of the map, if 1 you need to score on the left
        self.my_team_id = int(input())
        if self.my_team_id == 0:
            self.my_target = RIGHT_TARGET
            self.en_target = LEFT_TARGET
        else:
            self.my_target = LEFT_TARGET
            self.en_target = RIGHT_TARGET
        self.wizards = []
        self.enemies = []
        self.balls = []
        self.bludgers = []
        pass


    def next_round(self):
        my_score, my_magic = map(int, input().split())
        opponent_score, opponent_magic = map(int, input().split())
        self.wizards = []
        self.enemies = []
        self.balls = []
        self.bludgers = []

        # read inputs
        entities = int(input())  # number of entities still in game
        for i in range(entities):
            inputs = input().split()
            eid = int(inputs[0])  # entity identifier
            entity_type = inputs[1]  # "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
            x = int(inputs[2])  # position
            y = int(inputs[3])  # position
            vx = int(inputs[4])  # velocity
            vy = int(inputs[5])  # velocity
            has_ball = int(inputs[6]) == 1 # 1 if the wizard is holding a Snaffle, 0 otherwise
            if entity_type == "WIZARD":
                w = Wizard(eid, x, y, vx, vy, has_ball)
                self.wizards.append(w)
            elif entity_type == "OPPONENT_WIZARD":
                w = Wizard(eid, x, y, vx, vy, has_ball)
                self.enemies.append(w)
            elif entity_type == "SNAFFLE":
                b = Ball(eid, x, y, vx, vy)
                self.balls.append(b)
            elif entity_type == "BLUDGER":
                b = Ball(eid, x, y, vx, vy)
                self.bludgers.append(b)

        # make actions
        print(self.attack(self.wizards[0]))
        print(self.attack(self.wizards[1]))
        # print(self.stand_goal(self.wizards[1]))

    def attack(self, wizard):
        if wizard.has_ball is True:
            return wizard.throw(self.my_target)

        # find closest ball
        min_dist = 9999999
        ball = None
        for b in self.balls:
            new_dist = LA.norm(wizard.pos - b.pos)
            if new_dist < min_dist:
                min_dist = new_dist
                ball = b
        assert ball is not None
        return wizard.move(ball.pos)


    def stand_goal(self, wizard):
        if wizard.has_ball is True:
            return wizard.throw(self.my_target)
        return wizard.move(self.en_target)




if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
