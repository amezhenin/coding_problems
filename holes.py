#!/usr/bin/python
"""
http://www.codechef.com/problems/HOLES

Testing:
    nosetests --with-doctest <file>

Input:
2
CODECHEF
DRINKEATCODE

Output:
2
5
"""

from collections import defaultdict

HOLES = [(i, 1) for i in "qropad"] + [('b', 2)]
HOLES = defaultdict(int, HOLES)


def alg(a):
    """
    >>> alg("CODECHEF")
    2
    >>> alg("DRINKEATCODE")
    5
    """

    sum = 0
    for i in a.lower():
        sum += HOLES[i]  # simple dict can be used here: HOLES.get(i, 0)
    return sum


if __name__ == "__main__":

    for _ in range(input()):
        a = raw_input()
        print alg(a)