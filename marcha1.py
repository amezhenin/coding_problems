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


Performance tests:

In [2]: %timeit marcha1.alg(132, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
10000 loops, best of 3: 67.8 us per loop

In [3]: %timeit marcha1.alg2(132, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
10000 loops, best of 3: 62 us per loop

In [4]: %timeit marcha1.alg3(132, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
10000 loops, best of 3: 47.6 us per loop

In [5]: %timeit marcha1.alg(13200, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
1 loops, best of 3: 511 ms per loop

In [6]: %timeit marcha1.alg2(13200, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
100 loops, best of 3: 7.48 ms per loop

In [7]: %timeit marcha1.alg3(13200, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
100 loops, best of 3: 4.36 ms per loop


I've got different performance results on my other machine. Solutions 2 and 3 are almost equal in speed, but set is
slightly better in memory consumption:

In [20]: a = {i: True for i in xrange(10000)}

In [21]: b = {i for i in xrange(10000)}

In [24]: sys.getsizeof(a)
Out[24]: 786712

In [25]: sys.getsizeof(b)
Out[25]: 524520

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
    My initial solution with recursion.

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
    if ask < sum or len(a) == 0:
        return False

    if alg(ask, a[1:], sum+a[0]):
        return True
    if alg(ask, a[1:], sum):
        return True

    return False


def alg2(ask, a):
    """
    Alternative solution with dict. It is based on dynamic programming approach.

    >>> alg2(3, [1, 1, 1])
    True
    >>> alg2(11, [1, 2, 4, 8, 16])
    True
    >>> alg2(23, [1, 2, 4, 8, 16])
    True
    >>> alg2(13, [1, 5, 5, 10, 10])
    False
    >>> alg2(132, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
    True
    """

    sums = {0: True}
    for x in a:
        for i in sums.keys():
            if i+x <= ask:
                sums[i+x] = True

    return sums.get(ask, False)


def alg3(ask, a):
    """
    Alternative solution with set. It is based on dynamic programming approach.

    >>> alg3(3, [1, 1, 1])
    True
    >>> alg3(11, [1, 2, 4, 8, 16])
    True
    >>> alg3(23, [1, 2, 4, 8, 16])
    True
    >>> alg3(13, [1, 5, 5, 10, 10])
    False
    >>> alg3(132, [17, 6, 4, 998, 254, 137, 259, 153, 154, 3, 28, 19, 123, 542, 857, 23, 687, 35, 99, 999])
    True
    """

    sums = {0}
    for x in a:
        sums |= {s+x for s in sums if s+x <= ask}
    return ask in sums


if __name__ == "__main__":

    for _ in range(input()):
        n, ask = read_two()
        a = [input() for _ in xrange(n)]
        if alg(ask, a):
            print "Yes"
        else:
            print "No"
