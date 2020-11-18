"""
www.codechef.com/LTIME08/problems/CHRL1

Testing:
    nosetests --with-doctest <file>

Input:
2
1 3
2 2
3 4
2 1
2 2
3 5

Output:
2
5

Scoring:
Subtask 1 (30 points): All the oranges' weights equals to 1.
Subtask 2 (30 points): N = 5
Subtask 2 (40 points): See the constraints

Notes:
T[i] = (Ci, Wi)
"""


def alg(k, t):
    """
    Subtask 1,2
    >>> alg(4, [(4,1),(2,1),(3,1),(1,1)])
    2
    >>> alg(3, [(1,1),(1,1),(1,1),(1,1),(1,1),(1,1)])
    3

    Subtask 3
    > alg(3, [(2,2)])
    2
    > alg(4, [(2,1), (2,2), (3,5)]])
    5
    """
    w = [i[0] for i in t]
    w.sort()
    sum = 0
    while True:
        if len(w)==0:
            return sum
        wi = w.pop(0)
        k -= wi
        if k >= 0:
            sum += 1
        else:
            return sum


if __name__ == "__main__":

    for _ in range(input()):
        n, k = map(int, raw_input().split())
        t = []
        for j in xrange(n):
            c, w = map(int, raw_input().split())
            t.append((c,w))
        print alg(k, t)
