#!/usr/bin/python
"""
http://www.codechef.com/problems/HOTEL

Testing:
    nosetests --with-doctest <file>

Sample Input
3
3
1 2 3
4 5 6
5
1 2 3 4 5
2 3 4 5 6
7
13 6 5 8 2 10 12
19 18 6 9 9 11 15

Sample Output
3
1
3
"""


def alg(arr, dep):
    """
    >>> alg([1, 2, 3], [4, 5, 6])
    3
    >>> alg([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    1
    >>> alg([13, 6, 5, 8, 2, 10, 12], [19, 18, 6, 9, 9, 11, 15])
    3
    """

    arr.sort(reverse=True)
    dep.sort(reverse=True)
    cur_count = 0
    max_count = 0
    assert arr[-1] <= dep[-1], "guest left before arrival"

    while arr:
        if arr[-1] < dep[-1]:
            cur_count += 1
            _ = arr.pop()
            max_count = max(max_count, cur_count)
        else:
            cur_count -= 1
            _ = dep.pop()

    return max_count


if __name__ == "__main__":

    for _ in range(input()):
        _ = input()
        arr = map(int, raw_input().split())
        dep = map(int, raw_input().split())
        print alg(arr, dep)

