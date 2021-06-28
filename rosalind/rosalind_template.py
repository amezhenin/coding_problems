"""

"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(f"{a+b}")
    pass


if __name__ == "__main__":
    fin = None
    if fin:
        fout = "out_" + fin
    else:
        fin = "input.txt"
        fout = "output.txt"

    with open(fin, "r") as sys.stdin:
        with open(fout, "w") as sys.stdout:
            alg()
    pass