from collections import deque
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


POD_COST = 20


class Zone:
    def __init__(self, zid, pt, my_id):
        self.id = zid
        self.pt = pt
        self.my_id = my_id
        self.pods = None
        self.enemy = None
        self.owner_id = None
        self.owned = None
        self.pods = None
        self.move = None
        self.links = []
        self.visible = None

    def update_pods(self, owner_id, p0, p1, visible, platinum):
        self.owner_id = owner_id
        self.owned = self.my_id == owner_id
        if self.my_id == 0:
            self.pods, self.enemy = p0, p1
        else:
            self.pods, self.enemy = p1, p0
        self.visible = visible
        # FIXME: what is the diff with initial pt?
        if self.visible:
            log(f"Z {self.id} pt: {platinum}")
            self.pt = platinum


class Game:

    def __init__(self):
        self.round = 0
        self.my_base = None
        self.enemy_base = None

        # player_count: the amount of players (always 2)
        # my_id: my player ID (0 or 1)
        # zone_count: the amount of zones on the map
        # link_count: the amount of links between all zones
        player_count, my_id, zone_count, link_count = map(int, input().split())

        self.my_id = my_id
        self.zone_count = zone_count
        self.zones = {}

        for i in range(zone_count):
            # zone_id: this zone's ID (between 0 and zoneCount-1)
            # platinum_source: Because of the fog, will always be 0
            zid, pt = map(int, input().split())
            assert pt == 0
            self.zones[zid] = Zone(zid, pt, my_id)

        for i in range(link_count):
            z1, z2 = map(int, input().split())
            self.zones[z1].links.append(self.zones[z2])
            self.zones[z2].links.append(self.zones[z1])
        pass


    def next_round(self):
        self.round += 1

        my_pt = int(input())  # my available Platinum
        for i in range(self.zone_count):
            zid, owner_id, pods_p0, pods_p1, visible, platinum = map(int, input().split())
            self.zones[zid].update_pods(owner_id, pods_p0, pods_p1, visible, platinum)

        if self.round == 1:
            self.build_move_map()
            log("Map is ready")
            for z in self.zones.values():
                assert z.move is not None, f"{z.id} no move"

        # move
        move = []
        for z in self.zones.values():
            if z.pods == 0:
                continue

            pods = z.pods
            for l in z.links:
                if pods > 0 and not l.owned and l.id != z.move.id:
                    move.append(f"1 {z.id} {l.id}")
                    pods -= 1
            if pods > 0:
                move.append(f"{pods} {z.id} {z.move.id}")

        if len(move):
            print(" ".join(move))
        else:
            print("WAIT")

        print("WAIT")


    def build_move_map(self):

        self.my_base = None
        self.enemy_base = None
        for z in self.zones.values():
            if z.pods > 0:
                self.my_base = z
                log(f"My base {z.id}")
            if z.enemy > 0:
                self.enemy_base = z
                log(f"Enemy base {z.id}")

        assert self.enemy_base is not None

        q = deque([self.enemy_base])

        # log(f"Starting queue: {len(q)}")
        while len(q) > 0:
            target = q.popleft()
            for z in target.links:
                if not z.move:
                    z.move = target
                    q.append(z)




if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()



"""

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]

# game loop
while True:
    my_platinum = int(input())  # your available Platinum
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    print("WAIT")
    print("WAIT")
"""