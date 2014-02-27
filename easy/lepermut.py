#!/usr/bin/python
"""
http://www.codechef.com/problems/PERMUT2

Testing:
    nosetests --with-doctest <file>


Input:
4
1
1
2
2 1
3
3 2 1
4
1 3 2 4

Output:
YES
YES
NO
YES
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
    >>> alg([1])
    True
    >>> alg([2, 1])
    True
    >>> alg([3, 2, 1])
    False
    >>> alg([1, 3, 2, 4])
    True
    >>> alg([2, 3, 4, 5, 1])
    False
    >>> alg([5, 1, 2, 3, 4])
    False
    >>> alg([1, 2, 4, 5, 3])
    False
    """

    '''
    # Initial (wrong) solution, here is cases where you will get wrong answer:
    max = 0
    for i in xrange(len(a)):
        if a[i] > max:
            max = a[i]
            continue
        if max != a[i-1]:
            return False
    return True

    # straight forward solution
    n = len(a)
    invs = sum([a[i] > a[j] for i in xrange(0, n-1) for j in xrange(i+1, n)])
    local_invs = sum([a[i] > a[i+1] for i in xrange(0, n-1)])
    return invs == local_invs
    '''

    # Best solution
    for i in a:
        if (a[i-1]-i)*(a[i-1]-i) > 1:
            return False
    return True


if __name__ == "__main__":

    for _ in range(input()):
        _, a = read_n_array()
        if alg(a):
            print "YES"
        else:
            print "NO"
