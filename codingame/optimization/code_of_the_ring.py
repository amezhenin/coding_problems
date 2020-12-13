"""
https://www.codingame.com/multiplayer/optimization/code-of-the-rings
"""
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def get_alpha_pos(c):
    if c == " ":
        return N
    return ord(c) - ord("A") + 1 + N

A = " ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 3
N = len(A) // 3

word = input()
log(word)

res = ""
forest = [" "] * 30
cur_pos = 0
for c in word:
    # how much actions need to to transform each cell into what we want
    actions = []
    for x in range(30):
        # calc forward and back steps to that cell
        forward_steps = (x + 30 - cur_pos) % 30
        back_steps = (cur_pos + 30 - x) % 30
        if forward_steps < back_steps:
            steps = ">" * forward_steps
        else:
            steps = "<" * back_steps

        # calc + and - actions to transform that cell into what we want
        alpha_pos = get_alpha_pos(forest[x])
        plus = 0
        while c != A[alpha_pos + plus]:
            plus += 1

        alpha_pos = get_alpha_pos(forest[x])
        minus = 0
        while c != A[alpha_pos - minus]:
            minus += 1
        if plus < minus:
            acts = "+" * plus
        else:
            acts = "-" * minus
        actions.append((steps + acts + ".", x))

    actions.sort(key=lambda l: len(l[0]))
    final_steps, idx = actions[0]
    res += final_steps
    cur_pos = idx
    forest[cur_pos] = c

print(res)