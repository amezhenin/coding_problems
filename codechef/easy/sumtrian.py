#!/usr/bin/python
"""
http://www.codechef.com/problems/SUMTRIAN

Testing:
    nosetests --with-doctest <file>

Input:
2
3
1
2 1
1 2 3
4
1
1 2
4 1 2
2 3 1 1

Output:
5
9
"""


def alg(gen):
    """
    >>> alg(iter([[1], [2, 1], [1, 2, 3]]))
    5
    >>> alg(iter([[1], [1, 2], [4, 1, 2], [2, 3, 1, 1]]))
    9
    """

    prev = gen.next()
    for next in gen:
        prev = _merge(prev, next)
    return max(prev)


def _merge(prev, next):
    prev = [0] + prev + [0]
    res = [next[i] + max(prev[i], prev[i+1]) for i in xrange(len(next))]
    return res


def input_iter():
    for _ in range(input()):
        yield map(int, raw_input().split())


if __name__ == "__main__":
    for _ in range(input()):
        gen = input_iter()
        print alg(gen)
