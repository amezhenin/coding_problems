"""
http://rosalind.info/problems/gc/
"""
from collections import Counter
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg():
    titles = []
    nucs = []

    title = input()
    nuc = ""
    while True:
        line = input()
        if len(line) == 0:
            titles.append(title)
            nucs.append(nuc)
            break

        if line[0] == ">":
            titles.append(title)
            nucs.append(nuc)
            title = line
            nuc = ""
        else:
            nuc += line

    best = 0
    res = ""
    for title, nuc in zip(titles, nucs):
        c = Counter(nuc)
        new = (c["C"] + c["G"]) / len(nuc)
        if new >= best:
            best = new
            res = title

    print(res[1:])
    print(f"{best*100:.6f}")



if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass