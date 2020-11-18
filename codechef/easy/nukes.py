#!/usr/bin/python
"""
http://www.codechef.com/problems/<problem namer>

Testing:
    nosetests --with-doctest <file>

Input:
3 1 3

Output:
1 1 0
"""


def alg(a, n, k):
    """
    >>> alg(3, 1, 3)
    [1, 1, 0]
    >>> alg(7, 1, 3)
    [1, 1, 1]
    >>> alg(15, 1, 2)
    [1, 1]
    >>> alg(21, 2, 3)
    [0, 1, 2]
    """

    res = []
    n += 1
    for i in xrange(k):
        a, x = divmod(a, n)
        res.append(x)

    return res


if __name__ == "__main__":

    a, n, k = map(int, raw_input().split())
    print " ".join(map(str, alg(a, n, k)))
