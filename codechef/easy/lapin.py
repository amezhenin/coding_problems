#!/usr/bin/python
"""
http://www.codechef.com/problems/LAPIN

Testing:
    nosetests --with-doctest <file>

Input:
6
gaga
abcde
rotor
xyzxy
abbaab
ababc


Output:
YES
NO
YES
YES
NO
NO
"""


def alg(s):
    """
    >>> alg('gaga')
    True
    >>> alg('abcde')
    False
    >>> alg('rotor')
    True
    """

    l = len(s)
    a, b = s[:l/2], s[l/2+l%2:]
    return sorted(a) == sorted(b)


if __name__ == "__main__":

    for _ in range(input()):
        if alg(raw_input()):
            print "YES"
        else:
            print "NO"
