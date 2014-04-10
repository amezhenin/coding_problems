#!/usr/bin/python
"""
http://www.codechef.com/problems/STONES

Testing:
    nosetests --with-doctest <file>

Input:
4
abc
abcdef
aA
abAZ
aaa
a
what
none

Output:
3
2
1
0
"""

from collections import Counter


def alg(j, s):
    """
    >>> alg('abc', 'abcdef')
    3
    >>> alg('aA', 'abAZ')
    2
    >>> alg('aaa', 'a')
    1
    >>> alg('what', 'none')
    0
    """
    c = Counter(s)
    return sum(c[i] for i in set(j))


if __name__ == "__main__":
    for _ in range(input()):
        j, s = raw_input(), raw_input()
        print alg(j, s)
