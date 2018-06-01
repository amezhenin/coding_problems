#!/usr/bin/python
"""
https://www.codechef.com/JUNE18B/problems/BINSHFFL

Input:
2
2 4
1 5

Output:
2
1
"""


def alg(a, b):
    """
    >>> alg(2, 4)
    2

    >>> alg(1, 5)
    1
    """
    if b == 1 and a == 0:
        return 1
    if b == 0 or b == 1:
        return -1

    ca = "{0:b}".format(a)
    ca = ca.count("1")

    cb = "{0:b}".format(b)
    cb = cb.count("1")

    d = abs(ca - cb)
    if d == 0:
        return 2
    return d


if __name__ == "__main__":

    t = input()
    for i in range(t):
        a, b = map(int, raw_input().split())
        print alg(a, b)
