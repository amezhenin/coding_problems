#!/usr/bin/python
"""
http://www.codechef.com/problems/VOTERS
Testing:
    nosetests --with-doctest <file>

Sample input:
5 6 5
23
30
42
57
90
21
23
35
57
90
92
21
23
30
57
90

Sample output:
5
21
23
30
57
90

Note:

Best solution here should be using merge sort against three array (O(N)), but standard sort works much faster.
It is also O(N), but I've expect it to be O(N*log(N))
"""
from sys import stdin

def alg(a):
    """
    >>> alg([23, 30, 42, 57, 90, 21, 23, 35, 57, 90, 92, 21, 23, 30, 57, 90])
    [21, 23, 30, 57, 90]
    """

    prev = -1
    res = []
    for i in sorted(a):
        if i == prev:
            res.append(i)
            prev = -1
        else:
            prev = i
    return res


if __name__ == "__main__":

    _ = raw_input()
    a = map(int, stdin.readlines())
    #a = map(int, stdin.read().split()[3:])

    res = alg(a)

    print len(res)
    print '\n'.join(map(str, res))
