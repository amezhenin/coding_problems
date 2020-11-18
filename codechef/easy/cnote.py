#!/usr/bin/python3
"""
http://www.codechef.com/problems/CNOTE


Testing:
    nosetests --with-doctest <file>


Input:
3
3 1 2 2
3 4
2 2
3 1 2 2
2 3
2 3
3 1 2 2
1 1
1 2


Output:
LuckyChef
UnluckyChef
UnluckyChef
"""


def alg(x, y, k, notes):
    """
    >>> alg(3, 1, 2, [(3, 4), (2, 2)])
    True

    >>> alg(3, 1, 2, [(2, 3), (2, 3)])
    False

    >>> alg(3, 1, 2, [(1, 1), (1, 2)])
    False
    """
    req = x - y
    res = False
    for pages, cost in notes:
        if pages >= req and cost <= k:
            res = True
    return res


if __name__ == "__main__":

    for _ in range(int(input())):
        x, y, k, n = map(int, input().split())
        notes = (map(int, input().split()) for i in range(n))
        if alg(x, y, k, notes):
            print("LuckyChef")
        else:
            print("UnluckyChef")

