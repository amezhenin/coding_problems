#!/usr/bin/python
"""
http://www.codechef.com/problems/PERMUT2

Testing:
    nosetests --with-doctest <file>

Sample Input

4
1 4 3 2
5
2 3 4 5 1
1
1
0

Sample Output

ambiguous
not ambiguous
ambiguous

"""

def read_n_array(fn=int):
    a = map(fn, raw_input().split())
    return a


def alg(a):
    """
    >>> alg([1, 4, 3, 2])
    True
    >>> alg([2, 3, 4, 5, 1])
    False
    >>> alg([1])
    True
    """

    # My initial solution
    #for i, x in enumerate(a):
    #    if a[x-1] != i + 1:  # python lists are 0-indexed
    #        return False

    # Better solution: we can iterate only half of list
    # Note that in case with odd list len, we will not check middle element
    # since it's always on his place, because we checked all elements except this
    for i in xrange(len(a)/2):
        if a[a[i]-1] != i + 1:
            return False
    # consider for-else construction here: http://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
    return True


if __name__ == "__main__":
    while(input()):
        a = read_n_array()
        if alg(a):
            print "ambiguous"
        else:
            print "not ambiguous"
