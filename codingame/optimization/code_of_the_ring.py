"""
https://www.codingame.com/multiplayer/optimization/code-of-the-rings
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


word = "AZ" #input()
log(word)

s = ""
forest = [" "] * 30
p = 0
for c in word:
    try:
        x = forest.index(c)
        fs = (x+30 - p) % 30
        bs = (p+30 - x) % 30
        if fs <= bs:
            s += ">" * fs + "."
            p = (p+fs) % 30
        else:
            s += "<" * bs + "."
            p = (p - bs + 30) % 30
    except:
        s += ">"
        p += 1
        while forest[p] != c:
            s += "+"
            if forest[p] == "Z":
                forest[p] = " "
            elif forest[p] == " ":
                forest[p] = "A"
            else:
                forest[p] = chr(ord(forest[p]) + 1)
        s += "."
print(s)