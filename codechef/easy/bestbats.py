#!/usr/bin/python
"""
http://www.codechef.com/problems/BESTBATS

Testing:
    nosetests --with-doctest <file>

Input:
2
1 2 3 4 5 6 7 8 9 10 11
3
2 5 1 2 4 1 6 5 2 2 1
6

Output:
1
6
"""
from math import factorial as f


def nCr(n, r):
    return f(n) / f(r) / f(n-r)


def alg(k, a):
    """
    >>> alg(3, range(1, 12))
    1
    >>> alg(6, [2, 5, 1, 2, 4, 1, 6, 5, 2, 2, 1])
    6
    """
    last_best = sorted(a)[-k]
    n = a.count(last_best)
    r = k - sum(map(lambda x: x > last_best, a))
    return nCr(n, r)


if __name__ == "__main__":
    for _ in range(input()):
        a = map(int, raw_input().split())
        k = input()
        print alg(k, a)
