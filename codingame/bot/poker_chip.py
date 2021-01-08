"""
https://www.codingame.com/ide/puzzle/poker-chip-race
"""
import math
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)

import collections
Chip = collections.namedtuple("Chip", "id plr r x y vx vy mass speed")

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

WAIT_ROUNDS = 12

# It's the survival of the biggest!
# Propel your chips across a frictionless table top to avoid getting eaten by bigger foes.
# Aim for smaller oil droplets for an easy size boost.
# Tip: merging your chips will give you a sizeable advantage.

my_id = int(input())  # your id (0 to 4)

# game loop
round = 0
while True:
    round += 1
    player_chip_count = int(input())  # The number of chips under your control
    entity_count = int(input())  # The total number of entities on the table, including your chips
    enemy_chips = []
    op1 = None
    my_chips = []
    for i in range(entity_count):
        inputs = input().split()
        _id = int(inputs[0])  # Unique identifier for this entity
        player = int(inputs[1])  # The owner of this entity (-1 for neutral droplets)
        radius = float(inputs[2])  # the radius of this entity
        x = float(inputs[3])  # the X coordinate (0 to 799)
        y = float(inputs[4])  # the Y coordinate (0 to 514)
        vx = float(inputs[5])  # the speed of this entity along the X axis
        vy = float(inputs[6])  # the speed of this entity along the Y axis
        mass = math.pi * radius**2
        speed = dist(vx, vy, 0, 0)
        c = Chip(_id, player, radius, x, y, vx, vy, mass, speed)
        if player == my_id:
            my_chips.append(c)
            log(f"My chip: {c.id} M:{int(c.mass)} S:{int(c.speed)}")
        else:
            if player >= 0:
                op1 = c
                log(f"En chip: {c.id} {int(c.mass)}")
            # log(f"Chip: {c}")
            enemy_chips.append(c)

    other_mass = 0
    for c in enemy_chips:
        if op1.mass >= c.mass:
            other_mass += c.mass
    log(f"M {my_chips[0].mass} O {op1.mass} F {other_mass}")
    if my_chips[0].mass > other_mass:
        log("ALL MASS!")
        print("WAIT WON?")
        continue

    for chip in my_chips:
        min_dist = 1000000
        mo = None
        msg = ""
        for o in enemy_chips:
            new_dist = dist(chip.x, chip.y, o.x, o.y)
            if chip.mass * 14 / 15 > o.mass and min_dist > new_dist and o.plr == -1:
                min_dist = new_dist
                mo = o
                msg = str(o.id)
            if chip.mass * 14 / 15 > o.mass and o.plr >= 0:
                mo = o
                msg = "ATK"
                break

        if chip.speed:
            comp = min_dist / chip.speed
        else:
            comp = WAIT_ROUNDS / 2

        if mo is not None and round % WAIT_ROUNDS == 1:
            log(comp)
            print(f"{int(mo.x-mo.vx*comp)} {int(mo.y-mo.vy*comp)} {msg}")
            # print(f"{int(mo.x)} {int(mo.y)} {msg}")
        else:
            print("WAIT")