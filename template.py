#!/usr/bin/python3
"""
Testing:
    nosetests --with-doctest <file>

Python 2 cheat sheet:

    n = input()
    nx = raw_input()
    a = map(int, raw_input().split())

Python 3 cheat sheet:
    n = int(input())
    a, b, c = map(int, input().split())
    nn     = [map(int, input().split()) for i in range(n)]
    nn_gen = (map(int, input().split()) for i in range(n))
    nn_lst = [list(map(int, input().split())) for i in range(n)]

Fast IO:
    # fast read
    from sys import stdin
    return map(int, stdin.read().split())
    # fast write, most of the time "print" is OK
    from sys import stdout
    _ = stdout.write('\n'.join(res)+'\n')

# CodinGame debugging
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


import collections
Row = collections.namedtuple("Row", ["a", "b", "c"])
Row = collections.namedtuple("Row", "a b c"])

"""


def alg():
    """
    >>> alg()

    >>> alg()
    """
    pass


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(alg())

