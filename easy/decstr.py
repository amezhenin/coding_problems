#!/usr/bin/python
"""
http://www.codechef.com/problems/DECSTR

Testing:
    nosetests --with-doctest <file>

Sample Input
2
1
2

Sample Output
ba
cba
"""

import string
from itertools import cycle, islice


def alg(n):
    """
    My initial solution

    >>> alg(1)
    'ba'
    >>> alg(2)
    'cba'
    >>> alg(26)
    'bazyxwvutsrqponmlkjihgfedcba'
    >>> alg(25)
    'zyxwvutsrqponmlkjihgfedcba'
    >>> alg(52)
    'cbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba'
    >>> alg(51)
    'bazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba'
    >>> alg(50)
    'zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba'
    """

    chars = cycle(string.ascii_lowercase)
    d, m = divmod(n, 25)
    finish = n + d + (m > 0)
    res = list(islice(chars, 0, finish))
    return ''.join(res[::-1])


def alg(n):
    """
    Alternative solution
    """
    chars = string.ascii_lowercase
    d, m = divmod(n, 25)
    res = chars[:m+(m > 0)][::-1] + (chars * d)[::-1]
    return ''.join(res)


if __name__ == "__main__":
    for _ in range(input()):
        print alg(input())