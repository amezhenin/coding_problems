#!/usr/bin/python
"""
http://www.codechef.com/problems/LECANDY

Testing:
    nosetests --with-doctest <file>

Input:
2
2 3
1 1
3 7
4 2 2

Output:
Yes
No
"""


def alg(c, a):
    """
    >>> alg(3, [1, 1])
    True
    >>> alg(7, [4, 2, 2])
    False
    """
    return c >= sum(a)


if __name__ == "__main__":
    for _ in range(input()):
        _, c = map(int, raw_input().split())
        a = map(int, raw_input().split())
        if alg(c, a):
            print "Yes"
        else:
            print "No"
