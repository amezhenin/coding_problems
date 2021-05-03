"""
https://www.codingame.com/training/easy/mime-type

Input
3
3
html text/html
png image/png
gif image/gif
animated.gif
portrait.png
index.html

Output
image/gif
image/png
text/html

"""



def alg(nn, qq):
    d = {i[0].lower(): i[1] for i in nn}
    res = []
    for i in qq:
        ext = i.split(".")
        ext = ext[-1].lower() if len(ext) > 1 else ""
        res.append(d.get(ext, "UNKNOWN"))
    return res

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)

if __name__ == "__main__":
    n = int(input())  # Number of elements which make up the association table.
    q = int(input())  # Number Q of file names to be analyzed.

    nn = [input().split() for i in range(n)]
    qq = [input() for i in range(q)]

    # log(nn)
    # log(qq)
    for res in alg(nn, qq):
        print(res)

