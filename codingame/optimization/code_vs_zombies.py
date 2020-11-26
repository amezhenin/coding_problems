"""
https://www.codingame.com/ide/puzzle/code-vs-zombies
"""
import math
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


MAX_X, MAX_Y = 16000, 9000
ASH_SPEED = 1000
ASH_RANGE = 2000
ZOMBIE_SPEED = 400


def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def move(x1, y1, x2, y2, cap):
    d = dist(x1, y1, x2, y2)
    scale = cap / d if d > cap else 1.0
    move_x = x1 + int((x2 - x1) * scale)
    move_y = y1 + int((y2 - y1) * scale)
    return move_x, move_y


def can_save(human, ash_x, ash_y, zombies):
    d = min([dist(human["x"], human["y"], z["x"], z["y"]) for z in zombies])
    moves = int(d / ZOMBIE_SPEED)
    ash_dist = dist(human["x"], human["y"], ash_x, ash_y) - ASH_RANGE
    if moves == 0:
        return False
    can = ash_dist // moves <= ASH_SPEED
    return can


def step(x, y, humans, zombies):
    next_x = x + 100
    next_y = y + 100

    occupied = {(i["next_x"], i["next_y"]) for i in zombies}

    # for h in humans:
    #     log('can save %s: %s' % (h["id"], can_save(h, x, y, zombies)))

    hx, hy = 0, 0
    for h in humans:
        if can_save(h, x, y, zombies):
            hx, hy = h["x"], h["y"]
            break

    return move(x, y, hx, hy, ASH_SPEED)


def main():
    # game loop

    while True:
        x, y = map(int, input().split())

        human_count = int(input())
        humans = []
        for i in range(human_count):
            human_id, human_x, human_y = map(int, input().split())
            humans.append({"id": human_id, "x": human_x, "y": human_y})

        zombie_count = int(input())
        zombies = []
        for i in range(zombie_count):
            zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = map(int, input().split())
            zombies.append({
                "id": zombie_id,
                "x": zombie_x,
                "y": zombie_y,
                "next_x": zombie_xnext,
                "next_y": zombie_ynext
            })

        next_x, next_y = step(x, y, humans, zombies)
        print(f"{next_x} {next_y}")


if __name__ == "__main__":
    main()
