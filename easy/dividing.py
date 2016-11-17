#!/usr/bin/python
"""
https://www.codechef.com/problems/DIVIDING

Input:
5
7 4 1 1 2

Output:
YES


Input:
5
1 1 1 1 1

Output:
NO
"""


def alg(n, c):
    """
    >>> alg(5, [7, 4, 1, 1, 2])
    'YES'

    >>> alg(5, [1, 1, 1, 1, 1])
    'NO'
    """
    csum = sum(c)
    nsum = sum(xrange(1, n + 1))
    if csum == nsum:
        return "YES"
    return "NO"


if __name__ == "__main__":

    n = input()
    c = map(int, raw_input().split())
    print alg(n, c)
