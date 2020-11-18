#!/usr/bin/python
"""
http://www.codechef.com/problems/MUFFINS3

Testing:
    nosetests --with-doctest <file>

Sample Input

2
2
5

Sample Output

2
3

"""

def alg(n):
    """
    >>> alg(2)
    2
    >>> alg(5)
    3
    >>> alg(14)
    8
    >>> alg(25)
    13
    """
    return int(n/2) + 1


if __name__ == "__main__":

    for _ in range(input()):
        n = input()
        print alg(n)
