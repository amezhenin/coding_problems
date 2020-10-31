"""
https://www.codechef.com/LTIME89B/problems/ANDOR

Example Input
2
1
8

Example Output
0 1
5 3
"""


def alg(x):
    """
    >>> alg(1)
    0, 1

    >>> alg(8)
    0, 8
    """
    return 0, x


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x = int(input())
        print("%s %s" % alg(x))

