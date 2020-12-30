"""
https://www.codingame.com/ide/puzzle/1d-spreadsheet
NOT THAT EASY ))
"""

def pa(x, A):
    if x[0] == "$":
        return A[int(x[1:])]
    return int(x)


def px(x):
    if x[0] == "$":
        return int(x[1:])
    return -1


n = int(input())
res = {-1: None, "_": None}
ops = []
for i in range(n):
    op, arg_1, arg_2 = input().split()
    ops.append([i, op, arg_1, arg_2])

while len(ops) > 0:
    next_ops = []
    skip_ops = []
    for i, op, arg_1, arg_2 in ops:
        if px(arg_1) in res and px(arg_2) in res:
            next_ops.append([i, op, arg_1, arg_2])
        else:
            skip_ops.append([i, op, arg_1, arg_2])

    for i, op, arg_1, arg_2 in next_ops:
        if op == "VALUE":
            res[i] = pa(arg_1, res)
        elif op == "ADD":
            res[i] = pa(arg_1, res) + pa(arg_2, res)
        elif op == "SUB":
            res[i] = pa(arg_1, res) - pa(arg_2, res)
        elif op == "MULT":
            res[i] = pa(arg_1, res) * pa(arg_2, res)
        else:
            pass
    ops = skip_ops

for i in range(n):
    print(res[i])
