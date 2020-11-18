#!/usr/bin/python
"""
http://www.codechef.com/problems/SNAPE

Testing:
    nosetests --with-doctest <file>

Input:
3
4 5
10 12
10 20

Output:
3.0 6.40312
6.63325 15.6205
17.3205 22.3607
"""
from math import sqrt

def alg(b, ls):
    """
    >>> alg(4, 5)
    (3.0, 6.4031242374328485)
    >>> alg(10, 12)
    (6.6332495807108, 15.620499351813308)
    """
    mn = sqrt(ls*ls - b*b)
    mx = sqrt(ls*ls + b*b)
    return mn, mx


if __name__ == "__main__":

    for _ in range(input()):
        a = map(int, raw_input().split())
        print "%.6f %.6f" % alg(a[0], a[1])
