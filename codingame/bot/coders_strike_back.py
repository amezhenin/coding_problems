import math

COMPENSATION = 3
x = 0
y = 0
prevX = 0
prevy = 0

while True:
    previousX = x
    previousY = y

    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    elif next_checkpoint_dist < 1500:
        thrust = 30
    elif next_checkpoint_dist < 650:
        thrust = 20
    elif next_checkpoint_dist > 5000 and abs(next_checkpoint_angle) < 5:
        thrust = "BOOST"
    elif next_checkpoint_dist < 500 and math.hypot(abs(x - opponent_x), abs(y - opponent_y)) < 850:
        thrust = "SHIELD"
    else:
        thrust = 100

    nx = next_checkpoint_x - int((x - previousX) * COMPENSATION)
    ny = next_checkpoint_y - int((y - previousY) * COMPENSATION)
    print("%s %s %s %s" %(nx, ny, thrust, thrust))
