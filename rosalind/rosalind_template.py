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
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass