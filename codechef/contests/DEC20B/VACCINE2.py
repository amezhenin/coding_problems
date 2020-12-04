"""
https://www.codechef.com/DEC20B/problems/VACCINE2

Example Input
2
10 1
10 20 30 40 50 60 90 80 100 1
5 2
9 80 27 72 79

Example Output
10
3
"""
import math


def alg(d, ns):
    """
    >>> alg(1, [10, 20, 30, 40, 50, 60, 90, 80, 100, 1])
    10

    >>> alg(2, [9, 80, 27, 72, 79])
    3

    >>> alg(3, [9, 80, 1, 27, 72, 79, 55, 66])
    3

    >>> alg(3, [9, 80, 1, 2, 27, 72, 79])
    3

    >>> alg(3, [9, 80, 1, 2, 27, 72, 79, 55, 66])
    4
    """
    risk = sum(i <= 9 or i >= 80 for i in ns)
    res = math.ceil(risk/d) + math.ceil((len(ns)-risk)/d)
    return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        _, d = map(int, input().split())
        ns = list(map(int, input().split()))
        print(alg(d, ns))

