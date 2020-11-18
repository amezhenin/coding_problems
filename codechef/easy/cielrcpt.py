#!/usr/bin/python
"""
http://www.codechef.com/problems/CIELRCPT

Testing:
    nosetests --with-doctest <file>


Sample Input
4
10
256
255
4096

Sample Output
2
1
8
2
"""


def alg(n):
    """
    >>> alg(10)
    2
    >>> alg(256)
    1
    >>> alg(255)
    8
    >>> alg(4096)
    2
    >>> alg(4099)
    4
    """

    # initial solution
    res, n = divmod(n, 2**11)
    while n:
        res += n % 2
        n >>= 1

    # Alternative solution
    # res, n = divmod(n, 2**11)
    # res += bin(n)[2:].count('1')

    return res


    pass

if __name__ == "__main__":

    for _ in range(input()):
        print alg(input())
