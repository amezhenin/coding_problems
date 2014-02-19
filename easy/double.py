#!/usr/bin/python
"""
http://www.codechef.com/problems/DOUBLE

Testing:
    nosetests --with-doctest <file>

Input:
2
2
4

Output:
2
4
"""


def alg(n):
    """
    >>> alg(2)
    2
    >>> alg(4)
    4
    >>> alg(5)
    4
    """
    return n - (n % 2)


if __name__ == "__main__":

    for _ in range(input()):
        n = input()
        print alg(n)