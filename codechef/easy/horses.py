#!/usr/bin/python
"""
http://www.codechef.com/problems/HORSES

Testing:
    nosetests --with-doctest <file>

Input:
1
5
4 9 1 32 13

Output:
3
"""


def alg(a):
    """
    >>> alg([4, 9, 1, 32, 13])
    3
    >>> alg([4, 9])
    5
    >>> alg([4, 2, 2])
    0
    """
    assert len(a) > 1
    a.sort()
    dist = a[1] - a[0]
    for i in xrange(2, len(a)):
        dist = min(dist, a[i] - a[i-1])
    return dist


if __name__ == "__main__":

    for _ in range(input()):
        _ = input()
        a = map(int, raw_input().split())
        print alg(a)
