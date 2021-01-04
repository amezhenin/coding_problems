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
        # FIXME: do we know about enemy pods if it is not visible?
        if self.my_id == 0:
            self.pods, self.enemy = p0, p1
        else:
            self.pods, self.enemy = p1, p0
        self.visible = visible
        # FIXME: enemy base is always visible with pods, can it be used to analyze enemy income?
        if self.visible:
            # log(f"Z {self.id} pt: {platinum}")
            self.pt = platinum


class Game:

    def __init__(self):
        self.round = 0
        self.my_base = None
        self.enemy_base = None
        self.blitz_attack = False

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
            blitz = self.count_attack_steps()
            log(f"Attack distance: {blitz}")
            if blitz <= 10:
                self.blitz_attack = True


        # move
        move = []
        for z in self.zones.values():
            if z.pods == 0:
                continue

            pods = z.pods
            if self.blitz_attack is False:
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

    def count_attack_steps(self):
        cnt = 0
        z = self.my_base
        while z != self.enemy_base:
            z = z.move
            cnt += 1
        return cnt



if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
