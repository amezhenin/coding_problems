#!/usr/bin/python
"""
http://www.codechef.com/problems/MARCHA1

Testing:
    nosetests --with-doctest <file>

Input:
5
3 3
1
1
1
5 11
1
2
4
8
16
5 23
1
2
4
8
16
5 13
1
5
5
10
10
20 132
17
6
4
998
254
137
259
153
154
3
28
19
123
542
857
23
687
35
99
999

Output:
Yes
Yes
Yes
No
Yes
"""

def read_two(fn=int):
    """
    Read two integers from input
    :return:
    """
    nx = raw_input()
    nx = nx.split()
    return fn(nx[0]), fn(nx[1])


def alg(ask, a, sum=0):
    """
    >>> alg(3, [1, 1, 1])
    True
    >>> alg(11, [1, 2, 4, 8, 16])
    True
    >>> alg(23, [1, 2, 4, 8, 16])
    True
    >>> alg(13, [1, 5, 5, 10, 10])
    False
    >>> alg(132, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
    True
    """
    if ask == sum:
        return True
    if len(a) == 0:
        return False

    if alg(ask, a[1:], sum+a[0]):
        return True
    if alg(ask, a[1:], sum):
        return True

    return False


if __name__ == "__main__":

    for _ in range(input()):
        n, ask = read_two()
        a = [input() for _ in xrange(n)]
        if alg(ask, a):
            print "Yes"
        else:
            print "No"
