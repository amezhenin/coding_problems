"""
https://www.codechef.com/DEC20B/problems/EVENPSUM

Example Input
4
1 1
2 3
4 6
8 9

Example Output
1
3
12
36
"""


def alg(a, b):
    """
    >>> alg(1, 1)
    1

    >>> alg(2, 3)
    3

    >>> alg(4, 6)
    12

    >>> alg(8, 9)
    36
    """
    res = (a // 2) * (b // 2)
    res += ((a + 1) // 2) * ((b + 1) // 2)
    return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(alg(a, b))
