"""
https://stepik.org/lesson/205341/step/2?unit=179662
"""
import sys

def log(msg):
    print(msg, file=sys.stderr, flush=True)

delta = 0.00001

def alg():
    t = int(input())
    for i in range(t):
        n1, a, b = map(float, input().split())
        log(f"test {i+1}: {n1} {a} {b}")
        res = n1
        for k in range(10000):
            new = a * res - b * (res**2)
            if abs(new-res) < delta:
                print(f"{new:.6f}")
                break
            if new < 0:
                # res = 0
                print("0")
                break
            if new > 99999999:
                # res = -1
                print("-1")
                break
            res = new
        else:
            log(f"No break")
            # res = -1
            print("-1")


    pass


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass