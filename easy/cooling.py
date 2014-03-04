#!/usr/bin/python
"""
http://www.codechef.com/problems/COOLING

Testing:
    nosetests --with-doctest <file>


Sample input:
2
3
10 30 20
30 10 20
5
9 7 16 4 8
8 3 14 10 10

Sample output:
3
4
"""


def alg(pies, racks):
    """
    >>> alg([10, 30, 20], [30, 10, 20])
    3
    >>> alg([9, 7, 16, 4, 8], [8, 3, 14, 10, 10])
    4
    """

    pies.sort(reverse=True)

    for r in sorted(racks):
        p = pies[-1]
        if r >= p:
            _ = pies.pop()

    return len(racks) - len(pies)


if __name__ == "__main__":

    for _ in range(input()):
        _ = input()
        pies = map(int, raw_input().split())
        racks = map(int, raw_input().split())
        print alg(pies, racks)
