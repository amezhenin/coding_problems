#!/usr/bin/python
"""
http://www.codechef.com/problems/HS08TEST

Testing:
    nosetests --with-doctest <file>

Example - Successful Transaction
Input:
30 120.00
Output:
89.50

Example - Incorrect Withdrawal Amount (not multiple of 5)
Input:
42 120.00
Output:
120.00

Example - Insufficient Funds
Input:
300 120.00
Output:
120.00
"""


def alg(x, y):
    """

    :param x: float
    :param y: float
    :return : float
    >>> alg(30.0, 120.0)
    89.5
    >>> alg(42.0, 120.0)
    120.0
    >>> alg(30.0, 120.0)
    89.5
    >>> alg(120.0, 120.0)
    120.0
    
    """
    if x % 5:
        return y
    # it's important to count charge!
    elif x+0.5 > y:
        return y

    return y - x - 0.5


if __name__ == "__main__":

    x, y = raw_input().split()
    res = alg(float(x), float(y))
    print "%.2f" % res
