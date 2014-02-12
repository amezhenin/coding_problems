#!/usr/bin/python
"""
http://www.codechef.com/problems/CIELAB

Testing:
    nosetests --with-doctest <file>

Sample Input
5858 1234

Sample Output
1624
"""


def read_two(fn=int):
    """
    Read two integers from input
    """
    nx = raw_input()
    nx = nx.split()
    return fn(nx[0]), fn(nx[1])


def alg(a, b):
    """
    >>> alg(5858, 1234)
    4625
    >>> alg(10, 1)
    8
    >>> alg(1000, 11)
    988
    """
    res = a - b
    res += -1 if res % 10 == 9 else 1
    return res


if __name__ == "__main__":
    a, b = read_two()
    print alg(a, b)
