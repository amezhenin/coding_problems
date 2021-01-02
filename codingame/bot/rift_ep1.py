from collections import defaultdict
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


POD_COST = 20


class Game:

    def __init__(self):
        # player_count: the amount of players (2 to 4)
        # my_id: my player ID (0, 1, 2 or 3)
        # zone_count: the amount of zones on the map
        # link_count: the amount of links between all zones
        player_count, my_id, zone_count, link_count = map(int, input().split())

        self.my_id = my_id
        self.zone_count = zone_count
        self.zone_pt = {}
        self.links = defaultdict(list)

        for i in range(zone_count):
            # zone_id: this zone's ID (between 0 and zoneCount-1)
            # platinum_source: the amount of Platinum this zone can provide per game turn
            zid, pt = map(int, input().split())
            self.zone_pt[zid] = pt

        for i in range(link_count):
            z1, z2 = map(int, input().split())
            self.links[z1].append(z2)
            self.links[z2].append(z1)
        pass


    def next_round(self):
        platinum = int(input())  # my available Platinum
        zones = {}
        for i in range(self.zone_count):
            # z_id: this zone's ID
            # owner_id: the player who owns this zone (-1 otherwise)
            # pods_p0: player 0's PODs on this zone
            # pods_p1: player 1's PODs on this zone
            # pods_p2: player 2's PODs on this zone (always 0 for a two player game)
            # pods_p3: player 3's PODs on this zone (always 0 for a two or three player game)
            z_id, owner_id, pods_p0, pods_p1, pods_p2, pods_p3 = [int(j) for j in input().split()]
            zones[z_id] = owner_id

        # first line for movement commands, second line for POD purchase (see the protocol in the statement for details)
        # move
        move = []
        for i in range(self.zone_count):
            for l in self.links[i]:
                if zones[l] != self.my_id:
                    move.append(f"1 {i} {l}")
        if len(move):
            print(" ".join(move))
        else:
            print("WAIT")


        # buy
        zs = [(v, k) for k, v in self.zone_pt.items()]
        zs.sort(reverse=True)
        buy = []
        for _, i in zs:
            if zones[i] == -1:
                buy.append(f"1 {i}")
        log(f"Free zones {len(buy)}")
        for i in range(self.zone_count):
            score = 0
            for l in self.links[i]:
                if zones[l] != self.my_id:
                    score += 1
            if zones[i] == self.my_id and score > 0:
                buy.append(f"1 {i}")
        # for i in range(self.zone_count):
        #     if zones[i] != self.my_id:
        #         buy.append(f"2 {i}")
        # log(f"+ with enemy zones {len(buy)}")


        log(f"Can buy {platinum//POD_COST} out of {len(buy)} options")
        buy = buy[:platinum//POD_COST]
        print(" ".join(buy))



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
