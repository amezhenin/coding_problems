#!/usr/bin/python
"""
http://www.codechef.com/problems/CLEANUP

Testing:
    nosetests --with-doctest <file>

Input:
3
6 3
2 4 1
3 2
3 2
8 2
3 8

Output:
3 6
5
1

1 4 6
2 5 7
"""

def read_two(fn=int):
    """
    Read two integers from input
    :return: tuple(int, int)
    """
    nx = raw_input()
    nx = nx.split()
    return fn(nx[0]), fn(nx[1])


def alg(n, a):
    """
    >>> alg(6, [2, 4, 1])
    ([3, 6], [5])
    >>> alg(3, [3, 2])
    ([1], [])
    >>> alg(8, [3, 8])
    ([1, 4, 6], [2, 5, 7])
    """

    done = set(a)
    # initial solution
    tasks = [i for i in xrange(1, n+1) if i not in done]

    # Alternative #1
    #tasks = filter(lambda x: x not in done, xrange(1, n+1))
    # Alternative #2
    #tasks = sorted(list(set(xrange(1, n+1)) - done))

    return tasks[::2], tasks[1::2]


if __name__ == "__main__":

    for _ in range(input()):
        n, _ = read_two()
        a = map(int, raw_input().split())
        chef, assistant = alg(n, a)
        print " ".join(map(str, chef))
        print " ".join(map(str, assistant))
