#!/usr/bin/python
"""
http://www.codechef.com/problems/JOHNY

Input:
3
4
1 3 4 2
2
5
1 2 3 9 4
5
5
1 2 3 9 4
1

Output:
3
4
1
"""

if __name__ == "__main__":
    t = input()

    for _ in range(t):
        _ = input()
        a = raw_input()
        l = [int(i) for i in a.split()]
        k = input()
        k = l[k-1]
        l.sort()
        print l.index(k) + 1