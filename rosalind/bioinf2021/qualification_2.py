"""
https://stepik.org/lesson/541850/step/2?unit=535311
"""
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg2():
    _m, _k, _n = map(int, input().split())
    m = list(map(float, input().split()))
    k = list(map(float, input().split()))
    n = list(map(float, input().split()))

    for s_idx, s in enumerate(n):
        delta = float("inf")
        res = None
        for i_idx, i in enumerate(m):
            for j_idx, j in enumerate(k):
                if i + j <= 0:
                    continue
                new_delta = s - i - j
                if delta > abs(new_delta):
                    delta = abs(new_delta)
                    res = (i_idx, j_idx)
        p = f"{res[0]+1} {res[1]+1}"
        log(f"{s_idx}> {p}")
        print(p)
    pass



def alg():
    t = int(input())
    for i in range(t):
        alg2()


if __name__ == "__main__":
    with open("3.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass
