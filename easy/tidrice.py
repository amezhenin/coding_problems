#!/usr/bin/python
"""
http://www.codechef.com/problems/TIDRICE

Testing:
    nosetests --with-doctest <file>

Input:
3
4
tilak +
tilak +
tilak -
tilak +
3
ratna +
shashi -
ratna -
3
bhavani -
bhavani +
bhavani -

Output:
1
-2
-1
"""


def alg(a):
    """
    >>> alg(["tilak +", "tilak +", "tilak -", "tilak +"])
    1
    >>> alg(["ratna +", "shashi -", "ratna -"])
    -2
    >>> alg(["bhavani -", "bhavani +", "bhavani -"])
    -1
    """
    res = {}
    for i in a:
        key, value = i.split()
        value = 1 if value == "+" else -1
        res[key] = value

    return sum(res.values())


if __name__ == "__main__":

    for _ in range(input()):
        a = []
        for _ in range(input()):
            a.append(raw_input())
        print alg(a)
