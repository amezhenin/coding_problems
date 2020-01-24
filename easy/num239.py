#!/usr/bin/python
"""
https://www.codechef.com/problems/NUM239

Example Input
2
1 10
11 33

Example Output
3
8
"""


def alg(l, r):
    """
    >>> alg(1, 10)
    3
    >>> alg(11, 33)
    8
    >>> alg(17, 33)
    6
    >>> alg(17, 32)
    5
    """
    assert l <= r, "L must be <= R"
    lt, ld = l // 10, l % 10
    rt, rd = r // 10, r % 10

    res = (rt - lt) * 3
    if ld <= rd:
        for i in range(ld, rd + 1):
            if i in (2, 3, 9):
                res += 1
    else:
        for i in range(ld, rd, -1):
            if i in (2, 3, 9):
                res -= 1

    return res


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a = list(map(int, input().split()))
        print(alg(a[0], a[1]))
