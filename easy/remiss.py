#!/usr/bin/python
"""
http://www.codechef.com/problems/REMISS

Testing:
    nosetests --with-doctest <file>

Example

Input:
1
19 17

Output:
19 36

"""


def alg(x, y):
    """
    >>> alg(19, 17)
    (19, 36)
    >>> alg(17, 19)
    (19, 36)
    """
    return max(x, y), x + y


if __name__ == "__main__":

    for _ in range(input()):
        a = map(int, raw_input().split())
        print "%s %s" % alg(a[0], a[1])
