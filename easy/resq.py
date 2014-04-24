#!/usr/bin/python
"""
http://www.codechef.com/problems/RESQ

Testing:
    nosetests --with-doctest <file>

Input:
4
20
13
8
4

Output:
1
12
2
0
"""
from math import sqrt


def alg(n):
    """
    >>> alg(20)
    1
    >>> alg(13)
    12
    >>> alg(8)
    2
    >>> alg(4)
    0
    """

    assert n >= 1
    k = int(sqrt(n))
    while True:
        if not n % k:
            return abs(k - n / k)
        k -= 1


if __name__ == "__main__":

    for _ in range(input()):
        print alg(input())
