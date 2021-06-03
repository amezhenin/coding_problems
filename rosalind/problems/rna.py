"""
http://rosalind.info/problems/rna/
"""
import sys

def alg():
    line = input()
    line = line.replace("T", "U")
    print(f"{line}")
    pass


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass