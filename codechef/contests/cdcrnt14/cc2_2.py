#!/usr/bin/python
"""
http://www.codechef.com/CDCRNT14/problems/CC2

Testing:
    nosetests --with-doctest <file>

Input:

2
0 1 3
2 3 1


Output:
1
2

This is alternative solution. It takes advantage of this formula
for calculation fibonacci numbers:

F(2n-1) = F(n-1)^2 + F(n)^2
F(2n) = (2F(n-1) + F(n)) * F(n)

In this manner, you need only log(N) steps to get N-th fib. number.
This is also useful article:

http://fusharblog.com/solving-linear-recurrence-for-programming-contest/
"""

MAX = 10**9+7


def fib(k):
    """
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(7)
    13
    >>> fib(9)
    34
    """

    assert isinstance(k, int)

    if k <= 1:
        return FIBS[k]
    elif FIBS[k]:
        return FIBS[k]
    if k % 2 == 0:
        # F(2n) = (2F(n-1) + F(n)) * F(n)
        n = k/2
        fn = fib(n)
        fn_1 = fib(n-1)
        FIBS[k] = ((2*fn_1 + fn) * fn) % MAX
        return FIBS[k]
    else:
        # F(2n-1) = F(n-1)^2 + F(n)^2
        n = k/2 + 1
        fn = fib(n)
        fn_1 = fib(n-1)
        FIBS[k] = (fn_1**2 + fn**2) % MAX
        return FIBS[k]

    pass

FIBS = [0] * 1000010
FIBS[1] = 1

def alg(a, b, r):
    """
    >>> alg(0, 1, 3)
    1
    >>> alg(2, 3, 1)
    2
    >>> alg(0, 1, 8)
    13
    >>> alg(6, 2, 8)
    94
    >>> alg(6, 2, 1)
    6
    >>> alg(6, 2, 2)
    2
    >>> alg(1000000, 1000000, 1000000)
    259573363
    """
    r -= 1
    if r == 0:
        return a
    elif r == 1:
        return b

    a, b = min(a, b), max(a, b)
    n = b - a
    k = a

    res = fib(r) * n + fib(r+1) * k
    return res % MAX


if __name__ == "__main__":
    for _ in range(input()):
        a, b, r = map(int, raw_input().split())
        print alg(a, b, r) % MAX
