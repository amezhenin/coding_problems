#!/usr/bin/python
"""
http://www.codechef.com/problems/J7
Testing:
    nosetests --with-doctest <file>

Input:
2
20 14
20 16

Output:
3.00
4.15
"""
from math import sqrt


def read_two(fn=int):
    """
    Read two integers from input
    :return: tuple(int, int)
    """
    nx = raw_input()
    nx = nx.split()
    return fn(nx[0]), fn(nx[1])


def alg(p, s):
    """
    >>> round(alg(20, 14), 2)
    3.0
    >>> round(alg(20, 16), 2)
    4.15
    """

    d = sqrt(p * p - 24 * s)
    a = (p - d) / 12
    c = (p - 8 * a) / 4
    return a * a * c


if __name__ == "__main__":

    for _ in range(input()):
        p, s = read_two()
        print "%.2f" % alg(p, s)
