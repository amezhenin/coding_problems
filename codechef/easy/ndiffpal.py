#!/usr/bin/python
"""
http://www.codechef.com/problems/NDIFFPAL

Testing:
    nosetests --with-doctest <file>

Input:
3
6
7
2

Output:
noon
radar
ab
"""


def alg(n):
    """
    >>> alg(1)
    'a'
    >>> alg(5)
    'abcab'
    >>> alg(6)
    'abcabc'
    """
    res = "abc" * (n/3 + 1)
    res = res[:n]
    return res


if __name__ == "__main__":

    for _ in range(input()):
        n = input()
        print alg(n)
