"""
https://stepik.org/lesson/541854/step/7?unit=535315
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg():
    t = int(input())
    for i in range(t):
        n, l = map(int, input().split())
        good = [set() for _ in range(l)]
        bad = []

        for ni in range(n):
            s = input()
            ss = input()
            if s == "+":
                for idx, ssi in enumerate(ss):
                    good[idx].add(ssi)
            else:
                bad.append(ss)

        res = set()
        for b in bad:
            for idx, bi in enumerate(b):
                if bi not in good[idx]:
                    res.add(idx)
            pass
        mr = min(res)
        xr = max(res)
        print(f"{mr} {xr}")
    pass


if __name__ == "__main__":
    # fin = None
    fin = "04"
    if fin:
        fout = "out_" + fin
    else:
        fin = "input.txt"
        fout = "output.txt"

    with open(fin, "r") as sys.stdin:
        with open(fout, "w") as sys.stdout:
            alg()
    pass
