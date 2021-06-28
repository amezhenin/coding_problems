"""
https://stepik.org/lesson/541852/step/2?unit=535313
"""
import random
from concurrent.futures.process import ProcessPoolExecutor

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)

MAX_SIM = 1
THREADS = 11

def sim_run(vi, v, c):
    s = [0] * v
    s[vi] = 1
    for cd in c:
        new_s = list(s)
        for a, b, p in cd:
            if s[b] == 0:
                r = random.random()
                new_s[b] = s[a] * (r < p)
        s = new_s
    return sum(s)


def wrapper(args):
    log(f"Starting {args[0]}/{args[1]}")
    res = simulate_multiple(*args)
    return res, args[0]


def simulate_multiple(vi, v, c):
    s = []
    for i in range(MAX_SIM):
        s.append(sim_run(vi, v, c))
    # it is median, not average
    # res = float(sum(s)) / MAX_SIM
    s.sort()
    res = s[MAX_SIM//2]
    return res


def alg():

    t = int(input())
    for ti in range(t):
        v, d = map(int, input().split())
        c = []
        for di in range(d):
            e = int(input())
            cd = []
            for ei in range(e):
                a, b, p = map(float, input().split())
                cd.append((int(a)-1, int(b)-1, p))
            c.append(cd)

        score = []
        with ProcessPoolExecutor(max_workers=THREADS) as threads:
            args =  [(vi, v, c) for vi in range(v)]
            res = threads.map(wrapper, args)
            for vs, vi in res:
                score.append((vs, vi + 1))
            pass
        # single threaded
        # score = []
        # for vi in range(v):
        #     log(f"calc {vi} / {v}")
        #
        #     vs = simulate_multiple(vi, v, c)
        #     score.append((vs, vi+1))

        score.sort()
        print(score[-1][1])
        log(f"{ti+1}/{t}> {score[-1][1]}")


    pass


if __name__ == "__main__":
    # fin = None
    fin = "test5"
    if fin:
        fout = "out_" + fin
    else:
        fin = "input.txt"
        fout = "output.txt"

    with open(fin, "r") as sys.stdin:
        with open(fout, "w") as sys.stdout:
            alg()
    pass