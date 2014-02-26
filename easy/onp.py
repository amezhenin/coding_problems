#!/usr/bin/python
"""
http://www.codechef.com/problems/ONP

Testing:
    nosetests --with-doctest <file>

Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
"""


class Var(object):

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Var(self.x + other.x + "+")

    def __sub__(self, other):
        return Var(self.x + other.x + "-")

    def __mul__(self, other):
        return Var(self.x + other.x + "*")

    def __div__(self, other):
        return Var(self.x + other.x + "/")

    def __pow__(self, other, modulo=None):
        return Var(self.x + other.x + "^")

    def __repr__(self):
        return self.x


def alg(expr):
    """
    >>> alg("(a+(b*c))")
    abc*+
    >>> alg("((a+b)*(z+x))")
    ab+zx+*
    >>> alg("((a+t)*((b+(a+c))^(c+d)))")
    at+bac++cd+^*
    >>> alg("a*b+c")
    ab*c+
    >>> alg("(a+b*c)")
    abc*+
    """

    # power is ** in python, not ^
    expr = expr.replace("^", "**")
    for char in expr:
        if char.isalpha():
            exec("%s = Var('%s')" % (char, char))
    res = eval(expr)
    return res


if __name__ == "__main__":
    for _ in range(input()):
        print alg(raw_input())
