"""
https://stepik.org/lesson/541850/step/2?unit=535311
"""
from concurrent.futures.process import ProcessPoolExecutor
import sys
import numpy as np


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def delta_wrapper(args):
    log(f"Starting {args[3]}")
    return delta_search(*args)


def delta_search(m, k, s, s_idx):
    delta = float("inf")
    res = None
    for i_idx, i in enumerate(m):
        penalty = ((k + i) <= 0) * 9999
        new_delta = np.abs(k + i - s) + penalty
        j_idx = np.argmin(new_delta)
        if delta > new_delta[j_idx]:
            delta = new_delta[j_idx]
            res = (i_idx, j_idx)
    p = f"{res[0]+1} {res[1]+1}"
    log(f"{s_idx}> {p}")
    return p


def alg():
    """
    Use numpy arrays to speedup computations
    """
    t = int(input())
    for i in range(t):
        _m, _k, _n = map(int, input().split())
        # n = list(map(float, input().split()))

        m = np.array(input().split()).astype(float)
        k = np.array(input().split()).astype(float)
        # n = np.array(input().split()).astype(float)
        n = list(map(float, input().split()))

        with ProcessPoolExecutor(max_workers=7) as threads:
            args =  [(m, k, s, s_idx) for s_idx, s in enumerate(n)]
            res = threads.map(delta_wrapper, args)
            for r in res:
                print(r)
            pass
        pass



if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass
