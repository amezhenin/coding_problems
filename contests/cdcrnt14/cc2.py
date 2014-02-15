#!/usr/bin/python
"""
http://www.codechef.com/CDCRNT14/problems/CC2

Testing:
    nosetests --with-doctest <file>

Input:

2
0 1 3
2 3 1


Output:
1
2

"""

MAX = 10**9+7


def fib(N):
    """
    >>> fib(2)
    [0, 1]
    >>> fib(8)
    [0, 1, 1, 2, 3, 5, 8, 13]
    """
    res = [0, 1]
    for _ in xrange(N-2):
        res.append((res[-1] + res[-2]) % MAX)
    return res

FIBS = fib(1100010)


def alg(a, b, r):
    """
    >>> alg(0, 1, 3)
    1
    >>> alg(2, 3, 1)
    2
    >>> alg(0, 1, 8)
    13
    >>> alg(6, 2, 8)
    94
    >>> alg(6, 2, 1)
    6
    >>> alg(6, 2, 2)
    2
    >>> alg(1000000, 1000000, 1000000)
    259573363
    """

    if r == 1:
        return a
    elif r == 2:
        return b

    a, b = min(a, b), max(a, b)
    n = b - a
    k = a

    res = FIBS[r-1] * n + FIBS[r] * k
    return res


if __name__ == "__main__":

    for _ in range(input()):
        a, b, r = map(int, raw_input().split())
        print alg(a, b, r) % MAX
