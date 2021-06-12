"""
https://stepik.org/lesson/541851/step/2?unit=535312
"""
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg2():
    n, l = map(int, input().split())
    lines = []
    for i in range(n):
        lines.append(input())
    m = 0
    states = {}
    res = []
    for i in range(l):
        s = "".join(map(lambda x: x[i], lines))
        if s not in states:
            m += 1
            states[s] = str(m)
        res.append(states[s])
    print(m)
    print(" ".join(res))


def alg():
    t = int(input())
    for i in range(t):
        alg2()


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass
