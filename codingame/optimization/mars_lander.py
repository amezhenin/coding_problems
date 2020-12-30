"""
https://www.codingame.com/multiplayer/optimization/mars-lander


# Save the Planet.
# Use less Fossil Fuel.

n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # R P. R is the desired rotation angle. P is the desired thrust power.
    print("-20 3")


vertical speed must be limited ( ≤ 40m/s in absolute value)
horizontal speed must be limited ( ≤ 20m/s in absolute value)
"""
import math

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


MAX_VS = 40
MAX_HS = 20

# drawing surface and getting target plane
target_x1, target_x2, target_y = 0, 0, 0
last_x, last_y = 0, 0
surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    if last_y == land_y:
        target_x1 = last_x
        target_y = last_y
        target_x2 = land_x
    last_x = land_x
    last_y = land_y

# game loop
stage = 1
approach_from = ''
counter = 0

while True:
    counter += 1

    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # trajectory calculation
    if v_speed > 0:
        v_speed *= -1

    if h_speed != 0 and v_speed != 0:
        aoa = math.atan2(v_speed, h_speed)
        # print(f"aoa {round(math.degrees(aoa), 3)} degrees", file=sys.stderr)
        y0 = y - target_y  # height from target
        vector_mag = math.hypot(h_speed, v_speed)
        theta = aoa
        g = 3.711
        distance = (
            (vector_mag**2 / 2 * g) *
            (
                1 + (
                    1 + (
                        (2 * g * y0) / (
                            vector_mag**2 * math.sin(theta)**2)
                    )
                ) ** 0.5
            )
        ) * (math.sin(2 * theta))

        distance = (int(distance) / 10) * -1
        log(f"LD {distance}")

    angle = 0
    thrust = 4

    # FIRST STAGE
    if stage == 1:
        thrust = 4
        if x < target_x1:
            approach_from = "left"
            angle = -45  # go right
            if abs(h_speed) > 58:
                stage = 2
        elif x > target_x2:
            approach_from = "right"
            angle = 45  # go left
            if abs(h_speed) > 58:
                stage = 2

    elif stage == 2:
        angle = 0

        slow_rate = 13 if y0 > 400 else 20
        log(f"Y0 {y0} Slow {slow_rate}")
        if counter % slow_rate == 0:
            thrust = 3
        else:
            thrust = 4

        comp_dist = int((distance * 0.3) * abs(h_speed * 0.01))

        if approach_from == "left" and comp_dist + x > target_x1:
            stage = 3

        if approach_from == "right" and comp_dist + x < target_x2:
            stage = 3

    elif stage == 3:  # SLOW DOWN
        thrust = 4
        max_ang = 70

        opp_aoa = int((math.degrees(aoa) - 90) % 360 - 180)
        opp_aoa = max(-max_ang, min(max_ang, opp_aoa))


        if abs(h_speed) > 1:
            if h_speed > 1:
                angle = opp_aoa
            if h_speed < 1:
                angle = opp_aoa
        else:
            angle = 0
            stage = 4

    elif stage == 4:  # LANDING
        if v_speed < -MAX_VS + 1:
            thrust = 4
        else:
            thrust = 3

    print(str(angle) + " " + str(thrust))  # OUTPUT
