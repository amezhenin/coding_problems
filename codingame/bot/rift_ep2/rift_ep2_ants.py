"""
Ant colony algorithm for:
https://www.codingame.com/multiplayer/bot-programming/platinum-rift-episode-2
"""
from collections import deque
import random
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


POD_COST = 20


SCENT_DECAY = 0.2
UNEXPLORED_SCENT_FACTOR = 10
ATTACK_SCENT_FACTOR = 5
ENEMY_SCENT_FACTOR = 100

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
        # self.explored = False
        self.scent = {
            "explored": 0.0,
            "enemy": 0.0,
        }


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
            self.pt = platinum
            # self.explored = round
        self.decay_scent()

    def scent_scores(self):
        scents = {}
        for l in self.links:
            score = 1.0
            score += (1.0 - l.scent["explored"]) * UNEXPLORED_SCENT_FACTOR
            if l.enemy > 0:
                l.scent["enemy"] = 1.0
                self.scent["enemy"] = 1.0
            score += l.scent["enemy"] * ENEMY_SCENT_FACTOR
            if l == self.attack:
                score += ATTACK_SCENT_FACTOR
            scents[l.id] = score

        return scents


    def decay_scent(self):
        # lower all scents
        for k, v in self.scent.items():
            self.scent[k] = v * SCENT_DECAY
        # self.scent_score = self._calc_scent_score()


    def move(self, dest, pods):
        dest.scent["explored"] = 1.0
        return f"{pods} {self.id} {dest.id}"


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
            self.zones[zid] = Zone(zid, my_id)

        for i in range(link_count):
            z1, z2 = map(int, input().split())
            self.zones[z1].links.append(self.zones[z2])
            self.zones[z2].links.append(self.zones[z1])
        pass


    def next_round(self):
        self.round += 1

        self.read_state()

        if self.round == 1:
            self.init_map()

        # ant colony algorithm
        all_moves = []
        for z in self.zones.values():
            if z.pods == 0:
                # we don't have our pods here
                continue

            total_score = 0.0
            dest = {}
            scent_scores = z.scent_scores()
            for l_id, score in scent_scores.items():
                total_score += score
                dest[l_id] = 0

            for p in range(z.pods):
                moves = []
                for l in z.links:
                    r = random.random()
                    prob = scent_scores[l.id] / total_score
                    moves.append((r*prob, l.id))
                moves.sort()
                best = moves[-1][1]
                dest[best] += 1

            for k, v in dest.items():
                if v > 0:
                    m = z.move(self.zones[k], v)
                    all_moves.append(m)
            pass

        if len(all_moves):
            print(" ".join(all_moves))
        else:
            print("WAIT")

        print("WAIT")

    def read_state(self):
        """
        Read state from input and update zones
        """
        my_pt = int(input())  # my available Platinum
        for i in range(self.zone_count):
            zid, owner_id, pods_p0, pods_p1, visible, platinum = map(int, input().split())
            if self.my_id == 0:
                pods, enemy = pods_p0, pods_p1
            else:
                pods, enemy = pods_p1, pods_p0
            self.zones[zid].update_pods(owner_id, pods, enemy, visible, platinum)
        pass


    def init_map(self):
        """
        Initialize additional path and bases on the first round
        """

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

        # self check
        log("Map is ready")
        for z in self.zones.values():
            assert z.attack is not None, f"{z.id} no attack"
        pass


if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
