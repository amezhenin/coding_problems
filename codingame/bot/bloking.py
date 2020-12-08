import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def diag_dist(size, x, y):
    x = min(x, size - x - 1)
    y = min(y, size - y - 1)
    s = 0
    while x < size / 2 and y < size / 2:
        x += 1
        y += 1
        s += 1
    return s

# Blocking

nb_shapes = int(input())  # number of shapes
for i in range(nb_shapes):
    inputs = input().split()
    sid = inputs[0]  # letter of the shape
    scol = int(inputs[1])  # width of the shape
    srow = int(inputs[2])  # height of the shape
    definition = inputs[3]  # definition of the shape
nb_players = int(input())  # number of players
player_id = int(input())  # id of the current player
board_size = int(input())  # size of the board = 13
shapes = input()  # letters of all the shapes for this game

# game loop
while True:
    for i in range(board_size):
        line = input()  # line of the board with 0-3 cell owned, 'x' cell empty well connected, '.' cell empty
    played_moves = int(input())  # number of move from the other player
    for i in range(played_moves):
        inputs = input().split()
        player = int(inputs[0])  # id of the player
        col = int(inputs[1])  # column played
        row = int(inputs[2])  # row played
        shape = inputs[3]  # 4 char definition of the played shape
    valid_moves = [] # number of valid moves
    for i in range(int(input()) ):
        inputs = input().split()
        col = int(inputs[0])
        row = int(inputs[1])
        shape = inputs[2]
        points = 1
        if shape[0] > "A":
            points += 1
        if shape[0] > "B":
            points += 1
        if shape[0] > "D":
            points += 1
        if shape[0] > "I":
            points += 1
        points = points + diag_dist(board_size, col, row) / board_size
        log(points)
        valid_moves.append((col, row, shape, points))

    #log(valid_moves)

    # best_points = max(valid_moves, key=lambda x: x[3])[3]
    # log(f"Best points: {best_points}")
    # best_moves = list(filter(lambda x: x[3] == best_points, valid_moves))
    # log(best_moves)
    # move = random.choice(best_moves)
    move = max(valid_moves, key=lambda x: x[3])
    log(move)

    print(f"{move[0]} {move[1]} {move[2]}")
