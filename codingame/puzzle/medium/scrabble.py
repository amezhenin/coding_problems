"""
https://www.codingame.com/training/medium/scrabble

Input:
5
because
first
these
could
which
hicquwh

Output:
which
"""

COST = {}
for i in "eaionrtlsu":
    COST[i] = 1
for i in "dg":
    COST[i] = 2
for i in "bcmp":
    COST[i] = 3
for i in "fhvwy":
    COST[i] = 4
COST["k"] = 5
for i in "jx":
    COST[i] = 8
for i in "qz":
    COST[i] = 10


def estimate(word):
    s = 0
    for i in word:
        s += COST[i]
    return s


def contains(word, letters):
    l = list(letters)
    for w in word:
        if w in l:
            l.pop(l.index(w))
        else:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    words = []
    for i in range(n):
        w = input()
        words.append(w)
    letters = input()
    words = list(filter(lambda x: contains(x, letters), words))
    assert len(words) > 0
    res = max(words, key=estimate)

    print(res)
