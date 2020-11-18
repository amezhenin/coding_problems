#!/usr/bin/python
"""
http://www.codechef.com/problems/MARCHA2

Testing:
    nosetests --with-doctest <file>

Input:
2
3
0 1 2
3
0 0 3

Output:
Yes
No
"""
import sys


def alg(a):
    """
    >>> alg([0, 1, 2])
    True
    >>> alg([0, 0, 3])
    False
    >>> alg([0, 2, 0])
    False
    """
    stems = 1
    for i in a:
        if stems == 0:
            return False
        stems -= i
        stems *= 2

    return stems == 0


if __name__ == "__main__":
    for _ in range(input()):
        _ = int(sys.stdin.readline())
        a = map(int, sys.stdin.readline().split())
        if alg(a):
            print "Yes"
        else:
            print "No"
