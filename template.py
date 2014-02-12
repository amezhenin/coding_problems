#!/usr/bin/python
"""
http://www.codechef.com/problems/<problem namer>

Testing:
    nosetests --with-doctest <file>

Input:
...

Output:
...
"""

def read_n_array(fn=int):
    """
    Read array of integers with leading N. Optional param can change
    conversion to function to float.
    :return tuple (N, list)
    """
    n = input()
    a = map(fn, raw_input().split())
    return n, a


def read_two(fn=int):
    """
    Read two integers from input
    :return: tuple(int, int)
    """
    nx = raw_input()
    nx = nx.split()
    return fn(nx[0]), fn(nx[1])


def alg():
    """
    >>> alg()

    >>> alg()
    """
    pass

if __name__ == "__main__":

    for _ in range(input()):
        print alg()
