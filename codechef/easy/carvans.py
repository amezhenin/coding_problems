#!/usr/bin/python
"""
http://www.codechef.com/problems/CARVANS

Testing:
    nosetests --with-doctest <file>

Input:
3
1
10
3
8 3 6
5
4 5 1 2 3

Output:
1
2
2
"""

from sys import stdin


def alg(a):
    """
    >>> alg([10])
    1
    >>> alg([8, 3, 6])
    2
    >>> alg([4, 5, 1, 2, 3])
    2
    >>> alg([1, 2, 3])
    1
    >>> alg([3, 2, 1])
    3
    >>> alg([3, 2, 1, 5, 4])
    3
    """

    m = a[0]
    c = 1
    for i in xrange(1, len(a)):
        if a[i] <= m:
            c += 1
            m = a[i]
    return c


if __name__ == "__main__":

    t = input()
    inp = stdin.readlines()
    for i in xrange(t):
        a = map(int, inp[2*i + 1].split())
        print alg(a)
