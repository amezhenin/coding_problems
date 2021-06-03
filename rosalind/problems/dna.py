"""
http://rosalind.info/problems/dna/
"""
import sys
from collections import Counter


def alg():
    line = input()
    c = Counter(line)
    print(f"{c['A']} {c['C']} {c['G']} {c['T']}")
    pass


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass