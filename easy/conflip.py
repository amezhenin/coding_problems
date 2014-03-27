#!/usr/bin/python
"""
http://www.codechef.com/problems/CONFLIP

Testing:
    nosetests --with-doctest <file>

Input:
1
2
1 5 1
1 5 2

Output:
2
3
"""


def alg(i, n, q):
    """
    >>> alg(1, 5, 1)
    2
    >>> alg(1, 5, 2)
    3
    >>> alg(1, 6, 2)
    3
    >>> alg(1, 6, 1)
    3
    """

    # solution with 'if'
    # return n / 2 + (not i == q) if n % 2 else n / 2
    return n / 2 + (not i == q) * (n % 2)


if __name__ == "__main__":
    for _ in range(input()):
        for _ in range(input()):
            i, n, q = map(int, raw_input().split())
            print alg(i, n, q)
