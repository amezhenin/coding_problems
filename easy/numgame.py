#!/usr/bin/python
"""
http://www.codechef.com/problems/NUMGAME

Testing:
    nosetests --with-doctest <file>

Sample Input :
2
1
2

Sample Output :
BOB
ALICE
"""


def alg(n):
    """
    >>> alg(1)
    'BOB'
    >>> alg(2)
    'ALICE'
    """

    if n % 2:
        return "BOB"
    return "ALICE"


if __name__ == "__main__":
    for _ in range(input()):
        print alg(input())
