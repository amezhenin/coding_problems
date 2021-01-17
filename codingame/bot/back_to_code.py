"""
https://www.codingame.com/multiplayer/bot-programming/back-to-the-code
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)

COLS = 35
ROWS = 20
STEP = 1
opponent_count = int(input())  # Opponent count

dx, dy = 1, 1
nx, ny = None, None
# game loop
while True:
    game_round = int(input())
    log(f"Round {game_round}")
    # x: Your x position
    # y: Your y position
    # back_in_time_left: Remaining back in time
    x, y, back_in_time_left = [int(i) for i in input().split()]
    if game_round == 1:
        nx, ny = x, y
    for i in range(opponent_count):
        # opponent_x: X position of the opponent
        # opponent_y: Y position of the opponent
        # opponent_back_in_time_left: Remaining back in time of the opponent
        opponent_x, opponent_y, opponent_back_in_time_left = [int(j) for j in input().split()]
    m = []
    for i in range(ROWS):
        line = input()  # One line of the map ('.' = free, '0' = you, otherwise the id of the opponent)
        m.append(line)

    if game_round % (STEP*2) == 1:
        nx += dx*STEP
        ny += dy*STEP

    if nx < 0:
        nx = 0
        dx = 1
    if nx > COLS - 1:
        nx = COLS - 1
        dx = -1
        
    if ny < 0:
        ny = 0
        dy = 1
    if ny > ROWS - 1:
        ny = ROWS - 1
        dy = -1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # action: "x y" to move or "BACK rounds" to go back in time
    print(f"{nx} {ny}")
