"""
https://www.codingame.com/ide/puzzle/huffman-code

Input
5
4 1 1 2 2

Output
22
"""


def alg(freq):
    """
    >>> alg([4, 1, 1, 2, 2])
    22

    >>> alg([5])
    5
    """
    n = len(freq)
    # edge case
    if n == 1:
        return freq[0]

    bitlen = [0] * n
    tree = [(freq[i], (i, )) for i in range(n)]

    while len(tree) > 1:
        # FIXME: it is better to have binary heap here, instead of sorting all the time, but N is low in puzzle
        tree.sort(key=lambda x: -x[0])
        w = tree.pop()
        v = tree.pop()
        new_subtree = w[1] + v[1]
        cost = w[0] + v[0]
        for i in new_subtree:
            bitlen[i] += 1
        tree.append((cost, new_subtree))

    res = sum(freq[i] * bitlen[i] for i in range(n))
    return res


if __name__ == "__main__":
    _ = int(input())
    freq = list(map(int, input().split()))
    print(alg(freq))
