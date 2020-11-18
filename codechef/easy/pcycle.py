#!/usr/bin/python
"""
http://www.codechef.com/problems/PCYCLE

Testing:
    nosetests --with-doctest <file>

Sample input 1:

8
2 4 5 1 7 6 3 8

Sample output 1:

4
1 2 4 1
3 5 7 3
6 6
8 8 

Sample input 2:

8
1 2 3 4 5 6 7 8

Sample output 2:

8
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
"""


def read_n_array(fn=int):
    """
    Read array of integers with leading N. Optional param can change
    conversion to function to float.
    :return tuple (N, list)
    """
    n = input()
    a = map(fn, raw_input().split())
    return n, a


def alg(a):
    """
    All solutions I've seen on Codechef have O(N^2) complexity. This solution have O(N)
    >>> alg([2, 4, 5, 1, 7, 6, 3, 8])
    [[1, 2, 4, 1], [3, 5, 7, 3], [6, 6], [8, 8]]
    >>> alg([1, 2, 3, 4, 5, 6, 7, 8])
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
    """

    a.insert(0, 0)  # that is bad, this line adds N operations. I use it for simplicity.
    n = len(a)
    done = [0] * n  # Use flags for marking visited indexes. Really!!
    res = []

    for i in xrange(1, n):

        if not done[i]:
            cycle = [i]
            last = i
            while True:
                cycle.append(a[last])
                done[last] = 1
                last = a[last]
                if cycle[0] == last:
                    break
            res.append(cycle)

    return res


if __name__ == "__main__":

    _, a = read_n_array()
    res = alg(a)
    print len(res)
    for i in res:
        print " ".join(map(str, i))
