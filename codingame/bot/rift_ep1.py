from collections import deque
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


POD_COST = 20


class Continent:
    def __init__(self, cid, my_id):
        self.id = cid
        self.my_id = my_id
        self.pt = 0
        self.zones = {}

    def add(self, zone):
        assert zone.id not in self.zones
        self.zones[zone.id] = zone
        self.pt += zone.pt
        zone.continent = self

    @property
    def owned_pt(self):
        res = 0
        for z in self.zones.values():
            if z.owned:
                res += z.pt
        return res

    @property
    def free_zones(self):
        res = 0
        for z in self.zones.values():
            if z.owner_id == -1:
                res += 1
        return res

    @property
    def owned_zones(self):
        res = 0
        for z in self.zones.values():
            if z.owned:
                res += 1
        return res


    def __repr__(self):
        return f"C{self.id} S {self.pt} zones: {self.zones.keys()}"


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
        self.continent = None

    def update_pods(self, owner_id, p0, p1, p2, p3):
        self.owner_id = owner_id
        self.owned = self.my_id == owner_id
        self.pods = [p0, p1, p2, p3]
        self.my_pods = self.pods[self.my_id]
        # high priority move from this position
        self.move = None



class Game:

    def __init__(self):
        self.round = 0

        # player_count: the amount of players (2 to 4)
        # my_id: my player ID (0, 1, 2 or 3)
        # zone_count: the amount of zones on the map
        # link_count: the amount of links between all zones
        player_count, my_id, zone_count, link_count = map(int, input().split())

        self.my_id = my_id
        self.zone_count = zone_count
        self.zones = {}
        self.continents = []

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

        self.build_continents()
        for i in self.continents:
            log(i)


    def build_continents(self):

        def dfs(z, c):
            if not z.continent:
                c.add(z)
                for l in z.links:
                    dfs(l, c)

        # build continents
        zs = list(self.zones.values())
        cid = 0
        while len(zs) > 0:
            z = zs[0]
            cont = Continent(cid, self.my_id)
            self.continents.append(cont)
            cid += 1
            dfs(z, cont)
            zs = list(filter(lambda x: x.continent is None, zs))


    def next_round(self):
        self.round += 1

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
                cnt = z.my_pods - 1 if z.my_pods > 1 else 1
                move.append(f"{cnt} {i} {z.move.id}")
            pass
        if len(move):
            print(" ".join(move))
        else:
            print("WAIT")

        # buy
        cont = self.choose_continent()

        zs = [(z.pt, z.id, z) for z in cont.zones.values()]
        zs.sort(reverse=True)
        buy = []
        for _, _, z in zs:
            if z.owner_id == -1 and z.pt > 0:
                buy.append(z.id)
        # log(f"Free zones {len(buy)}")
        for z in cont.zones.values():
            if z.owner_id == -1 or z.owned:
                score = 0
                for l in z.links:
                    score += (not l.owned)
                if score > 0:
                    buy.append(z.id)

        for z in cont.zones.values():
            if z.owner_id == -1:
                buy.append(z.id)

        # log(f"Can buy {platinum//POD_COST} out of {len(buy)} options")
        amount = 1
        if platinum//POD_COST > len(buy) and len(buy):
            log("Custom buy")
            amount = platinum // (POD_COST * len(buy))
        else:
            buy = buy[:platinum//POD_COST]
        res = []
        for i in buy:
            res.append(f"{amount} {i}")
        print(" ".join(res))


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
        # log(f"Starting queue: {len(q)}")
        while len(q) > 0:
            target = q.popleft()
            for z in target.links:
                if not z.move:
                    z.move = target
                    q.append(z)


    def choose_continent(self):
        cs = list(filter(lambda x: x.free_zones > 0 or x.owned_zones > 0, self.continents))
        for c in cs:
            log(f"C {c.id} Upt: {c.pt - c.owned_pt} FZ:{c.free_zones} OZ:{c.owned_zones}")
        res = max(cs, key=lambda c: c.pt - c.owned_pt)
        log(f"Best continent: {res}")
        return res



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
