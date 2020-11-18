#!/usr/bin/python
"""
http://www.codechef.com/problems/COMM3

Testing:
    nosetests --with-doctest <file>

Input:
3
1
0 1
0 0
1 0
2
0 1
0 0
1 0
2
0 0
0 2
2 1

Output:
yes
yes
no
"""
import itertools
from math import hypot


def alg(r, a):
    """
    >>> alg(1, [[0, 1], [0, 0], [1, 0]])
    True
    >>> alg(2, [[0, 1], [0, 0], [1, 0]])
    True
    >>> alg(2, [[0, 0], [0, 2], [2, 1]])
    False
    """

    # calculate distances between all points
    dists = [hypot(x1[0] - x2[0], x1[1] - x2[1]) for x1, x2 in itertools.combinations(a, 2)]
    # there should be no more than 1 distance that is greater that `r`
    connected = sum(map(lambda x: x <= r, dists))
    return connected >= 2


if __name__ == "__main__":

    for _ in range(input()):
        r = input()
        a = [map(int, raw_input().split()) for _ in range(3)]
        if alg(r, a):
            print "yes"
        else:
            print "no"
