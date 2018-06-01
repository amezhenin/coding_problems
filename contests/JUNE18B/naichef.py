#!/usr/bin/python
"""
https://www.codechef.com/JUNE18B/problems/NAICHEF

Input:
2
5 1 1
1 1 1 1 1
2 1 1
1 2

Output:
1.0000000000
0.2500000000
"""
from collections import Counter


def alg(a, b, N):
    """
    >>> alg(1, 1, [1,1,1,1,1])
    1.0

    >>> alg(1, 1, [1,2])
    0.25

    >>> alg(1, 3, [1,2])
    0.0
    """
    l = len(N)
    c = Counter(N)
    if a not in c or b not in c:
        return 0.0

    pa = float(c[a]) / l
    pb = float(c[b]) / l
    return pa * pb


if __name__ == "__main__":

    t = input()
    for i in range(t):
        n, a, b = map(int, raw_input().split())
        N = map(int, raw_input().split())
        res = alg(a, b, N)
        print "%.10f" % res
