"""
https://www.codechef.com/DEC20B/problems/VACCINE1


Example Input 1
1 2 1 3 14

Example Output 1
3


Example Input 2
5 4 2 10 100

Example Output 2
9
"""


def alg(d1, v1, d2, v2, p):
    """
    >>> alg(1, 2, 1, 3, 14)
    3

    >>> alg(5, 4, 2, 10, 100)
    9
    """
    res = 0
    c = 0
    while c < p:
        res += 1
        if res >= d1:
            c += v1
        if res >= d2:
            c += v2
    return res


if __name__ == "__main__":
    d1, v1, d2, v2, p = map(int, input().split())
    print(alg(d1, v1, d2, v2, p))
