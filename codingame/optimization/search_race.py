"""
https://www.codingame.com/ide/puzzle/search-race
"""
import math

COMPENSATION = 2


import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def get_dist(x1, y1, x2, y2):
    return math.hypot(abs(x1 - x2), abs(y1 - y2))


cp_num = int(input())  # Count of checkpoints to read
checkpoints = []
for i in range(cp_num):
    x, y = map(int, input().split())
    checkpoints.append([x, y])
for i in range(-1, cp_num-1):
    from_cp = checkpoints[i]
    to_cp = checkpoints[i+1]
    dist = get_dist(from_cp[0], from_cp[1], to_cp[0], to_cp[1])


    thrust = int(max((dist-2000)/3000 * 70, 0) + 30)
    thrust = min(thrust, 100)
    # if dist > 5000:
    #     thrust = 100
    # elif dist > 4000:
    #     thrust = 80
    # elif dist > 3000:
    #     thrust = 60
    # elif dist > 2000:
    #     thrust = 35
    # else:
    #     thrust = 30

    log(f'CP: {i} {from_cp} {dist} {thrust}')
    checkpoints[i+1].append(thrust)

while True:
    # Angle are provided in degrees, and relative to the x axis
    # (0 degrees are pointing at (1.0). East = 0 degrees, South = 90 degrees.
    cp_id, x, y, vx, vy, angle = map(int, input().split())
    cp_x, cp_y, thrust = checkpoints[cp_id]
    dist = get_dist(x, y, cp_y, cp_x)

    if dist < 1500:
        thrust = 20
    # else:
    #     thrust = 100

    nx = cp_x - int(vx * COMPENSATION)
    ny = cp_y - int(vy * COMPENSATION)
    print(f'{nx} {ny} {thrust} {thrust}')
