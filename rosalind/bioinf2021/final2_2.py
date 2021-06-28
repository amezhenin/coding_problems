"""
https://stepik.org/lesson/541854/step/2?unit=535315
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg():
    t = int(input())
    for i in range(t):
        n, l = map(int, input().split())
        good1 = [set() for _ in range(l)]
        good2 = [set() for _ in range(l)]

        bad = []

        for ni in range(n):
            s = input()
            ss1 = input()
            ss2 = input()
            if s == "+":
                for idx, ssi in enumerate(ss1):
                    good1[idx].add(ssi)
                for idx, ssi in enumerate(ss2):
                    good2[idx].add(ssi)
            else:
                bad.append((ss1, ss2))

        res = set()
        for b1, b2 in bad:
            for idx, b1i in enumerate(b1):
                if b1i not in good1[idx]:
                    res.add(idx)
            for idx, b2i in enumerate(b2):
                if b2i not in good1[idx]:
                    res.add(idx)
            pass
        try:
            mr = min(res)
            xr = max(res)
        except:
            mr, xr = 0, l-1
        print(f"{mr} {xr}")
    pass


if __name__ == "__main__":
    # fin = None
    fin = "07"
    if fin:
        fout = "out_" + fin
    else:
        fin = "input.txt"
        fout = "output.txt"

    with open(fin, "r") as sys.stdin:
        with open(fout, "w") as sys.stdout:
            alg()
    pass