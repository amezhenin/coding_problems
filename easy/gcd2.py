#!/usr/bin/python3
"""
http://www.codechef.com/problems/GCD2
Testing:
    nosetests --with-doctest <file>

Input:
2
2 6
10 11

Output:
2
1
"""
from fractions import gcd


def alg(a, b):
    """
    >>> alg(int('1' *250), 13)
    1L
    >>> alg(int('1'+ '0' *250), 12)
    4L
    >>> alg(2, 6)
    2
    >>> alg(10, 11)
    1
    """
    return gcd(a, b)


if __name__ == "__main__":

    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(alg(a, b))
