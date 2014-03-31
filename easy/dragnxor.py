#!/usr/bin/python
"""
http://www.codechef.com/problems/DRAGNXOR

Testing:
    nosetests --with-doctest <file>

Input:
3
3 5 4
5 0 1
4 3 7


Output:
7
16
14
"""




def alg(n, a, b):
    """
    >>> alg(3, 5, 4)
    7
    >>> alg(5, 0, 1)
    16
    >>> alg(4, 3, 7)
    14
    >>> alg(3, 7, 7)
    0
    """

    ones = bin(a).count('1') + bin(b).count('1')
    if ones > n:
        ones -= (ones - n) * 2
    zeros = n - ones
    return int('1' * ones + '0' * zeros, 2)


if __name__ == "__main__":

    for _ in range(input()):
        n, a, b = map(int, raw_input().split())
        print alg(n, a, b)
