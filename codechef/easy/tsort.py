#!/usr/bin/python
"""
http://www.codechef.com/problems/TSORT

Testing:
    nosetests --with-doctest <file>

Input:
5
5
3
6
7
1

Output:

1
3
5
6
7
"""
import sys


def alg(a):
    """
    >>> alg([5, 3, 6, 7, 1])
    [1, 3, 5, 6, 7]
    >>> alg([5, 3, 1, 1, 1])
    [1, 1, 1, 3, 5]
    """
    return sorted(a)


if __name__ == "__main__":

    _ = input()
    # fast reading of all lines was the key for solving this problem
    a = map(int, sys.stdin.readlines())
    for i in alg(a):
        print i
