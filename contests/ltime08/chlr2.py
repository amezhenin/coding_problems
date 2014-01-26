"""
www.codechef.com/LTIME08/problems/CHRL2

Testing:
    nosetests --with-doctest <file>

Input:
CHEFCHEFFFF
Output:
2

Input:
CHHHEEEFFCC
Output:
1

Scoring
Subtask 1 (25 points): |S| <= 2000
Subtask 2 (75 points): See the constraints.

Notes:
"""

def pop(s, i):
    """
    >>> pop("0123456789", 5)
    '012346789'
    >>> pop("0123456789", 0)
    '123456789'
    >>> pop("0123456789", 9)
    '012345678'
    """
    s = s[:i] + s[i+1:]
    return s

def alg(s):
    """
    Subtask 1
    >>> alg("chefcheffff")
    2
    >>> alg("chhheeeffcc")
    1
    """
    res = 0
    while True:
        c = 0

        c = s.find("c", c)
        if c < 0:
            return res
        s = pop(s, c)

        c = s.find("h", c)
        if c < 0:
            return res
        s = pop(s, c)

        c = s.find("e", c)
        if c < 0:
            return res
        s = pop(s, c)

        c = s.find("f", c)
        if c < 0:
            return res
        s = pop(s, c)

        res+=1



if __name__ == "__main__":
    s = raw_input().lower()
    print alg(s)
