#!/usr/bin/python
"""
http://www.codechef.com/problems/INTEST

Testing:
    nosetests --with-doctest <file>

Input:
7 3
1
51
966369
7
9
999996
11

Output:
4
"""
import sys


def read_two(fn=int):
    """
    Read two integers from input
    :return: tuple(int, int)
    """
    nx = raw_input()
    nx = nx.split()
    return fn(nx[0]), fn(nx[1])


def alg(k, gen):
    """
    :param k: int
    :param gen: any iterable object

    >>> alg(3, [1, 51, 966369, 7, 9, 999996, 11])
    4
    """

    # My initial solution
    #res = 0
    #for i in gen:
    #    res += (i % k == 0)
    res = sum(i % k == 0 for i in gen)
    return res


if __name__ == "__main__":

    _, k = read_two()
    a = map(int, sys.stdin.readlines())
    print alg(k, a)

