"""
https://www.codingame.com/ide/puzzle/reverse-fizzbuzz
"""

import sys
import math

"""
# for future use
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
"""

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = 0
v = {
    "Fizz": [],
    "Buzz": [],
    "FizzBuzz": []
}
start = 0
for i in range(1, n + 1):
    line = input()
    try:
        s = int(line)
        if start == 0:
            start = s - i
    except:
        v[line].append(i)

if len(v["Fizz"]) > 0:
    f = v["Fizz"][0] + start
else:
    f = None
if len(v["Fizz"]) > 1:
    f = math.gcd(v["Fizz"][0] + start, v["Fizz"][1] + start)

if len(v["Buzz"]) > 0:
    b = v["Buzz"][0] + start
else:
    b = None
if len(v["Buzz"]) > 1:
    b = math.gcd(v["Buzz"][0] + start, v["Buzz"][1] + start)

if len(v["FizzBuzz"]) > 0:
    fb = v["FizzBuzz"][0] + start
else:
    fb = None
if len(v["FizzBuzz"]) > 1:
    fb = math.gcd(v["FizzBuzz"][0] + start, v["FizzBuzz"][1] + start)

for i in range(3):
    try:
        f = fb // b
    except:
        pass

    try:
        b = fb // f
    except:
        pass

    try:
        fb = f * b
    except:
        pass

if f is None:
    f = fb
    b = fb
print(f"{f} {b}")