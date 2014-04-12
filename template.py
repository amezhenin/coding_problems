#!/usr/bin/python
"""


Testing:
    nosetests --with-doctest <file>

Python cheat sheet:

    n = input()
    nx = raw_input()
    a = map(int, raw_input().split())

    # fast read
    from sys import stdin
    return map(int, stdin.read().split())
    # fast write, most of the time "print" is OK
    from sys import stdout
    stdout.write('\n'.join(res)+'\n')
"""


def alg():
    """
    >>> alg()

    >>> alg()
    """
    pass


if __name__ == "__main__":

    for _ in range(input()):
        print alg()
