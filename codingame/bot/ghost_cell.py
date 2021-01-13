"""
https://www.codingame.com/ide/puzzle/ghost-in-the-cell
"""

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)

# FIXME: Use BOMB
# FIXME: Use INC

class Factory:
    def __init__(self, factory_id):
        self.id = factory_id
        self.links = {}
        # player that owns the factory: 1 for you, -1 for your opponent and 0 if neutral
        self.owner = 0
        self.bots = 0
        self.production = 0
        self.inc_troops = []
        # self.inc_bomb = None
        self.attack_score = 0.0
        self.bots_to_capture = 0



    def update(self, owner, bots, production):
        self.owner = owner
        self.bots = bots
        self.production = production


    def reset(self):
        self.inc_troops = []
        # self.inc_bomb = None


    def add_inc_troop(self, troop):
        self.inc_troops.append(troop)


    def is_upgradable(self):
        return self.bots >= 10 and self.production < 3


    def _bots_to_capture(self):
        if self.owner == 1:
            bots = -self.bots
        else:
            bots = self.bots

        for t in self.inc_troops:
            if t.owner == 1:
                bots -= t.bots
            else:
                bots += t.bots
        if bots < 0:
            return 0
        if self.owner == 1:
            return bots
        return bots + 1


    def finalize(self):
        self.inc_troops.sort(key=lambda x: x.eta)
        self.attack_score = 0.0 if self.owner == 1 else 1.0
        self.bots_to_capture = self._bots_to_capture()
        if self.bots_to_capture > 0:
            self.attack_score = self.production / self.bots_to_capture
        # log(f"F:{self.id} ATK:{self.attack_score} BC:{self.bots_to_capture}")


class Troop:

    def __init__(self, troop_id, owner, src_fact, dest_fact, bots, eta):
        self.id = troop_id
        self.owner = owner
        self.src_fact = src_fact  # not used right now
        self.dest_fact = dest_fact
        self.bots = bots
        self.eta = eta
        pass


class Game:

    def __init__(self):
        self.factory_count = int(input())  # the number of factories
        link_count = int(input())  # the number of links between factories
        self.factories = [Factory(i) for i in range(self.factory_count)]
        for i in range(link_count):
            f1, f2, dist = map(int, input().split())
            # log(f"Links {f1}->{f2} {dist}")
            self.factories[f1].links[f2] = dist
            self.factories[f2].links[f1] = dist

        self.enemy_bomb = False


    def next_round(self):
        self.enemy_bomb = False

        for i in self.factories:
            i.reset()

        # the number of entities (e.g. factories and troops)
        entity_count = int(input())
        for i in range(entity_count):
            inputs = input().split()
            entity_id = int(inputs[0])
            entity_type = inputs[1]

            if entity_type == "FACTORY":
                player = int(inputs[2])
                bots = int(inputs[3])  # number of cyborgs in the factory
                production = int(inputs[4])  # factory production (between 0 and 3)
                self.factories[entity_id].update(player, bots, production)

            elif entity_type == "TROOP":
                owner = int(inputs[2])
                src_fact = int(inputs[3])
                dest_fact = int(inputs[4])
                bots = int(inputs[5])
                eta = int(inputs[6])
                t = Troop(entity_id, owner, src_fact, dest_fact, bots, eta)
                self.factories[dest_fact].add_inc_troop(t)
            else:
                assert entity_type == "BOMB"
                """
                arg1: player that send the bomb: 1 if it is you, -1 if it is your opponent
                arg2: identifier of the factory from where the bomb is launched
                arg3: identifier of the targeted factory if it's your bomb, -1 otherwise
                arg4: remaining number of turns before the bomb explodes (positive integer) if that's your bomb, -1 otherwise
                """
                owner = int(inputs[2])
                # src_fact = int(inputs[3])
                # dest_fact = int(inputs[4])
                # eta = int(inputs[5])
                log(f"Bomb: {inputs}")
                if owner == -1:
                    self.enemy_bomb = True

        for i in self.factories:
            i.finalize()

        moves = []
        my_facts = list(filter(lambda x: x.owner == 1, self.factories))

        my_facts.sort(key=lambda x: -x.bots)
        for factory in my_facts:
            # this factory will be captured
            if factory.bots_to_capture > 0:
                log(f"Fact {factory.id} needs help")
                continue
            link_facts = []
            for l in factory.links.keys():
                link_facts.append(self.factories[l])
            link_facts.sort(key=lambda x: -x.attack_score)
            for lf in link_facts:
                if 0 < lf.bots_to_capture <= factory.bots:
                    moves.append(f"MOVE {factory.id} {lf.id} {lf.bots_to_capture}")
                    # make sure we will not have double spending of our bots
                    factory.bots -= lf.bots_to_capture
                    # make sure we will not send other bots to that factory
                    lf.bots_to_capture = 0
            pass

        for factory in my_facts:
            if factory.bots_to_capture > 0:
                log(f"Fact {factory.id} STILL needs help")
                continue
            if factory.is_upgradable():
                log(f"INC {factory.id}")
                moves.append(f"INC {factory.id}")

        if len(moves):
            print(";".join(moves))
        else:
            print("WAIT")



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()