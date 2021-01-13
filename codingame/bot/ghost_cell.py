"""
https://www.codingame.com/ide/puzzle/ghost-in-the-cell
"""

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)

# FIXME: Use BOMB
# FIXME: Use INC
LINKS_MAX_DIST = 5
BOMB_ROUNDS = (1, 20)

class Factory:
    def __init__(self, factory_id):
        self.id = factory_id
        self.all_links = []
        self.links = []
        # player that owns the factory: 1 for you, -1 for your opponent and 0 if neutral
        self.owner = 0
        self.bots = 0
        self.production = 0
        self.inc_troops = []
        # self.inc_bomb = None
        self.attack_score = 0.0
        self.bots_to_capture = 0


    def pick_links(self):
        links = sorted(self.all_links, key=lambda x: x[1])
        flinks = list(filter(lambda x: x[1] <= LINKS_MAX_DIST, links))
        if len(flinks) > 0:
            self.links = list(map(lambda x: x[0], flinks))
        else:
            log(f"Fact {self.id} has one links to {links[0].id}!")
            self.links = links[0][0]

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
        self.bots_to_capture = self._bots_to_capture()
        self.attack_score = 0.0 if self.owner == 1 else 1.0

        if self.bots_to_capture > 0:
            self.attack_score += self.production / self.bots_to_capture
        # log(f"F:{self.id} ATK:{self.attack_score} BC:{self.bots_to_capture}")

    def send(self, dest_id, number):
        assert number <= self.bots, f"{number} <= {self.bots}"
        self.bots -= number
        return f"MOVE {self.id} {dest_id} {number}"


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
            self.factories[f1].all_links.append((self.factories[f2], dist))
            self.factories[f2].all_links.append((self.factories[f1], dist))

        for f in self.factories:
            f.pick_links()
        self.enemy_bomb = False
        self.round = 0


    def next_round(self):
        self.round += 1
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
        incs = []
        my_facts = list(filter(lambda x: x.owner == 1, self.factories))
        my_facts.sort(key=lambda x: -x.bots)
        for factory in my_facts:
            if factory.bots_to_capture > 0:
                log(f"Factory {factory.id} needs help")
                continue
            targets = []
            for l in factory.links:
                if l.bots_to_capture <= factory.bots:
                    targets.append(l)
                    log(f"F {l.id} ATK {l.attack_score}")
            if len(targets) > 0:
                targets.sort(key=lambda x: -x.attack_score)
                log(f"Best {l.id}")
                bots = max(factory.bots//2, targets[0].bots_to_capture)
                moves.append(factory.send(targets[0].id, bots))
                # moves.append(factory.send(targets[0].id, targets[0].bots_to_capture))
            if factory.is_upgradable():
                incs.append(f"INC {factory.id}")
        bomb = []
        if self.round in BOMB_ROUNDS:
            dest = None
            m_bots = -1
            for f in self.factories:
                if f.bots > m_bots and f.owner == -1:
                    dest = f
                    m_bots = f.bots
            if dest is not None:
                src = sorted(dest.all_links, key=lambda x: x[1])
                for s in src:
                    if s[0].owner == 1:
                        bomb.append(f"BOMB {s[0].id} {dest.id}")

        final = bomb + incs + moves[:1]
        if len(moves):
            print(";".join(final))
        else:
            log(f"WAIT")
            print("WAIT")



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()