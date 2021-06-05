"""
http://rosalind.info/problems/revc/
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg():
    line = input()
    m = {"A": "T", "T": "A", "C": "G", "G": "C"}
    res = "".join(map(lambda x: m[x], line[::-1]))
    print(res)


    pass


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass