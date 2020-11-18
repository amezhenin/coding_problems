#!/usr/bin/python
"""
http://www.codechef.com/problems/FCTRL

Testing:
    nosetests --with-doctest <file>


Sample Input:
6
3
60
100
1024
23456
8735373

Sample Output:
0
14
24
253
5861
2183837

"""


def alg(n):
    """
    >>> alg(3)
    0
    >>> alg(60)
    14
    >>> alg(100)
    24
    >>> alg(1024)
    253
    >>> alg(23456)
    5861
    >>> alg(8735373)
    2183837
    """

    s = 0
    while n:
        n /= 5
        s += n
    return s


if __name__ == "__main__":

    for _ in range(input()):
        print alg(input())
