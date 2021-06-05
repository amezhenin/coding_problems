"""
http://rosalind.info/problems/hamm/
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg():
    a = input()
    b = input()
    r = 0
    for i, j in zip(a,b):
        r += i != j
    print(r)


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass