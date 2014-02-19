#!/usr/bin/python
"""
http://www.codechef.com/problems/BUYING2

Testing:
    nosetests --with-doctest <file>

Input:
3
4 7
10 4 8 5
1 10
12
2 10
20 50

Output:
-1
1
7
"""

def rd2():
    nx = raw_input()
    nx = nx.split()
    return int(nx[0]), int(nx[1])

def alg(x, l):
    """
    >>> alg(7, [10, 4, 8, 5])
    -1
    >>> alg(10, [12])
    1
    >>> alg(10, [20, 50])
    7
    """
    l.sort()

    s = sum(l)
    r, o = divmod(s, x)

    if o >= l[0]:
        return -1
    else:
        return r


if __name__ == "__main__":

    for _ in range(input()):
        _, x = rd2()
        a = raw_input()
        l = [int(i) for i in a.split()]
        print alg(x, l)
