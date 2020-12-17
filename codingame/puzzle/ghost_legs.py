"""
https://www.codingame.com/ide/puzzle/ghost-legs

Input
7 7
A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3

Output
A2
B1
C3
"""

w, h = map(int, input().split())
ins = input().split()

m = []
for i in range(h - 2):
    l = input()
    k = [0] * (len(ins) - 1)
    for j in range(1, w, 3):
        if l[j] == "-":
            k[j // 3] = 1
    m.append(k)

outs = input().split()


def sim(line, pos):
    if pos == len(m):
        return outs[line]
    if line > 0:
        if m[pos][line-1] == 1:
            return sim(line - 1, pos + 1)
    if line < len(ins) - 1:
        if m[pos][line] == 1:
            return sim(line + 1, pos + 1)
    return sim(line, pos + 1)


for i in range(len(ins)):
    print(ins[i] + sim(i, 0))

