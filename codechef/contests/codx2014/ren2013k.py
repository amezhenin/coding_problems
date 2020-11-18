"""
http://www.codechef.com/CODX2014/problems/REN2013K

Testing:
    nosetests --with-doctest <file>

Input:
1
1 3

Output:
3

Solution note:

Code for Greatest Common Divisor in Python
>>> from fractions import gcd
>>> gcd(20,8)
4
>>> from math import factorial as f
>>> f(4)
24

Combinations without Repetition:

C(n,r) = n!/[(n-r)! * r!]
C(n,2) = n!/[(n-2)! * 2] => C(n,2) = [(n-1) * (n)] / 2
"""


def alg(x, y):
    """
    >>> alg(1,3)
    3
    >>> alg(1,4)
    6
    >>> alg(2,4)
    3
    >>> alg(2,5)
    6
    """
    n = y - x + 1
    res = (n * (n-1)) / 2
    return res



if __name__ == "__main__":

    for _ in range(input()):
        x, y = map(int, raw_input().split())
        print alg(x, y)
