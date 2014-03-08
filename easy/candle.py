#!/usr/bin/python
"""
http://www.codechef.com/problems/CANDLE

Testing:
    nosetests --with-doctest <file>

Sample input:
3
2 1 1 4 0 6 3 2 2 2
0 1 1 1 1 1 1 1 1 1
2 2 1 2 1 1 3 1 1 1

Sample output:
4
10
22
"""


def alg(a):
    """
    >>> alg([2, 1, 1, 4, 0, 6, 3, 2, 2, 2])
    '4'
    >>> alg([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    '10'
    >>> alg([1, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    '100'
    >>> alg([2, 2, 1, 2, 1, 1, 3, 1, 1, 1])
    '22'
    """

    a.append(a.pop(0))
    idx = a.index(min(a))

    if idx == 9:
        return '1' + '0' * (a[9] + 1)

    return str(idx + 1) * (a[idx] + 1)


if __name__ == "__main__":

    for _ in range(input()):
        a = map(int, raw_input().split())
        print alg(a)
