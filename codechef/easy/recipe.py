#!/usr/bin/python
"""
http://www.codechef.com/problems/RECIPE

Testing:
    nosetests --with-doctest <file>

Sample Input
3
2 4 4
3 2 3 4
4 3 15 9 6

Sample Output
1 1
2 3 4
1 5 3 2

Notes:
gcd(a,b,c)=gcd(gcd(a,b),c)

"""

from fractions import gcd


def gcd2(x, y):
    """
    Euclid's algorithm implementation.

    >>> gcd2(10, 15)
    5
    >>> gcd2(13, 29)
    1
    >>> gcd2(1071, 462)
    21
    """
    while y:
        x, y = y, x % y
    return x


def alg(a):
    """
    >>> alg([4, 4])
    [1, 1]
    >>> alg([2, 3, 4])
    [2, 3, 4]
    >>> alg([3, 15, 9, 6])
    [1, 5, 3, 2]
    """

    divisor = reduce(gcd, a)
    return [i/divisor for i in a]


if __name__ == "__main__":

    for _ in range(input()):
        a = map(int, raw_input().split())[1:]
        print " ".join(map(str, alg(a)))
