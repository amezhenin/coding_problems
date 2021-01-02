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
        self.my_pods = None
        self.owner_id = None
        self.owned = None
        self.pods = None
        self.move = None
        self.links = []

    def update_pods(self, owner_id, p0, p1, p2, p3):
        self.owner_id = owner_id
        self.owned = self.my_id == owner_id
        self.pods = [p0, p1, p2, p3]
        self.my_pods = self.pods[self.my_id]
        # high priority move from this position
        self.move = None



class Game:

    def __init__(self):
        # player_count: the amount of players (2 to 4)
        # my_id: my player ID (0, 1, 2 or 3)
        # zone_count: the amount of zones on the map
        # link_count: the amount of links between all zones
        player_count, my_id, zone_count, link_count = map(int, input().split())

        self.my_id = my_id
        self.zone_count = zone_count
        self.zones = {}

        for i in range(zone_count):
            # zone_id: this zone's ID (between 0 and zoneCount-1)
            # platinum_source: the amount of Platinum this zone can provide per game turn
            zid, pt = map(int, input().split())
            self.zones[zid] = Zone(zid, pt, my_id)

        for i in range(link_count):
            z1, z2 = map(int, input().split())
            self.zones[z1].links.append(self.zones[z2])
            self.zones[z2].links.append(self.zones[z1])
        pass


    def next_round(self):
        platinum = int(input())  # my available Platinum
        for i in range(self.zone_count):
            zid, owner_id, pods_p0, pods_p1, pods_p2, pods_p3 = map(int, input().split())
            self.zones[zid].update_pods(owner_id, pods_p0, pods_p1, pods_p2, pods_p3)

        self.update_move_map()

        # move
        move = []
        for i in range(self.zone_count):
            z = self.zones[i]
            if z.move:
                move.append(f"{z.my_pods} {i} {z.move.id}")
            pass
        if len(move):
            print(" ".join(move))
        else:
            print("WAIT")

        # buy
        zs = [(z.pt, z.id) for z in self.zones.values()]
        zs.sort(reverse=True)
        buy = []
        for _, i in zs:
            if self.zones[i].owner_id == -1:
                buy.append(f"1 {i}")
        log(f"Free zones {len(buy)}")
        for i in range(self.zone_count):
            score = 0
            z = self.zones[i]
            for l in z.links:
                score += (not l.owned)

            if z.owned and score > 0:
                buy.append(f"1 {i}")

        log(f"Can buy {platinum//POD_COST} out of {len(buy)} options")
        buy = buy[:platinum//POD_COST]
        print(" ".join(buy))


    def update_move_map(self):
        q = deque()
        for z in self.zones.values():
            if z.owned:
                continue
            # z NOT owned
            for l in z.links:
                if l.owned:
                    l.move = z
                    q.append(l)
                    break
        log(f"Starting queue: {len(q)}")
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
