#!/usr/bin/python3
"""
https://www.codechef.com/problems/TREEROOT

Input:
2
1
4 0
6
1 5
2 0
3 0
4 0
5 5
6 5

Output:
4
6
"""


def alg(nodes):
    """
    >>> alg([(4, 0)])
    4

    >>> alg([(1, 5), (2, 0), (3, 0), (4, 0), (5, 5), (6, 5)])
    6
    """
    res = 0
    for n in nodes:
        res += n[0] - n[1]
    return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        nodes = [list(map(int, input().split())) for i in range(n)]
        print(alg(nodes))
