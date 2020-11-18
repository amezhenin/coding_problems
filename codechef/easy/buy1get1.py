#!/usr/bin/python
"""
http://www.codechef.com/problems/BUY1GET1

Testing:
    nosetests --with-doctest <file>

Input:
4
ssss
ssas
sa
s

Output:
2
3
2
1
"""
from collections import Counter


def alg(s):
    """
    >>> alg('ssss')
    2
    >>> alg('ssas')
    3
    >>> alg('sa')
    2
    >>> alg('s')
    1
    >>> alg('s')
    1
    """

    count = Counter(s).values()
    res = sum(map(lambda x: (x + 1)/2, count))
    return res


if __name__ == "__main__":

    for _ in range(input()):
        print alg(raw_input().strip())  #doing strip is important here
