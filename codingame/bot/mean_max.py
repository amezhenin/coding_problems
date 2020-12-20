import sys
import math


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def dist(a, b):
    return int(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2))


# game loop
turn = 0
while True:
    turn += 1
    water = []
    bot = None

    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())

    for i in range(unit_count):
        inputs = input().split()
        # log(inputs)
        unit_id = int(inputs[0])
        unit_type = int(inputs[1])
        player = int(inputs[2])
        mass = float(inputs[3])
        radius = int(inputs[4])
        x = int(inputs[5])
        y = int(inputs[6])
        vx = int(inputs[7])
        vy = int(inputs[8])
        extra = int(inputs[9])
        extra_2 = int(inputs[10])

        if player == 0:
            bot = (x, y)
        if extra > 0:
            water.append((x, y, radius))

    tx, ty, tr = water[0]
    d = dist(bot, water[0])
    log(f"Water: {len(water)} {water}")
    log(f"Bot: {bot}")

    for i in water:
        dd = dist(bot, i)
        # log(f"W {i} D {dd}")
        if dd < d:
            tx, ty, tr = i
            d = dd
    throttle = 300
    if tr > d:
        throttle = 0
    elif d < 1000:
        throttle = 100
    elif d < 2000:
        throttle = 200

    print(f"{tx} {ty} {throttle} {throttle} {d}/{tr}")
    print(f"WAIT")
    print(f"WAIT")
