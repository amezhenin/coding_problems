#!/usr/bin/python
"""
http://www.codechef.com/problems/NUMGAME2

Testing:
    nosetests --with-doctest <file>

Sample Input:
2
1
2

Sample Output:
ALICE
BOB
"""


def alg(n):
    """
    >>> alg(1)
    'ALICE'
    >>> alg(2)
    'BOB'
    """

    if n % 4 == 1:
        return "ALICE"
    return "BOB"


if __name__ == "__main__":
    for _ in range(input()):
        print alg(input())
