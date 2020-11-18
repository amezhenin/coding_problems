#!/usr/bin/python
"""
http://www.codechef.com/problems/AMSGAME1

Solution was copied from recipe.py

Testing:
    nosetests --with-doctest <file>

Input
3
2
10 12
2
5 9
3
6 10 15

Output
2
1
1
"""

from fractions import gcd


def alg(a):
    """
    >>> alg([10, 12])
    2
    >>> alg([5, 9])
    1
    >>> alg([6, 10, 15])
    1
    >>> alg([6, 9, 15])
    3
    """

    divisor = reduce(gcd, a)
    return divisor


if __name__ == "__main__":

    for _ in range(input()):
        _ = input()
        a = map(int, raw_input().split())
        print alg(a)
