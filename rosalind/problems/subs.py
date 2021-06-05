"""
http://rosalind.info/problems/subs/
"""
import re
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def alg():
    line = input()
    pattern = input()
    for match in re.finditer('(?={0})'.format(re.escape(pattern)), line):
        s = match.start()
        print(s+1, end=" ")
    print()


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass
