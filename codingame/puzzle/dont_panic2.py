"""
https://www.codingame.com/ide/puzzle/don't-panic-episode-2

!!! INCOMPLETE !!!

"""
from collections import defaultdict
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: number of additional elevators that you can build
# nb_elevators: number of elevators


nb_floors, width, nb_rounds, exit_floor, exit_pos, \
nb_total_clones, nb_additional_elevators, nb_elevators = list(map(int, input().split()))

el = defaultdict(list)
for i in range(nb_elevators):
    ef, ep = map(int, input().split())
    el[ef].append(ep)


def step():
    inputs = input().split()
    log(inputs)
    cur_floor = int(inputs[0])
    cur_pos = int(inputs[1])
    d = inputs[2]
    if cur_floor == -1:
        return "WAIT"

    if cur_floor == exit_floor:
        target_el = exit_pos
    else:
        target_el = el[cur_floor][-1]

    if cur_pos == target_el and build[cur_floor]:
        build[cur_floor] = False
        return "ELEVATOR"

    if (cur_pos <= target_el and d == "RIGHT") or (cur_pos >= target_el and d == "LEFT"):
        return "WAIT"
    else:
        return "BLOCK"

while True:
    print(step())
