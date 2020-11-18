#!/usr/bin/python
"""
http://www.codechef.com/problems/TLG

Testing:
    nosetests --with-doctest <file>


Input:
5
140 82
89 134
90 110
112 106
88 90

Output:
1 58

"""


def iter_input():
    for _ in range(input()):
        ab = raw_input().split()
        yield int(ab[0]), int(ab[1])


def alg(a):
    """
    >>> alg([[140, 82], [89, 134], [90, 110], [112, 106], [88, 90]])
    (1, 58)
    """
    max_lead = 0
    min_lead = 0
    lead = 0
    for x, y in a:
        lead += x - y
        max_lead = max(max_lead, lead)
        min_lead = min(min_lead, lead)

    if max_lead + min_lead > 0:
        return 1, max_lead
    else:
        return 2, -min_lead


if __name__ == "__main__":
    print "%s %s" % alg(iter_input())
