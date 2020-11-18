#!/usr/bin/python
"""
http://www.codechef.com/problems/RIGHTRI

Testing:
    nosetests --with-doctest <file>

Example

Input:
5
0 5 19 5 0 0
17 19 12 16 19 0
5 14 6 13 8 7
0 4 0 14 3 14
0 2 0 14 9 2

Output:
3
"""

def alg(x):
    """
    >>> alg([[0, 5, 19, 5, 0, 0], [17, 19, 12, 16, 19, 0], [5, 14, 6, 13, 8, 7], [0, 4, 0, 14, 3, 14], [0, 2, 0, 14, 9, 2]])
    3
    """
    count = 0
    for i in x:
        l = [(i[0]-i[2])**2 + (i[1]-i[3])**2,
             (i[2]-i[4])**2 + (i[3]-i[5])**2,
             (i[0]-i[4])**2 + (i[1]-i[5])**2]
        l.sort()
        if l[2] == l[0] + l[1]:
            count += 1

    return count


if __name__ == "__main__":

    a = []
    for _ in range(input()):
        a.append(map(int, raw_input().split()))
    print alg(a)
