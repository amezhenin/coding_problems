#!/usr/bin/python
"""
http://www.codechef.com/problems/FCTRL2

Testing:
    nosetests --with-doctest <file>


Sample input:
4
1
2
5
3

Sample output:
1
2
120
6

Note:
Haha! Python cheating detected! With C++/Java you have to write arbitrary-precision arithmetic
(http://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic) to solve this problem.
"""

from math import factorial


def alg(n):
    """
    >>> alg(3)
    6
    >>> alg(5)
    120
    """
    return factorial(n)


if __name__ == "__main__":

    for _ in range(input()):
        print alg(input())
