"""
https://www.codingame.com/ide/puzzle/ghost-in-the-cell
"""

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


class Game:
    def __init__(self):
        self.factory_count = int(input())  # the number of factories
        self.link_count = int(input())  # the number of links between factories
        self.links = {i:[] for i in range(self.factory_count)}
        for i in range(self.link_count):
            f1, f2, dist = map(int, input().split())
            log(f"Links {f1}->{f2} {dist}")
            self.links[f1].append((f2, dist))
            self.links[f2].append((f1, dist))


    def next_round(self):
        entity_count = int(input())  # the number of entities (e.g. factories and troops)
        my_bots = []
        factory_owner = [0] * self.factory_count
        for i in range(entity_count):
            inputs = input().split()
            entity_id = int(inputs[0])
            entity_type = inputs[1]

            if entity_type == "FACTORY":
                player = int(inputs[2])  # player that owns the factory: 1 for you, -1 for your opponent and 0 if neutral
                bots = int(inputs[3])  # number of cyborgs in the factory
                # arg_3 = int(inputs[4])  # factory production (between 0 and 3)
                if player == 1 and bots > 0:
                    my_bots.append((entity_id, bots))
                factory_owner[entity_id] = player
            else:
                assert entity_type == "TROOP"
                """
                arg1: player that owns the troop: 1 for you or -1 for your opponent
                arg2: identifier of the factory from where the troop leaves
                arg3: identifier of the factory targeted by the troop
                arg4: number of cyborgs in the troop (positive integer)
                arg5: remaining number of turns before the troop arrives (positive integer)
                """
                # arg_1 = int(inputs[2])
                # arg_2 = int(inputs[3])
                # arg_3 = int(inputs[4])
                # arg_4 = int(inputs[5])
                # arg_5 = int(inputs[6])
                pass

        log(f"FO: {factory_owner}")
        my_bots.sort(key=lambda x: -x[1])
        log(f"Bots: {my_bots}")

        move = []
        for eid, bots in my_bots:
            links = self.links[eid]
            min_dist = 9999999
            dest_fact = None
            for target, t_dist in links:
                if factory_owner[target] != 1 and min_dist > t_dist:
                    min_dist = t_dist
                    dest_fact = target
            if dest_fact is not None:
                move.append(f"{eid} {dest_fact} {bots}")


        if len(move):
            print("MOVE " + move[0])
        else:
            print("WAIT")



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()