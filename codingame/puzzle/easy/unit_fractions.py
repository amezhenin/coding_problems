"""
https://www.codingame.com/training/easy/unit-fractions
"""

n = int(input())

for x in range(n+1, 2*n+1):
    if n*x % (x-n) == 0:
        y = n*x // (x-n)
        print(f"1/{n} = 1/{y} + 1/{x}")
