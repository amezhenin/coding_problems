"""
https://stepik.org/lesson/541853/step/2?unit=535314

WRONG
"""
import random

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg():
    n, m = map(int, input().split())
    _t = input()
    s1 = []
    s2 = []
    for i in range(n):
        s1.append(input())
        s2.append(input())
        _t = input()

    for i in range(m):
        k = input()
        try:
            _t = input()
        except:
            pass
        res = ""
        for idx, ki in enumerate(k):
            if ki == "?":
                ss1 = random.choice(s1)
                ss2 = random.choice(s2)
                new_ki = int(ss1[idx]) + int(ss2[idx])
                res += str(new_ki)
            else:
                res += ki
        print(res)
        print()
    pass


if __name__ == "__main__":
    # fin = None
    fin = "test1.txt"
    if fin:
        fout = "out_" + fin
    else:
        fin = "input.txt"
        fout = "output.txt"

    with open(fin, "r") as sys.stdin:
        with open(fout, "w") as sys.stdout:
            alg()
    pass