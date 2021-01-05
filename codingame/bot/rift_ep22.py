from collections import deque
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


POD_COST = 20


class Zone:

    def __init__(self, zid, my_id):
        self.id = zid
        self.pt = None
        self.my_id = my_id
        self.pods = None
        self.enemy = None
        self.owner_id = None
        self.owned = None
        self.pods = None
        self.links = []
        self.visible = None
        self.attack = None
        self.attack_dist = None
        self.explored = False


    def __eq__(self, other):
        return self.id == other.id


    def __repr__(self):
        return f"Zone {self.id}: pt {self.pt}"


    def update_pods(self, owner_id, my_pods, enemy, visible, platinum):
        self.owner_id = owner_id
        self.owned = self.my_id == owner_id
        self.pods = my_pods
        self.visible = visible
        # FIXME: enemy base is always visible with pods, can it be used to analyze enemy income?
        if self.visible:
            self.enemy = enemy
            if not self.explored:
                self.pt = platinum
                self.explored = True


    # @property
    # def lead_to_unexplored(self):
    #     for l in self.links:
    #         if not l.explored:
    #             return True
    #     return False


    def flee(self):
        q = deque()
        for l in self.links:
            q.append((l, l))
        while len(q) > 0:
            target, move = q.popleft()
            for z in target.links:
                if z.explored and z.pt > 0 and z.owned:
                    return move
                if z.explored:
                    q.append((z, move))
        log(f"Can't flee from {self}")
        return None


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
            self.zones[zid] = Zone(zid, my_id)

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
            if self.my_id == 0:
                pods, enemy = pods_p0, pods_p1
            else:
                pods, enemy = pods_p1, pods_p0
            self.zones[zid].update_pods(owner_id, pods, enemy, visible, platinum)

        if self.round == 1:
            self.build_move_map()
            log("Map is ready")
            for z in self.zones.values():
                assert z.attack is not None, f"{z.id} no attack"

            blitz = self.count_attack_steps()
            log(f"Attack distance: {blitz}")
            if blitz <= 8:
                self.blitz_attack = True

        # move
        all_moves = []
        for z in self.zones.values():
            if z.pods == 0:
                continue
            move = []
            for l in z.links:
                if self.lead_to_unexplored(l) or (l.pt > 0 and not l.owned):
                    move.append(l)
            move.sort(key=lambda x: -x.pt)

            for l in z.links:
                if l not in move and l.owner_id not in (-1, self.my_id):
                    move.append(l)
            move.append(z.attack)
            base_pods = z.pods // len(move)
            excess = z.pods % len(move)
            for idx, m in enumerate(move):
                pds = base_pods
                pds += (idx < excess)
                all_moves.append(f"{pds} {z.id} {m.id}")


        if len(all_moves):
            print(" ".join(all_moves))
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
            if z.enemy:
                self.enemy_base = z
                log(f"Enemy base {z.id}")

        assert self.enemy_base is not None

        # moves to attack enemy base
        q = deque([(self.enemy_base, 0)])
        while len(q) > 0:
            target, dist = q.popleft()
            for z in target.links:
                if not z.attack:
                    z.attack = target
                    z.attack_dist = dist + 1
                    q.append((z, dist + 1))

    def count_attack_steps(self):
        cnt = 0
        z = self.my_base
        while z != self.enemy_base:
            z = z.attack
            cnt += 1
        return cnt

    def lead_to_unexplored(self, zone):
        if zone == self.enemy_base:
            return True

        for l in zone.links:
            if not l.explored:
                return True
        return False


if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
